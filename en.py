
# English language pack for Green Law (ONE FILE / ONE DICT)
# ✅ Single flat dictionary (dot-keys)

EN = {
    # =========================
    # Language chooser
    # =========================
    "ui.lang.choose_language": "Choose a language:",
    "ui.lang.arabic": "العربية",
    "ui.lang.french": "Français",
    "ui.lang.english": "English",
    "ui.lang.enter_choice": "➤ ",
    "ui.lang.invalid_choice": "Invalid choice.",

    # =========================
    # Main / General
    # =========================
    "ui.welcome_title": "Welcome to Green Law",
    "ui.exit": "Exit",
    "ui.back": "Back",

    "general.back": "Back",
    "general.choose": "➤ ",
    "general.invalid_choice": "Invalid choice.",
    "general.invalid_choice_long": "❌ Invalid choice. Please enter a valid number from the list.\n",
    "general.logout": "Log out",

    # =========================
    # Main menu (home)
    # =========================
    "ui.main.title": "Welcome to {app}",
    "ui.main.login": "Log in",
    "ui.main.signup": "Create an account",
    "ui.main.exit": "Exit",
    "ui.main.enter_choice": "➤ ",
    "ui.main.thanks": "Thanks for using Green Law!",
    "ui.main.invalid_choice": "Invalid choice.",
    "footer.note": "A smart digital platform for Algerian farmers",
    "auth.register.error_required": "Please fill in all fields",
"auth.register.username_exists": "Username already exists",
"auth.login.error_required": "Please enter username and password",
"auth.login.error_invalid": "Incorrect username or password",
    # =========================
    # Sections / Section menu
    # =========================
    "sections.title": "Choose a section:",
    "sections.plant": "🌱 Plant section",
    "sections.animal": "🐄 Animal section",
    "ui.enter": "Enter",
    "ui.menu.title": "Welcome {username} - \n{section}\n",
    "ui.menu.option_1": "Farmer guide",
    "ui.menu.option_2": "Statistics",
    "ui.menu.option_3": "Legal guide",
    "ui.menu.option_4": "Farmer market",
    "ui.menu.option_5": "Smart map",
    "ui.menu.option_6": "Farmer passport (QR)",
    "ui.menu.back_to_sections": "Back to section selection",
    "ui.menu.enter_choice": "➤ ",

    # =========================
    # Auth
    # =========================
    "auth.login": "Log in",
    "auth.create": "Create an account",
    "auth.username": "Username: ",
    "auth.password": "Password: ",
    "auth.welcome_user": "Welcome {name}!",
    "auth.username_not_recognized": "Username not recognized.\n",

    # Extra auth used in main.py
    "auth.enter_new_username": "New username: ",
    "auth.enter_username": "Username: ",
    "auth.enter_password": "Password: ",
    "auth.invalid_username": "Invalid username.",
    "auth.username_exists": "Username already exists.",
    "auth.signup_success": "Account created successfully.",
    "auth.login_success": "Welcome {username}!",
    "auth.login_fail": "Login failed.",
"auth.password": "Password",
"auth.login": "Login",
"auth.create_account": "Create a new account",
"auth.register.error_required": "Please fill in all fields",
    # =========================
    # Voice / STT
    # =========================
    "voice.missing_libs": "❌ Voice libraries are not installed.",
    "voice.install_hint": "pip install sounddevice soundfile SpeechRecognition",
    "voice.listening": "🎤 Speak now...",
    "voice.no_understand": "❌ I didn't understand the audio.",
    "voice.error": "❌ Speech recognition error: {e}",
    "voice.generic_error": "❌ Error: {e}",

    # =========================
    # TTS
    # =========================
    "tts.gtts_failed": "⚠️ gTTS failed: {e}, trying pyttsx3...",
    "tts.pyttsx3_failed": "⚠️ pyttsx3 failed: {e}",

    # =========================
    # Basic data (Wilayas translated to EN)
    # =========================
    "basic_data.wilayas": [
        "Adrar (01)", "Chlef (02)", "Laghouat (03)", "Oum El Bouaghi (04)", "Batna (05)",
        "Bejaia (06)", "Biskra (07)", "Bechar (08)", "Blida (09)", "Bouira (10)",
        "Tamanrasset (11)", "Tebessa (12)", "Tlemcen (13)", "Tiaret (14)", "Tizi Ouzou (15)",
        "Algiers (16)", "Djelfa (17)", "Jijel (18)", "Setif (19)", "Saida (20)",
        "Skikda (21)", "Sidi Bel Abbes (22)", "Annaba (23)", "Guelma (24)", "Constantine (25)",
        "Medea (26)", "Mostaganem (27)", "M'Sila (28)", "Mascara (29)", "Ouargla (30)",
        "Oran (31)", "El Bayadh (32)", "Illizi (33)", "Bordj Bou Arreridj (34)", "Boumerdes (35)",
        "El Tarf (36)", "Tindouf (37)", "Tissemsilt (38)", "El Oued (39)", "Khenchela (40)",
        "Souk Ahras (41)", "Tipaza (42)", "Mila (43)", "Ain Defla (44)", "Naama (45)",
        "Ain Temouchent (46)", "Ghardaia (47)", "Relizane (48)", "Timimoun (49)", "Bordj Badji Mokhtar (50)",
        "Ouled Djellal (51)", "Beni Abbes (52)", "Ain Salah (53)", "Ain Guezzam (54)", "Touggourt (55)",
        "Djanet (56)", "El M'Ghair (57)", "El Meniaa (58)", 
        
    ],

    # =========================
    # Statistics
    # =========================
    "statistics.source_line": "Source: FAOSTAT (FAO) – https://www.fao.org/faostat/",
    "statistics.wilaya_disclaimer": (
        "📍 Detailed wilaya-level data is not available on the platform.\n"
        "It will be added as soon as official data is published by the Algerian Ministry of Agriculture\n"
        "and Rural Development."
    ),

    "statistics.menu_title": "📊 Statistics",
    "statistics.option_choose_product": "View product statistics (chart + table)",
    "statistics.option_wilaya_note": "Wilaya data (list of wilayas)",
    "statistics.option_pdf": "PDF reports",

    "statistics.choose_category_title": "Choose a category:",
    "statistics.choose_product_title": "Choose a product:",
    "statistics.choose_wilaya_title": "Choose a wilaya:",
    "statistics.wilaya_selected": "Selected wilaya",

    "statistics.no_categories_in_section": "⚠️ No categories in this section.",
    "statistics.wilayas_list_not_found": "⚠️ Wilayas list not found.",
    "statistics.no_data_for_product_range": "⚠️ No data for this product in 2016–2024.",
    "statistics.no_data": "⚠️ No data.",

    "statistics.title_plot": "📈 Production trend",
    "statistics.xlabel_year": "Year",
    "statistics.ylabel_value": "Production",
    "statistics.table_year": "Year",
    "statistics.table_value": "Value",

    "statistics.pdf_menu_title": "📄 PDF reports",
    "statistics.pdf_years": "Download PDF by years (2016–2024)",
    "statistics.pdf_wilaya_one": "Download PDF for one wilaya",
    "statistics.pdf_wilayas_all": "Download full PDF for all wilayas",

    "statistics.pdf_years_title": "Statistics by years (2016–2024)",
    "statistics.pdf_wilaya_title": "Statistics by wilaya",
    "statistics.pdf_wilayas_all_title": "Full file for all wilayas (Warning)",
    "statistics.pdf_no_data": "No data available at the moment.",

    "pdf.created": "✅ PDF created:",

    "stats.categories.vegetables": "Vegetables",
    "stats.categories.citrus": "Citrus",
    "stats.categories.fruits": "Fruits",
    "stats.categories.cereals": "Cereals",
    "stats.categories.legumes": "Legumes",
    "stats.categories.oils": "Oils and oilseeds",
    "stats.categories.industrial": "Industrial crops",
    "stats.categories.meat": "Meat",
    "stats.categories.milk": "Milk",
    "stats.categories.eggs": "Eggs",
    "stats.categories.honey": "Honey",
    "stats.categories.wool": "Wool",

    # Products labels (translated)
    "stats.products.artichokes": "Artichokes",
    "stats.products.asparagus": "Asparagus",
    "stats.products.aubergines_eggplants": "Eggplants",
    "stats.products.cabbages": "Cabbages",
    "stats.products.carrots_turnips": "Carrots and turnips",
    "stats.products.cauliflowers_broccoli": "Cauliflowers and broccoli",
    "stats.products.celery": "Celery",
    "stats.products.cucumbers_gherkins": "Cucumbers and gherkins",
    "stats.products.garlic": "Garlic",
    "stats.products.lettuce_chicory": "Lettuce and chicory",
    "stats.products.onions_dry": "Onions (dry)",
    "stats.products.potatoes": "Potatoes",
    "stats.products.tomatoes": "Tomatoes",
    "stats.products.lemons_limes": "Lemons and limes",
    "stats.products.oranges": "Oranges",
    "stats.products.apples": "Apples",
    "stats.products.apricots": "Apricots",
    "stats.products.cherries": "Cherries",
    "stats.products.dates": "Dates",
    "stats.products.figs": "Figs",
    "stats.products.pears": "Pears",
    "stats.products.strawberries": "Strawberries",
    "stats.products.barley": "Barley",
    "stats.products.maize_corn": "Maize (corn)",
    "stats.products.rice": "Rice",
    "stats.products.wheat": "Wheat",
    "stats.products.beans_dry": "Beans (dry)",
    "stats.products.beans_green": "Beans (green)",
    "stats.products.broad_beans_dry": "Broad beans (dry)",
    "stats.products.broad_beans_green": "Broad beans (green)",
    "stats.products.chick_peas_dry": "Chickpeas (dry)",
    "stats.products.lentils_dry": "Lentils (dry)",
    "stats.products.olive_oil": "Olive oil",
    "stats.products.olives": "Olives",
    "stats.products.sugar_beet": "Sugar beet",

    "stats.products.beef_bone_in": "Beef (bone-in) (fresh/chilled)",
    "stats.products.chicken_meat": "Chicken meat (fresh/chilled)",
    "stats.products.sheep_meat": "Sheep meat (fresh/chilled)",
    "stats.products.milk_cattle": "Raw milk (cattle)",
    "stats.products.eggs_hens_in_shell_fresh": "Hen eggs (in shell) fresh",
    "stats.products.honey_natural": "Natural honey",
    "stats.products.wool_greasy_shorn": "Greasy shorn wool (raw)",
"statistics.menu_title": "Statistics",
"statistics.current_section": "Current section",
"statistics.section.plant": "Plant section",
"statistics.section.animal": "Animal section",
"statistics.hero_subtitle": "Explore agricultural and animal statistics, charts, reports, and wilaya data inside Green Law.",
"statistics.open_section": "Open section",
"statistics.choose_product_hint": "Choose a category, then select a product to view statistics, charts, or download a PDF.",
"statistics.card.product": "Choose a product, then view the chart and annual table.",
"statistics.card.wilayas": "Browse the wilaya list and the note about detailed data availability.",
"statistics.card.pdf": "Generate professional PDF reports by years or by wilayas.",
"statistics.table_title": "Annual table",
"statistics.years_range": "Period",
"statistics.pdf_hint": "You can download yearly reports or wilaya-related reports based on the selected product.",
    # =========================
    # Farmer Guide
    # =========================
    "guide.menu_title": "🌿 Your farmer guide",
    "guide.home": "Back to home",
    "guide.empty": "⚠️ No content available yet.",
    "guide.ask_listen": "🔊 Would you like to listen to it? (y/n): ",
    "guide.press_enter_back": "⏎ Press Enter to go back...",
    "guide.listen": "Listen",
    "guide.stop": "Stop",
    "guide.tts_fail": "❌ Could not play audio.",
    "guide.plant.title": "Farmer guide (Plant)",
    "guide.animal.title": "Farmer guide (Animal)",
    "guide.plant.1.title": "Technical Agricultural Guidelines",
    "guide.plant.1.body": """Agriculture is not merely sowing and waiting for harvest; it is a science based on understanding life cycles, soil-climate interaction, and plant responses to environmental factors. Success begins with proper planning and crop selection.

Farmers must consider rainfall, temperature, humidity, and wind patterns.

Soil analysis is essential to determine pH, organic matter, and key nutrients.

Crop rotation prevents soil exhaustion and pest spread.

Modern agriculture relies on precision technologies such as smart irrigation and remote sensing.""",

    "guide.plant.2.title": "Practical Farming Advice",
    "guide.plant.2.body": """Successful farming requires daily monitoring and attention to detail.

Regular field inspection helps detect early signs of nutrient deficiency or disease.

Tool sanitation reduces disease spread.

Organizing farming activities improves efficiency.

Keeping records helps improve future performance.""",

    "guide.plant.3.title": "Irrigation, Soil and Fertilizers",
    "guide.plant.3.body": """Water is essential, but overuse damages soil.

Balanced irrigation depends on plant type and growth stage.

Drip irrigation is highly efficient.

Soil is a living ecosystem enriched by organic matter.

Fertilizers should be applied according to soil analysis.""",

    "guide.plant.4.title": "Seasonal Agricultural Guide",
    "guide.plant.4.body": """Each crop follows a specific cycle from sowing to harvest.

Seasonal timing is crucial.

Winter cereals are sown in autumn, summer vegetables in spring.

Pruning and pollination affect productivity.

Agriculture is a responsibility toward food security and the environment.""",

    "guide.animal.1.title": "Livestock and Poultry Farming Guidelines",
    "guide.animal.1.body": """Animal farming relies on health management, balanced nutrition, breeding improvement, and veterinary prevention.

Choosing suitable breeds is essential.

Proper ventilation and hygiene prevent disease.

Record-keeping improves herd management.""",

    "guide.animal.2.title": "Proper Nutrition and Feed",
    "guide.animal.2.body": """Nutrition is the backbone of animal production.

Rations include energy, protein, fiber, minerals, and vitamins.

Needs vary by species and production stage.

Diet changes should be gradual.

Clean water is vital.""",

    "guide.animal.3.title": "Common Diseases and Vaccination",
    "guide.animal.3.body": """Prevention is better than treatment.

Vaccination programs protect livestock.

Isolating sick animals limits spread.

Regular veterinary checks are recommended.""",

    "guide.animal.4.title": "Milk, Egg and Wool Production",
    "guide.animal.4.body": """Production depends on genetics, nutrition, and management.

Hygiene affects milk quality.

Lighting influences egg production.

Wool quality depends on animal health.

Quality matters as much as quantity.""",

    "guide.animal.5.title": "Seasonal Animal Farming Guide",
    "guide.animal.5.body": """Animal farming follows seasonal cycles.

Winter requires protection and extra energy.

Spring offers natural grazing opportunities.

Summer demands shade and water.

Autumn preparation ensures winter stability.

Understanding seasonal rhythms ensures sustainable production.""",

    # =========================
    # Legal Guide (Virtual Lawyer)
    # =========================
    "law.menu_title": "⚖️ Your legal guide",
    "law.menu.faq": "📌 Ready legal questions",
    "law.menu.search": "🔎 Text search",
    "law.menu.voice": "🎤 Voice search",
    "law.faq_title": "📌 Ready legal questions",

    "law.disclaimer.title": "Important legal notice",
    "law.disclaimer.body": (
        "This guide provides general information for awareness only and is not official legal advice.\n"
        "Procedures may vary by wilaya, municipality, competent authorities, and legal updates.\n"
        "For any dispute, legal decision, binding contract, or court procedure, please refer to the competent authorities "
        "or contact a licensed legal advisor."
    ),

    "law.search_prompt": "🔎 Type your legal question here: ",
    "law.best_matches": "Best suggested matches for your question:",
    "law.no_match": (
        "⚠️ No suitable answer was found based on the words you entered.\n"
        "Try rephrasing the question or using simpler keywords like: permit, rent, transport, vaccination, slaughter, feed, honey."
    ),
    "law.press_enter": "Press Enter to return to the menu...",
    "law.ask_listen": "🔊 Want to hear the answer? Type y for yes or n for no: ",

    "law.voice_listen": "🎤 Speak clearly... listening for a few seconds.",
    "law.voice_fail": (
        "❌ I couldn't understand the audio clearly.\n"
        "Try again, make sure the microphone works, speak clearly, and stay in a quiet place."
    ),
    "law.you_said": "You said: ",
    "law.voice.install_error": "❌ Some required libraries for voice recording or speech-to-text were not found.",
    "law.voice.install_cmd": (
        "To install the required libraries, open the terminal and run:\n"
        "pip install sounddevice soundfile SpeechRecognition"
    ),

    # Synonyms (EN)
    "law.synonyms.bases": ["rent", "permit", "veterinary", "vaccination", "transport", "slaughter", "honey", "feed", "mortality"],
    "law.synonyms.map.rent": ["rent", "rental", "lease", "hire"],
    "law.synonyms.map.permit": ["permit", "license", "authorization", "approval"],
    "law.synonyms.map.veterinary": ["vet", "veterinary", "animal doctor", "treatment"],
    "law.synonyms.map.vaccination": ["vaccine", "vaccination", "immunization"],
    "law.synonyms.map.transport": ["transport", "move", "shipment", "transfer"],
    "law.synonyms.map.slaughter": ["slaughter", "abattoir", "butchery"],
    "law.synonyms.map.honey": ["honey", "bees", "hives", "apiary"],
    "law.synonyms.map.feed": ["feed", "fodder", "nutrition", "feeding"],
    "law.synonyms.map.mortality": ["death", "mortality", "loss"],

    # ✅ Cases (translated)
    "law.plants.cases.rent_land.title": "Land rental",
    "law.plants.cases.rent_land.desc": "Detailed explanation: a written contract should be signed between the owner and the tenant...",

    "law.plants.cases.land_reclamation.title": "Agricultural land reclamation",
    "law.plants.cases.land_reclamation.desc": "Detailed explanation: when converting unused land into arable land...",

    "law.plants.cases.agri_partnership.title": "Agricultural partnership",
    "law.plants.cases.agri_partnership.desc": "Detailed explanation: before entering an agricultural partnership...",

    "law.plants.cases.sell_crops.title": "Selling crops",
    "law.plants.cases.sell_crops.desc": "Detailed explanation: selling crops should be done under a clear agreement...",

    "law.plants.cases.agri_insurance.title": "Agricultural insurance",
    "law.plants.cases.agri_insurance.desc": "Detailed explanation: agricultural insurance helps protect farmers...",

    "law.plants.cases.water_irrigation.title": "Water and irrigation",
    "law.plants.cases.water_irrigation.desc": "Detailed explanation: using water for irrigation is subject to legal rules...",

    "law.plants.cases.pesticides.title": "Pesticides and chemicals",
    "law.plants.cases.pesticides.desc": "Detailed explanation: using pesticides and chemicals must follow safety instructions...",

    "law.plants.cases.agri_marketing.title": "Agricultural marketing",
    "law.plants.cases.agri_marketing.desc": "Detailed explanation: agricultural marketing requires organizing the selling process...",

    "law.plants.cases.agri_taxes.title": "Agricultural taxes",
    "law.plants.cases.agri_taxes.desc": "Detailed explanation: some agricultural activities may require a declaration or registration...",

    "law.plants.cases.land_ownership.title": "Land ownership",
    "law.plants.cases.land_ownership.desc": "Detailed explanation: documenting land ownership is essential to protect rights...",

    "law.plants.cases.machines.title": "Agricultural machinery",
    "law.plants.cases.machines.desc": "Detailed explanation: buying or using agricultural machines must follow safety rules...",

    "law.plants.cases.farm_labor.title": "Farm labor",
    "law.plants.cases.farm_labor.desc": "Detailed explanation: hiring farm workers requires clarifying the legal relationship...",

    "law.plants.cases.environmental_pollution.title": "Environmental pollution",
    "law.plants.cases.environmental_pollution.desc": "Detailed explanation: environmental protection in farming includes preventing waste dumping...",

    "law.plants.cases.ip_products.title": "Intellectual property for products",
    "law.plants.cases.ip_products.desc": "Detailed explanation: protecting plant varieties and trademarks can be beneficial...",

    "law.plants.cases.transport_products.title": "Transporting agricultural products",
    "law.plants.cases.transport_products.desc": "Detailed explanation: transporting farm products requires hygiene and proper storage...",

    "law.plants.cases.legal_declarations.title": "Legal declarations",
    "law.plants.cases.legal_declarations.desc": "Detailed explanation: some operations like exporting or large contracts may require...",

    "law.plants.cases.farmer_disputes.title": "Disputes between farmers",
    "law.plants.cases.farmer_disputes.desc": "Detailed explanation: disputes may involve boundaries, irrigation, access routes...",

    "law.plants.cases.cooperative_farms.title": "Cooperative farms",
    "law.plants.cases.cooperative_farms.desc": "Detailed explanation: cooperative projects require clear organization...",

    "law.plants.cases.agri_loans.title": "Agricultural loans",
    "law.plants.cases.agri_loans.desc": "Detailed explanation: getting an agricultural loan usually requires a full file...",

    "law.plants.cases.work_safety.title": "Work safety",
    "law.plants.cases.work_safety.desc": "Detailed explanation: safety at work in farming is crucial to avoid accidents...",

    # Animals cases
    "law.animals.cases.livestock_license.title": "Livestock farming and permits",
    "law.animals.cases.livestock_license.desc": "Detailed explanation: running livestock activities requires complying with local regulations...",

    "law.animals.cases.vet_control.title": "Health permits and veterinary control",
    "law.animals.cases.vet_control.desc": "Detailed explanation: animal farming is subject to periodic veterinary monitoring...",

    "law.animals.cases.sell_animals.title": "Selling livestock and animals",
    "law.animals.cases.sell_animals.desc": "Detailed explanation: selling animals must follow rules that ensure a clear price...",

    "law.animals.cases.transport_animals.title": "Transporting animals",
    "law.animals.cases.transport_animals.desc": "Detailed explanation: transporting livestock must ensure safety and animal welfare...",

    "law.animals.cases.epidemics_reporting.title": "Epidemic diseases and mandatory reporting",
    "law.animals.cases.epidemics_reporting.desc": "Detailed explanation: if contagious disease symptoms appear in the herd...",

    "law.animals.cases.mandatory_vaccines.title": "Mandatory vaccines",
    "law.animals.cases.mandatory_vaccines.desc": "Detailed explanation: veterinary regulations impose periodic vaccination programs...",

    "law.animals.cases.milk_regulation.title": "Milk production and sales regulation",
    "law.animals.cases.milk_regulation.desc": "Detailed explanation: milk production is subject to strict hygiene control...",

    "law.animals.cases.eggs_marketing.title": "Egg production and marketing",
    "law.animals.cases.eggs_marketing.desc": "Detailed explanation: egg production must respect hygiene and storage conditions...",

    "law.animals.cases.slaughter_meat.title": "Slaughter and meat regulation",
    "law.animals.cases.slaughter_meat.desc": "Detailed explanation: slaughter must be carried out in approved slaughterhouses...",

    "law.animals.cases.beekeeping_honey.title": "Beekeeping and honey production",
    "law.animals.cases.beekeeping_honey.desc": "Detailed explanation: beekeeping requires organizing activity and respecting movement rules...",

    "law.animals.cases.wool_shearing.title": "Wool production and shearing",
    "law.animals.cases.wool_shearing.desc": "Detailed explanation: shearing must protect the animal and avoid injuries...",

    "law.animals.cases.feed_quality.title": "Feed and quality control",
    "law.animals.cases.feed_quality.desc": "Detailed explanation: buying feed from trusted sources protects herd health...",

    "law.animals.cases.manure_environment.title": "Manure and environmental safety",
    "law.animals.cases.manure_environment.desc": "Detailed explanation: disposing manure must follow environmental standards...",

    "law.animals.cases.livestock_insurance.title": "Livestock insurance",
    "law.animals.cases.livestock_insurance.desc": "Detailed explanation: farmers can subscribe to insurance to protect livestock from risks...",

    "law.animals.cases.breeding_loans.title": "Loans to finance livestock projects",
    "law.animals.cases.breeding_loans.desc": "Detailed explanation: financing livestock projects usually requires a feasibility study...",

    "law.animals.cases.breeding_partnership.title": "Partnership in livestock projects",
    "law.animals.cases.breeding_partnership.desc": "Detailed explanation: in a joint livestock project, contributions must be clearly defined...",

    "law.animals.cases.farm_workers.title": "Workers on livestock farms",
    "law.animals.cases.farm_workers.desc": "Detailed explanation: employing workers in livestock farming falls under labor law...",

    "law.animals.cases.environment_protection.title": "Environmental protection in livestock farming",
    "law.animals.cases.environment_protection.desc": "Detailed explanation: livestock activity can impact the environment through waste and odors...",

    "law.animals.cases.barn_safety.title": "Work safety in barns",
    "law.animals.cases.barn_safety.desc": "Detailed explanation: protective equipment should be provided to workers in barns...",

    "law.animals.cases.breeders_disputes.title": "Disputes between breeders",
    "law.animals.cases.breeders_disputes.desc": "Detailed explanation: disputes may come from unclear sales, debts, partnerships, or movement issues...",

    # =========================
    # Market
    # =========================
    "market.title": "🌿 Farmer market | Green Law",
    "market.current_section": "📌 Current section: ",
    "market.section.plant": "🌱 Plant",
    "market.section.animal": "🐄 Animal",

    "market.browse": "🔍 Browse ads",
    "market.add_new": "➕ Add a new ad",
    "market.edit": "✏️ Edit an ad (my ads only)",
    "market.delete": "🗑️ Delete an ad (my ads only)",

    "market.featured_short": "⭐ Featured ad",
    "market.featured_badge": "🟨 This is a featured ad (highlighted in gold)",
    "market.ad_id": "🔑 ID: ",
    "market.ad_id_inline": "ID: ",
    "market.price_label": "Price: ",
    "market.phone_label": "Phone: ",
    "market.phone_mask": "0X XX XX XX XX",
    "market.placeholder_dash": "—",

    "market.empty": "📭 No ads available yet.",
    "market.choose_category_browse": "Choose the ad type:",
    "market.count_ads": "📌 Number of ads: ",
    "market.none_in_category": "🟡 No ads in this category yet.",
    "market.press_enter_back": "Press Enter to go back...",

    "market.choose_category_add": "Choose the ad type:",
    "market.ad_info_title": "🧾 Ad information:",
    "market.field.first_name": "First name: ",
    "market.field.last_name": "Last name: ",
    "market.field.phone": "Phone number: ",
    "market.field.address_optional": "Address (optional): ",
    "market.field.wilaya": "Wilaya: ",
    "market.field.commune": "Commune: ",
    "market.field.title": "Ad title: ",
    "market.field.price": "Price: ",
    "market.field.qty": "Quantity or weight: ",
    "market.field.desc": "Free description: ",
    "market.field.featured_prompt": "⭐ Do you want to feature this ad? (y/n): ",
    "market.required_error": "❌ You must enter at least the ad title and the commune.",
    "market.published_success": "✅ Ad published successfully!",

    "market.my_ads_title": "📌 My ads:",
    "market.no_my_ads": "📭 You don't have any ads in this section yet.",
    "market.edit_intro": "✏️ Edit: leave the field empty to keep it unchanged.",
    "market.edit.title": "Current title is: ",
    "market.edit.price": "Current price is: ",
    "market.edit.qty": "Current quantity/weight is: ",
    "market.edit.wilaya": "Current wilaya is: ",
    "market.edit.commune": "Current commune is: ",
    "market.edit.desc": "Current description is: ",
    "market.edit.featured": "⭐ Featured? type y or n, or leave empty to keep unchanged: ",
    "market.edit_success": "✅ Ad updated successfully!",

    "market.delete_confirm": "⚠️ Do you confirm deleting the following ad? ",
    "market.delete_confirm_suffix": "(y/n): ",
    "market.delete_cancelled": "✅ Deletion cancelled.",
    "market.delete_success": "🗑️ Ad deleted successfully!",

    "market.category.plant.rent_equip": "Rent agricultural equipment",
    "market.category.plant.sell_products": "Sell agricultural products",
    "market.category.plant.inputs": "Agricultural inputs",
    "market.category.plant.lands_opportunities": "Lands and agricultural opportunities",
    "market.category.plant.plant_health": "Plant health services",
    "market.category.plant.factory_hotel_partnerships": "Factory and hotel partnerships",

    "market.category.animal.rent_equipment": "Rent livestock equipment",
    "market.category.animal.livestock_market": "Livestock and animal market",
    "market.category.animal.animal_products": "Animal products",
    "market.category.animal.facilities_warehouses": "Livestock facilities (warehouses)",
    "market.category.animal.feed": "Animal feed",
    "market.category.animal.organic_fertilizer": "Organic agricultural fertilizer",
    "market.category.animal.vet_services": "Veterinary services",
    "market.category.animal.factory_hotel_partnerships": "Factory and hotel partnerships",

    # Seeds
    "market.seed.name_placeholder": "X",
    "market.seed.address_placeholder": "—",
    "market.seed.qty_placeholder": "—",

    "market.seed.plant.potato.title": "Wholesale seasonal potatoes for sale",
    "market.seed.plant.potato.price": "8,000–12,000 DZD / quintal (approx., depends on season)",
    "market.seed.plant.potato.qty": "2 tons",
    "market.seed.plant.potato.wilaya": "Ain Defla",
    "market.seed.plant.potato.commune": "El Attaf",
    "market.seed.plant.potato.desc": "Good quality potatoes. Demo ad inside the app (can be removed later).",

    "market.seed.plant.tractor.title": "Tractor rental with driver (plowing & irrigation)",
    "market.seed.plant.tractor.price": "From 10,000 DZD / day (depending on service)",
    "market.seed.plant.tractor.wilaya": "Setif",
    "market.seed.plant.tractor.commune": "Setif",
    "market.seed.plant.tractor.desc": "Available for plowing, leveling, and irrigation. Demo ad inside the app (can be removed later).",

    "market.seed.plant.seedlings.title": "Seeds and seedlings for sale (tomato, pepper, onion)",
    "market.seed.plant.seedlings.price": "From 300 DZD (depending on type)",
    "market.seed.plant.seedlings.qty": "Various quantities",
    "market.seed.plant.seedlings.wilaya": "Blida",
    "market.seed.plant.seedlings.commune": "El Affroun",
    "market.seed.plant.seedlings.desc": "Seasonal seeds/seedlings available on request. Demo ad inside the app (can be removed later).",

    "market.seed.plant.contract.title": "Seasonal vegetables supply contract (restaurant/hotel)",
    "market.seed.plant.contract.price": "As agreed (weekly supply)",
    "market.seed.plant.contract.qty": "From 1 to 3 tons per week",
    "market.seed.plant.contract.wilaya": "Algiers",
    "market.seed.plant.contract.commune": "Bab Ezzouar",
    "market.seed.plant.contract.desc": "Regular supply with agreed quality standards. Demo ad inside the app (can be removed later).",

    "market.seed.animal.ram.title": "Local ram for Eid",
    "market.seed.animal.ram.price": "70,000 DZD - negotiable",
    "market.seed.animal.ram.qty": "Approx. weight 50 kg",
    "market.seed.animal.ram.wilaya": "Djelfa",
    "market.seed.animal.ram.commune": "Djelfa",
    "market.seed.animal.ram.desc": "Healthy local ram. Demo ad inside the app (can be removed later).",

    "market.seed.animal.eggs.title": "Farm eggs for sale (tray of 30 eggs)",
    "market.seed.animal.eggs.price": "500 DZD / tray (approx.)",
    "market.seed.animal.eggs.qty": "10 trays",
    "market.seed.animal.eggs.wilaya": "Constantine",
    "market.seed.animal.eggs.commune": "Constantine",
    "market.seed.animal.eggs.desc": "Fresh daily eggs. Demo ad inside the app (can be removed later).",

    "market.seed.animal.vet.title": "Mobile veterinarian for livestock and poultry",
    "market.seed.animal.vet.price": "Visit from 2,500 DZD",
    "market.seed.animal.vet.qty": "Coverage depends on area",
    "market.seed.animal.vet.wilaya": "Oran",
    "market.seed.animal.vet.commune": "Oran",
    "market.seed.animal.vet.desc": "Vaccination, treatment, and follow-up. Demo ad inside the app (can be removed later).",

    "market.seed.animal.milk_contract.title": "Daily fresh milk supply contract",
    "market.seed.animal.milk_contract.price": "From 75 DZD / liter (depending on quality/quantity)",
    "market.seed.animal.milk_contract.qty": "150 liters per day",
    "market.seed.animal.milk_contract.wilaya": "Tiaret",
    "market.seed.animal.milk_contract.commune": "Tiaret",
    "market.seed.animal.milk_contract.desc": "Daily supply with agreed quality standards. Demo ad inside the app (can be removed later).",

    # =========================
    # Farmer Passport
    # =========================
    "passport.menu_title": "🪪 Farmer passport",
    "passport.menu_myfiles": "My files (Search 🔍 + Download)",
    "passport.menu_add": "Add a new file (Scan / Camera / PDF)",
    "passport.menu_qr_gallery": "QR code gallery (Search 🔍)",
    "passport.menu_open_qr": "Open a file by selection (QR)",

    "passport.no_user": "❌ User ID not found.",
    "passport.empty": "📁 Farmer passport is empty.",

    "passport.add_title": "➕ Add a new file",
    "passport.add_scan": "Add via Scan",
    "passport.add_camera": "Add via Camera (photos)",
    "passport.add_pdf": "Add an existing PDF",

    "passport.doc_title": "File title: ",
    "passport.scan_path": "File path after scan (PDF/PNG/JPG): ",
    "passport.camera_path": "Image path (PNG/JPG): ",
    "passport.pdf_path": "PDF path: ",

    "passport.default_scan_title": "Scanned file",
    "passport.default_camera_title": "Image file",
    "passport.default_pdf_title": "PDF file",

    "passport.not_found": "❌ File not found.",
    "passport.read_fail": "❌ Could not read the file.",
    "passport.stored": "✅ File saved in the farmer passport.",

    "passport.myfiles_title": "📂 My files",
    "passport.search_hint": "🔍 Type a year to search (e.g., 2022) or leave blank to show all:",
    "passport.search_none": "❌ No files for this year.",
    "passport.list_title": "Files list:",
    "passport.year": "Year",
    "passport.type": "Type",
    "passport.download": "Download",
    "passport.press_enter": "Press Enter to go back...",

    "passport.qr_gallery_title": "🔳 QR code gallery",
    "passport.qr_list_title": "Codes list:",
    "passport.qr_missing": "(QR not available)",
    "passport.qr_scan_note": "📱 Scan the QR to download or open the file",

    "passport.open_title": "📌 Open a file by QR selection",
    "passport.open_path_only": "📄 This is a non-text file. Open it from the following path:",
    "passport.qr_rebuild_fail": "⚠️ Could not rebuild the QR code for this file.",

    # =========================
    # Smart Maps
    # =========================
"ui.menu.option_5": "Smart Map",

"smart_map.page_title": "Smart Map",
"smart_map.hero.title": "Smart Map",
"smart_map.hero.subtitle": "Explore interactive agriculture maps inside Green Law in a professional and fast way.",
"smart_map.section.current": "Current section",
"smart_map.section.plant": "Plant section",
"smart_map.section.animal": "Animal section",
"smart_map.stats.points": "Points count",
"smart_map.cta.open": "Open map",
"smart_map.cta.pdf": "Download PDF",
"smart_map.empty": "No maps are available at the moment.",
"smart_map.view.embed_title": "Interactive preview",
"smart_map.view.note": "You can zoom, pan, and explore the map directly.",
"smart_map.card.water": "Explore the distribution of well water by wilaya.",
"smart_map.card.agri": "Discover the main agricultural regions in Algeria.",
"smart_map.card.wool": "View the main wool-producing areas.",
"smart_map.card.honey": "View the main free-honey producing areas.",
"smart_map.card.milk": "View the main milk and dairy producing areas.",
"smart_map.card.meat": "View the main meat-producing areas.",

    "maps.menu.title": "🗺️ Smart map",

    "maps.title.water": "💧 Water wells distribution map in Algeria",
    "maps.title.agri": "🌿 Major agricultural zones map in Algeria",
    "maps.title.wool": "🧶 Main wool-producing areas map in Algeria",
    "maps.title.honey": "🍯 Main natural honey-producing areas map in Algeria",
    "maps.title.milk": "🥛 Main milk and dairy-producing areas map in Algeria",
    "maps.title.meat": "🥩 Main meat-producing areas map in Algeria",

    "maps.action.open": "Open the map",
    "maps.action.pdf": "Download PDF",

    "maps.pdf.summary_title": "Map points summary:",
    "maps.pdf.no_points": "No points available yet.",
    "maps.pdf.created": "✅ PDF created successfully: ",

    "maps.water.count": "✅ Number of well points: ",
    "maps.warn.missing_prefix": "⚠️ Missing names in WILAYA_CENTERS: ",

    "maps.legend.title": "🗝️ Legend",
    "maps.legend.default": "Data",
    "maps.legend.water": "💧 Water wells",
    "maps.legend.agri": "🌿 Agricultural zones",
    "maps.legend.honey": "🍯 Honey",
    "maps.legend.wool": "🧶 Wool",
    "maps.legend.milk": "🥛 Milk",
    "maps.legend.meat": "🥩 Meat",

    "maps.desc.water": "💧 Water wells",
    "maps.desc.meat": "🥩 Meat production",
    "maps.desc.wool": "🧶 Wool production",
    "maps.desc.honey": "🍯 Natural honey production",
    "maps.desc.milk": "🥛 Milk and dairy production"
}

# ---------------------------------
# Helpers
# ---------------------------------


def process_english(d: dict) -> dict:
    return d

def display_english(text: str) -> str:
    return text