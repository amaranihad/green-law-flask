# Arabic language pack for Green Law (ONE FILE / ONE DICT)
# ✅ Single flat dictionary (dot-keys)

AR = {
    # =========================
    # Language chooser
    # =========================
    "ui.lang.choose_language": "اختر اللغة:",
    "ui.lang.arabic": "العربية",
    "ui.lang.french": "Français",
    "ui.lang.english": "English",
    "ui.lang.enter_choice": "➤ ",
    "ui.lang.invalid_choice": "اختيار غير صحيح.",

    # =========================
    # Main / General
    # =========================
    "ui.welcome_title": "مرحبا بك في Green Law",
    "ui.exit": "الخروج",
    "ui.back": "رجوع",

    "general.back": "رجوع",
    "general.choose": "➤ ",
    "general.invalid_choice": "اختيار غير صحيح.",
    "general.invalid_choice_long": "❌ اختيار غير صحيح. يرجى إدخال رقم صحيح من القائمة.\n",
    "general.logout": "تسجيل الخروج",
"auth.register.error_required": "يرجى ملء جميع الحقول",
"auth.register.username_exists": "اسم المستخدم موجود من قبل",
    # =========================
    # Main menu (home)
    # =========================
    "ui.main.title": "مرحبا بك في {app}",
    "ui.main.login": "تسجيل الدخول",
    "ui.main.signup": "إنشاء حساب",
    "ui.main.exit": "خروج",
    "ui.main.enter_choice": "➤ ",
    "ui.main.thanks": "شكرا لاستعمالك Green Law!",
    "ui.main.invalid_choice": "اختيار غير صحيح.",
"auth.login.error_required": "يرجى إدخال اسم المستخدم وكلمة المرور",
"auth.login.error_invalid": "اسم المستخدم أو كلمة المرور غير صحيحة",
    # =========================
    # Sections / Section menu
    # =========================
    "sections.title": "اختيار القسم:",
    "sections.plant": "🌱 قسم نباتي",
    "sections.animal": "🐄 قسم حيواني",

    "ui.menu.title": "مرحباً {username} - \n{section}\n",
    "ui.menu.option_1": "مرشدك الفلاحي",
    "ui.menu.option_2": "الإحصائيات",
    "ui.menu.option_3": "مرشدك القانوني",
    "ui.menu.option_4": "السوق الفلاحي",
    "ui.menu.option_5": "الخريطة الذكية",
    "ui.menu.option_6": "جواز الفلاح (QR)",
    "ui.menu.back_to_sections": "رجوع إلى اختيار الأقسام",
    "ui.menu.enter_choice": "➤ ",

    # =========================
    # Auth
    # =========================
    "auth.login": "تسجيل الدخول",
    "auth.create": "إنشاء حساب",
    "auth.username": "اسم المستخدم: ",
    "auth.password": "كلمة المرور: ",
    "auth.welcome_user": "مرحبا {name}!",
    "auth.username_not_recognized": "لم يتم التعرف على اسم المستخدم.\n",

    # Extra auth used in main.py
    "auth.enter_new_username": "اسم مستخدم جديد: ",
    "auth.enter_username": "اسم المستخدم: ",
    "auth.enter_password": "كلمة المرور: ",
    "auth.invalid_username": "اسم المستخدم غير صالح.",
    "auth.username_exists": "اسم المستخدم موجود بالفعل.",
    "auth.signup_success": "تم إنشاء الحساب بنجاح.",
    "auth.login_success": "مرحبا {username}!",
    "auth.login_fail": "فشل تسجيل الدخول.",
"auth.password": "كلمة المرور",
"auth.login": "تسجيل الدخول",
"auth.create_account": "إنشاء حساب جديد",
"auth.register.error_required": "يرجى ملء جميع الحقول",
    # =========================
    # Voice / STT
    # =========================
    "voice.missing_libs": "❌ مكتبات الصوت غير مثبتة.",
    "voice.install_hint": "pip install sounddevice soundfile SpeechRecognition",
    "voice.listening": "🎤 تفضل اهدر الآن...",
    "voice.no_understand": "❌ لم أفهم الصوت.",
    "voice.error": "❌ خطأ في التعرف على الصوت: {e}",
    "voice.generic_error": "❌ خطأ: {e}",

    # =========================
    # TTS
    # =========================
    "tts.gTTS_failed": "⚠️ فشل gTTS: {e}، نحاول pyttsx3...",
    "tts.pyttsx3_failed": "⚠️ فشل pyttsx3: {e}",

    # =========================
    # Basic data
    # =========================
    "basic_data.wilayas": [
        "أدرار (01)", "الشلف (02)", "الأغواط (03)", "أم البواقي (04)", "باتنة (05)",
        "بجاية (06)", "بسكرة (07)", "بشار (08)", "البليدة (09)", "البويرة (10)",
        "تمنراست (11)", "تبسة (12)", "تلمسان (13)", "تيارت (14)", "تيزي وزو (15)",
        "الجزائر (16)", "الجلفة (17)", "جيجل (18)", "سطيف (19)", "سعيدة (20)",
        "سكيكدة (21)", "سيدي بلعباس (22)", "عنابة (23)", "قالمة (24)", "قسنطينة (25)",
        "المدية (26)", "مستغانم (27)", "المسيلة (28)", "معسكر (29)", "ورقلة (30)",
        "وهران (31)", "البيض (32)", "إليزي (33)", "برج بوعريريج (34)", "بومرداس (35)",
        "الطارف (36)", "تندوف (37)", "تيسمسيلت (38)", "الوادي (39)", "خنشلة (40)",
        "سوق أهراس (41)", "تيبازة (42)", "ميلة (43)", "عين الدفلى (44)", "النعامة (45)",
        "عين تموشنت (46)", "غرداية (47)", "غليزان (48)", "تيميمون (49)", "برج باجي مختار (50)",
        "أولاد جلال (51)", "بني عباس (52)", "عين صالح (53)", "عين قزام (54)", "تقرت (55)",
        "جانت (56)", "المغير (57)", "المنيعة (58)", 
    
    ],

    # =========================
    # Statistics
    # =========================
    "statistics.source_line": "المصدر: FAOSTAT (FAO) – https://www.fao.org/faostat/",
    "statistics.wilaya_disclaimer": (
        "📍 البيانات التفصيلية حسب الولايات غير متوفرة داخل المنصة.\n"
        "وسيتم إدراجها مباشرة فور صدور المعطيات الرسمية من وزارة الفلاحة\n"
        "والتنمية الريفية الجزائرية."
    ),

    "statistics.menu_title": "📊 الإحصائيات",
    "statistics.option_choose_product": "عرض إحصائيات منتوج (رسم + جدول)",
    "statistics.option_wilaya_note": "بيانات الولايات (قائمة الولايات)",
    "statistics.option_pdf": "تقارير PDF",

    "statistics.choose_category_title": "اختر الفئة:",
    "statistics.choose_product_title": "اختر المنتوج:",
    "statistics.choose_wilaya_title": "اختر الولاية:",
    "statistics.wilaya_selected": "الولاية المختارة",

    "statistics.no_categories_in_section": "⚠️ لا توجد أصناف في هذا القسم.",
    "statistics.wilayas_list_not_found": "⚠️ قائمة الولايات غير موجودة.",
    "statistics.no_data_for_product_range": "⚠️ لا توجد بيانات لهذا المنتج في 2016-2024.",
    "statistics.no_data": "⚠️ لا توجد بيانات.",

    "statistics.title_plot": "📈 تطور الإنتاج",
    "statistics.xlabel_year": "السنة",
    "statistics.ylabel_value": "الإنتاج",
    "statistics.table_year": "السنة",
    "statistics.table_value": "القيمة",

    "statistics.pdf_menu_title": "📄 تقارير PDF",
    "statistics.pdf_years": "تحميل PDF حسب السنوات (2016-2024)",
    "statistics.pdf_wilaya_one": "تحميل PDF لولاية واحدة",
    "statistics.pdf_wilayas_all": "تحميل PDF شامل لكل الولايات",

    "statistics.pdf_years_title": "إحصائيات حسب السنوات (2016-2024)",
    "statistics.pdf_wilaya_title": "إحصائيات حسب الولاية",
    "statistics.pdf_wilayas_all_title": "ملف شامل لكل الولايات (تنبيه)",
    "statistics.pdf_no_data": "لا توجد بيانات حاليا.",

    "pdf.created": "✅ تم إنشاء ملف PDF:",

    "stats.categories.vegetables": "الخضروات",
    "stats.categories.citrus": "الحمضيات",
    "stats.categories.fruits": "الفواكه",
    "stats.categories.cereals": "الحبوب",
    "stats.categories.legumes": "البقوليات",
    "stats.categories.oils": "زيوت وبذور زيتية",
    "stats.categories.industrial": "زراعات صناعية",
    "stats.categories.meat": "اللحوم",
    "stats.categories.milk": "الحليب",
    "stats.categories.eggs": "البيض",
    "stats.categories.honey": "العسل",
    "stats.categories.wool": "الصوف",

    # Products labels (kept as you wrote them)
    "stats.products.artichokes": "الخرشف",
    "stats.products.asparagus": "الهليون(السكوم)",
    "stats.products.aubergines_eggplants": "الباذنجان",
    "stats.products.cabbages": "الملفوف",
    "stats.products.carrots_turnips": "الجزر و اللفت",
    "stats.products.cauliflowers_broccoli": "القرنبيط(شوفلور) و البروكلي",
    "stats.products.celery": "الكرفس",
    "stats.products.cucumbers_gherkins": "الخيار و الخيار المخلل ",
    "stats.products.garlic": "الثوم",
    "stats.products.lettuce_chicory": "الخس و  (السريس) الهندباء",
    "stats.products.onions_dry": "بصل (جاف)",
    "stats.products.potatoes": "البطاطا",
    "stats.products.tomatoes": "الطماطم",
    "stats.products.lemons_limes": "الليمون الاصفر والليمون الاخضر",
    "stats.products.oranges": "البرتقال",
    "stats.products.apples": "التفاح",
    "stats.products.apricots": "المشمش",
    "stats.products.cherries": "الكرز",
    "stats.products.dates": "التمر",
    "stats.products.figs": "التين (الكرموس )",
    "stats.products.pears": "الإجاص",
    "stats.products.strawberries": "الفراولة",
    "stats.products.barley": "الشعير",
    "stats.products.maize_corn": "الذرة",
    "stats.products.rice": "الأرز",
    "stats.products.wheat": "القمح",
    "stats.products.beans_dry": "فاصولياء ",
    "stats.products.beans_green": "فاصولياء أخرى (خضراء)",
    "stats.products.broad_beans_dry": "الفول العريض والفول الحصاني (جاف)",
    "stats.products.broad_beans_green": "الفول العريض والفول الحصاني (أخضر)",
    "stats.products.chick_peas_dry": "الحمص (جاف)",
    "stats.products.lentils_dry": "العدس (جاف)",
    "stats.products.olive_oil": "زيت الزيتون",
    "stats.products.olives": "الزيتون",
    "stats.products.sugar_beet": "شمندر السكر",

    "stats.products.beef_bone_in": "لحم البقر (مع العظم) (طازج/مبرد)",
    "stats.products.chicken_meat": "لحم الدجاج (طازج/مبرد)",
    "stats.products.sheep_meat": "لحم الغنم (طازج/مبرد)",
    "stats.products.milk_cattle": "حليب خام (الأبقار)",
    "stats.products.eggs_hens_in_shell_fresh": "بيض الدجاج (بقشره) طازج",
    "stats.products.honey_natural": "العسل الطبيعي",
    "stats.products.wool_greasy_shorn": "صوف محلوق (دهني/خام)",
"statistics.menu_title": "الإحصائيات",
"statistics.current_section": "القسم الحالي",
"statistics.section.plant": "قسم نباتي",
"statistics.section.animal": "قسم حيواني",
"statistics.hero_subtitle": "استكشف الإحصائيات الزراعية والحيوانية، الرسوم البيانية، التقارير، وبيانات الولايات داخل منصة Green Law.",
"statistics.open_section": "فتح القسم",
"statistics.choose_product_hint": "اختر فئة ثم اختر منتوجًا لعرض الإحصائيات والرسوم البيانية أو تحميل PDF.",
"statistics.card.product": "اختر منتوجًا ثم شاهد الرسم البياني والجدول السنوي.",
"statistics.card.wilayas": "استعرض قائمة الولايات والتنبيه الخاص بتوفر البيانات التفصيلية.",
"statistics.card.pdf": "أنشئ تقارير PDF احترافية حسب السنوات أو حسب الولايات.",
"statistics.table_title": "الجدول السنوي",
"statistics.years_range": "الفترة",
"statistics.pdf_hint": "يمكنك تحميل تقارير حسب السنوات أو تقارير خاصة بالولايات انطلاقًا من المنتوج المختار.",
    # =========================
    # Farmer Guide
    # =========================
    "guide.menu_title": "🌿 مرشدك الفلاحي",
    "guide.home": "العودة للصفحة الرئيسية",
    "guide.empty": "⚠️ لا يوجد محتوى حالياً.",
    "guide.ask_listen": "🔊 هل تود سماعها مقروءة؟ (y/n): ",
    "guide.press_enter_back": "⏎ للرجوع اضغط Enter...",
    "guide.listen": "استمع للنص",
    "guide.stop": "إيقاف",
    "guide.tts_fail": "❌ تعذر تشغيل الصوت.",
    "guide.plant.title": "مرشدك الفلاحي (نباتي)",
    "guide.animal.title": "مرشدك الفلاحي (حيواني)",
      "guide.plant.1.title": "إرشادات تقنية فلاحية",
    "guide.plant.1.body": """الفلاحة ليست مجرد عملية بذرٍ وانتظار حصاد، بل هي علمٌ قائم على فهم عميق لدورة الحياة، تفاعل التربة مع المناخ، واستجابة النبات للعوامل البيئية المختلفة. إن نجاح المشروع الفلاحي يبدأ من مرحلة التخطيط، حيث يُعد اختيار المحصول المناسب أول قرار استراتيجي يؤثر على مردودية الموسم كاملاً.

ينبغي للفلاح أن يراعي الخصائص المناخية للمنطقة، مثل معدلات الأمطار، درجات الحرارة، الرطوبة، وطبيعة الرياح السائدة. فالمحاصيل الشتوية، على سبيل المثال، تحتاج إلى درجات حرارة معتدلة وبرودة نسبية لتحفيز الإنبات الجيد، بينما المحاصيل الصيفية تتطلب حرارة مرتفعة وفترات إضاءة طويلة.

كما أن دراسة طبيعة التربة عنصر أساسي في النجاح التقني. التربة الرملية تختلف جذرياً عن الطينية أو الكلسية من حيث قدرتها على الاحتفاظ بالماء والعناصر الغذائية. لذا فإن تحليل التربة مخبرياً يمنح الفلاح تصوراً دقيقاً حول مستوى الحموضة (pH)، ونسبة المواد العضوية، ووفرة العناصر الكبرى كالأزوت والفوسفور والبوتاسيوم.

ومن المبادئ التقنية المهمة اعتماد الدورة الزراعية، وهي نظام تناوب المحاصيل على نفس الأرض عبر المواسم المختلفة. هذا الأسلوب يمنع إنهاك التربة، ويحد من انتشار الآفات، ويحسن التوازن البيولوجي داخل الحقل.

إن الزراعة الحديثة لم تعد تعتمد فقط على الخبرة التقليدية، بل أصبحت تستند إلى التكنولوجيا الدقيقة، مثل استخدام أجهزة قياس الرطوبة، أنظمة الري الذكية، والاستشعار عن بعد لمراقبة صحة النباتات. هذه الأدوات تساهم في تحسين الإنتاج وتقليل الهدر، وتضع الفلاح في موقع الفاعل الواعي، لا المتلقي للظروف فقط.""",

    "guide.plant.2.title": "نصائح عملية عن الزراعة",
    "guide.plant.2.body": """الإدارة الفلاحية الناجحة تقوم على المراقبة اليومية والانتباه للتفاصيل الصغيرة التي قد تُحدث فرقاً كبيراً في نهاية الموسم. فالنبات، كالكائن الحي، يستجيب بسرعة لأي خلل في البيئة المحيطة به.

من الضروري تفقد الحقول بانتظام، خصوصاً في المراحل الأولى من النمو. أي تغير في لون الأوراق، أو ظهور بقع غير طبيعية، أو ضعف في النمو قد يكون مؤشراً مبكراً على نقص عنصر غذائي أو بداية إصابة مرضية.

التعقيم الدوري للأدوات الزراعية، خاصة أدوات التقليم، يقلل من انتقال الأمراض بين النباتات. كما يُستحسن تجنب العمل في الحقول خلال فترات الرطوبة العالية لتفادي انتشار الفطريات.

تنظيم العمليات الزراعية في جدول زمني واضح – من الحرث إلى البذر، مروراً بالتسميد والري، وصولاً إلى الحصاد – يساعد على تفادي التداخل العشوائي للمهام ويضمن أفضل استغلال للموارد.

كما يُنصح الفلاح بتوثيق نشاطه الزراعي، من خلال تسجيل مواعيد الزراعة وكميات الأسمدة المستعملة ونسب الإنتاج، لأن هذه البيانات تشكل مرجعاً قيماً لتحسين الأداء في المواسم القادمة.""",

    "guide.plant.3.title": "الري والتربة والأسمدة",
    "guide.plant.3.body": """الماء هو شريان الحياة في الزراعة، غير أن استعماله العشوائي قد يتحول من نعمة إلى سبب في تدهور التربة والمحصول. إن التوازن في الري مسألة علمية تعتمد على نوع النبات، ومرحلة نموه، وطبيعة التربة.

السقي الزائد يؤدي إلى اختناق الجذور بسبب نقص الأكسجين، كما يساهم في غسل العناصر الغذائية نحو الطبقات العميقة. في المقابل، نقص المياه يضع النبات تحت ضغط مائي يؤثر على عملية البناء الضوئي ويقلل من الإنتاج.

يُعتبر نظام الري بالتقطير من أكثر الأنظمة كفاءة، لأنه يوفر الماء ويوجهه مباشرة إلى منطقة الجذور، مما يقلل التبخر والهدر.

أما التربة، فهي منظومة حية تحتوي على كائنات دقيقة تساهم في تحليل المادة العضوية وتحرير العناصر الغذائية. إضافة السماد العضوي المتحلل بانتظام يعزز خصوبة التربة ويحسن بنيتها الفيزيائية.

الأسمدة المعدنية ينبغي استعمالها بناءً على نتائج تحليل التربة، واحترام الجرعات الموصى بها لتفادي تملح التربة أو تلوث المياه الجوفية. إن التسميد المتوازن يعزز النمو الخضري والإزهار والإثمار، ويمنح المحصول جودة عالية وقابلية تسويقية أفضل.""",

    "guide.plant.4.title": "دليل قصير للموسمية الزراعية",
    "guide.plant.4.body": """لكل محصول دورة زمنية دقيقة تبدأ بالبذر وتنتهي بالحصاد، وبينهما مراحل نمو حساسة تتطلب عناية خاصة. إن احترام التقويم الزراعي المحلي هو مفتاح النجاح في الإنتاج.

في المناطق ذات المناخ المتوسطي، تُزرع الحبوب غالباً في الخريف لتستفيد من أمطار الشتاء، بينما تُغرس الخضروات الصيفية في الربيع بعد زوال خطر الصقيع.

الأشجار المثمرة تحتاج إلى تقليم مدروس خلال فترات السكون الشتوي لتحفيز نمو متوازن في الربيع. كما أن عمليات التلقيح، سواء الطبيعية أو الاصطناعية، تلعب دوراً حاسماً في تحسين نسبة العقد والإنتاج.

الموسمية لا تعني فقط توقيت الزرع، بل تشمل أيضاً توقيت التسميد، الري، مكافحة الآفات، وحتى الحصاد. فالحصاد المبكر قد يؤثر على الطعم والقيمة الغذائية، بينما التأخر فيه قد يؤدي إلى فقدان جزء من الإنتاج.

إن الفلاح الواعي هو من يقرأ الأرض كما يقرأ كتاباً مفتوحاً، يفهم إشاراتها، ويتفاعل مع تغيراتها، ويُدرك أن الزراعة ليست مجرد مهنة، بل مسؤولية تجاه الغذاء والبيئة والمجتمع.""",

    "guide.animal.1.title": "إرشادات تربية المواشي والدواجن",
    "guide.animal.1.body": """إن تربية المواشي والدواجن ليست نشاطاً عشوائياً يعتمد على الإطعام والرعاية البسيطة، بل هي منظومة إنتاجية متكاملة تقوم على أسس علمية دقيقة تجمع بين الإدارة الصحية، التغذية المتوازنة، تحسين السلالات، والوقاية البيطرية.

تبدأ التربية الناجحة باختيار السلالة المناسبة للبيئة المحلية. فالسلالات المحلية غالباً ما تتميز بقدرتها على التأقلم مع المناخ وظروف التغذية المحدودة، بينما السلالات المحسّنة قد تمنح إنتاجاً أعلى لكنها تحتاج إلى رعاية دقيقة وإدارة مكثفة.

يجب أن تتوفر في أماكن التربية شروط التهوية الجيدة، الإضاءة المناسبة، الحماية من الرطوبة والتيارات الهوائية الباردة، مع احترام المساحة اللازمة لكل رأس من الماشية أو لكل طائر لتفادي الاكتظاظ الذي يؤدي إلى الإجهاد وانتشار الأمراض.

النظافة عنصر أساسي في استدامة الإنتاج؛ تنظيف الحظائر بانتظام، التخلص من الفضلات بطريقة صحية، وتعقيم المشارب والمعالف يقلل بشكل كبير من المخاطر الصحية.

كما أن تسجيل بيانات القطيع – مثل تاريخ الولادة، التلقيحات، الإنتاج، والحالات المرضية – يُعد أداة إدارية ضرورية لتحسين الأداء ومتابعة التطور الإنتاجي.""",

    "guide.animal.2.title": "التغذية والأعلاف المناسبة",
    "guide.animal.2.body": """التغذية تمثل العمود الفقري للإنتاج الحيواني، إذ ترتبط مباشرة بصحة الحيوان ومردوديته. فالحيوان الذي يحصل على تغذية متوازنة يُظهر نمواً منتظماً، مناعة قوية، وإنتاجاً مستقراً.

تتكون العليقة الغذائية من عناصر أساسية تشمل الطاقة (الحبوب)، البروتينات (كسب الصويا، البقوليات)، الألياف (التبن)، والمعادن والفيتامينات. يجب أن تتوازن هذه المكونات وفقاً لنوع الحيوان، عمره، مرحلته الإنتاجية، وهدف التربية (لحم، حليب، بيض).

في الأبقار الحلوب، مثلاً، تزداد الحاجة إلى الطاقة والبروتين خلال فترة الإدرار، بينما في الدواجن البيّاضة، يُعد الكالسيوم عنصراً أساسياً لضمان جودة قشرة البيض.

من المهم تجنب التغييرات المفاجئة في النظام الغذائي، لأن الجهاز الهضمي للحيوان يحتاج إلى فترة تأقلم. كما ينبغي تخزين الأعلاف في أماكن جافة ومهوّاة لمنع التعفن أو التلوث الفطري.

توفير الماء النظيف بكميات كافية لا يقل أهمية عن العلف، فالماء يدخل في جميع العمليات الحيوية، ونقصه يؤدي إلى تراجع فوري في الإنتاج.""",

    "guide.animal.3.title": "الأمراض الشائعة والتلقيحات",
    "guide.animal.3.body": """الوقاية خير من العلاج، وهذه القاعدة تنطبق بقوة على قطاع التربية الحيوانية. فالأمراض المعدية يمكن أن تنتشر بسرعة داخل القطيع، مسببة خسائر اقتصادية جسيمة.

من بين الأمراض الشائعة في المواشي: الحمى القلاعية، التسممات الغذائية، الطفيليات الداخلية والخارجية، وأمراض الجهاز التنفسي. أما في الدواجن، فتنتشر أمراض مثل النيوكاسل، الكوكسيديا، والتهاب القصبات المعدي.

التلقيح الدوري وفق برنامج بيطري معتمد هو الوسيلة الأنجع للحماية. ينبغي الالتزام بمواعيد اللقاحات وتسجيلها بدقة، مع احترام شروط الحفظ والنقل لضمان فعاليتها.

العزل الفوري للحيوانات المريضة، واستشارة الطبيب البيطري عند ظهور أعراض غير طبيعية، يمنع تفاقم الوضع وانتشار العدوى.

كما يُستحسن إجراء فحوصات دورية للكشف المبكر عن الأمراض الطفيلية أو نقص العناصر الغذائية، مما يساهم في الحفاظ على قطيع صحي ومنتج.""",

    "guide.animal.4.title": "إنتاج الحليب والبيض والصوف",
    "guide.animal.4.body": """الإنتاج الحيواني يعتمد على التوازن بين الوراثة، التغذية، والإدارة الجيدة.

في إنتاج الحليب، تلعب العوامل الوراثية والتغذية المتوازنة دوراً محورياً. يجب احترام أوقات الحلب، والحفاظ على نظافة الضرع والمعدات لتفادي التهابات الضرع التي تؤثر على جودة الحليب وكميته.

أما في إنتاج البيض، فإن انتظام الإضاءة في حظائر الدواجن يؤثر مباشرة على معدل الإنتاج، حيث تحتاج الدجاجة البيّاضة إلى عدد ساعات إضاءة مناسب لتحفيز وضع البيض.

فيما يخص الصوف، فإن جودة التغذية وصحة القطيع تؤثران على نعومة الألياف وكثافتها. كما أن توقيت الجزّ يجب أن يكون مدروساً لتفادي تعريض الحيوان للإجهاد الحراري أو البرد.

الإنتاج الجيد لا يُقاس فقط بالكمية، بل بالجودة أيضاً. فالمنتج النظيف والمطابق للمعايير الصحية يكتسب ثقة المستهلك ويحقق قيمة سوقية أعلى.""",

    "guide.animal.5.title": "دليل موسمي للتربية الحيوانية",
    "guide.animal.5.body": """التربية الحيوانية نشاط يرتبط ارتباطاً وثيقاً بدورات الفصول. ففي الشتاء، تحتاج الحيوانات إلى حماية إضافية من البرد والرطوبة، مع زيادة نسب الطاقة في العليقة لتعويض فقدان الحرارة.

في الربيع، تُعد هذه الفترة مناسبة لتحسين التغذية والاستفادة من المراعي الطبيعية، كما أنها موسم ولادات في العديد من الأنظمة التقليدية.

أما الصيف، فيتطلب اهتماماً خاصاً بتوفير الظل والماء لتجنب الإجهاد الحراري، خاصة في الأبقار الحلوب والدواجن.

في الخريف، يُستحسن التحضير لفترة الشتاء من خلال تخزين الأعلاف، صيانة الحظائر، ومراجعة البرامج الصحية.

إن فهم الإيقاع الموسمي للتربية الحيوانية يمكّن المربي من توقع الاحتياجات مسبقاً، واتخاذ قرارات مدروسة تضمن استمرارية الإنتاج واستقرار الدخل.""",

    # =========================
    # Legal Guide (Virtual Lawyer)
    # =========================
    "law.menu_title": "⚖️ مرشدك القانوني",
    "law.menu.faq": "📌 أسئلة قانونية جاهزة",
    "law.menu.search": "🔎 بحث بالكتابة",
    "law.menu.voice": "🎤 بحث بالصوت",
    "law.faq_title": "📌 الأسئلة القانونية الجاهزة",

    "law.disclaimer.title": "تنبيه قانوني مهم",
    "law.disclaimer.body": (
        "هذا المرشد يقدم معلومات عامة للتوعية فقط، ولا يُعتبر استشارة قانونية رسمية.\n"
        "قد تختلف الإجراءات حسب الولاية والبلدية والجهات المختصة وحسب التحديثات القانونية.\n"
        "لأي نزاع أو قرار قانوني أو عقد ملزم أو متابعة قضائية، يرجى الرجوع إلى الجهات المختصة "
        "أو التواصل مع مستشار قانوني معتمد."
    ),

    "law.search_prompt": "🔎 اكتب سؤالك القانوني هنا: ",
    "law.best_matches": "أفضل النتائج المقترحة حسب سؤالك:",
    "law.no_match": (
        "⚠️ لم يتم العثور على جواب مناسب حسب الكلمات التي أدخلتها.\n"
        "حاول إعادة صياغة السؤال أو استعمال كلمات أبسط أو كلمات مفتاحية مثل: ترخيص، كراء، نقل، تلقيح، ذبح، أعلاف، عسل."
    ),
    "law.press_enter": "اضغط Enter للرجوع إلى القائمة...",
    "law.ask_listen": "🔊 هل تريد سماع الإجابة بالصوت؟ اكتب y للموافقة أو n للرفض: ",

    "law.voice_listen": "🎤 تفضل، تكلم الآن بوضوح... يتم الاستماع لبضع ثوانٍ.",
    "law.voice_fail": (
        "❌ لم أفهم الصوت بشكل واضح.\n"
        "حاول مرة أخرى، وتأكد من أن الميكروفون يعمل، وتكلم بوضوح وفي مكان هادئ."
    ),
    "law.you_said": "قلت: ",
    "law.voice.install_error": "❌ لم يتم العثور على بعض المكتبات اللازمة للتسجيل الصوتي أو تحويل الصوت إلى نص.",
    "law.voice.install_cmd": (
        "لتثبيت المكتبات المطلوبة، افتح الطرفية واكتب الأمر التالي:\n"
        "pip install sounddevice soundfile SpeechRecognition"
    ),

    # Synonyms
    "law.synonyms.bases": ["كراء", "ترخيص", "بيطري", "تلقيح", "نقل", "ذبح", "عسل", "أعلاف", "نفوق"],
    "law.synonyms.map.كراء": ["كرا", "ايجار", "إيجار", "استئجار", "تأجير"],
    "law.synonyms.map.ترخيص": ["رخصة", "تصريح", "اعتماد", "إذن"],
    "law.synonyms.map.بيطري": ["طبيب", "طبيب بيطري", "البيطرة", "مداواة"],
    "law.synonyms.map.تلقيح": ["لقاح", "تحصين", "تطعيم"],
    "law.synonyms.map.نقل": ["تنقل", "شحن", "ترحيل"],
    "law.synonyms.map.ذبح": ["مذبح", "سلخ", "مجزرة"],
    "law.synonyms.map.عسل": ["نحل", "خلايا", "منحل"],
    "law.synonyms.map.أعلاف": ["علف", "تغذية", "مأكول"],
    "law.synonyms.map.نفوق": ["موت", "هلاك"],

    # ✅ Cases (keep as-is, just included in same dict)
    "law.plants.cases.rent_land.title": "كراء الأراضي",
    "law.plants.cases.rent_land.desc": "شرح معمق: يجب توقيع عقد مكتوب بين المؤجر والمستأجر...",

    "law.plants.cases.land_reclamation.title": "الاستصلاح الزراعي",
    "law.plants.cases.land_reclamation.desc": "شرح معمق: عند تحويل أرض بور إلى أرض صالحة للزراعة...",

    "law.plants.cases.agri_partnership.title": "الشراكة الزراعية",
    "law.plants.cases.agri_partnership.desc": "شرح معمق: قبل الدخول في شراكة زراعية...",

    "law.plants.cases.sell_crops.title": "بيع المحاصيل",
    "law.plants.cases.sell_crops.desc": "شرح معمق: بيع المحاصيل يجب أن يتم وفق اتفاق واضح...",

    "law.plants.cases.agri_insurance.title": "التأمين الزراعي",
    "law.plants.cases.agri_insurance.desc": "شرح معمق: التأمين الزراعي يساعد على حماية الفلاح...",

    "law.plants.cases.water_irrigation.title": "المياه والري",
    "law.plants.cases.water_irrigation.desc": "شرح معمق: استعمال المياه في السقي يخضع لقواعد قانونية...",

    "law.plants.cases.pesticides.title": "المبيدات والكيماويات",
    "law.plants.cases.pesticides.desc": "شرح معمق: استعمال المبيدات والمواد الكيميائية يجب أن يكون وفق تعليمات...",

    "law.plants.cases.agri_marketing.title": "التسويق الزراعي",
    "law.plants.cases.agri_marketing.desc": "شرح معمق: التسويق الزراعي يتطلب تنظيم عملية البيع...",

    "law.plants.cases.agri_taxes.title": "الضرائب الزراعية",
    "law.plants.cases.agri_taxes.desc": "شرح معمق: بعض الأنشطة الفلاحية قد تتطلب تصريحاً أو تسجيلاً...",

    "law.plants.cases.land_ownership.title": "الملكية العقارية",
    "law.plants.cases.land_ownership.desc": "شرح معمق: توثيق ملكية الأرض ضروري لحماية الحقوق...",

    "law.plants.cases.machines.title": "الآلات الزراعية",
    "law.plants.cases.machines.desc": "شرح معمق: شراء أو استعمال الآلات الزراعية يجب أن يكون وفق شروط...",

    "law.plants.cases.farm_labor.title": "العمالة الزراعية",
    "law.plants.cases.farm_labor.desc": "شرح معمق: تشغيل العمال في الفلاحة يستلزم تحديد العلاقة القانونية...",

    "law.plants.cases.environmental_pollution.title": "الملوثات البيئية",
    "law.plants.cases.environmental_pollution.desc": "شرح معمق: حماية البيئة في المجال الفلاحي تشمل منع رمي النفايات...",

    "law.plants.cases.ip_products.title": "الملكية الفكرية للمنتجات",
    "law.plants.cases.ip_products.desc": "شرح معمق: حماية الأصناف النباتية والعلامات التجارية مفيدة...",

    "law.plants.cases.transport_products.title": "نقل المنتجات الزراعية",
    "law.plants.cases.transport_products.desc": "شرح معمق: نقل المنتجات الزراعية يتطلب احترام شروط النظافة...",

    "law.plants.cases.legal_declarations.title": "الإقرارات القانونية",
    "law.plants.cases.legal_declarations.desc": "شرح معمق: بعض العمليات مثل التصدير أو التعاقدات الكبيرة قد تتطلب...",

    "law.plants.cases.farmer_disputes.title": "النزاعات بين الفلاحين",
    "law.plants.cases.farmer_disputes.desc": "شرح معمق: النزاعات قد تكون حول الحدود، السقي، المرور...",

    "law.plants.cases.cooperative_farms.title": "المزارع التعاونية",
    "law.plants.cases.cooperative_farms.desc": "شرح معمق: المشاريع التعاونية تتطلب تنظيماً واضحاً...",

    "law.plants.cases.agri_loans.title": "القروض الزراعية",
    "law.plants.cases.agri_loans.desc": "شرح معمق: الحصول على قرض زراعي يتطلب غالباً ملفاً...",

    "law.plants.cases.work_safety.title": "السلامة المهنية",
    "law.plants.cases.work_safety.desc": "شرح معمق: السلامة المهنية في الفلاحة مهمة لتجنب الحوادث...",

    # Animals cases (same idea)
    "law.animals.cases.livestock_license.title": "تربية المواشي والترخيص",
    "law.animals.cases.livestock_license.desc": "شرح معمق: ممارسة نشاط تربية المواشي تتطلب احترام التنظيمات المحلية...",

    "law.animals.cases.vet_control.title": "الرخص الصحية والرقابة البيطرية",
    "law.animals.cases.vet_control.desc": "شرح معمق: يخضع نشاط تربية الحيوانات لرقابة بيطرية دورية...",

    "law.animals.cases.sell_animals.title": "بيع المواشي والحيوانات",
    "law.animals.cases.sell_animals.desc": "شرح معمق: بيع الحيوانات يجب أن يتم وفق ضوابط قانونية...",

    "law.animals.cases.transport_animals.title": "نقل الحيوانات",
    "law.animals.cases.transport_animals.desc": "شرح معمق: نقل المواشي يتطلب احترام شروط السلامة والرفق بالحيوان...",

    "law.animals.cases.epidemics_reporting.title": "الأمراض الوبائية والتبليغ الإجباري",
    "law.animals.cases.epidemics_reporting.desc": "شرح معمق: في حال ظهور أعراض مرض معدٍ داخل القطيع...",

    "law.animals.cases.mandatory_vaccines.title": "التلقيحات الإجبارية",
    "law.animals.cases.mandatory_vaccines.desc": "شرح معمق: تفرض القوانين البيطرية برامج تلقيح دورية...",

    "law.animals.cases.milk_regulation.title": "إنتاج الحليب وتنظيم بيعه",
    "law.animals.cases.milk_regulation.desc": "شرح معمق: يخضع إنتاج الحليب لرقابة صحية صارمة...",

    "law.animals.cases.eggs_marketing.title": "إنتاج البيض وتسويقه",
    "law.animals.cases.eggs_marketing.desc": "شرح معمق: إنتاج البيض يخضع لشروط تتعلق بالنظافة...",

    "law.animals.cases.slaughter_meat.title": "الذبح وتنظيم اللحوم",
    "law.animals.cases.slaughter_meat.desc": "شرح معمق: عمليات الذبح يجب أن تتم في مذابح معتمدة...",

    "law.animals.cases.beekeeping_honey.title": "تربية النحل وإنتاج العسل",
    "law.animals.cases.beekeeping_honey.desc": "شرح معمق: تربية النحل تستوجب تنظيم النشاط واحترام قوانين التنقل...",

    "law.animals.cases.wool_shearing.title": "إنتاج الصوف وجزّه",
    "law.animals.cases.wool_shearing.desc": "شرح معمق: إنتاج الصوف وجزّ الأغنام يجب أن يتم بطريقة تحافظ على سلامة الحيوان...",

    "law.animals.cases.feed_quality.title": "الأعلاف والرقابة على جودتها",
    "law.animals.cases.feed_quality.desc": "شرح معمق: شراء الأعلاف من مصادر معتمدة يساهم في حماية صحة القطيع...",

    "law.animals.cases.manure_environment.title": "الأسمدة العضوية الحيوانية",
    "law.animals.cases.manure_environment.desc": "شرح معمق: التخلص من الروث والمخلفات الحيوانية يجب أن يتم وفق معايير بيئية...",

    "law.animals.cases.livestock_insurance.title": "التأمين على المواشي",
    "law.animals.cases.livestock_insurance.desc": "شرح معمق: يمكن للمربي الاشتراك في برامج التأمين لحماية قطيعه...",

    "law.animals.cases.breeding_loans.title": "القروض لتمويل مشاريع التربية",
    "law.animals.cases.breeding_loans.desc": "شرح معمق: تمويل مشاريع التربية الحيوانية يتطلب غالباً دراسة جدوى...",

    "law.animals.cases.breeding_partnership.title": "الشراكة في مشاريع تربية الحيوانات",
    "law.animals.cases.breeding_partnership.desc": "شرح معمق: في حال إقامة مشروع مشترك لتربية الحيوانات...",

    "law.animals.cases.farm_workers.title": "العمالة في المزارع الحيوانية",
    "law.animals.cases.farm_workers.desc": "شرح معمق: تشغيل العمال في نشاط التربية الحيوانية يخضع لقوانين العمل...",

    "law.animals.cases.environment_protection.title": "حماية البيئة في التربية الحيوانية",
    "law.animals.cases.environment_protection.desc": "شرح معمق: النشاط الحيواني قد يؤثر على البيئة من خلال الروائح...",

    "law.animals.cases.barn_safety.title": "السلامة المهنية في الحظائر",
    "law.animals.cases.barn_safety.desc": "شرح معمق: يجب توفير معدات الوقاية للعاملين داخل الحظائر...",

    "law.animals.cases.breeders_disputes.title": "النزاعات بين المربين",
    "law.animals.cases.breeders_disputes.desc": "شرح معمق: عند حدوث نزاع بين المربين قد يكون السبب بيع غير واضح...",

    # =========================
    # Market
    # =========================
    "market.title": "🌿 السوق الفلاحي | Green Law",
    "market.current_section": "📌 القسم الحالي: ",
    "market.section.plant": "🌱 نباتي",
    "market.section.animal": "🐄 حيواني",

    "market.browse": "🔍 تصفح الإعلانات",
    "market.add_new": "➕ إضافة إعلان جديد",
    "market.edit": "✏️ تعديل إعلان (إعلاناتي فقط)",
    "market.delete": "🗑️ حذف إعلان (إعلاناتي فقط)",

    "market.featured_short": "⭐ إعلان مميز",
    "market.featured_badge": "🟨 هذا إعلان مميز (مُميز بالذهبي)",
    "market.ad_id": "🔑 ID: ",
    "market.ad_id_inline": "ID: ",
    "market.price_label": "السعر: ",
    "market.phone_label": "الهاتف: ",
    "market.phone_mask": "0X XX XX XX XX",
    "market.placeholder_dash": "—",

    "market.empty": "📭 لا توجد إعلانات حاليا.",
    "market.choose_category_browse": "اختر نوع الإعلانات:",
    "market.count_ads": "📌 عدد الإعلانات: ",
    "market.none_in_category": "🟡 لا يوجد أي إعلان في هذا النوع حاليا.",
    "market.press_enter_back": "اضغط Enter للرجوع...",

    "market.choose_category_add": "اختر نوع الإعلان:",
    "market.ad_info_title": "🧾 معلومات الإعلان:",
    "market.field.first_name": "الاسم: ",
    "market.field.last_name": "اللقب: ",
    "market.field.phone": "رقم الهاتف: ",
    "market.field.address_optional": "العنوان (اختياري): ",
    "market.field.wilaya": "الولاية: ",
    "market.field.commune": "البلدية: ",
    "market.field.title": "عنوان الإعلان: ",
    "market.field.price": "السعر: ",
    "market.field.qty": "الكمية أو الوزن: ",
    "market.field.desc": "وصف حر: ",
    "market.field.featured_prompt": "⭐ هل تريد جعل الإعلان مميزاً؟ (y/n): ",
    "market.required_error": "❌ يجب إدخال عنوان الإعلان والبلدية على الأقل.",
    "market.published_success": "✅ تم نشر الإعلان بنجاح!",

    "market.my_ads_title": "📌 إعلاناتي:",
    "market.no_my_ads": "📭 لا تملك أي إعلان في هذا القسم حاليا.",
    "market.edit_intro": "✏️ تعديل الإعلان: اترك الحقل فارغا ليبقى كما هو.",
    "market.edit.title": "عنوان الإعلان الحالي هو: ",
    "market.edit.price": "السعر الحالي هو: ",
    "market.edit.qty": "الكمية أو الوزن الحالي هو: ",
    "market.edit.wilaya": "الولاية الحالية هي: ",
    "market.edit.commune": "البلدية الحالية هي: ",
    "market.edit.desc": "الوصف الحالي هو: ",
    "market.edit.featured": "⭐ إعلان مميز؟ اكتب y أو n، أو اتركه فارغا بدون تغيير: ",
    "market.edit_success": "✅ تم تعديل الإعلان بنجاح!",

    "market.delete_confirm": "⚠️ هل تؤكد حذف الإعلان التالي؟ ",
    "market.delete_confirm_suffix": "(y/n): ",
    "market.delete_cancelled": "✅ تم إلغاء عملية الحذف.",
    "market.delete_success": "🗑️ تم حذف الإعلان بنجاح!",

    "market.category.plant.rent_equip": "تأجير المعدات الزراعية",
    "market.category.plant.sell_products": "بيع المنتجات الزراعية",
    "market.category.plant.inputs": "المدخلات الزراعية",
    "market.category.plant.lands_opportunities": "الأراضي والفرص الزراعية",
    "market.category.plant.plant_health": "خدمات صحة النباتات",
    "market.category.plant.factory_hotel_partnerships": "شراكات المصانع والفنادق",

    "market.category.animal.rent_equipment": "تأجير معدات التربية الحيوانية",
    "market.category.animal.livestock_market": "سوق المواشي والحيوانات",
    "market.category.animal.animal_products": "المنتجات الحيوانية",
    "market.category.animal.facilities_warehouses": "منشآت التربية الحيوانية (المستودعات)",
    "market.category.animal.feed": "الأعلاف الحيوانية",
    "market.category.animal.organic_fertilizer": "الأسمدة العضوية الزراعية",
    "market.category.animal.vet_services": "الخدمات البيطرية",
    "market.category.animal.factory_hotel_partnerships": "شراكات المصانع والفنادق",

    # Seeds
    "market.seed.name_placeholder": "X",
    "market.seed.address_placeholder": "—",
    "market.seed.qty_placeholder": "—",

    "market.seed.plant.potato.title": "بيع بطاطا موسمية بالجملة",
    "market.seed.plant.potato.price": "8.000–12.000 دج / قنطار (تقريبي حسب الموسم)",
    "market.seed.plant.potato.qty": "2 طن",
    "market.seed.plant.potato.wilaya": "عين الدفلى",
    "market.seed.plant.potato.commune": "العطاف",
    "market.seed.plant.potato.desc": "بطاطا نوعية جيدة. هذا إعلان توضيحي داخل التطبيق ويمكن حذفه لاحقاً.",

    "market.seed.plant.tractor.title": "كراء جرّار مع سائق للحرث والسقي",
    "market.seed.plant.tractor.price": "ابتداءً من 10.000 دج / يوم (حسب الخدمة)",
    "market.seed.plant.tractor.wilaya": "سطيف",
    "market.seed.plant.tractor.commune": "سطيف",
    "market.seed.plant.tractor.desc": "متوفر للحرث والتسوية والسقي. هذا إعلان توضيحي داخل التطبيق ويمكن حذفه لاحقاً.",

    "market.seed.plant.seedlings.title": "بيع بذور وشتلات (طماطم وفلفل وبصل)",
    "market.seed.plant.seedlings.price": "ابتداءً من 300 دج (حسب النوع)",
    "market.seed.plant.seedlings.qty": "كميات مختلفة",
    "market.seed.plant.seedlings.wilaya": "البليدة",
    "market.seed.plant.seedlings.commune": "العفرون",
    "market.seed.plant.seedlings.desc": "توفير بذور وشتلات موسمية حسب الطلب. هذا إعلان توضيحي داخل التطبيق ويمكن حذفه لاحقاً.",

    "market.seed.plant.contract.title": "عقد توريد خضر موسمية لمطعم أو فندق",
    "market.seed.plant.contract.price": "حسب الاتفاق (توريد أسبوعي)",
    "market.seed.plant.contract.qty": "من 1 إلى 3 طن في الأسبوع",
    "market.seed.plant.contract.wilaya": "الجزائر",
    "market.seed.plant.contract.commune": "باب الزوار",
    "market.seed.plant.contract.desc": "توريد منتظم وفق معايير جودة متفق عليها. هذا إعلان توضيحي داخل التطبيق ويمكن حذفه لاحقاً.",

    "market.seed.animal.ram.title": "كبش محلي للعيد",
    "market.seed.animal.ram.price": "70.000 دج (7 ملايين) - قابل للتفاوض",
    "market.seed.animal.ram.qty": "وزن تقريبي 50 كغ",
    "market.seed.animal.ram.wilaya": "الجلفة",
    "market.seed.animal.ram.commune": "الجلفة",
    "market.seed.animal.ram.desc": "كبش محلي بصحة جيدة. هذا إعلان توضيحي داخل التطبيق ويمكن حذفه لاحقاً.",

    "market.seed.animal.eggs.title": "بيع بيض بلدي (صفيحة 30 بيضة)",
    "market.seed.animal.eggs.price": "500 دج / صفيحة (تقريبي)",
    "market.seed.animal.eggs.qty": "10 صفائح",
    "market.seed.animal.eggs.wilaya": "قسنطينة",
    "market.seed.animal.eggs.commune": "قسنطينة",
    "market.seed.animal.eggs.desc": "بيض طازج يومي. هذا إعلان توضيحي داخل التطبيق ويمكن حذفه لاحقاً.",

    "market.seed.animal.vet.title": "طبيب بيطري متنقل للمواشي والدواجن",
    "market.seed.animal.vet.price": "زيارة ابتداءً من 2.500 دج",
    "market.seed.animal.vet.qty": "تغطية حسب المنطقة",
    "market.seed.animal.vet.wilaya": "وهران",
    "market.seed.animal.vet.commune": "وهران",
    "market.seed.animal.vet.desc": "تلقيح وعلاج ومتابعة. هذا إعلان توضيحي داخل التطبيق ويمكن حذفه لاحقاً.",

    "market.seed.animal.milk_contract.title": "توريد حليب طازج يومي بعقد",
    "market.seed.animal.milk_contract.price": "ابتداءً من 75 دج / لتر (حسب الجودة والكمية)",
    "market.seed.animal.milk_contract.qty": "150 لتر في اليوم",
    "market.seed.animal.milk_contract.wilaya": "تيارت",
    "market.seed.animal.milk_contract.commune": "تيارت",
    "market.seed.animal.milk_contract.desc": "توريد يومي بمعايير جودة متفق عليها. هذا إعلان توضيحي داخل التطبيق ويمكن حذفه لاحقاً.",

    # =========================
    # Farmer Passport
    # =========================
    "passport.menu_title": "🪪 جواز الفلاح",
    "passport.menu_myfiles": "ملفاتي (بحث 🔍 + تحميل)",
    "passport.menu_add": "إضافة ملف جديد (Scan / Camera / PDF)",
    "passport.menu_qr_gallery": "معرض أكواد QR (بحث 🔍)",
    "passport.menu_open_qr": "فتح ملف عبر اختيار (QR)",

    "passport.no_user": "❌ لم يتم العثور على رقم المستخدم.",
    "passport.empty": "📁 جواز الفلاح فارغ.",

    "passport.add_title": "➕ إضافة ملف جديد",
    "passport.add_scan": "إضافة عبر Scan (مسح ضوئي)",
    "passport.add_camera": "إضافة عبر Camera (صور)",
    "passport.add_pdf": "إضافة PDF جاهز",

    "passport.doc_title": "عنوان الملف: ",
    "passport.scan_path": "مسار الملف بعد المسح (PDF/PNG/JPG): ",
    "passport.camera_path": "مسار الصورة (PNG/JPG): ",
    "passport.pdf_path": "مسار PDF: ",

    "passport.default_scan_title": "ملف مسح ضوئي",
    "passport.default_camera_title": "ملف صورة",
    "passport.default_pdf_title": "ملف PDF",

    "passport.not_found": "❌ الملف غير موجود.",
    "passport.read_fail": "❌ تعذر قراءة الملف.",
    "passport.stored": "✅ تم حفظ الملف في جواز الفلاح.",

    "passport.myfiles_title": "📂 ملفاتي",
    "passport.search_hint": "🔍 اكتب سنة للبحث (مثال: 2022) أو اتركها فارغة لعرض الكل:",
    "passport.search_none": "❌ لا توجد ملفات لهذه السنة.",
    "passport.list_title": "قائمة الملفات:",
    "passport.year": "السنة",
    "passport.type": "النوع",
    "passport.download": "تحميل",
    "passport.press_enter": "اضغط Enter للرجوع...",

    "passport.qr_gallery_title": "🔳 معرض أكواد QR",
    "passport.qr_list_title": "قائمة الأكواد:",
    "passport.qr_missing": "(QR غير متوفر)",
    "passport.qr_scan_note": "📱 امسح QR لتحميل أو فتح الملف",

    "passport.open_title": "📌 فتح ملف عبر اختيار QR",
    "passport.open_path_only": "📄 هذا ملف غير نصي. افتحه من المسار التالي:",
    "passport.qr_rebuild_fail": "⚠️ تعذر إعادة إنشاء رمز QR لهذا الملف.",

    # =========================
    # Smart Maps
    # =========================
    "ui.menu.option_5": "الخريطة الذكية",

"smart_map.page_title": "الخريطة الذكية",
"smart_map.hero.title": "الخريطة الذكية",
"smart_map.hero.subtitle": "استكشف الخرائط التفاعلية للقطاع الفلاحي بطريقة احترافية وسريعة داخل منصة Green Law.",
"smart_map.section.current": "القسم الحالي",
"smart_map.section.plant": "قسم نباتي",
"smart_map.section.animal": "قسم حيواني",
"smart_map.stats.points": "عدد النقاط",
"smart_map.cta.open": "فتح الخريطة",
"smart_map.cta.pdf": "تحميل PDF",
"smart_map.empty": "لا توجد خرائط متاحة حاليا.",
"smart_map.view.embed_title": "المعاينة التفاعلية",
"smart_map.view.note": "يمكنك التكبير والتصغير والتحرك داخل الخريطة مباشرة.",
"smart_map.card.water": "استكشف توزيع مياه الآبار حسب الولايات.",
"smart_map.card.agri": "تعرف على أهم المناطق الزراعية في الجزائر.",
"smart_map.card.wool": "عرض أهم المناطق المنتجة للصوف.",
"smart_map.card.honey": "عرض أهم المناطق المنتجة للعسل الحر.",
"smart_map.card.milk": "عرض أهم المناطق المنتجة للحليب ومشتقاته.",
"smart_map.card.meat": "عرض أهم المناطق المنتجة للحوم.",
    "maps.menu.title": "🗺️ الخريطة الذكية",

    "maps.title.water": "💧 خريطة توزيع مياه الآبار في الجزائر",
    "maps.title.agri": "🌿 خريطة أهم المناطق الزراعية في الجزائر",
    "maps.title.wool": "🧶 خريطة أهم المناطق المنتجة للصوف في الجزائر",
    "maps.title.honey": "🍯 خريطة أهم المناطق المنتجة للعسل الحر في الجزائر",
    "maps.title.milk": "🥛 خريطة أهم المناطق المنتجة للحليب ومشتقاته في الجزائر",
    "maps.title.meat": "🥩 خريطة أهم المناطق المنتجة للحوم في الجزائر",

    "maps.action.open": "فتح الخريطة",
    "maps.action.pdf": "تحميل PDF",

    "maps.pdf.summary_title": "ملخص نقاط الخريطة:",
    "maps.pdf.no_points": "لا توجد نقاط حاليا.",
    "maps.pdf.created": "✅ تم إنشاء ملف PDF بنجاح: ",

    "maps.water.count": "✅ عدد نقاط الآبار: ",
    "maps.warn.missing_prefix": "⚠️ أسماء ناقصة في WILAYA_CENTERS: ",

    "maps.legend.title": "🗝️ المفتاح",
    "maps.legend.default": "بيانات",
    "maps.legend.water": "💧 مياه الآبار",
    "maps.legend.agri": "🌿 مناطق زراعية",
    "maps.legend.honey": "🍯 عسل",
    "maps.legend.wool": "🧶 صوف",
    "maps.legend.milk": "🥛 حليب",
    "maps.legend.meat": "🥩 لحوم",

    "maps.desc.water": "💧 مياه الآبار",
    "maps.desc.meat": "🥩 إنتاج اللحوم",
    "maps.desc.wool": "🧶 إنتاج الصوف",
    "maps.desc.honey": "🍯 إنتاج العسل الحر",
    "maps.desc.milk": "🥛 إنتاج الحليب ومشتقاته"
}

# ---------------------------------
# Helpers
# ---------------------------------


def process_arabic(d: dict) -> dict:
    # إذا حبيتي تديري RTL shaping لاحقاً خليه هنا
    return d

def display_arabic(text: str) -> str:
    return text