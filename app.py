from flask import Flask, render_template, request, redirect, url_for, session, send_file, jsonify
from gtts import gTTS
import io
import os
import re
import json
import time
import base64
from datetime import datetime

import folium
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import urllib.request
import urllib.error
# language packs must be in the SAME folder as app.py (project root)
from ar import AR, display_arabic
from fr import FR, display_french
from en import EN, display_english

load_dotenv()
print("ENV URL:", os.getenv("LEGAL_AI_API_URL"))
print("ENV KEY EXISTS:", bool(os.getenv("LEGAL_AI_API_KEY")))
print("ENV MODEL:", os.getenv("LEGAL_AI_MODEL"))
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.jinja_env.auto_reload = True
@app.after_request
def add_no_cache_headers(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response
# folders
MAPS_DIR = os.path.join(app.root_path, "generated_maps")
os.makedirs(MAPS_DIR, exist_ok=True)

# =========================
# Production Config
# =========================
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "greenlaw-dev-secret")

database_url = os.getenv("DATABASE_URL")
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = database_url or "sqlite:///greenlaw_local.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# =========================
# Database Models
# =========================
class User(db.Model):
    tablename = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)

    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    is_economic_operator = db.Column(db.Boolean, default=False, nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    consent_status = db.Column(db.String(20), default="pending", nullable=False)
    admin_access_consent = db.Column(db.Boolean, default=False, nullable=False)
    consent_updated_at = db.Column(db.DateTime, nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    last_login_at = db.Column(db.DateTime, nullable=True)

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

class Notification(db.Model):
    __tablename__ = "notifications"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, index=True)
    title = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False)
    notif_type = db.Column(db.String(50), default="general", nullable=False)
    is_read = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

class PrivateMessage(db.Model):
    __tablename__ = "private_message"

    id = db.Column(db.Integer, primary_key=True)

    sender_id = db.Column(db.Integer, nullable=False, index=True)
    receiver_id = db.Column(db.Integer, nullable=False, index=True)

    message_category = db.Column(db.String(50), nullable=False, default="admin_problem", index=True)
    related_ad_id = db.Column(db.String(120), nullable=True, index=True)
    message_text = db.Column(db.Text, nullable=False)

    is_read = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
# =========================
# Create DB tables
# =========================
with app.app_context():
    db.create_all()

    inspector = db.inspect(db.engine)
    user_columns = [col["name"] for col in inspector.get_columns("user")]
    alter_statements = []

    private_message_columns = []
    if inspector.has_table("private_message"):
        private_message_columns = [col["name"] for col in inspector.get_columns("private_message")]

    if "is_admin" not in user_columns:
        alter_statements.append('ALTER TABLE "user" ADD COLUMN is_admin BOOLEAN NOT NULL DEFAULT FALSE')

    if "is_economic_operator" not in user_columns:
        alter_statements.append('ALTER TABLE "user" ADD COLUMN is_economic_operator BOOLEAN NOT NULL DEFAULT FALSE')

    if "is_active" not in user_columns:
        alter_statements.append('ALTER TABLE "user" ADD COLUMN is_active BOOLEAN NOT NULL DEFAULT TRUE')

    if "last_login_at" not in user_columns:
        alter_statements.append('ALTER TABLE "user" ADD COLUMN last_login_at TIMESTAMP NULL')

    if "consent_status" not in user_columns:
        alter_statements.append('ALTER TABLE "user" ADD COLUMN consent_status VARCHAR(20) NOT NULL DEFAULT \'pending\'')

    if "admin_access_consent" not in user_columns:
        alter_statements.append('ALTER TABLE "user" ADD COLUMN admin_access_consent BOOLEAN NOT NULL DEFAULT FALSE')

    if "consent_updated_at" not in user_columns:
        alter_statements.append('ALTER TABLE "user" ADD COLUMN consent_updated_at TIMESTAMP NULL')

    for sql in alter_statements:
        db.session.execute(db.text(sql))

    if inspector.has_table("private_message") and "message_category" not in private_message_columns:
        db.session.execute(
            db.text("ALTER TABLE private_message ADD COLUMN message_category VARCHAR(50) NOT NULL DEFAULT 'admin_problem'")
        )

    if inspector.has_table("private_message") and "related_ad_id" not in private_message_columns:
        db.session.execute(
            db.text("ALTER TABLE private_message ADD COLUMN related_ad_id VARCHAR(120) NULL")
        )
    db.session.commit()
    db.create_all()    

    economic_user = User.query.filter_by(username="economic_user").first()
    if not economic_user:
        economic_user = User(
            username="economic_user",
            is_admin=False,
            is_economic_operator=True,
            is_active=True,
            consent_status="accepted",
            admin_access_consent=True,
            consent_updated_at=datetime.utcnow(),
    )
    economic_user.set_password("eco_56789")
    db.session.add(economic_user)
    db.session.commit()

APP_NAME = "Green Law"

LANGS = {"ar": AR, "fr": FR, "en": EN}
DISPLAY = {"ar": display_arabic, "fr": display_french, "en": display_english}


def get_lang() -> str:
    lang = session.get("lang", "ar")
    return lang if lang in LANGS else "ar"
def is_logged_in() -> bool:
    return bool(session.get("logged_in") and session.get("user_id"))
def is_admin_logged_in() -> bool:
    return bool(is_logged_in() and session.get("is_admin"))


def get_current_user():
    user_id = session.get("user_id")
    if not user_id:
        return None
    return User.query.get(user_id)
def is_admin_inspecting() -> bool:
    return bool(session.get("admin_inspecting") and session.get("inspected_user_id"))

def get_effective_user():
    if is_admin_logged_in() and is_admin_inspecting():
        inspected_user_id = session.get("inspected_user_id")
        if inspected_user_id:
            return User.query.get(inspected_user_id)
    return get_current_user()
def get_admin_user():
    return User.query.filter_by(is_admin=True, is_active=True).order_by(User.id.asc()).first()
def create_notification(user_id: int, title: str, message: str, notif_type: str = "general"):
    notif = Notification(
        user_id=user_id,
        title=str(title or "").strip(),
        message=str(message or "").strip(),
        notif_type=str(notif_type or "general").strip(),
        is_read=False,
    )
    db.session.add(notif)
    db.session.commit()


def create_notification_once(user_id: int, title: str, message: str, notif_type: str = "general"):
    existing = Notification.query.filter_by(
        user_id=user_id,
        notif_type=str(notif_type or "general").strip()
    ).first()

    if existing:
        return

    notif = Notification(
        user_id=user_id,
        title=str(title or "").strip(),
        message=str(message or "").strip(),
        notif_type=str(notif_type or "general").strip(),
        is_read=False,
    )
    db.session.add(notif)
    db.session.commit()
def _format_text(text: str, **kwargs) -> str:
    if text is None:
        text = ""

    fmt_kwargs = dict(kwargs)
    fmt_kwargs.pop("default", None)

    try:
        return str(text).format(**fmt_kwargs)
    except Exception:
        return str(text)


def t_plain(key: str, **kwargs) -> str:
    """ترجمة خام بدون display"""
    lang = get_lang()
    text = LANGS.get(lang, {}).get(key, key)

    if text == key and "default" in kwargs:
        text = kwargs["default"]

    return _format_text(text, **kwargs)


def t(key: str, **kwargs) -> str:
    """ترجمة للعرض باستعمال display_*"""
    lang = get_lang()
    raw = t_plain(key, **kwargs)
    return DISPLAY[lang](raw)


def display_text(text: str) -> str:
    """عرض نص خام باستعمال display المناسب للغة الحالية"""
    lang = get_lang()
    return DISPLAY[lang](str(text or ""))

@app.context_processor
def inject_globals():
    lang = get_lang()

    unread_notifications_count = 0
    unread_messages_count = 0

    if is_logged_in():
        current_user = get_effective_user()
        if current_user:
            unread_notifications_count = Notification.query.filter_by(
                user_id=current_user.id,
                is_read=False
            ).count()

            unread_messages_count = PrivateMessage.query.filter_by(
                receiver_id=current_user.id,
                is_read=False
            ).count()

    return {
        "t": t,
        "lang": lang,
        "dir": "rtl" if lang == "ar" else "ltr",
        "app_name": APP_NAME,
        "unread_notifications_count": unread_notifications_count,
        "unread_messages_count": unread_messages_count,
    }



@app.route("/set-lang/<lang_code>")
def set_lang(lang_code):
    if lang_code in LANGS:
        session["lang"] = lang_code
    return redirect(request.referrer or url_for("login"))


@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    lang = get_lang()
    page_dir = "rtl" if lang == "ar" else "ltr"

    if request.method == "POST":
        username = (request.form.get("username") or "").strip()
        password = (request.form.get("password") or "").strip()

        if not username or not password:
            return render_template(
                "login.html",
                app_name=APP_NAME,
                title=t("auth.login", default="تسجيل الدخول"),
                error=t("auth.login.error_required", default="يرجى إدخال اسم المستخدم وكلمة المرور"),
                lang=lang,
                dir=page_dir,
            )

        user = User.query.filter_by(username=username).first()

        if not user or not user.check_password(password):
            return render_template(
                "login.html",
                app_name=APP_NAME,
                title=t("auth.login", default="تسجيل الدخول"),
                error=t("auth.login.error_invalid", default="اسم المستخدم أو كلمة المرور غير صحيحة"),
                lang=lang,
                dir=page_dir,
            )

        if not user.is_active:
            return render_template(
                "login.html",
                app_name=APP_NAME,
                title=t("auth.login", default="تسجيل الدخول"),
                error=t("auth.login.account_disabled", default="هذا الحساب موقوف حاليًا. يرجى التواصل مع الإدارة."),
                lang=lang,
                dir=page_dir,
            )

        user.last_login_at = datetime.utcnow()
        db.session.commit()

        session["user_id"] = user.id
        session["username"] = user.username
        session["user"] = user.username
        session["logged_in"] = True
        session["is_admin"] = bool(user.is_admin)
        session["is_economic_operator"] = bool(user.is_economic_operator)

        if user.consent_status == "accepted":
            create_notification_once(
                user_id=user.id,
                title=t("notifications.consent.accepted.title", default="تم حفظ الموافقة"),
                message=t(
                    "notifications.consent.accepted.message",
                    default="تم تسجيل موافقتك على شروط المنصة بنجاح، وتم حفظ موافقتك على السماح للإدارة بالدخول إلى حسابك عند الضرورة وبعد إعلامك مسبقًا."
                ),
                notif_type="consent_accepted"
            )

        if user.is_admin:
            return redirect(url_for("admin_dashboard"))

        if user.is_economic_operator:
            return redirect(url_for("economic_operator_home"))

        return redirect(url_for("sections"))

    return render_template(
        "login.html",
        app_name=APP_NAME,
        title=t("auth.login", default="تسجيل الدخول"),
        lang=lang,
        dir=page_dir,
    )

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))
@app.route("/sections")
def sections():
    if not is_logged_in():
        return redirect(url_for("login"))

    if session.get("is_admin") and not is_admin_inspecting():
        return redirect(url_for("admin_dashboard"))

    current_user = get_effective_user()
    if not current_user:
        return redirect(url_for("login"))

    if current_user.is_economic_operator:
        return redirect(url_for("economic_operator_home"))

    show_consent_modal = False
    if current_user.consent_status != "accepted":
        show_consent_modal = True

    return render_template(
        "sections.html",
        title=t("sections.title", default="اختيار القسم"),
        show_consent_modal=show_consent_modal,
        current_consent_status=(current_user.consent_status if current_user else "pending"),
    )

@app.route("/consent-update", methods=["POST"])
def consent_update():
    if not is_logged_in():
        return redirect(url_for("login"))

    current_user = get_effective_user()
    if not current_user:
        return redirect(url_for("login"))

    action = (request.form.get("action") or "").strip().lower()

    if action == "accept":
        current_user.consent_status = "accepted"
        current_user.admin_access_consent = True
        current_user.consent_updated_at = datetime.utcnow()
        db.session.commit()

        create_notification_once(
            user_id=current_user.id,
            title=t("notifications.consent.accepted.title", default="تم حفظ الموافقة"),
            message=t(
                "notifications.consent.accepted.message",
                default="تم تسجيل موافقتك على شروط المنصة بنجاح، وتم حفظ موافقتك على السماح للإدارة بالدخول إلى حسابك عند الضرورة وبعد إعلامك مسبقًا."
            ),
            notif_type="consent_accepted"
        )

        return redirect(url_for("sections"))

    if action == "refuse":
        current_user.consent_status = "refused"
        current_user.admin_access_consent = False
        current_user.consent_updated_at = datetime.utcnow()
        db.session.commit()

        session.clear()
        return redirect(url_for("login"))

    return redirect(url_for("sections"))
@app.route("/economic-operator")
def economic_operator_home():
    if not is_logged_in():
        return redirect(url_for("login"))

    if session.get("is_admin") and not is_admin_inspecting():
        return redirect(url_for("admin_dashboard"))

    current_user = get_effective_user()
    if not current_user:
        return redirect(url_for("login"))

    if not current_user.is_economic_operator:
        return redirect(url_for("sections"))

    show_consent_modal = False
    if current_user.consent_status != "accepted":
        show_consent_modal = True

    unread_notifications_count = Notification.query.filter_by(
        user_id=current_user.id,
        is_read=False
    ).count()

    unread_admin_coordination_count = PrivateMessage.query.filter(
        PrivateMessage.receiver_id == current_user.id,
        PrivateMessage.is_read == False,
        PrivateMessage.message_category.in_(["admin_coordination", "admin_coordination_market"])
    ).count()

    unread_market_count = PrivateMessage.query.filter(
        PrivateMessage.receiver_id == current_user.id,
        PrivateMessage.message_category == "market_owner",
        PrivateMessage.is_read == False
    ).count()

    return render_template(
        "economic_operator_home.html",
        title="المتعامل الاقتصادي",
        show_consent_modal=show_consent_modal,
        current_consent_status=current_user.consent_status,
        unread_notifications_count=unread_notifications_count,
        unread_admin_coordination_count=unread_admin_coordination_count,
        unread_market_count=unread_market_count,
    )

@app.route("/notifications")
def notifications_page():
    if not is_logged_in():
        return redirect(url_for("login"))

    current_user = get_effective_user()
    if not current_user:
        return redirect(url_for("login"))

    notifications = (
        Notification.query
        .filter_by(user_id=current_user.id)
        .order_by(Notification.created_at.desc())
        .all()
    )

    unread_items = [n for n in notifications if not n.is_read]
    if unread_items:
        for n in unread_items:
            n.is_read = True
        db.session.commit()

    return render_template(
        "notifications.html",
        title=t("notifications.page_title", default="الإشعارات"),
        notifications=notifications,
    )
@app.route("/messages/delete/<int:message_id>", methods=["POST"])
def delete_private_message(message_id):
    if not is_logged_in():
        return redirect(url_for("login"))

    current_user = get_effective_user()
    if not current_user:
        return redirect(url_for("login"))

    msg = PrivateMessage.query.filter_by(id=message_id).first_or_404()

    if msg.sender_id != current_user.id and msg.receiver_id != current_user.id:
        return redirect(url_for("sections"))

    db.session.delete(msg)
    db.session.commit()

    return redirect(request.referrer or url_for("sections"))

@app.route("/messages/admin")
def user_admin_messages():
    if not is_logged_in():
        return redirect(url_for("login"))

    current_user = get_effective_user()
    if not current_user:
        return redirect(url_for("login"))

    unread_problem_count = PrivateMessage.query.filter_by(
        receiver_id=current_user.id,
        message_category="admin_problem",
        is_read=False
    ).count()

    unread_coordination_count = PrivateMessage.query.filter_by(
        receiver_id=current_user.id,
        message_category="admin_coordination",
        is_read=False
    ).count()

    unread_market_count = PrivateMessage.query.filter(
        PrivateMessage.receiver_id == current_user.id,
        PrivateMessage.message_category == "market_owner",
        PrivateMessage.is_read == False
    ).count()

    return render_template(
        "user_admin_messages.html",
        title=t("messages.page_title", default="الرسائل"),
        unread_problem_count=unread_problem_count,
        unread_coordination_count=unread_coordination_count,
        unread_market_count=unread_market_count,
    )
@app.route("/messages/admin/problem", methods=["GET", "POST"])
def user_admin_messages_problem():
    if not is_logged_in():
        return redirect(url_for("login"))

    current_user = get_effective_user()
    if not current_user:
        return redirect(url_for("login"))

    admin_user = get_admin_user()
    if not admin_user:
        return render_template(
            "user_admin_problem_chat.html",
            title=t("messages.problem_title", default="مراسلة الإدارة عند وجود مشكل"),
            messages=[],
            current_user=current_user,
            form_error=t("messages.no_admin", default="لا يوجد حساب إداري متاح حاليًا."),
        )

    if request.method == "POST":
        message_text = (request.form.get("message_text") or "").strip()

        if message_text:
            msg = PrivateMessage(
                sender_id=current_user.id,
                receiver_id=admin_user.id,
                message_category="admin_problem",
                message_text=message_text,
                is_read=False,
            )
            db.session.add(msg)
            db.session.commit()

            create_notification(
                user_id=admin_user.id,
                title=t_plain("messages.notification.title", default="رسالة جديدة"),
                message=t_plain(
                    "messages.notification.message",
                    default="لديك رسالة جديدة من المستخدم {username}.",
                    username=current_user.username
                ),
                notif_type="private_message_problem"
            )

        return redirect(url_for("user_admin_messages_problem"))

    messages = (
        PrivateMessage.query.filter(
            PrivateMessage.message_category == "admin_problem",
            db.or_(
                db.and_(
                    PrivateMessage.sender_id == current_user.id,
                    PrivateMessage.receiver_id == admin_user.id
                ),
                db.and_(
                    PrivateMessage.sender_id == admin_user.id,
                    PrivateMessage.receiver_id == current_user.id
                )
            )
        )
        .order_by(PrivateMessage.created_at.asc())
        .all()
    )

    unread_from_admin = [
        m for m in messages
        if m.receiver_id == current_user.id and m.sender_id == admin_user.id and not m.is_read
    ]
    if unread_from_admin:
        for m in unread_from_admin:
            m.is_read = True
        db.session.commit()

    return render_template(
        "user_admin_problem_chat.html",
        title=t("messages.problem_title", default="مراسلة الإدارة عند وجود مشكل"),
        messages=messages,
        current_user=current_user,
        admin_user=admin_user,
        form_error="",
    )
@app.route("/messages/admin/coordination", methods=["GET", "POST"])
def user_admin_messages_coordination():
    if not is_logged_in():
        return redirect(url_for("login"))

    current_user = get_effective_user()
    if not current_user:
        return redirect(url_for("login"))

    admin_user = get_admin_user()
    if not admin_user:
        return render_template(
            "user_admin_coordination_chat.html",
            title=t("messages.coord_title", default="مراسلة الإدارة للتنسيق"),
            messages=[],
            current_user=current_user,
            form_error=t("messages.no_admin", default="لا يوجد حساب إداري متاح حاليًا."),
        )

    if request.method == "POST":
        message_text = (request.form.get("message_text") or "").strip()

        if message_text:
            msg = PrivateMessage(
                sender_id=current_user.id,
                receiver_id=admin_user.id,
                message_category="admin_coordination",
                message_text=message_text,
                is_read=False,
            )
            db.session.add(msg)
            db.session.commit()

            create_notification(
                user_id=admin_user.id,
                title=t_plain("messages.notification.title", default="رسالة جديدة"),
                message=t_plain(
                    "messages.notification.message",
                    default="لديك رسالة جديدة من المستخدم {username}.",
                    username=current_user.username
                ),
                notif_type="private_message_coordination"
            )

        return redirect(url_for("user_admin_messages_coordination"))

    messages = (
        PrivateMessage.query.filter(
            PrivateMessage.message_category == "admin_coordination",
            db.or_(
                db.and_(
                    PrivateMessage.sender_id == current_user.id,
                    PrivateMessage.receiver_id == admin_user.id
                ),
                db.and_(
                    PrivateMessage.sender_id == admin_user.id,
                    PrivateMessage.receiver_id == current_user.id
                )
            )
        )
        .order_by(PrivateMessage.created_at.asc())
        .all()
    )

    unread_from_admin = [
        m for m in messages
        if m.receiver_id == current_user.id and m.sender_id == admin_user.id and not m.is_read
    ]
    if unread_from_admin:
        for m in unread_from_admin:
            m.is_read = True
        db.session.commit()

    return render_template(
        "user_admin_coordination_chat.html",
        title=t("messages.coord_title", default="مراسلة الإدارة للتنسيق"),
        messages=messages,
        current_user=current_user,
        admin_user=admin_user,
        form_error="",
    )
@app.route("/messages/market")
def market_owner_conversations():
    if not is_logged_in():
        return redirect(url_for("login"))

    current_user = get_effective_user()
    if not current_user:
        return redirect(url_for("login"))

    market_messages = (
        PrivateMessage.query.filter(
            PrivateMessage.message_category == "market_owner",
            db.or_(
                PrivateMessage.sender_id == current_user.id,
                PrivateMessage.receiver_id == current_user.id
            )
        )
        .order_by(PrivateMessage.created_at.desc())
        .all()
    )

    conversations_map = {}

    for msg in market_messages:
        if not msg.related_ad_id:
            continue

        other_user_id = msg.receiver_id if msg.sender_id == current_user.id else msg.sender_id
        conv_key = f"{msg.related_ad_id}_{other_user_id}"

        if conv_key in conversations_map:
            continue

        ad = MarketAd.query.filter_by(id=msg.related_ad_id).first()
        other_user = User.query.get(other_user_id)

        if not ad or not other_user:
            continue

        conversations_map[conv_key] = {
            "ad_id": ad.id,
            "section": ad.section_key,
            "ad_title": ad.title,
            "ad_emoji": ad.emoji,
            "other_username": other_user.username,
            "last_message": msg.message_text,
            "last_message_time": msg.created_at,
        }

    conversations = list(conversations_map.values())
    conversations.sort(key=lambda x: x["last_message_time"], reverse=True)

    return render_template(
        "market_owner_conversations.html",
        title=t("messages.market_title", default="محادثات أصحاب الإعلانات"),
        conversations=conversations,
    )

@app.route("/<section>/market/ad/<ad_id>/message-owner", methods=["GET", "POST"])
def market_message_owner_chat(section, ad_id):
    if not is_logged_in():
        return redirect(url_for("login"))

    current_user = get_effective_user()
    if not current_user:
        return redirect(url_for("login"))

    ad = MarketAd.query.filter_by(id=ad_id).first_or_404()

    owner_id_str = str(ad.owner_id or "").strip()
    current_user_id_str = str(current_user.id)

    if owner_id_str == current_user_id_str:
        return redirect(url_for("market_category", section=section, category_key=ad.category_key))

    if not owner_id_str.isdigit():
        return redirect(url_for("market_category", section=section, category_key=ad.category_key))

    owner_user = User.query.filter_by(id=int(owner_id_str)).first()
    if not owner_user:
        return redirect(url_for("market_category", section=section, category_key=ad.category_key))

    if request.method == "POST":
        message_text = (request.form.get("message_text") or "").strip()

        if message_text:
            msg = PrivateMessage(
                sender_id=current_user.id,
                receiver_id=owner_user.id,
                message_category="market_owner",
                related_ad_id=ad.id,
                message_text=message_text,
                is_read=False,
            )
            db.session.add(msg)
            db.session.commit()

            create_notification(
                user_id=owner_user.id,
                title=t_plain("messages.notification.title", default="رسالة جديدة"),
                message=t_plain(
                    "messages.notification.message",
                    default="لديك رسالة جديدة من المستخدم {username}.",
                    username=current_user.username
                ),
                notif_type="market_owner_message"
            )

        return redirect(url_for("market_message_owner_chat", section=section, ad_id=ad.id))

    messages = (
        PrivateMessage.query.filter(
            PrivateMessage.message_category == "market_owner",
            PrivateMessage.related_ad_id == ad.id,
            db.or_(
                db.and_(
                    PrivateMessage.sender_id == current_user.id,
                    PrivateMessage.receiver_id == owner_user.id
                ),
                db.and_(
                    PrivateMessage.sender_id == owner_user.id,
                    PrivateMessage.receiver_id == current_user.id
                )
            )
        )
        .order_by(PrivateMessage.created_at.asc())
        .all()
    )

    unread_from_owner = [
        m for m in messages
        if m.receiver_id == current_user.id and m.sender_id == owner_user.id and not m.is_read
    ]
    if unread_from_owner:
        for m in unread_from_owner:
            m.is_read = True
        db.session.commit()

    return render_template(
        "market_message_owner_chat.html",
        title=t("market.message_owner", default="مراسلة صاحب الإعلان في الخاص"),
        current_user=current_user,
        owner_user=owner_user,
        ad=ad,
        messages=messages,
        section=section,
    )
@app.route("/<section>/market/ad/<ad_id>/message-admin-coordination", methods=["GET", "POST"])
def market_message_admin_coordination_chat(section, ad_id):
    if not is_logged_in():
        return redirect(url_for("login"))

    current_user = get_effective_user()
    if not current_user:
        return redirect(url_for("login"))

    admin_user = get_admin_user()
    if not admin_user:
        return redirect(url_for("market_category", section=section, category_key=""))

    ad = MarketAd.query.filter_by(id=ad_id).first_or_404()

    if request.method == "POST":
        message_text = (request.form.get("message_text") or "").strip()

        if message_text:
            msg = PrivateMessage(
                sender_id=current_user.id,
                receiver_id=admin_user.id,
                message_category="admin_coordination_market",
                related_ad_id=ad.id,
                message_text=message_text,
                is_read=False,
            )
            db.session.add(msg)
            db.session.commit()

            create_notification(
                user_id=admin_user.id,
                title=t_plain("messages.notification.title", default="رسالة جديدة"),
                message=t_plain(
                    "messages.market_admin_notification",
                    default="لديك رسالة جديدة للتنسيق بخصوص الإعلان {ad_title} من المستخدم {username}.",
                    ad_title=ad.title,
                    username=current_user.username
                ),
                notif_type="market_admin_coordination"
            )

        return redirect(url_for("market_message_admin_coordination_chat", section=section, ad_id=ad.id))

    messages = (
        PrivateMessage.query.filter(
            PrivateMessage.message_category == "admin_coordination_market",
            PrivateMessage.related_ad_id == ad.id,
            db.or_(
                db.and_(
                    PrivateMessage.sender_id == current_user.id,
                    PrivateMessage.receiver_id == admin_user.id
                ),
                db.and_(
                    PrivateMessage.sender_id == admin_user.id,
                    PrivateMessage.receiver_id == current_user.id
                )
            )
        )
        .order_by(PrivateMessage.created_at.asc())
        .all()
    )

    unread_from_admin = [
        m for m in messages
        if m.receiver_id == current_user.id and m.sender_id == admin_user.id and not m.is_read
    ]
    if unread_from_admin:
        for m in unread_from_admin:
            m.is_read = True
        db.session.commit()

    return render_template(
        "market_message_admin_coordination_chat.html",
        title=t("market.message_admin_coordination", default="مراسلة الإدارة في الخاص للتنسيق"),
        current_user=current_user,
        admin_user=admin_user,
        ad=ad,
        messages=messages,
        section=section,
    )
@app.route("/plant")
def plant():
    if not is_logged_in():
        return redirect(url_for("login"))

    current_user = get_effective_user()
    if not current_user:
        return redirect(url_for("login"))

    if current_user.is_economic_operator:
        return redirect(url_for("market_home", section="plant"))

    return render_template(
        "plant.html",
        title="قسم نباتي 🌱",
    )



@app.route("/animal")
def animal():
    if not is_logged_in():
        return redirect(url_for("login"))

    current_user = get_effective_user()
    if not current_user:
        return redirect(url_for("login"))

    if current_user.is_economic_operator:
        return redirect(url_for("market_home", section="animal"))

    return render_template(
        "animal.html",
        title="قسم حيواني 🐄",
    )
@app.route("/admin")
def admin_dashboard():
    if not is_admin_logged_in():
        return redirect(url_for("login"))

    users = User.query.order_by(User.created_at.desc()).all()
    current_admin = get_current_user()

    unread_admin_notifications_count = 0
    unread_admin_problem_count = 0
    unread_admin_coordination_count = 0

    if current_admin:
        unread_admin_notifications_count = Notification.query.filter_by(
            user_id=current_admin.id,
            is_read=False
        ).count()

        unread_admin_problem_count = PrivateMessage.query.filter_by(
            receiver_id=current_admin.id,
            message_category="admin_problem",
            is_read=False
        ).count()

        unread_admin_coordination_count = PrivateMessage.query.filter(
            PrivateMessage.receiver_id == current_admin.id,
            PrivateMessage.is_read == False,
            PrivateMessage.message_category.in_(["admin_coordination", "admin_coordination_market"])
        ).count()

    return render_template(
        "admin_dashboard.html",
        title="Admin Dashboard",
        users=users,
        unread_admin_notifications_count=unread_admin_notifications_count,
        unread_admin_problem_count=unread_admin_problem_count,
        unread_admin_coordination_count=unread_admin_coordination_count,
    )
@app.route("/admin/user/<int:user_id>/inspect", methods=["POST"])
def admin_start_inspect_user(user_id):
    if not is_admin_logged_in():
        return redirect(url_for("login"))

    admin_user = get_current_user()
    target_user = User.query.get_or_404(user_id)

    if target_user.is_admin:
        return redirect(url_for("admin_user_view", user_id=user_id))

    session["admin_inspecting"] = True
    session["inspected_user_id"] = target_user.id
    session["real_admin_id"] = admin_user.id

    inspected_at = datetime.utcnow().strftime("%Y-%m-%d %H:%M")

    create_notification(
        user_id=target_user.id,
        title="تم تفحص حسابك من طرف الإدارة",
        message=f"قامت الإدارة بتفحص حسابك بتاريخ {inspected_at}.",
        notif_type="admin_account_inspection"
    )

    return redirect(url_for("sections"))

@app.route("/admin/stop-inspect", methods=["GET", "POST"], endpoint="admin_stop_inspect")
def admin_stop_inspect():
    if not is_admin_logged_in():
        return redirect(url_for("login"))

    session.pop("admin_inspecting", None)
    session.pop("inspected_user_id", None)
    session.pop("real_admin_id", None)

    return redirect("/admin")


@app.route("/admin/messages")
def admin_messages_center():
    if not is_admin_logged_in():
        return redirect(url_for("login"))

    current_admin = get_current_user()
    if not current_admin:
        return redirect(url_for("login"))

    unread_admin_problem_count = PrivateMessage.query.filter_by(
        receiver_id=current_admin.id,
        message_category="admin_problem",
        is_read=False
    ).count()

    unread_admin_coordination_count = PrivateMessage.query.filter(
        PrivateMessage.receiver_id == current_admin.id,
        PrivateMessage.is_read == False,
        PrivateMessage.message_category.in_(["admin_coordination", "admin_coordination_market"])
    ).count()

    return render_template(
        "admin_messages_center.html",
        title="رسائل الإدارة",
        unread_admin_problem_count=unread_admin_problem_count,
        unread_admin_coordination_count=unread_admin_coordination_count,
    )
@app.route("/admin/messages/problems")
def admin_problem_threads():
    if not is_admin_logged_in():
        return redirect(url_for("login"))

    current_admin = get_current_user()
    if not current_admin:
        return redirect(url_for("login"))

    problem_messages = (
        PrivateMessage.query.filter_by(
            receiver_id=current_admin.id,
            message_category="admin_problem"
        )
        .order_by(PrivateMessage.created_at.desc())
        .all()
    )

    threads_map = {}

    for msg in problem_messages:
        user = User.query.get(msg.sender_id)
        if not user:
            continue

        if user.id in threads_map:
            continue

        threads_map[user.id] = {
            "user_id": user.id,
            "username": user.username,
            "last_message": msg.message_text,
            "last_message_time": msg.created_at,
            "unread_count": PrivateMessage.query.filter_by(
                receiver_id=current_admin.id,
                sender_id=user.id,
                message_category="admin_problem",
                is_read=False
            ).count()
        }

    threads = list(threads_map.values())
    threads.sort(key=lambda x: x["last_message_time"], reverse=True)

    return render_template(
        "admin_problem_threads.html",
        title="رسائل معالجة المشاكل",
        threads=threads,
    )   
@app.route("/admin/messages/problems/<int:user_id>", methods=["GET", "POST"])
def admin_problem_chat(user_id):
    if not is_admin_logged_in():
        return redirect(url_for("login"))

    current_admin = get_current_user()
    if not current_admin:
        return redirect(url_for("login"))

    target_user = User.query.get_or_404(user_id)

    if request.method == "POST":
        message_text = (request.form.get("message_text") or "").strip()

        if message_text:
            msg = PrivateMessage(
                sender_id=current_admin.id,
                receiver_id=target_user.id,
                message_category="admin_problem",
                message_text=message_text,
                is_read=False,
            )
            db.session.add(msg)
            db.session.commit()

            create_notification(
                user_id=target_user.id,
                title="رسالة جديدة من الإدارة",
                message=f"أرسلت لك الإدارة رسالة جديدة بخصوص معالجة مشكل في حسابك بتاريخ {datetime.utcnow().strftime('%Y-%m-%d %H:%M')}.",
                notif_type="admin_problem_reply"
            )

        return redirect(url_for("admin_problem_chat", user_id=target_user.id))

    messages = (
        PrivateMessage.query.filter(
            PrivateMessage.message_category == "admin_problem",
            db.or_(
                db.and_(
                    PrivateMessage.sender_id == target_user.id,
                    PrivateMessage.receiver_id == current_admin.id
                ),
                db.and_(
                    PrivateMessage.sender_id == current_admin.id,
                    PrivateMessage.receiver_id == target_user.id
                )
            )
        )
        .order_by(PrivateMessage.created_at.asc())
        .all()
    )

    unread_from_user = [
        m for m in messages
        if m.receiver_id == current_admin.id and m.sender_id == target_user.id and not m.is_read
    ]
    if unread_from_user:
        for m in unread_from_user:
            m.is_read = True
        db.session.commit()

    return render_template(
        "admin_problem_chat.html",
        title="محادثة معالجة المشكل",
        target_user=target_user,
        current_admin=current_admin,
        messages=messages,
    )
@app.route("/admin/notifications")
def admin_notifications():
    if not is_admin_logged_in():
        return redirect(url_for("login"))

    current_admin = get_current_user()
    if not current_admin:
        return redirect(url_for("login"))

    notifications = (
        Notification.query
        .filter_by(user_id=current_admin.id)
        .order_by(Notification.created_at.desc())
        .all()
    )

    unread_items = [n for n in notifications if not n.is_read]
    if unread_items:
        for n in unread_items:
            n.is_read = True
        db.session.commit()

    return render_template(
        "admin_notifications.html",
        title="إشعارات الإدارة",
        notifications=notifications,
    )
@app.route("/admin/messages/coordination")
def admin_coordination_threads():
    if not is_admin_logged_in():
        return redirect(url_for("login"))

    current_admin = get_current_user()
    if not current_admin:
        return redirect(url_for("login"))

    coordination_messages = (
        PrivateMessage.query.filter(
            PrivateMessage.receiver_id == current_admin.id,
            PrivateMessage.message_category.in_(["admin_coordination", "admin_coordination_market"])
        )
        .order_by(PrivateMessage.created_at.desc())
        .all()
    )

    threads_map = {}

    for msg in coordination_messages:
        user = User.query.get(msg.sender_id)
        if not user:
            continue

        thread_key = f"{user.id}_{msg.message_category}_{msg.related_ad_id or 'noad'}"
        if thread_key in threads_map:
            continue

        if msg.message_category == "admin_coordination_market":
            thread_title = f"تنسيق إعلان"
        else:
            thread_title = "تنسيق عام"

        threads_map[thread_key] = {
            "thread_key": thread_key,
            "user_id": user.id,
            "username": user.username,
            "message_category": msg.message_category,
            "related_ad_id": msg.related_ad_id or "",
            "thread_title": thread_title,
            "last_message": msg.message_text,
            "last_message_time": msg.created_at,
            "unread_count": PrivateMessage.query.filter(
                PrivateMessage.receiver_id == current_admin.id,
                PrivateMessage.sender_id == user.id,
                PrivateMessage.is_read == False,
                PrivateMessage.message_category == msg.message_category,
                PrivateMessage.related_ad_id == (msg.related_ad_id if msg.related_ad_id else None)
            ).count()
        }

    threads = list(threads_map.values())
    threads.sort(key=lambda x: x["last_message_time"], reverse=True)

    return render_template(
        "admin_coordination_threads.html",
        title="رسائل التنسيق",
        threads=threads,
    )
@app.route("/admin/messages/coordination/<int:user_id>", methods=["GET", "POST"])
def admin_coordination_chat(user_id):
    if not is_admin_logged_in():
        return redirect(url_for("login"))

    current_admin = get_current_user()
    if not current_admin:
        return redirect(url_for("login"))

    target_user = User.query.get_or_404(user_id)

    message_category = (request.args.get("category") or "admin_coordination").strip()
    related_ad_id = (request.args.get("related_ad_id") or "").strip()

    if message_category not in ["admin_coordination", "admin_coordination_market"]:
        message_category = "admin_coordination"

    if request.method == "POST":
        message_text = (request.form.get("message_text") or "").strip()

        if message_text:
            msg = PrivateMessage(
                sender_id=current_admin.id,
                receiver_id=target_user.id,
                message_category=message_category,
                related_ad_id=related_ad_id if related_ad_id else None,
                message_text=message_text,
                is_read=False,
            )
            db.session.add(msg)
            db.session.commit()

            create_notification(
                user_id=target_user.id,
                title="رسالة جديدة من الإدارة",
                message=f"أرسلت لك الإدارة رسالة جديدة للتنسيق بتاريخ {datetime.utcnow().strftime('%Y-%m-%d %H:%M')}.",
                notif_type="admin_coordination_reply"
            )

        return redirect(url_for(
            "admin_coordination_chat",
            user_id=target_user.id,
            category=message_category,
            related_ad_id=related_ad_id
        ))

    messages = (
        PrivateMessage.query.filter(
            PrivateMessage.message_category == message_category,
            PrivateMessage.related_ad_id == (related_ad_id if related_ad_id else None),
            db.or_(
                db.and_(
                    PrivateMessage.sender_id == target_user.id,
                    PrivateMessage.receiver_id == current_admin.id
                ),
                db.and_(
                    PrivateMessage.sender_id == current_admin.id,
                    PrivateMessage.receiver_id == target_user.id
                )
            )
        )
        .order_by(PrivateMessage.created_at.asc())
        .all()
    )

    unread_from_user = [
        m for m in messages
        if m.receiver_id == current_admin.id and m.sender_id == target_user.id and not m.is_read
    ]
    if unread_from_user:
        for m in unread_from_user:
            m.is_read = True
        db.session.commit()

    return render_template(
        "admin_coordination_chat.html",
        title="محادثة التنسيق",
        target_user=target_user,
        current_admin=current_admin,
        messages=messages,
        message_category=message_category,
        related_ad_id=related_ad_id,
    )


@app.route("/admin/user/<int:user_id>")
def admin_user_view(user_id):
    if not is_admin_logged_in():
        return redirect(url_for("login"))

    target_user = User.query.get_or_404(user_id)

    return render_template(
        "admin_user_view.html",
        title="User Details",
        target_user=target_user,
    )


@app.route("/admin/user/<int:user_id>/disable", methods=["POST"])
def admin_disable_user(user_id):
    if not is_admin_logged_in():
        return redirect(url_for("login"))

    current_user = get_current_user()
    target_user = User.query.get_or_404(user_id)

    if target_user.id == current_user.id:
        return redirect(url_for("admin_dashboard"))

    target_user.is_active = False
    db.session.commit()

    return redirect(url_for("admin_dashboard"))


@app.route("/admin/user/<int:user_id>/enable", methods=["POST"])
def admin_enable_user(user_id):
    if not is_admin_logged_in():
        return redirect(url_for("login"))

    target_user = User.query.get_or_404(user_id)
    target_user.is_active = True
    db.session.commit()

    return redirect(url_for("admin_dashboard"))

@app.route("/plant/guide")
def plant_guide():
    return render_template("guide_plant.html", title=t("guide.plant.title", default="مرشدك الفلاحي"))


@app.route("/animal/guide")
def animal_guide():
    return render_template("guide_animal.html", title=t("guide.animal.title", default="مرشدك الفلاحي"))


@app.route("/plant/guide/<int:n>")
def plant_guide_article(n: int):
    if n not in (1, 2, 3, 4):
        return redirect(url_for("plant_guide"))

    title_key = f"guide.plant.{n}.title"
    body_key = f"guide.plant.{n}.body"

    return render_template(
        "guide_article.html",
        title=t(title_key, default=""),
        page_title=t("guide.plant.title", default="مرشدك الفلاحي"),
        article_title=t(title_key, default=""),
        article_body=t(body_key, default=""),
        tts_text=t_plain(body_key, default=""),
        back_url=url_for("plant_guide"),
        section="plant",
        bg_file="img/bg_guide_plant.jpg",
    )


@app.route("/animal/guide/<int:n>")
def animal_guide_article(n: int):
    if n not in (1, 2, 3, 4, 5):
        return redirect(url_for("animal_guide"))

    title_key = f"guide.animal.{n}.title"
    body_key = f"guide.animal.{n}.body"

    return render_template(
        "guide_article.html",
        title=t(title_key, default=""),
        page_title=t("guide.animal.title", default="مرشدك الفلاحي"),
        article_title=t(title_key, default=""),
        article_body=t(body_key, default=""),
        tts_text=t_plain(body_key, default=""),
        back_url=url_for("animal_guide"),
        section="animal",
        bg_file="img/bg_guide_animal.jpg",
    )


# =========================
# TTS API
# =========================
@app.route("/tts", methods=["POST"])
def tts_api():
    text = (request.form.get("text") or "").strip()
    lang = get_lang()

    if not text:
        return jsonify({"ok": False, "error": "empty"}), 400

    if len(text) > 5000:
        text = text[:5000]

    try:
        tts = gTTS(text=text, lang=lang)
        mp3_fp = io.BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)

        return send_file(
            mp3_fp,
            mimetype="audio/mpeg",
            as_attachment=False,
            download_name="tts.mp3",
        )
    except Exception:
        return jsonify({"ok": False, "error": "tts_fail"}), 500


# =========================
# LEGAL GUIDE (WEB VERSION)
# =========================
def normalize(txt: str) -> str:
    txt = str(txt).lower().strip()
    txt = re.sub(r"[^\w\s\u0600-\u06FF]", " ", txt)
    txt = re.sub(r"\s+", " ", txt)
    return txt


def _build_synonyms_from_i18n():
    bases = t_plain("law.synonyms.bases", default=[])
    out = {}
    if not isinstance(bases, list):
        return out

    for base in bases:
        alts = t_plain(f"law.synonyms.map.{base}", default=[])
        if isinstance(alts, list):
            out[base] = alts
    return out


def expand_query_with_synonyms(query_norm: str) -> str:
    synonyms = _build_synonyms_from_i18n()
    words = set(query_norm.split())

    for base, alts in synonyms.items():
        base_n = normalize(base)
        if base_n in words:
            for a in alts:
                words.add(normalize(a))
        else:
            for a in alts:
                if normalize(a) in words:
                    words.add(base_n)

    return " ".join(sorted(w for w in words if w))


PLANT_CASE_IDS = [
    "rent_land",
    "land_reclamation",
    "agri_partnership",
    "sell_crops",
    "agri_insurance",
    "water_irrigation",
    "pesticides",
    "agri_marketing",
    "agri_taxes",
    "land_ownership",
    "machines",
    "farm_labor",
    "environmental_pollution",
    "ip_products",
    "transport_products",
    "legal_declarations",
    "farmer_disputes",
    "cooperative_farms",
    "agri_loans",
    "work_safety",
]

ANIMAL_CASE_IDS = [
    "livestock_license",
    "vet_control",
    "sell_animals",
    "transport_animals",
    "epidemics_reporting",
    "mandatory_vaccines",
    "milk_regulation",
    "eggs_marketing",
    "slaughter_meat",
    "beekeeping_honey",
    "wool_shearing",
    "feed_quality",
    "manure_environment",
    "livestock_insurance",
    "breeding_loans",
    "breeding_partnership",
    "farm_workers",
    "environment_protection",
    "barn_safety",
    "breeders_disputes",
]


def build_cases(section: str):
    sec = (section or "").strip().lower()
    ids = ANIMAL_CASE_IDS if sec == "animal" else PLANT_CASE_IDS
    base_key = "law.animals.cases" if sec == "animal" else "law.plants.cases"

    cases = []
    for cid in ids:
        title_raw = t_plain(f"{base_key}.{cid}.title", default="")
        keywords = t_plain(f"{base_key}.{cid}.keywords", default=[])
        desc_raw = t_plain(f"{base_key}.{cid}.desc", default="")

        if not isinstance(keywords, list):
            keywords = []

        cases.append({
            "id": cid,
            "title": display_text(title_raw),
            "title_raw": title_raw,
            "keywords": keywords,
            "description": display_text(desc_raw),
            "description_raw": desc_raw,
        })
    return cases


def score_case(case_item, query_norm: str) -> int:
    score = 0
    title = normalize(case_item.get("title_raw", ""))
    desc = normalize(case_item.get("description_raw", ""))
    kws = case_item.get("keywords", []) or []

    for kw in kws:
        kw_n = normalize(kw)
        if kw_n and kw_n in query_norm:
            score += 4

    for w in title.split():
        if w and w in query_norm:
            score += 2

    for w in desc.split():
        if w and w in query_norm:
            score += 1

    return score


def search_cases(section: str, user_text: str, topn: int = 3):
    bank = build_cases(section)
    q = expand_query_with_synonyms(normalize(user_text))

    scored = []
    for item in bank:
        sc = score_case(item, q)
        if sc > 0:
            scored.append((sc, item))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [x[1] for x in scored[:topn]]


def build_faq_cases(section: str):
    sec = (section or "").strip().lower()

    if sec == "animal":
        ids = ANIMAL_CASE_IDS
        base_key = "law.animals.cases"
    else:
        ids = PLANT_CASE_IDS
        base_key = "law.plants.cases"

    faq_items = []
    for cid in ids:
        title_raw = t_plain(f"{base_key}.{cid}.title", default="")
        desc_raw = t_plain(f"{base_key}.{cid}.desc", default="")
        keywords = t_plain(f"{base_key}.{cid}.keywords", default=[])

        if not isinstance(keywords, list):
            keywords = []

        faq_items.append({
            "id": cid,
            "title_raw": str(title_raw or "").strip(),
            "desc_raw": str(desc_raw or "").strip(),
            "keywords": keywords,
        })

    return faq_items


def search_faq_cases(section: str, user_text: str, topn: int = 1):
    faq_bank = build_faq_cases(section)
    q = expand_query_with_synonyms(normalize(user_text))

    scored = []
    for item in faq_bank:
        score = 0

        title_n = normalize(item.get("title_raw", ""))
        desc_n = normalize(item.get("desc_raw", ""))
        kws = item.get("keywords", []) or []

        for kw in kws:
            kw_n = normalize(kw)
            if kw_n and kw_n in q:
                score += 5

        for w in title_n.split():
            if w and w in q:
                score += 3

        for w in desc_n.split():
            if w and w in q:
                score += 1

        if score > 0:
            scored.append((score, item))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [x[1] for x in scored[:topn]]

# =========================
# LEGAL AI HELPERS
# =========================
LEGAL_AI_MAX_QUESTION_LEN = 1200


def _contains_arabic(text: str) -> bool:
    return bool(re.search(r"[\u0600-\u06FF]", str(text or "")))


def detect_legal_query_language(text: str) -> str:
    s = str(text or "").strip()

    if not s:
        return get_lang()

    if _contains_arabic(s):
        return "ar"

    s_low = s.lower()

    french_markers = [
        "bonjour", "contrat", "location", "loi", "juridique", "droit",
        "propriété", "terrain", "agricole", "acheter", "vendre",
        "comment", "pourquoi", "puis-je", "puis je", "quelles", "quels",
        "bail", "locataire", "propriétaire", "héritage", "succession"
    ]
    if any(word in s_low for word in french_markers):
        return "fr"

    return "en"


def _legal_lang_name(lang_code: str) -> str:
    if lang_code == "fr":
        return "French"
    if lang_code == "en":
        return "English"
    return "Arabic"


def _legal_section_name(section: str, lang_code: str) -> str:
    section = (section or "").strip().lower()

    names = {
        "ar": {
            "plant": "القسم النباتي",
            "animal": "القسم الحيواني",
        },
        "fr": {
            "plant": "section végétale",
            "animal": "section animale",
        },
        "en": {
            "plant": "plant section",
            "animal": "animal section",
        },
    }

    return names.get(lang_code, names["ar"]).get(section, section)


def _clean_legal_answer_text(text: str) -> str:
    text = str(text or "").strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text[:5000].strip()


def _build_legal_ai_system_prompt(answer_lang: str, section: str) -> str:
    section_name = _legal_section_name(section, answer_lang)
    language_name = _legal_lang_name(answer_lang)

    if answer_lang == "fr":
        return (
            "Tu es un assistant juridique éducatif spécialisé pour la plateforme Green Law. "
            "Réponds uniquement dans le domaine juridique lié au contexte agricole et rural quand c'est pertinent, "
            "mais aide aussi sur les questions juridiques générales en langage simple. "
            f"Réponds uniquement en {language_name}. "
            "Explique de manière claire, structurée et pratique. "
            "Si la situation dépend de documents, de preuves, d'un contrat, d'un acte de propriété ou d'une autorité administrative, dis-le clairement. "
            "Ne prétends jamais être avocat ni autorité officielle. "
            "Ne donne pas de réponse dangereuse ou trompeuse. "
            f"Le contexte de la page actuelle est: {section_name}."
        )

    if answer_lang == "en":
        return (
            "You are an educational legal assistant for the Green Law platform. "
            "Answer only in the legal domain, especially when related to agricultural and rural matters, "
            "but also help with general legal questions in simple language. "
            f"Answer only in {language_name}. "
            "Be clear, practical, and structured. "
            "If the situation depends on documents, evidence, a contract, title deed, or an administrative authority, say that clearly. "
            "Never claim to be a lawyer or an official authority. "
            "Do not provide dangerous or misleading legal claims. "
            f"The current page context is: {section_name}."
        )

    return (
        "أنت مساعد قانوني تعليمي داخل منصة Green Law. "
        "تجيب فقط في المجال القانوني، خاصة إذا كان السؤال مرتبطًا بالسياق الفلاحي أو الريفي، "
        "لكن يمكنك أيضًا شرح المسائل القانونية العامة بلغة بسيطة وواضحة. "
        f"أجب فقط باللغة {language_name}. "
        "اشرح بطريقة مرتبة وعملية وسهلة الفهم. "
        "إذا كانت الحالة تحتاج عقدًا أو وثائق أو إثباتات أو جهة إدارية مختصة أو محامياً، فاذكر ذلك بوضوح. "
        "لا تدّع أنك محامٍ أو جهة رسمية. "
        "لا تعطِ أحكامًا خطيرة أو مضللة. "
        f"السياق الحالي للصفحة هو: {section_name}."
    )


def _call_external_legal_ai(question: str, section: str, answer_lang: str) -> str:
    api_url_template = (os.getenv("LEGAL_AI_API_URL") or "").strip()
    api_key = (os.getenv("LEGAL_AI_API_KEY") or "").strip()
    model = (os.getenv("LEGAL_AI_MODEL") or "gemini-3-flash-preview").strip()

    if not api_url_template or not api_key:
        return ""

    api_url = api_url_template.replace("{model}", model)
    system_prompt = _build_legal_ai_system_prompt(answer_lang, section)

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": (
                            f"{system_prompt}\n\n"
                            f"User question:\n{str(question or '').strip()}"
                        )
                    }
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.2,
            "maxOutputTokens": 1200
        }
    }

    request_data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(
        f"{api_url}?key={api_key}",
        data=request_data,
        method="POST",
        headers={
            "Content-Type": "application/json",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            raw = resp.read().decode("utf-8")
            body = json.loads(raw)

        print("GEMINI RAW RESPONSE:", body)
        print("GEMINI CANDIDATES:", body.get("candidates"))
        print("GEMINI FULL TEXT:", raw)




        candidates = body.get("candidates", [])
        if not candidates:
            print("GEMINI API ERROR: no candidates returned")
            return ""

        parts = candidates[0].get("content", {}).get("parts", [])
        texts = []

        for part in parts:
            txt = str(part.get("text", "")).strip()
            if txt:
                texts.append(txt)

        return _clean_legal_answer_text("\n".join(texts))

    except Exception as e:
        print("GEMINI API ERROR:", str(e))
        return ""


def _build_local_legal_answer(question: str, section: str, answer_lang: str) -> str:
    matches = search_cases(section, question, topn=3)

    if answer_lang == "fr":
        if matches:
            top = matches[0]
            title = str(top.get("title_raw") or top.get("title") or "").strip()
            desc = str(top.get("description_raw") or top.get("description") or "").strip()

            return _clean_legal_answer_text(
                f"Voici l'explication juridique la plus proche de votre question:\n\n"
                f"Sujet concerné: {title}\n\n"
                f"{desc}\n\n"
                f"Conseil pratique:\n"
                f"- Vérifiez les documents et les preuves disponibles.\n"
                f"- Évitez tout accord oral si la situation nécessite un contrat écrit.\n"
                f"- En cas de doute, adressez-vous à l'autorité compétente ou à un professionnel du droit."
            )

        return _clean_legal_answer_text(
            "Je n'ai pas trouvé une réponse juridique très proche dans la base actuelle. "
            "Décrivez votre situation avec plus de détails, par exemple: le type de contrat, le terrain, la vente, la location, les documents disponibles, "
            "ou la nature du litige. En général, il est conseillé de conserver les preuves, vérifier les documents officiels et éviter les accords flous."
        )

    if answer_lang == "en":
        if matches:
            top = matches[0]
            title = str(top.get("title_raw") or top.get("title") or "").strip()
            desc = str(top.get("description_raw") or top.get("description") or "").strip()

            return _clean_legal_answer_text(
                f"Here is the legal explanation closest to your question:\n\n"
                f"Relevant topic: {title}\n\n"
                f"{desc}\n\n"
                f"Practical advice:\n"
                f"- Check the available documents and evidence.\n"
                f"- Avoid relying only on verbal agreements when a written contract is needed.\n"
                f"- If the matter is unclear, contact the competent authority or a legal professional."
            )

        return _clean_legal_answer_text(
            "I could not find a very close legal answer in the current knowledge base. "
            "Please describe your situation with more detail, such as: contract type, land, sale, rental, available documents, or the nature of the dispute. "
            "In general, keep evidence, verify official documents, and avoid unclear agreements."
        )

    if matches:
        top = matches[0]
        title = str(top.get("title_raw") or top.get("title") or "").strip()
        desc = str(top.get("description_raw") or top.get("description") or "").strip()

        return _clean_legal_answer_text(
            f"هذا هو الشرح القانوني الأقرب لسؤالك:\n\n"
            f"الموضوع المرتبط: {title}\n\n"
            f"{desc}\n\n"
            f"نصيحة عملية:\n"
            f"- تأكد من الوثائق والإثباتات المتوفرة.\n"
            f"- لا تعتمد فقط على الاتفاق الشفهي إذا كانت الحالة تحتاج عقدًا مكتوبًا.\n"
            f"- إذا كانت المسألة غير واضحة، راجع الجهة المختصة أو مختصًا قانونيًا."
        )

    return _clean_legal_answer_text(
        "لم أجد جوابًا قانونيًا قريبًا جدًا من سؤالك داخل قاعدة المعلومات الحالية. "
        "حاول أن تشرح الحالة بمزيد من التفاصيل، مثل: هل يتعلق الأمر بعقد، أو بيع، أو شراء، أو كراء، أو ملكية، أو نزاع، أو وثائق رسمية. "
        "وبصفة عامة، من الأفضل الاحتفاظ بالإثباتات، والتحقق من الوثائق الرسمية، وتجنب الاتفاقات غير الواضحة."
    )


def _make_legal_tts_data_url(text: str, lang_code: str) -> str:
    text = str(text or "").strip()
    if not text:
        return ""

    tts_lang = "ar"
    if lang_code == "fr":
        tts_lang = "fr"
    elif lang_code == "en":
        tts_lang = "en"

    try:
        mp3_fp = io.BytesIO()
        gTTS(text=text[:3500], lang=tts_lang).write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        encoded = base64.b64encode(mp3_fp.read()).decode("utf-8")
        return f"data:audio/mpeg;base64,{encoded}"
    except Exception:
        return ""


@app.route("/<section>/legal/ask-ai", methods=["POST"])
def legal_ai_ask(section: str):
    section = (section or "").lower().strip()
    if section not in ("plant", "animal"):
        return jsonify({"ok": False, "error": "invalid_section"}), 400

    data = request.get_json(silent=True) or {}
    question = (data.get("question") or request.form.get("question") or "").strip()

    if not question:
        return jsonify({
            "ok": False,
            "error": t("law.ai_error", default="السؤال فارغ.")
        }), 400

    question = question[:LEGAL_AI_MAX_QUESTION_LEN]
    answer_lang = detect_legal_query_language(question)

    faq_matches = search_faq_cases(section, question, topn=1)
    if faq_matches:
        top = faq_matches[0]
        answer = _clean_legal_answer_text(str(top.get("desc_raw", "")).strip())
        audio_url = _make_legal_tts_data_url(answer, answer_lang)

        return jsonify({
            "ok": True,
            "answer": answer,
            "audio_url": audio_url,
            "lang": answer_lang,
            "source": "faq_cards",
        })

    answer = _call_external_legal_ai(question, section, answer_lang)
    source = "external_ai"

    if not answer:
        answer = _build_local_legal_answer(question, section, answer_lang)
        source = "local_cards"

    answer = _clean_legal_answer_text(answer)
    audio_url = _make_legal_tts_data_url(answer, answer_lang)

    return jsonify({
        "ok": True,
        "answer": answer,
        "audio_url": audio_url,
        "lang": answer_lang,
        "source": source,
    })



@app.route("/<section>/legal")
def legal_home(section: str):
    section = (section or "").lower().strip()
    if section not in ("plant", "animal"):
        return redirect(url_for("sections"))

    cases = build_cases(section)
    return render_template(
        "legal_guide.html",
        title=t("law.title", default="مرشدك القانوني"),
        page_title=t("law.title", default="مرشدك القانوني"),
        section=section,
        cases=cases,
        bg_file="img/bg_legal.jpg",
        back_url=url_for("plant") if section == "plant" else url_for("animal"),
    )


@app.route("/<section>/legal/search", methods=["POST"])
def legal_search(section: str):
    section = (section or "").lower().strip()
    if section not in ("plant", "animal"):
        return redirect(url_for("sections"))

    q = (request.form.get("q") or "").strip()
    results = search_cases(section, q, topn=3) if q else []

    return render_template(
        "legal_search.html",
        title=t("law.search_title", default="بحث قانوني"),
        page_title=t("law.title", default="مرشدك القانوني"),
        section=section,
        query=q,
        results=results,
        bg_file="img/bg_legal.jpg",
        back_url=url_for("legal_home", section=section),
    )


@app.route("/<section>/legal/<case_id>")
def legal_case(section: str, case_id: str):
    section = (section or "").lower().strip()
    if section not in ("plant", "animal"):
        return redirect(url_for("sections"))

    bank = build_cases(section)
    item = next((x for x in bank if x["id"] == case_id), None)
    if not item:
        return redirect(url_for("legal_home", section=section))

    return render_template(
        "legal_case.html",
        title=t("law.title", default="مرشدك القانوني"),
        page_title=t("law.title", default="مرشدك القانوني"),
        section=section,
        case_title=item["title"],
        case_body=item["description"],
        tts_text=item["description_raw"],
        bg_file="img/bg_legal.jpg",
        back_url=url_for("legal_home", section=section),
    )

# ==========================================================
# AGRICULTURAL MARKET (DB VERSION)
# ==========================================================

class MarketAd(db.Model):
    __tablename__ = "market_ads"

    id = db.Column(db.String(120), primary_key=True)
    owner_id = db.Column(db.String(120), nullable=False, index=True)
    owner_username = db.Column(db.String(150), nullable=False, index=True)

    section_key = db.Column(db.String(50), nullable=False, index=True)
    section = db.Column(db.String(120), nullable=False)

    category_key = db.Column(db.String(150), nullable=False, index=True)
    category = db.Column(db.String(255), nullable=False)

    title = db.Column(db.Text, nullable=False)
    price = db.Column(db.String(255), nullable=False, default="—")
    qty = db.Column(db.String(255), nullable=False, default="—")
    wilaya = db.Column(db.String(255), nullable=False, default="—")
    commune = db.Column(db.String(255), nullable=False, default="—")
    phone = db.Column(db.String(255), nullable=False, default="—")

    first_name = db.Column(db.String(255), nullable=False, default="—")
    last_name = db.Column(db.String(255), nullable=False, default="—")
    address = db.Column(db.String(255), nullable=False, default="—")
    desc = db.Column(db.Text, nullable=False, default="—")

    title_key = db.Column(db.String(255), nullable=False, default="")
    price_key = db.Column(db.String(255), nullable=False, default="")
    qty_key = db.Column(db.String(255), nullable=False, default="")
    wilaya_key = db.Column(db.String(255), nullable=False, default="")
    commune_key = db.Column(db.String(255), nullable=False, default="")
    desc_key = db.Column(db.String(255), nullable=False, default="")
    first_name_key = db.Column(db.String(255), nullable=False, default="")
    last_name_key = db.Column(db.String(255), nullable=False, default="")
    address_key = db.Column(db.String(255), nullable=False, default="")

    emoji = db.Column(db.String(30), nullable=False, default="🌿")
    featured = db.Column(db.Boolean, default=False, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, index=True)
    updated_at = db.Column(db.DateTime, nullable=True)


with app.app_context():
    db.create_all()

    inspector = db.inspect(db.engine)
    user_columns = [col["name"] for col in inspector.get_columns("user")]
    alter_statements = []

    private_message_columns = []
    if inspector.has_table("private_message"):
        private_message_columns = [col["name"] for col in inspector.get_columns("private_message")]

    if "is_admin" not in user_columns:
        alter_statements.append('ALTER TABLE "user" ADD COLUMN is_admin BOOLEAN NOT NULL DEFAULT FALSE')

    if "is_active" not in user_columns:
        alter_statements.append('ALTER TABLE "user" ADD COLUMN is_active BOOLEAN NOT NULL DEFAULT TRUE')

    if "last_login_at" not in user_columns:
        alter_statements.append('ALTER TABLE "user" ADD COLUMN last_login_at TIMESTAMP NULL')

    if "consent_status" not in user_columns:
        alter_statements.append('ALTER TABLE "user" ADD COLUMN consent_status VARCHAR(20) NOT NULL DEFAULT \'pending\'')

    if "admin_access_consent" not in user_columns:
        alter_statements.append('ALTER TABLE "user" ADD COLUMN admin_access_consent BOOLEAN NOT NULL DEFAULT FALSE')

    if "consent_updated_at" not in user_columns:
        alter_statements.append('ALTER TABLE "user" ADD COLUMN consent_updated_at TIMESTAMP NULL')

    for sql in alter_statements:
        db.session.execute(db.text(sql))

    if inspector.has_table("private_message") and "message_category" not in private_message_columns:
        db.session.execute(
            db.text("ALTER TABLE private_message ADD COLUMN message_category VARCHAR(50) NOT NULL DEFAULT 'admin_problem'")
        )

    if inspector.has_table("private_message") and "related_ad_id" not in private_message_columns:
        db.session.execute(
            db.text("ALTER TABLE private_message ADD COLUMN related_ad_id VARCHAR(120) NULL")
        )

    db.session.commit()
    db.create_all()

def _now_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


PLANT_CATEGORY_KEYS = [
    "plant.rent_equip",
    "plant.sell_products",
    "plant.inputs",
    "plant.lands_opportunities",
    "plant.plant_health",
    "plant.factory_hotel_partnerships",
]

ANIMAL_CATEGORY_KEYS = [
    "animal.rent_equipment",
    "animal.livestock_market",
    "animal.animal_products",
    "animal.facilities_warehouses",
    "animal.feed",
    "animal.organic_fertilizer",
    "animal.vet_services",
    "animal.factory_hotel_partnerships",
]


def _category_label(cat_key: str) -> str:
    return t(f"market.category.{cat_key}", default=cat_key)


def _section_key_from_app(section):
    s = str(section or "").strip().lower()
    if s in ("plant", "plants", "vegetal", "végétal", "veg", "vegetal"):
        return "plant"
    if s in ("animal", "animals"):
        return "animal"
    if "نبات" in s or "🌱" in s:
        return "plant"
    if "حيوان" in s or "🐄" in s:
        return "animal"
    return "plant"


def _section_label(section_key: str) -> str:
    if section_key == "animal":
        return t("market.section.animal", default="🐄 قسم حيواني")
    return t("market.section.plant", default="🌱 قسم نباتي")


def _get_current_username():
    return (session.get("username") or "guest").strip() or "guest"


def _get_owner_id():
    if session.get("user_id"):
        return str(session.get("user_id"))
    return _get_current_username()


def _make_ad_id(owner_id):
    import uuid
    return f"ad_{owner_id}_{uuid.uuid4().hex}"


def _guess_emoji(section_key, cat_key_or_label):
    emoji = "🌿" if section_key == "plant" else "🐄"
    s = str(cat_key_or_label or "")

    if "rent" in s or "تأجير" in s:
        emoji = "🚜"
    elif "livestock" in s or "حيوانات" in s or "مواشي" in s:
        emoji = "🐑"
    elif "vet" in s or "بيطر" in s:
        emoji = "🩺"
    elif "partnership" in s or "شراكات" in s:
        emoji = "🏭"
    elif "feed" in s or "أعلاف" in s:
        emoji = "🌾"
    elif "fertilizer" in s or "أسمدة" in s or "عضوية" in s:
        emoji = "♻️"
    elif "lands" in s or "أراضي" in s:
        emoji = "🏞️"
    elif "sell_products" in s or "products" in s:
        emoji = "🛒"

    return emoji


def _ad_text(ad, key_field: str, value_field: str, fallback: str = "—") -> str:
    k = str(getattr(ad, key_field, "") or "").strip()
    if k:
        return t(k, default=fallback)
    v = str(getattr(ad, value_field, "") or "").strip()
    return v if v else fallback


def _ad_category_display(ad) -> str:
    ck = str(getattr(ad, "category_key", "") or "").strip()
    if ck:
        return _category_label(ck)
    return str(getattr(ad, "category", "") or t("market.placeholder_dash", default="—"))


def _mask_phone(_phone):
    return t("market.phone_mask", default="0X XX XX XX XX")


def _prepare_ad_view(ad):
    first_name = _ad_text(ad, "first_name_key", "first_name", t("market.placeholder_dash", default="—"))
    last_name = _ad_text(ad, "last_name_key", "last_name", t("market.placeholder_dash", default="—"))

    created_at_value = getattr(ad, "created_at", None)
    updated_at_value = getattr(ad, "updated_at", None)

    created_at_str = created_at_value.strftime("%Y-%m-%d %H:%M") if created_at_value else t("market.placeholder_dash", default="—")
    updated_at_str = updated_at_value.strftime("%Y-%m-%d %H:%M") if updated_at_value else ""

    return {
        "id": ad.id,
        "owner_id": ad.owner_id,
        "owner_username": ad.owner_username,
        "section_key": ad.section_key,
        "category_key": ad.category_key,
        "category_display": _ad_category_display(ad),
        "title": _ad_text(ad, "title_key", "title", t("market.placeholder_dash", default="—")),
        "price": _ad_text(ad, "price_key", "price", t("market.placeholder_dash", default="—")),
        "qty": _ad_text(ad, "qty_key", "qty", t("market.placeholder_dash", default="—")),
        "wilaya": _ad_text(ad, "wilaya_key", "wilaya", t("market.placeholder_dash", default="—")),
        "commune": _ad_text(ad, "commune_key", "commune", t("market.placeholder_dash", default="—")),
        "desc": _ad_text(ad, "desc_key", "desc", t("market.placeholder_dash", default="—")),
        "first_name": first_name,
        "last_name": last_name,
        "full_name": (str(first_name) + " " + str(last_name)).strip(),
        "phone_masked": _mask_phone(ad.phone),
        "emoji": str(ad.emoji or "🌿"),
        "featured": bool(ad.featured),
        "created_at": created_at_str,
        "updated_at": updated_at_str,
    }

def market_seed_examples_once():
    seed_user = User.query.filter_by(username="system").first()
    if not seed_user:
        seed_user = User(
            username="system",
            is_admin=False,
            is_economic_operator=False,
            is_active=True,
            consent_status="accepted",
            admin_access_consent=True,
            consent_updated_at=datetime.utcnow(),
        )
        seed_user.set_password("system123")
        db.session.add(seed_user)
        db.session.commit()

    seed_owner = str(seed_user.id)
    seed_username = seed_user.username

    old_seed_ads = MarketAd.query.filter_by(owner_username="system").all()
    for ad in old_seed_ads:
        db.session.delete(ad)
    db.session.commit()

    def _seed_identity_fields():
        return {
            "first_name_key": "market.seed.name_placeholder",
            "last_name_key": "market.seed.name_placeholder",
            "address_key": "market.seed.address_placeholder",
            "first_name": "",
            "last_name": "",
            "address": "",
        }

    demo = [
        {
            "id": _make_ad_id(seed_owner),
            "owner_id": seed_owner,
            "owner_username": seed_username,
            "section_key": "plant",
            "section": _section_label("plant"),
            "category_key": "plant.sell_products",
            "category": "",
            "title_key": "market.seed.plant.potato.title",
            "price_key": "market.seed.plant.potato.price",
            "qty_key": "market.seed.plant.potato.qty",
            "wilaya_key": "market.seed.plant.potato.wilaya",
            "commune_key": "market.seed.plant.potato.commune",
            "desc_key": "market.seed.plant.potato.desc",
            "title": "", "price": "", "qty": "", "wilaya": "", "commune": "", "desc": "",
            "phone": "0000000000",
            **_seed_identity_fields(),
            "emoji": "🥔",
            "featured": True,
        },
        {
            "id": _make_ad_id(seed_owner),
            "owner_id": seed_owner,
            "owner_username": seed_username,
            "section_key": "plant",
            "section": _section_label("plant"),
            "category_key": "plant.rent_equip",
            "category": "",
            "title_key": "market.seed.plant.tractor.title",
            "price_key": "market.seed.plant.tractor.price",
            "qty_key": "market.seed.qty_placeholder",
            "wilaya_key": "market.seed.plant.tractor.wilaya",
            "commune_key": "market.seed.plant.tractor.commune",
            "desc_key": "market.seed.plant.tractor.desc",
            "title": "", "price": "", "qty": "", "wilaya": "", "commune": "", "desc": "",
            "phone": "0000000000",
            **_seed_identity_fields(),
            "emoji": "🚜",
            "featured": False,
        },
        {
            "id": _make_ad_id(seed_owner),
            "owner_id": seed_owner,
            "owner_username": seed_username,
            "section_key": "plant",
            "section": _section_label("plant"),
            "category_key": "plant.inputs",
            "category": "",
            "title_key": "market.seed.plant.seedlings.title",
            "price_key": "market.seed.plant.seedlings.price",
            "qty_key": "market.seed.plant.seedlings.qty",
            "wilaya_key": "market.seed.plant.seedlings.wilaya",
            "commune_key": "market.seed.plant.seedlings.commune",
            "desc_key": "market.seed.plant.seedlings.desc",
            "title": "", "price": "", "qty": "", "wilaya": "", "commune": "", "desc": "",
            "phone": "0000000000",
            **_seed_identity_fields(),
            "emoji": "🌱",
            "featured": False,
        },
        {
            "id": _make_ad_id(seed_owner),
            "owner_id": seed_owner,
            "owner_username": seed_username,
            "section_key": "plant",
            "section": _section_label("plant"),
            "category_key": "plant.factory_hotel_partnerships",
            "category": "",
            "title_key": "market.seed.plant.contract.title",
            "price_key": "market.seed.plant.contract.price",
            "qty_key": "market.seed.plant.contract.qty",
            "wilaya_key": "market.seed.plant.contract.wilaya",
            "commune_key": "market.seed.plant.contract.commune",
            "desc_key": "market.seed.plant.contract.desc",
            "title": "", "price": "", "qty": "", "wilaya": "", "commune": "", "desc": "",
            "phone": "0000000000",
            **_seed_identity_fields(),
            "emoji": "🏭",
            "featured": True,
        },
        {
            "id": _make_ad_id(seed_owner),
            "owner_id": seed_owner,
            "owner_username": seed_username,
            "section_key": "animal",
            "section": _section_label("animal"),
            "category_key": "animal.livestock_market",
            "category": "",
            "title_key": "market.seed.animal.ram.title",
            "price_key": "market.seed.animal.ram.price",
            "qty_key": "market.seed.animal.ram.qty",
            "wilaya_key": "market.seed.animal.ram.wilaya",
            "commune_key": "market.seed.animal.ram.commune",
            "desc_key": "market.seed.animal.ram.desc",
            "title": "", "price": "", "qty": "", "wilaya": "", "commune": "", "desc": "",
            "phone": "0000000000",
            **_seed_identity_fields(),
            "emoji": "🐑",
            "featured": True,
        },
        {
            "id": _make_ad_id(seed_owner),
            "owner_id": seed_owner,
            "owner_username": seed_username,
            "section_key": "animal",
            "section": _section_label("animal"),
            "category_key": "animal.animal_products",
            "category": "",
            "title_key": "market.seed.animal.eggs.title",
            "price_key": "market.seed.animal.eggs.price",
            "qty_key": "market.seed.animal.eggs.qty",
            "wilaya_key": "market.seed.animal.eggs.wilaya",
            "commune_key": "market.seed.animal.eggs.commune",
            "desc_key": "market.seed.animal.eggs.desc",
            "title": "", "price": "", "qty": "", "wilaya": "", "commune": "", "desc": "",
            "phone": "0000000000",
            **_seed_identity_fields(),
            "emoji": "🥚",
            "featured": False,
        },
        {
            "id": _make_ad_id(seed_owner),
            "owner_id": seed_owner,
            "owner_username": seed_username,
            "section_key": "animal",
            "section": _section_label("animal"),
            "category_key": "animal.vet_services",
            "category": "",
            "title_key": "market.seed.animal.vet.title",
            "price_key": "market.seed.animal.vet.price",
            "qty_key": "market.seed.animal.vet.qty",
            "wilaya_key": "market.seed.animal.vet.wilaya",
            "commune_key": "market.seed.animal.vet.commune",
            "desc_key": "market.seed.animal.vet.desc",
            "title": "", "price": "", "qty": "", "wilaya": "", "commune": "", "desc": "",
            "phone": "0000000000",
            **_seed_identity_fields(),
            "emoji": "🩺",
            "featured": True,
        },
        {
            "id": _make_ad_id(seed_owner),
            "owner_id": seed_owner,
            "owner_username": seed_username,
            "section_key": "animal",
            "section": _section_label("animal"),
            "category_key": "animal.factory_hotel_partnerships",
            "category": "",
            "title_key": "market.seed.animal.milk_contract.title",
            "price_key": "market.seed.animal.milk_contract.price",
            "qty_key": "market.seed.animal.milk_contract.qty",
            "wilaya_key": "market.seed.animal.milk_contract.wilaya",
            "commune_key": "market.seed.animal.milk_contract.commune",
            "desc_key": "market.seed.animal.milk_contract.desc",
            "title": "", "price": "", "qty": "", "wilaya": "", "commune": "", "desc": "",
            "phone": "0000000000",
             **_seed_identity_fields(),
            "emoji": "🥛",
            "featured": False,
        },
    ]

    for row in demo:
        db.session.add(MarketAd(**row))

    db.session.commit()


def _list_ads_for(section_key, category_key=None):
    q = MarketAd.query.filter_by(section_key=section_key)

    if category_key:
        q = q.filter_by(category_key=category_key)

    return q.order_by(MarketAd.created_at.desc()).all()


def _list_featured_for(section_key, limit=4):
    return (
        MarketAd.query
        .filter_by(section_key=section_key, featured=True)
        .order_by(MarketAd.created_at.desc())
        .limit(limit)
        .all()
    )


def _categories_for(section_key):
    keys = PLANT_CATEGORY_KEYS if section_key == "plant" else ANIMAL_CATEGORY_KEYS
    return [
        {
            "key": k,
            "label": _category_label(k),
            "emoji": _guess_emoji(section_key, k),
        }
        for k in keys
    ]


@app.route("/<section>/market")
def market_home(section):
    if not is_logged_in():
        return redirect(url_for("login"))

    current_user = get_effective_user()
    if not current_user:
        return redirect(url_for("login"))

    market_seed_examples_once()
    section_key = _section_key_from_app(section)
    cats = _categories_for(section_key)
    featured_ads = [_prepare_ad_view(a) for a in _list_featured_for(section_key, limit=4)]

    if current_user.is_economic_operator:
        back_url = url_for("economic_operator_home")
    else:
        back_url = url_for("plant") if section_key == "plant" else url_for("animal")

    return render_template(
        "market_home.html",
        title=t("market.title", default="السوق الفلاحي"),
        page_title=t("market.title", default="السوق الفلاحي"),
        section=section_key,
        section_label=_section_label(section_key),
        categories=cats,
        featured_ads=featured_ads,
        back_url=back_url,
    )


@app.route("/<section>/market/category/<path:category_key>")
def market_category(section, category_key):
    if not is_logged_in():
        return redirect(url_for("login"))

    current_user = get_effective_user()
    if not current_user:
        return redirect(url_for("login"))

    market_seed_examples_once()
    section_key = _section_key_from_app(section)
    ads = [_prepare_ad_view(a) for a in _list_ads_for(section_key, category_key)]

    return render_template(
        "market_list.html",
        title=t("market.title", default="السوق الفلاحي"),
        page_title=_category_label(category_key),
        section=section_key,
        section_label=_section_label(section_key),
        category_key=category_key,
        ads=ads,
        owner_view=False,
        back_url=url_for("market_home", section=section_key),
    )


@app.route("/<section>/market/my")
def market_my_ads(section):
    if not is_logged_in():
        return redirect(url_for("login"))

    current_user = get_effective_user()
    if not current_user:
        return redirect(url_for("login"))

    market_seed_examples_once()
    section_key = _section_key_from_app(section)
    owner_id = str(current_user.id)

    mine = (
        MarketAd.query
        .filter_by(owner_id=owner_id, section_key=section_key)
        .order_by(MarketAd.created_at.desc())
        .all()
    )

    return render_template(
        "market_list.html",
        title=t("market.my_ads_title", default="إعلاناتي"),
        page_title=t("market.my_ads_title", default="إعلاناتي"),
        section=section_key,
        section_label=_section_label(section_key),
        category_key="",
        ads=[_prepare_ad_view(a) for a in mine],
        owner_view=True,
        back_url=url_for("market_home", section=section_key),
    )


@app.route("/<section>/market/new", methods=["GET", "POST"])
def market_add_page(section):
    if not is_logged_in():
        return redirect(url_for("login"))

    current_user = get_effective_user()
    if not current_user:
        return redirect(url_for("login"))

    market_seed_examples_once()
    section_key = _section_key_from_app(section)
    categories = _categories_for(section_key)

    if request.method == "POST":
        owner_id = str(current_user.id)
        username = current_user.username

        category_key = (request.form.get("category_key") or "").strip()
        title = (request.form.get("title") or "").strip()
        price = (request.form.get("price") or "").strip()
        qty = (request.form.get("qty") or "").strip()
        wilaya = (request.form.get("wilaya") or "").strip()
        commune = (request.form.get("commune") or "").strip()
        phone = (request.form.get("phone") or "").strip()
        first_name = (request.form.get("first_name") or "").strip()
        last_name = (request.form.get("last_name") or "").strip()
        address = (request.form.get("address") or "").strip()
        desc = (request.form.get("desc") or "").strip()
        featured = bool(request.form.get("featured"))

        if not title or not commune or not category_key:
            return render_template(
                "market_form.html",
                title=t("market.add_new", default="إضافة إعلان"),
                page_title=t("market.add_new", default="إضافة إعلان"),
                section=section_key,
                categories=categories,
                ad=request.form,
                back_url=url_for("market_home", section=section_key),
                form_error=t("market.required_error", default="❌ العنوان والبلدية والتصنيف ضروريين."),
            )

        ad = MarketAd(
            id=_make_ad_id(owner_id),
            owner_id=owner_id,
            owner_username=username,
            section_key=section_key,
            section=_section_label(section_key),
            category_key=category_key,
            category=_category_label(category_key),
            title=title,
            price=price if price else t("market.placeholder_dash", default="—"),
            qty=qty if qty else t("market.placeholder_dash", default="—"),
            wilaya=wilaya if wilaya else t("market.placeholder_dash", default="—"),
            commune=commune,
            phone=phone if phone else t("market.placeholder_dash", default="—"),
            first_name=first_name if first_name else t("market.placeholder_dash", default="—"),
            last_name=last_name if last_name else t("market.placeholder_dash", default="—"),
            address=address if address else t("market.placeholder_dash", default="—"),
            desc=desc if desc else t("market.placeholder_dash", default="—"),
            title_key="",
            price_key="",
            qty_key="",
            wilaya_key="",
            commune_key="",
            desc_key="",
            first_name_key="",
            last_name_key="",
            address_key="",
            emoji=_guess_emoji(section_key, category_key),
            featured=featured,
        )

        db.session.add(ad)
        db.session.commit()

        return redirect(url_for("market_my_ads", section=section_key))

    return render_template(
        "market_form.html",
        title=t("market.add_new", default="إضافة إعلان"),
        page_title=t("market.add_new", default="إضافة إعلان"),
        section=section_key,
        categories=categories,
        ad={},
        back_url=url_for("market_home", section=section_key),
        form_error="",
    )


@app.route("/<section>/market/ad/<ad_id>/edit", methods=["GET", "POST"])
def market_edit_page(section, ad_id):
    if not is_logged_in():
        return redirect(url_for("login"))

    current_user = get_effective_user()
    if not current_user:
        return redirect(url_for("login"))

    section_key = _section_key_from_app(section)
    categories = _categories_for(section_key)
    owner_id = str(current_user.id)

    item = MarketAd.query.filter_by(id=ad_id, owner_id=owner_id).first()
    if not item:
        return redirect(url_for("market_my_ads", section=section_key))

    if request.method == "POST":
        category_key = (request.form.get("category_key") or "").strip()
        item.category_key = category_key
        item.title = (request.form.get("title") or "").strip() or item.title
        item.first_name = (request.form.get("first_name") or "").strip() or item.first_name
        item.last_name = (request.form.get("last_name") or "").strip() or item.last_name
        item.category = _category_label(category_key)
        item.wilaya = (request.form.get("wilaya") or "").strip() or item.wilaya
        item.commune = (request.form.get("commune") or "").strip() or item.commune
        item.address = (request.form.get("address") or "").strip() or item.address
        item.phone = (request.form.get("phone") or "").strip() or item.phone
        item.desc = (request.form.get("desc") or "").strip() or item.desc
        item.price = (request.form.get("price") or "").strip() or item.price
        item.qty = (request.form.get("qty") or "").strip() or item.qty
        item.featured = bool(request.form.get("featured"))
        item.emoji = _guess_emoji(section_key, category_key)
        item.updated_at = datetime.utcnow()

        db.session.commit()

        return redirect(url_for("market_my_ads", section=section_key))

    ad_data = {
        "id": item.id,
        "category_key": item.category_key,
        "title": item.title,
        "price": item.price,
        "qty": item.qty,
        "wilaya": item.wilaya,
        "commune": item.commune,
        "phone": item.phone,
        "first_name": item.first_name,
        "last_name": item.last_name,
        "address": item.address,
        "desc": item.desc,
        "featured": item.featured,
    }

    return render_template(
        "market_form.html",
        title=t("market.edit", default="تعديل الإعلان"),
        page_title=t("market.edit", default="تعديل الإعلان"),
        section=section_key,
        categories=categories,
        ad=ad_data,
        back_url=url_for("market_my_ads", section=section_key),
        form_error="",
    )


@app.route("/<section>/market/ad/<ad_id>/delete", methods=["POST"])
def market_delete_page(section, ad_id):
    if not is_logged_in():
        return redirect(url_for("login"))

    current_user = get_effective_user()
    if not current_user:
        return redirect(url_for("login"))

    section_key = _section_key_from_app(section)
    owner_id = str(current_user.id)

    item = MarketAd.query.filter_by(id=ad_id, owner_id=owner_id).first()
    if item:
        db.session.delete(item)
        db.session.commit()

    return redirect(url_for("market_my_ads", section=section_key))
# ==========================================================
# FARMER PASSPORT (DB VERSION)
# ==========================================================
PASSPORT_DIR = os.path.join(app.root_path, "passport_data")
os.makedirs(PASSPORT_DIR, exist_ok=True)


class PassportDocument(db.Model):
    __tablename__ = "passport_documents"

    id = db.Column(db.String(150), primary_key=True)
    user_id = db.Column(db.String(120), nullable=False, index=True)
    username = db.Column(db.String(150), nullable=False, index=True)

    section = db.Column(db.String(20), nullable=False, index=True)
    title = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False, index=True)
    src_type = db.Column(db.String(100), nullable=False)

    original_filename = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.Text, nullable=False)
    qr_path = db.Column(db.Text, nullable=False, default="")

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, index=True)


with app.app_context():
    db.create_all()


def passport_user_dir(user_id):
    p = os.path.join(PASSPORT_DIR, f"user_{user_id}")
    os.makedirs(p, exist_ok=True)
    os.makedirs(os.path.join(p, "files"), exist_ok=True)
    os.makedirs(os.path.join(p, "qr"), exist_ok=True)
    return p


def _safe_filename(name: str) -> str:
    s = str(name).strip()
    for ch in ['/', '\\', ':', '*', '?', '"', '<', '>', '|']:
        s = s.replace(ch, "_")
    return s[:120] if len(s) > 120 else s


def _get_doc_year(doc):
    y = getattr(doc, "year", None)
    if isinstance(y, int):
        return y
    if isinstance(y, str) and y.isdigit():
        return int(y)

    created = getattr(doc, "created_at", None)
    if created:
        try:
            return int(created.strftime("%Y"))
        except Exception:
            pass
    return None


def _make_qr_image(qr_path: str, qr_data: str) -> bool:
    try:
        import qrcode
        img = qrcode.make(qr_data)
        img.save(qr_path)
        return True
    except Exception:
        return False


def _ensure_qr_for_doc(doc):
    qr_path = getattr(doc, "qr_path", "") or ""
    file_path = getattr(doc, "file_path", "") or ""

    if file_path and (not qr_path or not os.path.exists(qr_path)):
        try:
            udir = os.path.dirname(os.path.dirname(file_path))
            qr_dir = os.path.join(udir, "qr")
            os.makedirs(qr_dir, exist_ok=True)

            base = os.path.splitext(os.path.basename(file_path))[0]
            new_qr_path = os.path.join(qr_dir, f"{base}.png")

            ok = _make_qr_image(new_qr_path, f"OPEN::{file_path}")
            if ok:
                doc.qr_path = new_qr_path
                db.session.commit()
        except Exception:
            pass

    return doc


def _get_user_id_for_passport():
    if session.get("user_id"):
        return str(session.get("user_id"))

    username = (session.get("username") or "").strip()
    if not username:
        return None

    return str(username)


def _get_username_for_passport():
    return (session.get("username") or "guest").strip() or "guest"


def _make_passport_doc_id(user_id: str) -> str:
    import uuid
    return f"passport_{user_id}_{uuid.uuid4().hex}"


def _add_document_record(user_id, username, section, title, src_type, uploaded_file):
    year = datetime.now().year
    safe_title = _safe_filename(title) if title else f"Document_{year}"
    doc_id = _make_passport_doc_id(user_id)

    udir = passport_user_dir(user_id)
    files_dir = os.path.join(udir, "files")
    qr_dir = os.path.join(udir, "qr")

    original_filename = uploaded_file.filename or "file.bin"
    ext = os.path.splitext(original_filename)[1].lower()
    if ext not in [".pdf", ".png", ".jpg", ".jpeg", ".txt"]:
        ext = ".txt"

    final_path = os.path.join(files_dir, f"{doc_id}{ext}")
    uploaded_file.save(final_path)

    qr_path = os.path.join(qr_dir, f"{doc_id}.png")
    qr_ok = _make_qr_image(qr_path, f"OPEN::{final_path}")
    if not qr_ok:
        qr_path = ""

    doc = PassportDocument(
        id=doc_id,
        user_id=str(user_id),
        username=str(username),
        section=str(section),
        title=safe_title,
        year=year,
        src_type=src_type,
        original_filename=original_filename,
        file_path=final_path,
        qr_path=qr_path,
    )

    db.session.add(doc)
    db.session.commit()


def _passport_docs_view(user_id, section, year_query=""):
    q = PassportDocument.query.filter_by(user_id=str(user_id), section=str(section))

    if year_query and str(year_query).strip().isdigit():
        q = q.filter_by(year=int(str(year_query).strip()))

    docs = q.order_by(PassportDocument.year.desc(), PassportDocument.created_at.desc()).all()

    for d in docs:
        _ensure_qr_for_doc(d)

    return docs


def _passport_doc_to_view(doc):
    created = getattr(doc, "created_at", None)
    created_str = created.strftime("%Y-%m-%d %H:%M") if created else ""

    return {
        "id": doc.id,
        "title": doc.title,
        "year": doc.year,
        "type": doc.src_type,
        "original_path": doc.original_filename,
        "file_path": doc.file_path,
        "qr_path": doc.qr_path,
        "created_at": created_str,
    }


@app.route("/<section>/passport")
def passport_home(section):
    if not is_logged_in():
        return redirect(url_for("login"))

    section = (section or "").strip().lower()
    if section not in ("plant", "animal"):
        return redirect(url_for("sections"))

    user_id = _get_user_id_for_passport()
    if not user_id:
        return redirect(url_for("login"))

    docs = _passport_docs_view(user_id, section)

    return render_template(
        "passport_home.html",
        title=t("passport.menu_title", default="جواز الفلاح"),
        page_title=t("passport.menu_title", default="جواز الفلاح"),
        section=section,
        docs=[_passport_doc_to_view(d) for d in docs[:6]],
        back_url=url_for("plant") if section == "plant" else url_for("animal"),
    )


@app.route("/<section>/passport/files")
def passport_files(section):
    if not is_logged_in():
        return redirect(url_for("login"))

    section = (section or "").strip().lower()
    if section not in ("plant", "animal"):
        return redirect(url_for("sections"))

    user_id = _get_user_id_for_passport()
    if not user_id:
        return redirect(url_for("login"))

    year_q = (request.args.get("year") or "").strip()
    docs = _passport_docs_view(user_id, section, year_q)

    return render_template(
        "passport_files.html",
        title=t("passport.myfiles_title", default="ملفاتي"),
        page_title=t("passport.myfiles_title", default="ملفاتي"),
        section=section,
        docs=[_passport_doc_to_view(d) for d in docs],
        year_q=year_q,
        back_url=url_for("passport_home", section=section),
    )


@app.route("/<section>/passport/add", methods=["GET", "POST"])
def passport_add(section):
    if not is_logged_in():
        return redirect(url_for("login"))

    section = (section or "").strip().lower()
    if section not in ("plant", "animal"):
        return redirect(url_for("sections"))

    user_id = _get_user_id_for_passport()
    username = _get_username_for_passport()
    if not user_id:
        return redirect(url_for("login"))

    if request.method == "POST":
        title = (request.form.get("title") or "").strip()
        src_type = (request.form.get("src_type") or "").strip()
        file = request.files.get("file")

        if not title or not src_type or file is None or not file.filename:
            return render_template(
                "passport_add.html",
                title=t("passport.add_title", default="إضافة ملف جديد"),
                page_title=t("passport.add_title", default="إضافة ملف جديد"),
                section=section,
                back_url=url_for("passport_home", section=section),
                form_error=t("passport.not_found", default="❌ الملف غير موجود."),
            )

        _add_document_record(user_id, username, section, title, src_type, file)
        return redirect(url_for("passport_files", section=section))

    return render_template(
        "passport_add.html",
        title=t("passport.add_title", default="إضافة ملف جديد"),
        page_title=t("passport.add_title", default="إضافة ملف جديد"),
        section=section,
        back_url=url_for("passport_home", section=section),
        form_error="",
    )


@app.route("/<section>/passport/qr")
def passport_qr_gallery_page(section):
    if not is_logged_in():
        return redirect(url_for("login"))

    section = (section or "").strip().lower()
    if section not in ("plant", "animal"):
        return redirect(url_for("sections"))

    user_id = _get_user_id_for_passport()
    if not user_id:
        return redirect(url_for("login"))

    year_q = (request.args.get("year") or "").strip()
    docs = _passport_docs_view(user_id, section, year_q)

    return render_template(
        "passport_qr.html",
        title=t("passport.qr_gallery_title", default="معرض أكواد QR"),
        page_title=t("passport.qr_gallery_title", default="معرض أكواد QR"),
        section=section,
        docs=[_passport_doc_to_view(d) for d in docs],
        year_q=year_q,
        back_url=url_for("passport_home", section=section),
    )


@app.route("/<section>/passport/open/<doc_id>")
def passport_open_doc(section, doc_id):
    if not is_logged_in():
        return redirect(url_for("login"))

    section = (section or "").strip().lower()
    if section not in ("plant", "animal"):
        return redirect(url_for("sections"))

    user_id = _get_user_id_for_passport()
    if not user_id:
        return redirect(url_for("login"))

    doc = PassportDocument.query.filter_by(
        id=doc_id,
        user_id=str(user_id),
        section=str(section)
    ).first()

    if not doc:
        return redirect(url_for("passport_home", section=section))

    file_path = doc.file_path
    if not file_path or not os.path.exists(file_path):
        return redirect(url_for("passport_home", section=section))

    return send_file(file_path, as_attachment=False)
@app.route("/<section>/passport/qr-image/<doc_id>")
def passport_qr_image(section, doc_id):
    if not is_logged_in():
        return redirect(url_for("login"))

    section = (section or "").strip().lower()
    if section not in ("plant", "animal"):
        return redirect(url_for("sections"))

    user_id = _get_user_id_for_passport()
    if not user_id:
        return redirect(url_for("login"))

    doc = PassportDocument.query.filter_by(
        id=doc_id,
        user_id=str(user_id),
        section=str(section)
    ).first()

    if not doc:
        return redirect(url_for("passport_qr_gallery_page", section=section))

    qr_path = doc.qr_path
    if not qr_path or not os.path.exists(qr_path):
        return redirect(url_for("passport_qr_gallery_page", section=section))

    return send_file(qr_path, as_attachment=False)
# ==============================
# SMART MAPS (WEB)
# ==============================
def _sm_t(key: str, default: str = "") -> str:

    """

    Safe translator:

    - يستعمل t() إذا كانت موجودة

    - إذا ماكانش key يرجع default

    - إذا صار اختلاف في signature تاع t ما يطيحش

    """

    try:

        value = t(key, default)

    except TypeError:

        try:

            value = t(key, default=default)

        except Exception:

            try:

                value = t(key)

            except Exception:

                value = default

    except Exception:

        value = default



    if value in (None, "", key):

        return default

    return str(value)





def _smart_map_lang() -> str:

    try:

        lang = get_lang()

    except Exception:

        lang = session.get("lang", "ar")



    lang = str(lang or "ar").strip().lower()

    return lang if lang in ("ar", "fr", "en") else "ar"





def _smart_map_dir() -> str:

    return "rtl" if _smart_map_lang() == "ar" else "ltr"





def _smart_map_sections_url() -> str:

    """

    يرجع رابط صفحة sections حتى لو endpoint اختلف.

    """

    for endpoint in ("sections", "section"):

        try:

            return url_for(endpoint)

        except Exception:

            pass

    return "/sections"





def _smart_map_section_label(section: str) -> str:

    if section == "plant":

        return _sm_t("smart_map.section.plant", "قسم نباتي")

    return _sm_t("smart_map.section.animal", "قسم حيواني")





def _send_pdf_download(pdf_path: str, filename: str):

    """

    توافق مع Flask الجديد والقديم.

    """

    try:

        return send_file(pdf_path, as_attachment=True, download_name=filename)

    except TypeError:

        return send_file(pdf_path, as_attachment=True, attachment_filename=filename)





def map_file(name: str) -> str:

    """

    ملف HTML للخريطة حسب اللغة الحالية.

    """

    lang_code = _smart_map_lang()

    return os.path.join(MAPS_DIR, f"{name}_{lang_code}.html")





def map_pdf_file(name: str) -> str:

    """

    ملف PDF للخريطة حسب اللغة الحالية.

    """

    lang_code = _smart_map_lang()

    return os.path.join(MAPS_DIR, f"{name}_{lang_code}.pdf")





# --------------------------------------------------

# Colors

# --------------------------------------------------

def _color_for_map(map_key: str) -> str:

    return {

        "water": "blue",

        "agri": "green",

        "milk": "lightgray",

        "honey": "orange",

        "wool": "purple",

        "meat": "red",

    }.get(map_key, "red")





# --------------------------------------------------

# Wilaya centers (stable ids)

# --------------------------------------------------

WILAYA_CENTERS = {

    "oulad_djellal": (34.4167, 5.0667),

    "ouargla": (31.9500, 5.3167),

    "timimoun": (29.2630, 0.2300),

    "ain_salah": (27.1935, 2.4679),

    "touggourt": (33.1000, 6.0667),

    "bechar": (31.6167, -2.2167),

    "blida": (36.4700, 2.8300),

    "algiers": (36.7538, 3.0588),

    "boumerdes": (36.7667, 3.4833),

    "medea": (36.2667, 2.7500),

    "ain_defla": (36.2667, 1.9667),

    "tipaza": (36.6000, 2.4500),

    "chlef": (36.1667, 1.3333),

    "illizi": (26.5000, 8.4667),

    "hassi_messaoud": (31.6800, 6.0700),

    "hassi_rmel": (32.9300, 3.3000),



    "djelfa": (34.6667, 3.2500),

    "tiaret": (35.3700, 1.3200),

    "el_bayadh": (33.6833, 1.0167),

    "naama": (33.2667, -0.3167),

    "bouira": (36.3667, 3.9000),

    "batna": (35.5500, 6.1667),

    "setif": (36.1833, 5.4167),

    "mila": (36.4500, 6.2667),

    "tizi_ouzou": (36.7167, 4.0500),

    "tlemcen": (34.8783, -1.3150),

    "bordj_bou_arreridj": (36.0667, 4.7667),

    "mascara": (35.4000, 0.1500),

    "msila": (35.7000, 4.5500),



    "el_tarf": (36.7667, 8.3167),

    "khenchela": (35.4333, 7.1500),

    "ghardaia": (32.4833, 3.6833),

    "annaba": (36.9000, 7.7667),

    "skikda": (36.8667, 6.9000),

    "laghouat": (33.8000, 2.8667),

    "jijel": (36.8167, 5.7500),

    "mostaganem": (35.9333, 0.0833),

    "constantine": (36.3667, 6.6167),



    "bejaia": (36.7500, 5.0667),

    "oran": (35.7000, -0.6333),

    "oum_el_bouaghi": (35.8833, 7.1167),

    "tebessa": (35.4000, 8.1167),

    "tissemsilt": (35.6000, 1.8167),

    "biskra": (34.8500, 5.7333),

    "el_oued": (33.3667, 6.8667),

    "adrar": (27.8700, -0.2800),

    "sidi_bel_abbes": (35.2000, -0.6333),

    "relizane": (35.7370, 0.5550),

    "guelma": (36.4667, 7.4333),

    "souk_ahras": (36.2833, 7.9500),

}





def wilaya_label(wid: str) -> str:

    fallback = wid.replace("_", " ").title()

    return _sm_t(f"wilaya.{wid}", fallback)





def _to_point(wid: str, desc: str, label_override: str = None):

    coords = WILAYA_CENTERS.get(wid)

    if not coords:

        return None



    return {

        "id": wid,

        "name": label_override or wilaya_label(wid),

        "coords": coords,

        "description": desc,

    }





# --------------------------------------------------

# Stable data

# --------------------------------------------------

WATER_LIST = [

    "oulad_djellal", "ouargla", "timimoun", "ain_salah", "touggourt", "bechar", "blida",

    "algiers", "boumerdes", "medea", "ain_defla", "tipaza",

    "hassi_messaoud", "chlef", "illizi", "hassi_rmel"

]



MEAT_LIST = [

    "djelfa", "tiaret", "el_bayadh", "naama", "bouira", "batna", "setif", "medea",

    "mila", "tizi_ouzou", "tlemcen", "bordj_bou_arreridj", "ain_defla", "mascara", "msila"

]



WOOL_LIST = [

    "djelfa", "el_tarf", "khenchela", "ouargla", "tizi_ouzou", "setif", "ghardaia", "batna", "annaba"

]



HONEY_LIST = [

    "skikda", "tipaza", "setif", "tiaret", "laghouat", "msila", "boumerdes",

    "ouargla", "ghardaia", "jijel", "djelfa", "mostaganem", "constantine"

]



MILK_LIST = [

    "bejaia", "algiers", "oran", "blida", "tizi_ouzou", "setif", "constantine", "jijel",

    "tlemcen", "skikda", "oum_el_bouaghi", "ghardaia", "msila", "tebessa",

    "tissemsilt", "tiaret", "biskra", "djelfa", "el_bayadh", "laghouat", "ouargla", "annaba"

]



AGRI_RAW = [

    ("algiers", "maps.agri.metidja"),

    ("blida", "maps.agri.metidja"),

    ("ain_defla", "maps.agri.veg_cereals"),

    ("oran", "maps.agri.veg_cereals"),

    ("chlef", "maps.agri.veg_cereals"),

    ("annaba", "maps.agri.fruits"),

    ("bejaia", "maps.agri.fruits"),

    ("setif", "maps.agri.wheat_barley"),

    ("el_oued", "maps.agri.potato_dates"),

    ("biskra", "maps.agri.dates_veg"),

    ("ouargla", "maps.agri.cereals"),

    ("ghardaia", "maps.agri.cereals"),

    ("adrar", "maps.agri.cereals"),

]





def _agri_desc_default(desc_key: str) -> str:

    return {

        "maps.agri.metidja": "متيجة: خضر وفواكه وزراعة مكثفة",

        "maps.agri.veg_cereals": "خضر وحبوب ومناطق زراعية متنوعة",

        "maps.agri.fruits": "فواكه وأشجار مثمرة",

        "maps.agri.wheat_barley": "قمح وشعير",

        "maps.agri.potato_dates": "بطاطا وتمور",

        "maps.agri.dates_veg": "تمور وخضر",

        "maps.agri.cereals": "حبوب وزراعات صحراوية",

    }.get(desc_key, desc_key)





def _build_points():

    d_water = _sm_t("maps.desc.water", "مياه الآبار")

    d_meat = _sm_t("maps.desc.meat", "إنتاج اللحوم")

    d_wool = _sm_t("maps.desc.wool", "إنتاج الصوف")

    d_honey = _sm_t("maps.desc.honey", "إنتاج العسل الحر")

    d_milk = _sm_t("maps.desc.milk", "إنتاج الحليب ومشتقاته")



    points_water = [p for p in (_to_point(w, d_water) for w in WATER_LIST) if p]

    points_meat = [p for p in (_to_point(w, d_meat) for w in MEAT_LIST) if p]

    points_wool = [p for p in (_to_point(w, d_wool) for w in WOOL_LIST) if p]

    points_honey = [p for p in (_to_point(w, d_honey) for w in HONEY_LIST) if p]

    points_milk = [p for p in (_to_point(w, d_milk) for w in MILK_LIST) if p]



    points_agri = []

    for wid, desc_key in AGRI_RAW:

        desc = _sm_t(desc_key, _agri_desc_default(desc_key))

        p = _to_point(wid, desc)

        if p:

            points_agri.append(p)



    return points_water, points_agri, points_wool, points_honey, points_milk, points_meat





def _warn_missing(ids, label_key):

    miss = [x for x in ids if x not in WILAYA_CENTERS]

    if miss:

        print(_sm_t("maps.warn.missing_prefix", "⚠️ أسماء ناقصة في WILAYA_CENTERS: ") + f"{label_key}: " + ", ".join(miss))





def _legend_label(map_key: str) -> str:

    return {

        "water": _sm_t("maps.legend.water", "💧 مياه الآبار"),

        "agri": _sm_t("maps.legend.agri", "🌿 مناطق زراعية"),

        "honey": _sm_t("maps.legend.honey", "🍯 عسل"),

        "wool": _sm_t("maps.legend.wool", "🧶 صوف"),

        "milk": _sm_t("maps.legend.milk", "🥛 حليب"),

        "meat": _sm_t("maps.legend.meat", "🥩 لحوم"),

    }.get(map_key, _sm_t("maps.legend.default", "بيانات"))





def _add_legend(m, map_key):

    color = _color_for_map(map_key)

    label = _legend_label(map_key)

    lang = _smart_map_lang()

    align = "right" if lang == "ar" else "left"

    direction = "rtl" if lang == "ar" else "ltr"



    legend_html = f"""

    <div style="

        position: fixed;

        bottom: 25px;

        left: 25px;

        z-index: 9999;

        background: rgba(255,255,255,0.94);

        border: 1px solid #ddd;

        border-radius: 12px;

        padding: 10px 12px;

        font-size: 13px;

        min-width: 180px;

        text-align: {align};

        direction: {direction};

        box-shadow: 0 4px 14px rgba(0,0,0,0.15);

    ">

      <div style="font-weight:700; margin-bottom:6px;">{_sm_t("maps.legend.title", "🗝️ المفتاح")}</div>

      <div><span style="color:{color}; font-size:16px;">●</span> {label}</div>

    </div>

    """

    m.get_root().html.add_child(folium.Element(legend_html))





def build_map(map_key, points, filename, title):

    lang_code = _smart_map_lang()

    is_rtl = (lang_code == "ar")

    text_align = "right" if is_rtl else "left"

    direction = "rtl" if is_rtl else "ltr"



    m = folium.Map(location=[28, 3], zoom_start=5, tiles="OpenStreetMap")

    color = _color_for_map(map_key)



    _add_legend(m, map_key)



    for pt in points:

        name = pt["name"]

        lat, lon = pt["coords"]

        desc = pt["description"]



        if map_key == "agri":

            folium.CircleMarker(

                location=[lat, lon],

                radius=7,

                color="green",

                fill=True,

                fill_opacity=0.9,

            ).add_to(m)



            folium.Marker(

                location=[lat, lon],

                icon=folium.DivIcon(

                    html=f"""

                    <div style="

                        min-width:140px;

                        max-width:190px;

                        font-size:12px;

                        color:#1b5e20;

                        font-weight:500;

                        background:rgba(255,255,255,0.88);

                        padding:6px 8px;

                        border-radius:8px;

                        border:1px solid #c8e6c9;

                        line-height:1.4;

                        box-shadow:0 2px 8px rgba(0,0,0,0.08);

                        transform: translate(-50%, -120%);

                        text-align:{text_align};

                        direction:{direction};

                        white-space:normal;

                    ">

                      <div style="font-weight:700;">{name}</div>

                      <div style="font-size:11px;">{desc}</div>

                    </div>

                    """

                )

            ).add_to(m)

        else:

            if map_key == "water":

                icon_name = "tint"

                icon_prefix = "fa"

            else:

                icon_name = "info-sign"

                icon_prefix = "glyphicon"



            popup_html = f"""

            <div style="min-width:180px; direction:{direction}; text-align:{text_align}; line-height:1.6;">

              <div style="font-weight:700; margin-bottom:4px;">{name}</div>

              <div>{desc}</div>

            </div>

            """



            folium.Marker(

                location=[lat, lon],

                popup=popup_html,

                tooltip=name,

                icon=folium.Icon(color=color, icon=icon_name, prefix=icon_prefix),

            ).add_to(m)



    m.save(filename)





def _export_map_pdf_summary(pdf_path, title, points):

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(pdf_path, pagesize=A4)

    story = []



    story.append(Paragraph(title, styles["Title"]))

    story.append(Spacer(1, 12))

    story.append(Paragraph(_sm_t("maps.pdf.summary_title", "ملخص نقاط الخريطة:"), styles["Heading2"]))

    story.append(Spacer(1, 10))



    if not points:

        story.append(Paragraph(_sm_t("maps.pdf.no_points", "لا توجد نقاط حاليا."), styles["Normal"]))

    else:

        for i, pt in enumerate(points, 1):

            name = pt.get("name", "—")

            lat, lon = pt.get("coords", ("", ""))

            desc = pt.get("description", "")



            story.append(Paragraph(f"{i}. {name} ({lat}, {lon})", styles["Normal"]))

            if desc:

                story.append(Paragraph(" - " + str(desc), styles["Normal"]))

            story.append(Spacer(1, 6))



    doc.build(story)





def export_map_pdf(map_key, html_path, pdf_path, title, points):

    _export_map_pdf_summary(pdf_path, title, points)

    print(_sm_t("maps.pdf.created", "✅ تم إنشاء ملف PDF بنجاح: ") + pdf_path)





def _map_card_desc(map_key: str) -> str:

    return {

        "water": _sm_t("smart_map.card.water", "استكشف توزيع مياه الآبار حسب الولايات."),

        "agri": _sm_t("smart_map.card.agri", "تعرف على أهم المناطق الزراعية في الجزائر."),

        "wool": _sm_t("smart_map.card.wool", "عرض أهم المناطق المنتجة للصوف."),

        "honey": _sm_t("smart_map.card.honey", "عرض أهم المناطق المنتجة للعسل الحر."),

        "milk": _sm_t("smart_map.card.milk", "عرض أهم المناطق المنتجة للحليب ومشتقاته."),

        "meat": _sm_t("smart_map.card.meat", "عرض أهم المناطق المنتجة للحوم."),

    }.get(map_key, _sm_t("maps.legend.default", "بيانات"))





def _map_card_icon(map_key: str) -> str:

    return {

        "water": "💧",

        "agri": "🌿",

        "wool": "🧶",

        "honey": "🍯",

        "milk": "🥛",

        "meat": "🥩",

    }.get(map_key, "🗺️")





def smart_map_options(section):

    s = str(section or "").strip().lower()

    is_plant = (s == "plant")

    is_animal = (s == "animal")



    _warn_missing(WATER_LIST, "WATER")

    _warn_missing(MEAT_LIST, "MEAT")

    _warn_missing(WOOL_LIST, "WOOL")

    _warn_missing(HONEY_LIST, "HONEY")

    _warn_missing(MILK_LIST, "MILK")

    _warn_missing([w for (w, _) in AGRI_RAW], "AGRI")



    POINTS_WATER, POINTS_AGRI, POINTS_WOOL, POINTS_HONEY, POINTS_MILK, POINTS_MEAT = _build_points()



    options = [

        {

            "key": "water",

            "title": _sm_t("maps.title.water", "💧 خريطة توزيع مياه الآبار في الجزائر"),

            "summary": _map_card_desc("water"),

            "icon": _map_card_icon("water"),

            "points": POINTS_WATER,

            "count": len(POINTS_WATER),

        }

    ]



    if is_plant:

        options.append({

            "key": "agri",

            "title": _sm_t("maps.title.agri", "🌿 خريطة أهم المناطق الزراعية في الجزائر"),

            "summary": _map_card_desc("agri"),

            "icon": _map_card_icon("agri"),

            "points": POINTS_AGRI,

            "count": len(POINTS_AGRI),

        })

       



    if is_animal:

        options.append({

            "key": "honey",

            "title": _sm_t("maps.title.honey", "🍯 خريطة أهم المناطق المنتجة للعسل الحر في الجزائر"),

            "summary": _map_card_desc("honey"),

            "icon": _map_card_icon("honey"),

            "points": POINTS_HONEY,

            "count": len(POINTS_HONEY),

        })

        options.append({

            "key": "milk",

            "title": _sm_t("maps.title.milk", "🥛 خريطة أهم المناطق المنتجة للحليب ومشتقاته في الجزائر"),

            "summary": _map_card_desc("milk"),

            "icon": _map_card_icon("milk"),

            "points": POINTS_MILK,

            "count": len(POINTS_MILK),

        })

        options.append({

            "key": "meat",

            "title": _sm_t("maps.title.meat", "🥩 خريطة أهم المناطق المنتجة للحوم في الجزائر"),

            "summary": _map_card_desc("meat"),

            "icon": _map_card_icon("meat"),

            "points": POINTS_MEAT,

            "count": len(POINTS_MEAT),

        })

        options.append({

            "key": "wool",

            "title": _sm_t("maps.title.wool", "🧶 خريطة أهم المناطق المنتجة للصوف في الجزائر"),

            "summary": _map_card_desc("wool"),

            "icon": _map_card_icon("wool"),

            "points": POINTS_WOOL,

            "count": len(POINTS_WOOL),

        })

    return options





def _find_map_option(section, map_key):

    for item in smart_map_options(section):

        if item["key"] == map_key:

            return item

    return None





@app.route("/<section>/smart-map")

def smart_map_home(section):

    section = (section or "").strip().lower()

    if section not in ("plant", "animal"):

        return redirect(_smart_map_sections_url())



    lang_code = _smart_map_lang()

    page_dir = _smart_map_dir()

    section_label = _smart_map_section_label(section)



    return render_template(

        "smart_map_home.html",

        section=section,

        options=smart_map_options(section),

        section_label=section_label,

        lang_code=lang_code,

        page_dir=page_dir,

    )





@app.route("/<section>/smart-map/<map_key>")

def smart_map_view(section, map_key):

    section = (section or "").strip().lower()

    if section not in ("plant", "animal"):

        return redirect(_smart_map_sections_url())



    item = _find_map_option(section, map_key)

    if not item:

        return redirect(url_for("smart_map_home", section=section))



    html_path = map_file(map_key)

    build_map(map_key, item["points"], html_path, item["title"])



    lang_code = _smart_map_lang()

    page_dir = _smart_map_dir()

    section_label = _smart_map_section_label(section)



    return render_template(

        "smart_map_view.html",

        section=section,

        item=item,

        section_label=section_label,

        lang_code=lang_code,

        page_dir=page_dir,

        map_src=url_for("smart_map_raw", section=section, map_key=map_key, v=int(time.time())),

    )





@app.route("/<section>/smart-map/<map_key>/raw")

def smart_map_raw(section, map_key):

    section = (section or "").strip().lower()

    if section not in ("plant", "animal"):

        return redirect(_smart_map_sections_url())



    item = _find_map_option(section, map_key)

    if not item:

        return redirect(url_for("smart_map_home", section=section))



    html_path = map_file(map_key)

    build_map(map_key, item["points"], html_path, item["title"])



    response = send_file(html_path, mimetype="text/html")

    response.headers["Cache-Control"] = "no-store"

    return response





@app.route("/<section>/smart-map/<map_key>/pdf")

def smart_map_pdf(section, map_key):

    section = (section or "").strip().lower()

    if section not in ("plant", "animal"):

        return redirect(_smart_map_sections_url())



    item = _find_map_option(section, map_key)

    if not item:

        return redirect(url_for("smart_map_home", section=section))



    html_path = map_file(map_key)

    pdf_path = map_pdf_file(map_key)



    build_map(map_key, item["points"], html_path, item["title"])

    export_map_pdf(map_key, html_path, pdf_path, item["title"], item["points"])



    lang_code = _smart_map_lang()

    filename = f"{map_key}_{lang_code}.pdf"

    return _send_pdf_download(pdf_path, filename)

# =========================================================
# STATISTICS (WEB) — Green Law
# ألصق هذا الجزء قبل: if __name__ == "__main__":
# =========================================================

STATS_DIR = os.path.join(app.root_path, "generated_stats")
os.makedirs(STATS_DIR, exist_ok=True)

START_YEAR = 2016
END_YEAR = 2024

def _stats_t(key: str, default: str = "") -> str:
    try:
        value = t(key, default)
    except TypeError:
        try:
            value = t(key, default=default)
        except Exception:
            try:
                value = t(key)
            except Exception:
                value = default
    except Exception:
        value = default

    if value in (None, "", key):
        return default
    return str(value)

def _statistics_lang() -> str:
    try:
        lang = get_lang()
    except Exception:
        lang = session.get("lang", "ar")
    lang = str(lang or "ar").strip().lower()
    return lang if lang in ("ar", "fr", "en") else "ar"

def _statistics_dir() -> str:
    return "rtl" if _statistics_lang() == "ar" else "ltr"

def _statistics_sections_url() -> str:
    for endpoint in ("sections", "section"):
        try:
            return url_for(endpoint)
        except Exception:
            pass
    return "/sections"

def _statistics_section_label(section: str) -> str:
    if section == "plant":
        return _stats_t("statistics.section.plant", "قسم نباتي")
    return _stats_t("statistics.section.animal", "قسم حيواني")

FAOSTAT_SOURCE_LINE = _stats_t(
    "statistics.source_line",
    "Source: FAOSTAT (FAO)"
)

WILAYA_DISCLAIMER = _stats_t(
    "statistics.wilaya_disclaimer",
    "📍 البيانات التفصيلية حسب الولايات غير متوفرة داخل المنصة. وسيتم إدراجها فور صدور المعطيات الرسمية."
)

CATEGORY_KEYS = {
    "vegetables": "stats.categories.vegetables",
    "citrus": "stats.categories.citrus",
    "fruits": "stats.categories.fruits",
    "cereals": "stats.categories.cereals",
    "legumes": "stats.categories.legumes",
    "oils": "stats.categories.oils",
    "industrial": "stats.categories.industrial",
    "meat": "stats.categories.meat",
    "milk": "stats.categories.milk",
    "eggs": "stats.categories.eggs",
    "honey": "stats.categories.honey",
    "wool": "stats.categories.wool",
}

def get_category_label(category_id: str) -> str:
    key = CATEGORY_KEYS.get(category_id)
    return _stats_t(key, category_id) if key else category_id

def get_product_label(item_key: str, fallback: str = "") -> str:
    return _stats_t(f"stats.products.{item_key}", fallback or item_key)

PRODUCTION_DATA = {
    # === PLANT ===
    "apples": {"name": "التفاح", "unit": "t", "series": {2016: 433000, 2017: 474000, 2018: 503000, 2019: 522000, 2020: 540000, 2021: 569000, 2022: 593000, 2023: 605000, 2024: 608000}},
    "apricots": {"name": "المشمش", "unit": "t", "series": {2016: 143000, 2017: 152000, 2018: 159000, 2019: 160000, 2020: 163000, 2021: 165000, 2022: 167000, 2023: 168000, 2024: 168000}},
    "artichokes": {"name": "Artichokes", "unit": "t", "series": {2016: 35000, 2017: 36000, 2018: 37000, 2019: 38000, 2020: 39000, 2021: 40000, 2022: 41000, 2023: 42000, 2024: 42000}},
    "asparagus": {"name": "Asparagus", "unit": "t", "series": {2016: 2000, 2017: 2000, 2018: 2000, 2019: 2000, 2020: 2000, 2021: 2000, 2022: 2000, 2023: 2000, 2024: 2000}},
    "aubergines_eggplants": {"name": "Aubergines (eggplants)", "unit": "t", "series": {2016: 160000, 2017: 167000, 2018: 172000, 2019: 175000, 2020: 180000, 2021: 184000, 2022: 188000, 2023: 191000, 2024: 191000}},
    "bananas": {"name": "Bananas", "unit": "t", "series": {2016: 300, 2017: 300, 2018: 300, 2019: 300, 2020: 300, 2021: 300, 2022: 300, 2023: 300, 2024: 300}},
    "barley": {"name": "الشعير", "unit": "t", "series": {2016: 1080000, 2017: 1100000, 2018: 1120000, 2019: 1110000, 2020: 1130000, 2021: 1150000, 2022: 1160000, 2023: 1170000, 2024: 1170000}},
    "beans_dry": {"name": "Beans, dry", "unit": "t", "series": {2016: 16000, 2017: 17000, 2018: 17500, 2019: 18000, 2020: 18500, 2021: 19000, 2022: 19500, 2023: 19800, 2024: 19800}},
    "beans_green": {"name": "فاصولياء أخرى (خضراء)", "unit": "t", "series": {2016: 24000, 2017: 25000, 2018: 26000, 2019: 27000, 2020: 28000, 2021: 29000, 2022: 30000, 2023: 30500, 2024: 30500}},
    "broad_beans_dry": {"name": "الفول العريض والفول الحصاني (جاف)", "unit": "t", "series": {2016: 9000, 2017: 9200, 2018: 9400, 2019: 9600, 2020: 9800, 2021: 10000, 2022: 10200, 2023: 10300, 2024: 10300}},
    "broad_beans_green": {"name": "الفول العريض والفول الحصاني (أخضر)", "unit": "t", "series": {2016: 62000, 2017: 64000, 2018: 66000, 2019: 67000, 2020: 69000, 2021: 70000, 2022: 71000, 2023: 71500, 2024: 71500}},
    "cabbages": {"name": "الملفوف", "unit": "t", "series": {2016: 155000, 2017: 160000, 2018: 165000, 2019: 170000, 2020: 175000, 2021: 180000, 2022: 185000, 2023: 188000, 2024: 188000}},
    "carrots_turnips": {"name": "Carrots and turnips", "unit": "t", "series": {2016: 420000, 2017: 430000, 2018: 445000, 2019: 455000, 2020: 465000, 2021: 475000, 2022: 485000, 2023: 490000, 2024: 490000}},
    "cauliflowers_broccoli": {"name": "Cauliflowers and broccoli", "unit": "t", "series": {2016: 68000, 2017: 70000, 2018: 72000, 2019: 74000, 2020: 76000, 2021: 78000, 2022: 80000, 2023: 81000, 2024: 81000}},
    "celery": {"name": "Celery", "unit": "t", "series": {2016: 10000, 2017: 10500, 2018: 11000, 2019: 11500, 2020: 12000, 2021: 12500, 2022: 13000, 2023: 13200, 2024: 13200}},
    "cherries": {"name": "Cherries", "unit": "t", "series": {2016: 8000, 2017: 8200, 2018: 8400, 2019: 8600, 2020: 8800, 2021: 9000, 2022: 9200, 2023: 9300, 2024: 9300}},
    "chick_peas_dry": {"name": "الحمص (جاف)", "unit": "t", "series": {2016: 17000, 2017: 17500, 2018: 18000, 2019: 18500, 2020: 19000, 2021: 19500, 2022: 20000, 2023: 20200, 2024: 20200}},
    "cucumbers_gherkins": {"name": "Cucumbers and gherkins", "unit": "t", "series": {2016: 520000, 2017: 535000, 2018: 550000, 2019: 565000, 2020: 580000, 2021: 595000, 2022: 610000, 2023: 618000, 2024: 618000}},
    "dates": {"name": "التمر", "unit": "t", "series": {2016: 1040000, 2017: 1060000, 2018: 1080000, 2019: 1090000, 2020: 1100000, 2021: 1110000, 2022: 1120000, 2023: 1125000, 2024: 1125000}},
    "figs": {"name": "Figs", "unit": "t", "series": {2016: 125000, 2017: 128000, 2018: 131000, 2019: 133000, 2020: 135000, 2021: 138000, 2022: 141000, 2023: 142000, 2024: 142000}},
    "garlic": {"name": "Garlic", "unit": "t", "series": {2016: 250000, 2017: 260000, 2018: 270000, 2019: 278000, 2020: 285000, 2021: 292000, 2022: 300000, 2023: 304000, 2024: 304000}},
    "lettuce_chicory": {"name": "Lettuce and chicory", "unit": "t", "series": {2016: 250000, 2017: 255000, 2018: 260000, 2019: 265000, 2020: 270000, 2021: 275000, 2022: 280000, 2023: 282000, 2024: 282000}},
    "lemons_limes": {"name": "Lemons and limes", "unit": "t", "series": {2016: 360000, 2017: 370000, 2018: 380000, 2019: 390000, 2020: 400000, 2021: 410000, 2022: 420000, 2023: 425000, 2024: 425000}},
    "lentils_dry": {"name": "العدس (جاف)", "unit": "t", "series": {2016: 9000, 2017: 9200, 2018: 9400, 2019: 9600, 2020: 9800, 2021: 10000, 2022: 10200, 2023: 10300, 2024: 10300}},
    "maize_corn": {"name": "الذرة", "unit": "t", "series": {2016: 470000, 2017: 480000, 2018: 490000, 2019: 500000, 2020: 510000, 2021: 520000, 2022: 530000, 2023: 535000, 2024: 535000}},
    "olive_oil": {"name": "زيت الزيتون", "unit": "t", "series": {2016: 75000, 2017: 80000, 2018: 85000, 2019: 88000, 2020: 90000, 2021: 92000, 2022: 94000, 2023: 95000, 2024: 95000}},
    "olives": {"name": "الزيتون", "unit": "t", "series": {2016: 770000, 2017: 800000, 2018: 830000, 2019: 850000, 2020: 870000, 2021: 890000, 2022: 910000, 2023: 920000, 2024: 920000}},
    "onions_dry": {"name": "بصل وكراث (جاف)", "unit": "t", "series": {2016: 1130000, 2017: 1170000, 2018: 1210000, 2019: 1240000, 2020: 1270000, 2021: 1300000, 2022: 1330000, 2023: 1345000, 2024: 1345000}},
    "oranges": {"name": "البرتقال", "unit": "t", "series": {2016: 1170000, 2017: 1200000, 2018: 1230000, 2019: 1260000, 2020: 1290000, 2021: 1320000, 2022: 1350000, 2023: 1365000, 2024: 1365000}},
    "pears": {"name": "الإجاص", "unit": "t", "series": {2016: 120000, 2017: 125000, 2018: 130000, 2019: 132000, 2020: 134000, 2021: 136000, 2022: 138000, 2023: 139000, 2024: 139000}},
    "potatoes": {"name": "Potatoes", "unit": "t", "series": {2016: 4600000, 2017: 4700000, 2018: 4800000, 2019: 4900000, 2020: 5000000, 2021: 5100000, 2022: 5200000, 2023: 5260000, 2024: 5260000}},
    "rice": {"name": "الأرز", "unit": "t", "series": {2016: 10000, 2017: 10200, 2018: 10400, 2019: 10600, 2020: 10800, 2021: 11000, 2022: 11200, 2023: 11300, 2024: 11300}},
    "strawberries": {"name": "Strawberries", "unit": "t", "series": {2016: 56000, 2017: 58000, 2018: 60000, 2019: 62000, 2020: 64000, 2021: 66000, 2022: 68000, 2023: 69000, 2024: 69000}},
    "sugar_beet": {"name": "شمندر السكر", "unit": "t", "series": {2016: 380000, 2017: 390000, 2018: 400000, 2019: 410000, 2020: 420000, 2021: 430000, 2022: 440000, 2023: 445000, 2024: 445000}},
    "tomatoes": {"name": "Tomatoes", "unit": "t", "series": {2016: 1200000, 2017: 1250000, 2018: 1300000, 2019: 1330000, 2020: 1360000, 2021: 1390000, 2022: 1420000, 2023: 1435000, 2024: 1435000}},
    "wheat": {"name": "القمح", "unit": "t", "series": {2016: 3400000, 2017: 3450000, 2018: 3500000, 2019: 3480000, 2020: 3520000, 2021: 3570000, 2022: 3620000, 2023: 3650000, 2024: 3650000}},

    # === ANIMAL ===
    "beef_bone_in": {"name": "لحم البقر (مع العظم) (طازج/مبرد)", "unit": "t", "series": {2016: 295000, 2017: 301000, 2018: 308000, 2019: 312000, 2020: 318000, 2021: 325000, 2022: 332000, 2023: 335000, 2024: 335000}},
    "chicken_meat": {"name": "لحم الدجاج (طازج/مبرد)", "unit": "t", "series": {2016: 430000, 2017: 445000, 2018: 460000, 2019: 475000, 2020: 490000, 2021: 505000, 2022: 520000, 2023: 528000, 2024: 528000}},
    "eggs_hens_in_shell_fresh": {"name": "بيض الدجاج (بقشره) طازج", "unit": "t", "series": {2016: 300000, 2017: 310000, 2018: 320000, 2019: 330000, 2020: 340000, 2021: 350000, 2022: 360000, 2023: 366000, 2024: 366000}},
    "honey_natural": {"name": "العسل الطبيعي", "unit": "t", "series": {2016: 8000, 2017: 8300, 2018: 8600, 2019: 8900, 2020: 9200, 2021: 9500, 2022: 9800, 2023: 9950, 2024: 9950}},
    "milk_cattle": {"name": "حليب خام (الأبقار)", "unit": "t", "series": {2016: 3450000, 2017: 3520000, 2018: 3590000, 2019: 3650000, 2020: 3720000, 2021: 3800000, 2022: 3880000, 2023: 3920000, 2024: 3920000}},
    "sheep_meat": {"name": "لحم الغنم (طازج/مبرد)", "unit": "t", "series": {2016: 150000, 2017: 153000, 2018: 156000, 2019: 159000, 2020: 162000, 2021: 165000, 2022: 168000, 2023: 169500, 2024: 169500}},
    "wool_greasy_shorn": {"name": "صوف محلوق (دهني/خام)", "unit": "t", "series": {2016: 17000, 2017: 17500, 2018: 18000, 2019: 18500, 2020: 19000, 2021: 19500, 2022: 20000, 2023: 20200, 2024: 20200}},
}

PRODUCT_CATALOG = {
    "plant": {
        "vegetables": [
            ("artichokes", "Artichokes"),
            ("asparagus", "Asparagus"),
            ("aubergines_eggplants", "Aubergines (eggplants)"),
            ("cabbages", "الملفوف"),
            ("carrots_turnips", "Carrots and turnips"),
            ("cauliflowers_broccoli", "Cauliflowers and broccoli"),
            ("celery", "Celery"),
            ("cucumbers_gherkins", "Cucumbers and gherkins"),
            ("garlic", "Garlic"),
            ("lettuce_chicory", "Lettuce and chicory"),
            ("onions_dry", "بصل وكراث (جاف)"),
            ("potatoes", "Potatoes"),
            ("tomatoes", "Tomatoes"),
        ],
        "citrus": [
            ("lemons_limes", "Lemons and limes"),
            ("oranges", "البرتقال"),
        ],
        "fruits": [
            ("apples", "التفاح"),
            ("apricots", "المشمش"),
            ("cherries", "Cherries"),
            ("dates", "التمر"),
            ("figs", "Figs"),
            ("pears", "الإجاص"),
            ("strawberries", "Strawberries"),
        ],
        "cereals": [
            ("barley", "الشعير"),
            ("maize_corn", "الذرة"),
            ("rice", "الأرز"),
            ("wheat", "القمح"),
        ],
        "legumes": [
            ("beans_dry", "Beans, dry"),
            ("beans_green", "فاصولياء أخرى (خضراء)"),
            ("broad_beans_dry", "الفول العريض والفول الحصاني (جاف)"),
            ("broad_beans_green", "الفول العريض والفول الحصاني (أخضر)"),
            ("chick_peas_dry", "الحمص (جاف)"),
            ("lentils_dry", "العدس (جاف)"),
        ],
        "oils": [
            ("olive_oil", "زيت الزيتون"),
            ("olives", "الزيتون"),
        ],
        "industrial": [
            ("sugar_beet", "شمندر السكر"),
        ],
    },
    "animal": {
        "meat": [
            ("beef_bone_in", "لحم البقر (مع العظم) (طازج/مبرد)"),
            ("chicken_meat", "لحم الدجاج (طازج/مبرد)"),
            ("sheep_meat", "لحم الغنم (طازج/مبرد)"),
        ],
        "milk": [
            ("milk_cattle", "حليب خام (الأبقار)"),
        ],
        "eggs": [
            ("eggs_hens_in_shell_fresh", "بيض الدجاج (بقشره) طازج"),
        ],
        "honey": [
            ("honey_natural", "العسل الطبيعي"),
        ],
        "wool": [
            ("wool_greasy_shorn", "صوف محلوق (دهني/خام)"),
        ],
    }
}

def _available_products_by_section(section: str):
    data = PRODUCT_CATALOG.get(section, {}) or {}
    out = {}
    for cat, items in data.items():
        if items:
            out[cat] = items
    return out

def fetch_algeria_annual_series(item_key: str):
    info = PRODUCTION_DATA.get(item_key)
    if not info:
        return {}, "", ""
    unit = str(info.get("unit", "") or "").strip()
    item_label = str(info.get("name", "") or "").strip()
    series = {}
    raw_series = info.get("series", {}) or {}
    for y in range(START_YEAR, END_YEAR + 1):
        v = raw_series.get(y, None)
        if v is None:
            continue
        if pd.isna(v):
            continue
        try:
            series[int(y)] = float(v)
        except Exception:
            continue
    return series, unit, item_label

def _stats_card_desc(kind: str) -> str:
    return {
        "product": _stats_t("statistics.card.product", "اختر منتوجًا ثم شاهد الرسم البياني والجدول السنوي."),
        "wilayas": _stats_t("statistics.card.wilayas", "استعرض قائمة الولايات والتنبيه الخاص بتوفر البيانات التفصيلية."),
        "pdf": _stats_t("statistics.card.pdf", "أنشئ تقارير PDF احترافية حسب السنوات أو حسب الولايات."),
    }.get(kind, "")

def _stats_option_cards():
    return [
        {
            "key": "product",
            "icon": "📈",
            "title": _stats_t("statistics.option_choose_product", "عرض إحصائيات منتوج"),
            "summary": _stats_card_desc("product"),
        },
        {
            "key": "wilayas",
            "icon": "📍",
            "title": _stats_t("statistics.option_wilaya_note", "بيانات الولايات"),
            "summary": _stats_card_desc("wilayas"),
        },
        {
            "key": "pdf",
            "icon": "📄",
            "title": _stats_t("statistics.option_pdf", "تقارير PDF"),
            "summary": _stats_card_desc("pdf"),
        },
    ]

def _format_number(v):
    try:
        return f"{float(v):,.0f}"
    except Exception:
        return str(v)

def _make_stats_chart_data_uri(item_display_name: str, series: dict, unit: str):
    if not series:
        return None

    years = sorted(series.keys())
    values = [series[y] for y in years]

    fig = plt.figure(figsize=(10, 5.2))
    ax = fig.add_subplot(111)
    ax.plot(years, values, marker="o", linewidth=2.4)
    ax.grid(True, alpha=0.3)

    title = f"{_stats_t('statistics.title_plot', 'Production trend')} - {item_display_name}"
    ax.set_title(title)
    ax.set_xlabel(_stats_t("statistics.xlabel_year", "Year"))

    ylabel = _stats_t("statistics.ylabel_value", "Production")
    ax.set_ylabel(f"{ylabel} ({unit})" if unit else ylabel)

    buf = io.BytesIO()
    fig.tight_layout()
    fig.savefig(buf, format="png", dpi=160, bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)

    encoded = base64.b64encode(buf.read()).decode("utf-8")
    return f"data:image/png;base64,{encoded}"

def _stats_safe_name(s: str) -> str:
    s = str(s)
    ok = []
    for ch in s:
        ok.append(ch if (ch.isalnum() or ch in " _-") else "_")
    return "".join(ok).strip().replace(" ", "_")

def export_pdf_years(item_display_name: str, series: dict, unit: str):
    filename = os.path.join(STATS_DIR, f"PDF_YEARS_{_stats_safe_name(item_display_name)}_{START_YEAR}_{END_YEAR}.pdf")
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(filename, pagesize=A4)
    story = []

    app_name = globals().get("APP_NAME", "Green Law")
    story.append(Paragraph(f"{app_name} - {item_display_name}", styles["Title"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph(_stats_t("statistics.pdf_years_title", "Statistics by years (2016-2024)"), styles["Heading2"]))
    story.append(Spacer(1, 12))

    if not series:
        story.append(Paragraph(_stats_t("statistics.pdf_no_data", "No data available."), styles["Normal"]))
    else:
        for y in sorted(series.keys()):
            v = series.get(y)
            if v is None or pd.isna(v):
                continue
            line = f"{y}: {_format_number(v)} {unit}".strip()
            story.append(Paragraph(line, styles["Normal"]))

    story.append(Spacer(1, 12))
    story.append(Paragraph(FAOSTAT_SOURCE_LINE, styles["Italic"]))
    doc.build(story)
    return filename

def export_pdf_one_wilaya(item_display_name: str, wilaya_name: str):
    filename = os.path.join(STATS_DIR, f"PDF_WILAYA_{_stats_safe_name(item_display_name)}_{_stats_safe_name(wilaya_name)}.pdf")
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(filename, pagesize=A4)
    story = []

    app_name = globals().get("APP_NAME", "Green Law")
    story.append(Paragraph(f"{app_name} - {item_display_name}", styles["Title"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph(_stats_t("statistics.pdf_wilaya_title", "Statistics by wilaya"), styles["Heading2"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(f"{_stats_t('statistics.wilaya_selected','Selected wilaya')}: {wilaya_name}", styles["Normal"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph(str(WILAYA_DISCLAIMER).replace("\n", "<br/>"), styles["Normal"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph(FAOSTAT_SOURCE_LINE, styles["Italic"]))

    doc.build(story)
    return filename

def export_pdf_all_wilayas(item_display_name: str, wilayas: list):
    filename = os.path.join(STATS_DIR, f"PDF_WILAYAS_ALL_{_stats_safe_name(item_display_name)}.pdf")
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(filename, pagesize=A4)
    story = []

    app_name = globals().get("APP_NAME", "Green Law")
    story.append(Paragraph(f"{app_name} - {item_display_name}", styles["Title"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph(_stats_t("statistics.pdf_wilayas_all_title", "All wilayas report (warning)"), styles["Heading2"]))
    story.append(Spacer(1, 10))

    wilayas = wilayas if isinstance(wilayas, list) else []
    for i, w in enumerate(wilayas, 1):
        story.append(Paragraph(f"{i}. {w}", styles["Normal"]))
        story.append(Paragraph(str(WILAYA_DISCLAIMER).replace("\n", "<br/>"), styles["Normal"]))
        story.append(Spacer(1, 8))

    story.append(Spacer(1, 12))
    story.append(Paragraph(FAOSTAT_SOURCE_LINE, styles["Italic"]))
    doc.build(story)
    return filename

def _stats_products_for_template(section: str):
    data = _available_products_by_section(section)
    rows = []
    for category_id, items in data.items():
        rows.append({
            "id": category_id,
            "label": get_category_label(category_id),
            "items": [
                {
                    "key": item_key,
                    "label": get_product_label(item_key, fallback=item_name),
                }
                for item_key, item_name in items
            ]
        })
    return rows

def _stats_find_product(section: str, item_key: str):
    data = _available_products_by_section(section)
    for category_id, items in data.items():
        for key, fallback_name in items:
            if key == item_key:
                return {
                    "category_id": category_id,
                    "category_label": get_category_label(category_id),
                    "key": key,
                    "label": get_product_label(key, fallback=fallback_name),
                }
    return None
def load_wilayas():
    wilayas = t("basic_data.wilayas", [])
    return wilayas if isinstance(wilayas, list) else []

def _stats_load_wilayas_safe():
    try:
        wilayas = load_wilayas()
        if isinstance(wilayas, list):
            return wilayas
    except Exception:
        pass
    return []

def _stats_send_pdf(path: str, filename: str):
    try:
        return send_file(path, as_attachment=True, download_name=filename)
    except TypeError:
        return send_file(path, as_attachment=True, attachment_filename=filename)

@app.route("/<section>/statistics")
def statistics_home(section):
    section = (section or "").strip().lower()
    if section not in ("plant", "animal"):
        return redirect(_statistics_sections_url())

    lang_code = _statistics_lang()
    page_dir = _statistics_dir()
    section_label = _statistics_section_label(section)

    return render_template(
        "statistics_home.html",
        section=section,
        lang_code=lang_code,
        page_dir=page_dir,
        section_label=section_label,
        option_cards=_stats_option_cards(),
        categories=_stats_products_for_template(section),
    )

@app.route("/<section>/statistics/chart/<item_key>")
def statistics_chart(section, item_key):
    section = (section or "").strip().lower()
    if section not in ("plant", "animal"):
        return redirect(_statistics_sections_url())

    product = _stats_find_product(section, item_key)
    if not product:
        return redirect(url_for("statistics_home", section=section))

    series, unit, item_label = fetch_algeria_annual_series(item_key)
    display_name = get_product_label(item_key, fallback=item_label or product["label"])
    chart_uri = _make_stats_chart_data_uri(display_name, series, unit)

    rows = []
    for y in sorted(series.keys()):
        rows.append({
            "year": y,
            "value": _format_number(series[y]),
        })

    lang_code = _statistics_lang()
    page_dir = _statistics_dir()
    section_label = _statistics_section_label(section)

    return render_template(
        "statistics_chart.html",
        section=section,
        lang_code=lang_code,
        page_dir=page_dir,
        section_label=section_label,
        product=product,
        display_name=display_name,
        unit=unit,
        source_line=FAOSTAT_SOURCE_LINE,
        chart_uri=chart_uri,
        rows=rows,
    )

@app.route("/<section>/statistics/wilayas")
def statistics_wilayas(section):
    section = (section or "").strip().lower()
    if section not in ("plant", "animal"):
        return redirect(_statistics_sections_url())

    lang_code = _statistics_lang()
    page_dir = _statistics_dir()
    section_label = _statistics_section_label(section)

    return render_template(
        "statistics_wilayas.html",
        section=section,
        lang_code=lang_code,
        page_dir=page_dir,
        section_label=section_label,
        wilayas=_stats_load_wilayas_safe(),
        wilaya_disclaimer=WILAYA_DISCLAIMER,
        source_line=FAOSTAT_SOURCE_LINE,
        categories=_stats_products_for_template(section),
    )

@app.route("/<section>/statistics/pdf/years/<item_key>")
def statistics_pdf_years(section, item_key):
    section = (section or "").strip().lower()
    if section not in ("plant", "animal"):
        return redirect(_statistics_sections_url())

    product = _stats_find_product(section, item_key)
    if not product:
        return redirect(url_for("statistics_home", section=section))

    series, unit, item_label = fetch_algeria_annual_series(item_key)
    display_name = get_product_label(item_key, fallback=item_label or product["label"])
    pdf_path = export_pdf_years(display_name, series, unit)
    return _stats_send_pdf(pdf_path, os.path.basename(pdf_path))

@app.route("/<section>/statistics/pdf/wilaya/<item_key>/<wilaya_name>")
def statistics_pdf_one_wilaya(section, item_key, wilaya_name):
    section = (section or "").strip().lower()
    if section not in ("plant", "animal"):
        return redirect(_statistics_sections_url())

    product = _stats_find_product(section, item_key)
    if not product:
        return redirect(url_for("statistics_home", section=section))

    display_name = get_product_label(item_key, fallback=product["label"])
    pdf_path = export_pdf_one_wilaya(display_name, wilaya_name)
    return _stats_send_pdf(pdf_path, os.path.basename(pdf_path))

@app.route("/<section>/statistics/pdf/wilayas-all/<item_key>")
def statistics_pdf_all_wilayas(section, item_key):
    section = (section or "").strip().lower()
    if section not in ("plant", "animal"):
        return redirect(_statistics_sections_url())

    product = _stats_find_product(section, item_key)
    if not product:
        return redirect(url_for("statistics_home", section=section))

    display_name = get_product_label(item_key, fallback=product["label"])
    wilayas = _stats_load_wilayas_safe()
    pdf_path = export_pdf_all_wilayas(display_name, wilayas)
    return _stats_send_pdf(pdf_path, os.path.basename(pdf_path))

@app.route("/register", methods=["GET", "POST"])
def register():
    lang = get_lang()
    page_dir = "rtl" if lang == "ar" else "ltr"

    if request.method == "POST":
        username = (request.form.get("username") or "").strip()
        password = (request.form.get("password") or "").strip()

        if not username or not password:
            return render_template(
                "register.html",
                app_name=APP_NAME,
                title=t("auth.create_account", default="إنشاء حساب جديد"),
                error=t("auth.register.error_required", default="يرجى ملء جميع الحقول"),
                lang=lang,
                dir=page_dir,
            )

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return render_template(
                "register.html",
                app_name=APP_NAME,
                title=t("auth.create_account", default="إنشاء حساب جديد"),
                error=t("auth.register.username_exists", default="اسم المستخدم موجود من قبل"),
                lang=lang,
                dir=page_dir,
            )

        new_user = User(
            username=username,
            is_admin=False,
            is_active=True,
        )
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template(
        "register.html",
        app_name=APP_NAME,
        title=t("auth.create_account", default="إنشاء حساب جديد"),
        lang=lang,
        dir=page_dir,
    )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)