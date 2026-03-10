# French language pack for Green Law (ONE FILE / ONE DICT)
# ✅ Single flat dictionary (dot-keys)

FR = {
    # =========================
    # Language chooser
    # =========================
    "ui.lang.choose_language": "Choisissez la langue :",
    "ui.lang.arabic": "العربية",
    "ui.lang.french": "Français",
    "ui.lang.english": "English",
    "ui.lang.enter_choice": "➤ ",
    "ui.lang.invalid_choice": "Choix invalide.",
    
    # =========================
    # Main / General
    # =========================
    "ui.welcome_title": "Bienvenue sur Green Law",
    "ui.exit": "Quitter",
    "ui.back": "Retour",

    "general.back": "Retour",
    "general.choose": "➤ ",
    "general.invalid_choice": "Choix invalide.",
    "general.invalid_choice_long": "❌ Choix invalide. Veuillez saisir un numéro valide dans la liste.\n",
    "general.logout": "Déconnexion",
"auth.register.error_required": "Veuillez remplir tous les champs",
"auth.register.username_exists": "Le nom d'utilisateur existe déjà",
    # =========================
    # Main menu (home)
    # =========================
    "ui.main.title": "Bienvenue sur {app}",
    "ui.main.login": "Connexion",
    "ui.main.signup": "Créer un compte",
    "ui.main.exit": "Quitter",
    "ui.main.enter_choice": "➤ ",
    "ui.main.thanks": "Merci d'avoir utilisé Green Law !",
    "ui.main.invalid_choice": "Choix invalide.",
    "footer.note": "Plateforme numérique intelligente pour l’agriculteur algérien",
   "auth.login.error_required": "Veuillez saisir le nom d'utilisateur et le mot de passe",
"auth.login.error_invalid": "Nom d'utilisateur ou mot de passe incorrect",
    # =========================
    # Sections / Section menu
    # =========================
    "sections.title": "Choisir la section :",
    "sections.plant": "🌱 Section végétale",
    "sections.animal": "🐄 Section animale",
    "ui.enter": "Entrer",
    "ui.menu.title": "Bienvenue {username} - \n{section}\n",
    "ui.menu.option_1": "Guide agricole",
    "ui.menu.option_2": "Statistiques",
    "ui.menu.option_3": "Guide juridique",
    "ui.menu.option_4": "Marché agricole",
    "ui.menu.option_5": "Carte intelligente",
    "ui.menu.option_6": "Passeport de l'agriculteur (QR)",
    "ui.menu.back_to_sections": "Retour au choix des sections",
    "ui.menu.enter_choice": "➤ ",

    # =========================
    # Auth
    # =========================
    "auth.login": "Connexion",
    "auth.create": "Créer un compte",
    "auth.username": "Nom d'utilisateur : ",
    "auth.password": "Mot de passe : ",
    "auth.welcome_user": "Bienvenue {name} !",
    "auth.username_not_recognized": "Nom d'utilisateur non reconnu.\n",

    # Extra auth used in main.py
    "auth.enter_new_username": "Nouveau nom d'utilisateur : ",
    "auth.enter_username": "Nom d'utilisateur : ",
    "auth.enter_password": "Mot de passe : ",
    "auth.invalid_username": "Nom d'utilisateur invalide.",
    "auth.username_exists": "Ce nom d'utilisateur existe déjà.",
    "auth.signup_success": "Compte créé avec succès.",
    "auth.login_success": "Bienvenue {username} !",
    "auth.login_fail": "Échec de la connexion.",
"auth.password": "Mot de passe",
"auth.login": "Se connecter",
"auth.create_account": "Créer un nouveau compte",
"auth.register.error_required": "Veuillez remplir tous les champs",
    # =========================
    # Voice / STT
    # =========================
    "voice.missing_libs": "❌ Les bibliothèques audio ne sont pas installées.",
    "voice.install_hint": "pip install sounddevice soundfile SpeechRecognition",
    "voice.listening": "🎤 Parlez maintenant...",
    "voice.no_understand": "❌ Je n'ai pas compris l'audio.",
    "voice.error": "❌ Erreur de reconnaissance vocale : {e}",
    "voice.generic_error": "❌ Erreur : {e}",

    # =========================
    # TTS
    # =========================
    "tts.gtts_failed": "⚠️ Échec de gTTS : {e}, tentative avec pyttsx3...",
    "tts.pyttsx3_failed": "⚠️ Échec de pyttsx3 : {e}",

    # =========================
    # Basic data (Wilayas translated to FR)
    # =========================
    "basic_data.wilayas": [
        "Adrar (01)", "Chlef (02)", "Laghouat (03)", "Oum El Bouaghi (04)", "Batna (05)",
        "Béjaïa (06)", "Biskra (07)", "Béchar (08)", "Blida (09)", "Bouira (10)",
        "Tamanrasset (11)", "Tébessa (12)", "Tlemcen (13)", "Tiaret (14)", "Tizi Ouzou (15)",
        "Alger (16)", "Djelfa (17)", "Jijel (18)", "Sétif (19)", "Saïda (20)",
        "Skikda (21)", "Sidi Bel Abbès (22)", "Annaba (23)", "Guelma (24)", "Constantine (25)",
        "Médéa (26)", "Mostaganem (27)", "M'Sila (28)", "Mascara (29)", "Ouargla (30)",
        "Oran (31)", "El Bayadh (32)", "Illizi (33)", "Bordj Bou Arréridj (34)", "Boumerdès (35)",
        "El Tarf (36)", "Tindouf (37)", "Tissemsilt (38)", "El Oued (39)", "Khenchela (40)",
        "Souk Ahras (41)", "Tipaza (42)", "Mila (43)", "Aïn Defla (44)", "Naâma (45)",
        "Aïn Témouchent (46)", "Ghardaïa (47)", "Relizane (48)", "Timimoun (49)", "Bordj Badji Mokhtar (50)",
        "Ouled Djellal (51)", "Béni Abbès (52)", "Aïn Salah (53)", "Aïn Guezzam (54)", "Touggourt (55)",
        "Djanet (56)", "El M'Ghair (57)", "El Meniaa (58)",
  
    ],

    # =========================
    # Statistics
    # =========================
    "statistics.source_line": "Source : FAOSTAT (FAO) – https://www.fao.org/faostat/",
    "statistics.wilaya_disclaimer": (
        "📍 Les données détaillées par wilaya ne sont pas disponibles sur la plateforme.\n"
        "Elles seront intégrées dès la publication des données officielles du Ministère de l'Agriculture\n"
        "et du Développement Rural (Algérie)."
    ),

    "statistics.menu_title": "📊 Statistiques",
    "statistics.option_choose_product": "Afficher les statistiques d'un produit (graphique + tableau)",
    "statistics.option_wilaya_note": "Données des wilayas (liste des wilayas)",
    "statistics.option_pdf": "Rapports PDF",

    "statistics.choose_category_title": "Choisissez la catégorie :",
    "statistics.choose_product_title": "Choisissez le produit :",
    "statistics.choose_wilaya_title": "Choisissez la wilaya :",
    "statistics.wilaya_selected": "Wilaya sélectionnée",

    "statistics.no_categories_in_section": "⚠️ Aucune catégorie dans cette section.",
    "statistics.wilayas_list_not_found": "⚠️ Liste des wilayas introuvable.",
    "statistics.no_data_for_product_range": "⚠️ Aucune donnée pour ce produit sur 2016–2024.",
    "statistics.no_data": "⚠️ Aucune donnée.",

    "statistics.title_plot": "📈 Évolution de la production",
    "statistics.xlabel_year": "Année",
    "statistics.ylabel_value": "Production",
    "statistics.table_year": "Année",
    "statistics.table_value": "Valeur",

    "statistics.pdf_menu_title": "📄 Rapports PDF",
    "statistics.pdf_years": "Télécharger PDF par années (2016–2024)",
    "statistics.pdf_wilaya_one": "Télécharger PDF pour une seule wilaya",
    "statistics.pdf_wilayas_all": "Télécharger PDF complet pour toutes les wilayas",

    "statistics.pdf_years_title": "Statistiques par années (2016–2024)",
    "statistics.pdf_wilaya_title": "Statistiques par wilaya",
    "statistics.pdf_wilayas_all_title": "Fichier complet pour toutes les wilayas (Avertissement)",
    "statistics.pdf_no_data": "Aucune donnée disponible pour le moment.",

    "pdf.created": "✅ Fichier PDF créé :",

    "stats.categories.vegetables": "Légumes",
    "stats.categories.citrus": "Agrumes",
    "stats.categories.fruits": "Fruits",
    "stats.categories.cereals": "Céréales",
    "stats.categories.legumes": "Légumineuses",
    "stats.categories.oils": "Huiles et graines oléagineuses",
    "stats.categories.industrial": "Cultures industrielles",
    "stats.categories.meat": "Viandes",
    "stats.categories.milk": "Lait",
    "stats.categories.eggs": "Œufs",
    "stats.categories.honey": "Miel",
    "stats.categories.wool": "Laine",

    # Products labels (translated)
    "stats.products.artichokes": "Artichauts",
    "stats.products.asparagus": "Asperges",
    "stats.products.aubergines_eggplants": "Aubergines",
    "stats.products.cabbages": "Choux",
    "stats.products.carrots_turnips": "Carottes et navets",
    "stats.products.cauliflowers_broccoli": "Choux-fleurs et brocolis",
    "stats.products.celery": "Céleri",
    "stats.products.cucumbers_gherkins": "Concombres et cornichons",
    "stats.products.garlic": "Ail",
    "stats.products.lettuce_chicory": "Laitue et chicorée",
    "stats.products.onions_dry": "Oignons (secs)",
    "stats.products.potatoes": "Pommes de terre",
    "stats.products.tomatoes": "Tomates",
    "stats.products.lemons_limes": "Citrons et citrons verts",
    "stats.products.oranges": "Oranges",
    "stats.products.apples": "Pommes",
    "stats.products.apricots": "Abricots",
    "stats.products.cherries": "Cerises",
    "stats.products.dates": "Dattes",
    "stats.products.figs": "Figues",
    "stats.products.pears": "Poires",
    "stats.products.strawberries": "Fraises",
    "stats.products.barley": "Orge",
    "stats.products.maize_corn": "Maïs",
    "stats.products.rice": "Riz",
    "stats.products.wheat": "Blé",
    "stats.products.beans_dry": "Haricots (secs)",
    "stats.products.beans_green": "Haricots (verts)",
    "stats.products.broad_beans_dry": "Fèves (sèches)",
    "stats.products.broad_beans_green": "Fèves (vertes)",
    "stats.products.chick_peas_dry": "Pois chiches (secs)",
    "stats.products.lentils_dry": "Lentilles (sèches)",
    "stats.products.olive_oil": "Huile d'olive",
    "stats.products.olives": "Olives",
    "stats.products.sugar_beet": "Betterave sucrière",

    "stats.products.beef_bone_in": "Viande de bœuf (avec os) (fraîche/réfrigérée)",
    "stats.products.chicken_meat": "Viande de poulet (fraîche/réfrigérée)",
    "stats.products.sheep_meat": "Viande de mouton (fraîche/réfrigérée)",
    "stats.products.milk_cattle": "Lait cru (bovins)",
    "stats.products.eggs_hens_in_shell_fresh": "Œufs de poule (avec coquille) frais",
    "stats.products.honey_natural": "Miel naturel",
    "stats.products.wool_greasy_shorn": "Laine tondue (grasse/brute)",
"statistics.menu_title": "Statistiques",
"statistics.current_section": "Section actuelle",
"statistics.section.plant": "Section végétale",
"statistics.section.animal": "Section animale",
"statistics.hero_subtitle": "Explorez les statistiques agricoles et animales, les graphiques, les rapports et les données des wilayas dans Green Law.",
"statistics.open_section": "Ouvrir la section",
"statistics.choose_product_hint": "Choisissez une catégorie puis un produit pour afficher les statistiques, les graphiques ou télécharger un PDF.",
"statistics.card.product": "Choisissez un produit puis consultez le graphique et le tableau annuel.",
"statistics.card.wilayas": "Consultez la liste des wilayas et la note concernant la disponibilité des données détaillées.",
"statistics.card.pdf": "Générez des rapports PDF professionnels par années ou par wilayas.",
"statistics.table_title": "Tableau annuel",
"statistics.years_range": "Période",
"statistics.pdf_hint": "Vous pouvez télécharger des rapports par années ou des rapports liés aux wilayas à partir du produit choisi.",
    # =========================
    # Farmer Guide
    # =========================
    "guide.menu_title": "🌿 Votre guide agricole",
    "guide.home": "Retour à l'accueil",
    "guide.empty": "⚠️ Aucun contenu pour le moment.",
    "guide.ask_listen": "🔊 Voulez-vous l'écouter en audio ? (y/n) : ",
    "guide.press_enter_back": "⏎ Appuyez sur Entrée pour revenir...",
    "guide.listen": "Écouter le texte",
    "guide.stop": "Arrêter",
    "guide.tts_fail": "❌ Impossible de lire l'audio.",
    "guide.plant.title": "Guide agricole (végétal)",
    "guide.animal.title": "Guide agricole (animal)",
    "guide.plant.1.title": "Recommandations techniques agricoles",
    "guide.plant.1.body": """L’agriculture n’est pas simplement l’action de semer et d’attendre la récolte ; c’est une science fondée sur une compréhension approfondie du cycle de la vie, de l’interaction entre le sol et le climat, et de la réaction des plantes aux facteurs environnementaux. La réussite d’un projet agricole commence dès la planification, où le choix de la culture constitue la première décision stratégique influençant la rentabilité de la saison.

L’agriculteur doit tenir compte des caractéristiques climatiques de la région : précipitations, températures, humidité et vents dominants. Les cultures d’hiver nécessitent des températures modérées et une certaine fraîcheur pour favoriser la germination, tandis que les cultures d’été exigent davantage de chaleur et de longues périodes d’ensoleillement.

L’étude du sol est essentielle. Les sols sableux diffèrent des sols argileux ou calcaires quant à leur capacité de rétention d’eau et de nutriments. L’analyse en laboratoire permet d’évaluer le pH, la teneur en matière organique et la disponibilité des éléments majeurs tels que l’azote, le phosphore et le potassium.

La rotation des cultures constitue un principe technique fondamental : elle prévient l’épuisement du sol, limite la propagation des parasites et améliore l’équilibre biologique.

L’agriculture moderne repose désormais sur des technologies de précision comme les capteurs d’humidité, l’irrigation intelligente et la télédétection pour surveiller la santé des plantes. Ces outils améliorent la production et réduisent les pertes.""",

    "guide.plant.2.title": "Conseils pratiques en agriculture",
    "guide.plant.2.body": """Une gestion agricole réussie repose sur une observation quotidienne et une attention aux détails. Les plantes réagissent rapidement aux déséquilibres de leur environnement.

Il est essentiel d’inspecter régulièrement les champs, surtout aux premières phases de croissance. Un changement de couleur des feuilles, des taches inhabituelles ou un ralentissement de croissance peuvent signaler une carence ou une maladie.

La désinfection des outils agricoles, notamment de taille, limite la propagation des maladies. Il est également conseillé d’éviter le travail en période de forte humidité afin de réduire les risques fongiques.

L’organisation des opérations agricoles selon un calendrier clair optimise l’utilisation des ressources.

Tenir un registre des activités agricoles permet d’améliorer les performances futures.""",

    "guide.plant.3.title": "Irrigation, sol et fertilisation",
    "guide.plant.3.body": """L’eau est la source de vie en agriculture, mais son usage excessif peut détériorer le sol. L’équilibre de l’irrigation dépend du type de plante, de son stade de croissance et de la nature du sol.

Un excès d’eau asphyxie les racines, tandis qu’un déficit provoque un stress hydrique et réduit la production.

L’irrigation goutte-à-goutte est l’un des systèmes les plus efficaces.

Le sol est un écosystème vivant. L’ajout régulier de matière organique améliore sa fertilité.

Les engrais minéraux doivent être appliqués selon les analyses du sol et dans les doses recommandées.""",

    "guide.plant.4.title": "Guide simplifié de la saisonnalité agricole",
    "guide.plant.4.body": """Chaque culture suit un cycle précis du semis à la récolte. Respecter le calendrier agricole local est essentiel.

Dans les climats méditerranéens, les céréales sont semées en automne, tandis que les légumes d’été sont plantés au printemps.

Les arbres fruitiers nécessitent une taille hivernale.

La saisonnalité inclut aussi la fertilisation, l’irrigation et la lutte contre les parasites.

L’agriculture est une responsabilité envers l’alimentation, l’environnement et la société.""",

    "guide.animal.1.title": "Recommandations pour l’élevage",
    "guide.animal.1.body": """L’élevage repose sur des bases scientifiques incluant la gestion sanitaire, la nutrition équilibrée, l’amélioration génétique et la prévention vétérinaire.

Le choix de la race adaptée à l’environnement est primordial.

Les bâtiments doivent assurer ventilation, lumière et espace suffisant.

La propreté est essentielle pour éviter les maladies.

Le suivi des données du troupeau améliore la gestion.""",

    "guide.animal.2.title": "Alimentation et fourrages adaptés",
    "guide.animal.2.body": """L’alimentation est fondamentale pour la santé et la productivité animale.

La ration comprend énergie, protéines, fibres, minéraux et vitamines.

Les besoins varient selon l’espèce et le stade de production.

Les changements alimentaires doivent être progressifs.

L’eau propre est indispensable.""",

    "guide.animal.3.title": "Maladies courantes et vaccination",
    "guide.animal.3.body": """La prévention est essentielle en élevage.

Les maladies infectieuses peuvent causer des pertes importantes.

La vaccination régulière selon un programme vétérinaire est indispensable.

L’isolement des animaux malades limite la propagation.

Des contrôles réguliers permettent un dépistage précoce.""",

    "guide.animal.4.title": "Production de lait, d’œufs et de laine",
    "guide.animal.4.body": """La production dépend de la génétique, de l’alimentation et de la gestion.

Le respect de l’hygiène influence la qualité du lait.

L’éclairage influence la production d’œufs.

La qualité de la laine dépend de la santé du troupeau.

La qualité est aussi importante que la quantité.""",

    "guide.animal.5.title": "Guide saisonnier de l’élevage",
    "guide.animal.5.body": """L’élevage est lié aux saisons.

En hiver, les animaux nécessitent protection et énergie supplémentaire.

Au printemps, les pâturages naturels sont exploités.

En été, l’ombre et l’eau sont essentielles.

En automne, il faut préparer l’hiver.

Comprendre le rythme saisonnier assure la stabilité de la production.""",

    # =========================
    # Legal Guide (Virtual Lawyer)
    # =========================
    "law.menu_title": "⚖️ Votre guide juridique",
    "law.menu.faq": "📌 Questions juridiques prêtes",
    "law.menu.search": "🔎 Recherche (texte)",
    "law.menu.voice": "🎤 Recherche (voix)",
    "law.faq_title": "📌 Questions juridiques prêtes",

    "law.disclaimer.title": "Avertissement juridique important",
    "law.disclaimer.body": (
        "Ce guide fournit des informations générales à titre de sensibilisation uniquement et ne constitue pas un avis juridique officiel.\n"
        "Les procédures peuvent varier selon la wilaya, la commune, les autorités compétentes et selon les mises à jour juridiques.\n"
        "Pour tout litige, décision juridique, contrat engageant ou procédure judiciaire, veuillez consulter les autorités compétentes "
        "ou contacter un conseiller juridique agréé."
    ),

    "law.search_prompt": "🔎 Écrivez votre question juridique ici : ",
    "law.best_matches": "Meilleures correspondances proposées selon votre question :",
    "law.no_match": (
        "⚠️ Aucune réponse correspondante n'a été trouvée selon les mots saisis.\n"
        "Essayez de reformuler la question ou d'utiliser des mots clés simples comme : autorisation, location, transport, vaccination, abattage, fourrages, miel."
    ),
    "law.press_enter": "Appuyez sur Entrée pour revenir au menu...",
    "law.ask_listen": "🔊 Voulez-vous écouter la réponse ? Tapez y pour oui ou n pour non : ",

    "law.voice_listen": "🎤 Parlez clairement... écoute pendant quelques secondes.",
    "law.voice_fail": (
        "❌ Je n'ai pas compris l'audio clairement.\n"
        "Réessayez et assurez-vous que le micro fonctionne, parlez clairement et dans un endroit calme."
    ),
    "law.you_said": "Vous avez dit : ",
    "law.voice.install_error": "❌ Certaines bibliothèques nécessaires à l'enregistrement vocal ou à la conversion voix→texte sont introuvables.",
    "law.voice.install_cmd": (
        "Pour installer les bibliothèques requises, ouvrez le terminal et tapez :\n"
        "pip install sounddevice soundfile SpeechRecognition"
    ),

    # Synonyms (FR)
    "law.synonyms.bases": ["location", "autorisation", "vétérinaire", "vaccination", "transport", "abattage", "miel", "fourrages", "mortalité"],
    "law.synonyms.map.location": ["location", "louer", "bail", "leasing"],
    "law.synonyms.map.autorisation": ["autorisation", "permis", "licence", "agrément"],
    "law.synonyms.map.vétérinaire": ["vétérinaire", "docteur", "soins", "médecine vétérinaire"],
    "law.synonyms.map.vaccination": ["vaccination", "vaccin", "immunisation"],
    "law.synonyms.map.transport": ["transport", "déplacement", "expédition", "acheminement"],
    "law.synonyms.map.abattage": ["abattage", "abattoir", "boucherie", "égorgement"],
    "law.synonyms.map.miel": ["miel", "abeilles", "ruches", "apiculture"],
    "law.synonyms.map.fourrages": ["fourrage", "aliments", "alimentation", "provende"],
    "law.synonyms.map.mortalité": ["mortalité", "mort", "décès"],

    # ✅ Cases (translated)
    "law.plants.cases.rent_land.title": "Location des terres",
    "law.plants.cases.rent_land.desc": "Explication approfondie : un contrat écrit doit être signé entre le bailleur et le locataire...",

    "law.plants.cases.land_reclamation.title": "Mise en valeur agricole",
    "law.plants.cases.land_reclamation.desc": "Explication approfondie : lors de la transformation d'une terre en friche en terre cultivable...",

    "law.plants.cases.agri_partnership.title": "Partenariat agricole",
    "law.plants.cases.agri_partnership.desc": "Explication approfondie : avant d'entrer dans un partenariat agricole...",

    "law.plants.cases.sell_crops.title": "Vente des récoltes",
    "law.plants.cases.sell_crops.desc": "Explication approfondie : la vente des récoltes doit se faire selon un accord clair...",

    "law.plants.cases.agri_insurance.title": "Assurance agricole",
    "law.plants.cases.agri_insurance.desc": "Explication approfondie : l'assurance agricole aide l'agriculteur à se protéger...",

    "law.plants.cases.water_irrigation.title": "Eau et irrigation",
    "law.plants.cases.water_irrigation.desc": "Explication approfondie : l'utilisation de l'eau pour l'irrigation est soumise à des règles juridiques...",

    "law.plants.cases.pesticides.title": "Pesticides et produits chimiques",
    "law.plants.cases.pesticides.desc": "Explication approfondie : l'usage des pesticides et produits chimiques doit respecter les consignes...",

    "law.plants.cases.agri_marketing.title": "Commercialisation agricole",
    "law.plants.cases.agri_marketing.desc": "Explication approfondie : la commercialisation agricole exige l'organisation de la vente...",

    "law.plants.cases.agri_taxes.title": "Fiscalité agricole",
    "law.plants.cases.agri_taxes.desc": "Explication approfondie : certaines activités agricoles peuvent nécessiter une déclaration ou un enregistrement...",

    "law.plants.cases.land_ownership.title": "Propriété foncière",
    "law.plants.cases.land_ownership.desc": "Explication approfondie : la preuve de propriété est essentielle pour protéger les droits...",

    "law.plants.cases.machines.title": "Machines agricoles",
    "law.plants.cases.machines.desc": "Explication approfondie : l'achat ou l'utilisation des machines agricoles doit respecter les règles...",

    "law.plants.cases.farm_labor.title": "Main-d'œuvre agricole",
    "law.plants.cases.farm_labor.desc": "Explication approfondie : l'emploi des travailleurs agricoles exige de clarifier la relation juridique...",

    "law.plants.cases.environmental_pollution.title": "Pollution environnementale",
    "law.plants.cases.environmental_pollution.desc": "Explication approfondie : la protection de l'environnement en agriculture inclut l'interdiction de jeter des déchets...",

    "law.plants.cases.ip_products.title": "Propriété intellectuelle des produits",
    "law.plants.cases.ip_products.desc": "Explication approfondie : protéger les variétés végétales et les marques peut être utile...",

    "law.plants.cases.transport_products.title": "Transport des produits agricoles",
    "law.plants.cases.transport_products.desc": "Explication approfondie : transporter des produits agricoles nécessite de respecter l'hygiène...",

    "law.plants.cases.legal_declarations.title": "Déclarations légales",
    "law.plants.cases.legal_declarations.desc": "Explication approfondie : certaines opérations comme l'exportation ou de grands contrats peuvent nécessiter...",

    "law.plants.cases.farmer_disputes.title": "Litiges entre agriculteurs",
    "law.plants.cases.farmer_disputes.desc": "Explication approfondie : les litiges peuvent concerner les limites, l'irrigation, le passage...",

    "law.plants.cases.cooperative_farms.title": "Exploitations coopératives",
    "law.plants.cases.cooperative_farms.desc": "Explication approfondie : les projets coopératifs exigent une organisation claire...",

    "law.plants.cases.agri_loans.title": "Prêts agricoles",
    "law.plants.cases.agri_loans.desc": "Explication approfondie : obtenir un prêt agricole nécessite souvent un dossier...",

    "law.plants.cases.work_safety.title": "Sécurité au travail",
    "law.plants.cases.work_safety.desc": "Explication approfondie : la sécurité professionnelle en agriculture est importante pour éviter les accidents...",

    # Animals cases
    "law.animals.cases.livestock_license.title": "Élevage et autorisation",
    "law.animals.cases.livestock_license.desc": "Explication approfondie : exercer une activité d'élevage implique de respecter la réglementation locale...",

    "law.animals.cases.vet_control.title": "Autorisation sanitaire et contrôle vétérinaire",
    "law.animals.cases.vet_control.desc": "Explication approfondie : l'élevage est soumis à un contrôle vétérinaire périodique...",

    "law.animals.cases.sell_animals.title": "Vente de bétail et d'animaux",
    "law.animals.cases.sell_animals.desc": "Explication approfondie : la vente d'animaux doit suivre des règles garantissant un prix clair...",

    "law.animals.cases.transport_animals.title": "Transport des animaux",
    "law.animals.cases.transport_animals.desc": "Explication approfondie : le transport du bétail doit respecter la sécurité et le bien-être animal...",

    "law.animals.cases.epidemics_reporting.title": "Maladies épidémiques et déclaration obligatoire",
    "law.animals.cases.epidemics_reporting.desc": "Explication approfondie : en cas de symptômes d'une maladie contagieuse dans le troupeau...",

    "law.animals.cases.mandatory_vaccines.title": "Vaccinations obligatoires",
    "law.animals.cases.mandatory_vaccines.desc": "Explication approfondie : les réglementations vétérinaires imposent des programmes de vaccination...",

    "law.animals.cases.milk_regulation.title": "Production de lait et réglementation de la vente",
    "law.animals.cases.milk_regulation.desc": "Explication approfondie : la production laitière est soumise à un contrôle sanitaire strict...",

    "law.animals.cases.eggs_marketing.title": "Production d'œufs et commercialisation",
    "law.animals.cases.eggs_marketing.desc": "Explication approfondie : la production d'œufs dépend des règles d'hygiène...",

    "law.animals.cases.slaughter_meat.title": "Abattage et réglementation des viandes",
    "law.animals.cases.slaughter_meat.desc": "Explication approfondie : l'abattage doit se faire dans des abattoirs agréés...",

    "law.animals.cases.beekeeping_honey.title": "Apiculture et production de miel",
    "law.animals.cases.beekeeping_honey.desc": "Explication approfondie : l'apiculture nécessite d'organiser l'activité et de respecter les règles...",

    "law.animals.cases.wool_shearing.title": "Production et tonte de la laine",
    "law.animals.cases.wool_shearing.desc": "Explication approfondie : la tonte doit préserver la sécurité de l'animal...",

    "law.animals.cases.feed_quality.title": "Fourrages et contrôle de la qualité",
    "law.animals.cases.feed_quality.desc": "Explication approfondie : acheter des aliments auprès de sources fiables protège la santé du troupeau...",

    "law.animals.cases.manure_environment.title": "Fumier et environnement",
    "law.animals.cases.manure_environment.desc": "Explication approfondie : la gestion des déjections animales doit respecter des normes environnementales...",

    "law.animals.cases.livestock_insurance.title": "Assurance du bétail",
    "law.animals.cases.livestock_insurance.desc": "Explication approfondie : l'éleveur peut souscrire une assurance contre les risques...",

    "law.animals.cases.breeding_loans.title": "Prêts pour financer l'élevage",
    "law.animals.cases.breeding_loans.desc": "Explication approfondie : financer un projet d'élevage nécessite souvent une étude de faisabilité...",

    "law.animals.cases.breeding_partnership.title": "Partenariat en élevage",
    "law.animals.cases.breeding_partnership.desc": "Explication approfondie : dans un projet commun d'élevage, les contributions doivent être clairement définies...",

    "law.animals.cases.farm_workers.title": "Main-d'œuvre dans les fermes d'élevage",
    "law.animals.cases.farm_workers.desc": "Explication approfondie : l'emploi des travailleurs en élevage est soumis au droit du travail...",

    "law.animals.cases.environment_protection.title": "Protection de l'environnement en élevage",
    "law.animals.cases.environment_protection.desc": "Explication approfondie : l'activité d'élevage peut impacter l'environnement via les odeurs et déchets...",

    "law.animals.cases.barn_safety.title": "Sécurité au travail dans les étables",
    "law.animals.cases.barn_safety.desc": "Explication approfondie : il faut fournir des équipements de protection aux travailleurs...",

    "law.animals.cases.breeders_disputes.title": "Litiges entre éleveurs",
    "law.animals.cases.breeders_disputes.desc": "Explication approfondie : les litiges peuvent être liés à une vente non claire, des dettes ou des partenariats...",

    # =========================
    # Market
    # =========================
    "market.title": "🌿 Marché agricole | Green Law",
    "market.current_section": "📌 Section actuelle : ",
    "market.section.plant": "🌱 Végétal",
    "market.section.animal": "🐄 Animal",

    "market.browse": "🔍 Parcourir les annonces",
    "market.add_new": "➕ Ajouter une nouvelle annonce",
    "market.edit": "✏️ Modifier une annonce (mes annonces uniquement)",
    "market.delete": "🗑️ Supprimer une annonce (mes annonces uniquement)",

    "market.featured_short": "⭐ Annonce mise en avant",
    "market.featured_badge": "🟨 Ceci est une annonce mise en avant (en doré)",
    "market.ad_id": "🔑 ID : ",
    "market.ad_id_inline": "ID : ",
    "market.price_label": "Prix : ",
    "market.phone_label": "Téléphone : ",
    "market.phone_mask": "0X XX XX XX XX",
    "market.placeholder_dash": "—",

    "market.empty": "📭 Aucune annonce pour le moment.",
    "market.choose_category_browse": "Choisissez le type d'annonces :",
    "market.count_ads": "📌 Nombre d'annonces : ",
    "market.none_in_category": "🟡 Aucune annonce dans cette catégorie pour le moment.",
    "market.press_enter_back": "Appuyez sur Entrée pour revenir...",

    "market.choose_category_add": "Choisissez le type d'annonce :",
    "market.ad_info_title": "🧾 Informations de l'annonce :",
    "market.field.first_name": "Prénom : ",
    "market.field.last_name": "Nom : ",
    "market.field.phone": "Numéro de téléphone : ",
    "market.field.address_optional": "Adresse (optionnel) : ",
    "market.field.wilaya": "Wilaya : ",
    "market.field.commune": "Commune : ",
    "market.field.title": "Titre de l'annonce : ",
    "market.field.price": "Prix : ",
    "market.field.qty": "Quantité ou poids : ",
    "market.field.desc": "Description libre : ",
    "market.field.featured_prompt": "⭐ Voulez-vous mettre l'annonce en avant ? (y/n) : ",
    "market.required_error": "❌ Vous devez saisir au moins le titre de l'annonce et la commune.",
    "market.published_success": "✅ Annonce publiée avec succès !",

    "market.my_ads_title": "📌 Mes annonces :",
    "market.no_my_ads": "📭 Vous n'avez aucune annonce dans cette section pour le moment.",
    "market.edit_intro": "✏️ Modification : laissez vide pour conserver la valeur.",
    "market.edit.title": "Titre actuel : ",
    "market.edit.price": "Prix actuel : ",
    "market.edit.qty": "Quantité/poids actuel : ",
    "market.edit.wilaya": "Wilaya actuelle : ",
    "market.edit.commune": "Commune actuelle : ",
    "market.edit.desc": "Description actuelle : ",
    "market.edit.featured": "⭐ Mise en avant ? tapez y ou n, ou laissez vide pour ne pas changer : ",
    "market.edit_success": "✅ Annonce modifiée avec succès !",

    "market.delete_confirm": "⚠️ Confirmez-vous la suppression de l'annonce suivante ? ",
    "market.delete_confirm_suffix": "(y/n) : ",
    "market.delete_cancelled": "✅ Suppression annulée.",
    "market.delete_success": "🗑️ Annonce supprimée avec succès !",

    "market.category.plant.rent_equip": "Location de matériel agricole",
    "market.category.plant.sell_products": "Vente de produits agricoles",
    "market.category.plant.inputs": "Intrants agricoles",
    "market.category.plant.lands_opportunities": "Terres et opportunités agricoles",
    "market.category.plant.plant_health": "Services de santé des plantes",
    "market.category.plant.factory_hotel_partnerships": "Partenariats usines et hôtels",

    "market.category.animal.rent_equipment": "Location de matériel d'élevage",
    "market.category.animal.livestock_market": "Marché du bétail et des animaux",
    "market.category.animal.animal_products": "Produits d'origine animale",
    "market.category.animal.facilities_warehouses": "Infrastructures d'élevage (entrepôts)",
    "market.category.animal.feed": "Aliments pour bétail",
    "market.category.animal.organic_fertilizer": "Engrais organique agricole",
    "market.category.animal.vet_services": "Services vétérinaires",
    "market.category.animal.factory_hotel_partnerships": "Partenariats usines et hôtels",

    # Seeds
    "market.seed.name_placeholder": "X",
    "market.seed.address_placeholder": "—",
    "market.seed.qty_placeholder": "—",

    "market.seed.plant.potato.title": "Vente en gros de pommes de terre de saison",
    "market.seed.plant.potato.price": "8 000–12 000 DZD / quintal (indicatif selon la saison)",
    "market.seed.plant.potato.qty": "2 tonnes",
    "market.seed.plant.potato.wilaya": "Aïn Defla",
    "market.seed.plant.potato.commune": "El Attaf",
    "market.seed.plant.potato.desc": "Pommes de terre de bonne qualité. Annonce de démonstration (supprimable plus tard).",

    "market.seed.plant.tractor.title": "Location de tracteur avec chauffeur (labour et irrigation)",
    "market.seed.plant.tractor.price": "À partir de 10 000 DZD / jour (selon le service)",
    "market.seed.plant.tractor.wilaya": "Sétif",
    "market.seed.plant.tractor.commune": "Sétif",
    "market.seed.plant.tractor.desc": "Disponible pour labour, nivellement et irrigation. Annonce de démonstration (supprimable plus tard).",

    "market.seed.plant.seedlings.title": "Vente de graines et plants (tomate, poivron, oignon)",
    "market.seed.plant.seedlings.price": "À partir de 300 DZD (selon le type)",
    "market.seed.plant.seedlings.qty": "Quantités variées",
    "market.seed.plant.seedlings.wilaya": "Blida",
    "market.seed.plant.seedlings.commune": "El Affroun",
    "market.seed.plant.seedlings.desc": "Fourniture selon demande. Annonce de démonstration (supprimable plus tard).",

    "market.seed.plant.contract.title": "Contrat de fourniture de légumes de saison (restaurant/hôtel)",
    "market.seed.plant.contract.price": "Selon accord (fourniture hebdomadaire)",
    "market.seed.plant.contract.qty": "De 1 à 3 tonnes par semaine",
    "market.seed.plant.contract.wilaya": "Alger",
    "market.seed.plant.contract.commune": "Bab Ezzouar",
    "market.seed.plant.contract.desc": "Fourniture régulière selon des critères de qualité. Annonce de démonstration (supprimable plus tard).",

    "market.seed.animal.ram.title": "Bélier local pour l'Aïd",
    "market.seed.animal.ram.price": "70 000 DZD (négociable)",
    "market.seed.animal.ram.qty": "Poids approx. 50 kg",
    "market.seed.animal.ram.wilaya": "Djelfa",
    "market.seed.animal.ram.commune": "Djelfa",
    "market.seed.animal.ram.desc": "Bélier local en bonne santé. Annonce de démonstration (supprimable plus tard).",

    "market.seed.animal.eggs.title": "Vente d'œufs fermiers (plateau de 30)",
    "market.seed.animal.eggs.price": "500 DZD / plateau (indicatif)",
    "market.seed.animal.eggs.qty": "10 plateaux",
    "market.seed.animal.eggs.wilaya": "Constantine",
    "market.seed.animal.eggs.commune": "Constantine",
    "market.seed.animal.eggs.desc": "Œufs frais quotidiens. Annonce de démonstration (supprimable plus tard).",

    "market.seed.animal.vet.title": "Vétérinaire itinérant (bétail et volailles)",
    "market.seed.animal.vet.price": "Visite à partir de 2 500 DZD",
    "market.seed.animal.vet.qty": "Couverture selon zone",
    "market.seed.animal.vet.wilaya": "Oran",
    "market.seed.animal.vet.commune": "Oran",
    "market.seed.animal.vet.desc": "Vaccination, traitement et suivi. Annonce de démonstration (supprimable plus tard).",

    "market.seed.animal.milk_contract.title": "Fourniture quotidienne de lait frais (contrat)",
    "market.seed.animal.milk_contract.price": "À partir de 75 DZD / litre (selon qualité/quantité)",
    "market.seed.animal.milk_contract.qty": "150 litres par jour",
    "market.seed.animal.milk_contract.wilaya": "Tiaret",
    "market.seed.animal.milk_contract.commune": "Tiaret",
    "market.seed.animal.milk_contract.desc": "Fourniture quotidienne selon des critères de qualité. Annonce de démonstration (supprimable plus tard).",

    # =========================
    # Farmer Passport
    # =========================
    "passport.menu_title": "🪪 Passeport de l'agriculteur",
    "passport.menu_myfiles": "Mes fichiers (Recherche 🔍 + Téléchargement)",
    "passport.menu_add": "Ajouter un nouveau fichier (Scan / Caméra / PDF)",
    "passport.menu_qr_gallery": "Galerie de QR codes (Recherche 🔍)",
    "passport.menu_open_qr": "Ouvrir un fichier via sélection (QR)",

    "passport.no_user": "❌ ID utilisateur introuvable.",
    "passport.empty": "📁 Le passeport de l'agriculteur est vide.",

    "passport.add_title": "➕ Ajouter un nouveau fichier",
    "passport.add_scan": "Ajouter via Scan (numérisation)",
    "passport.add_camera": "Ajouter via Caméra (photos)",
    "passport.add_pdf": "Ajouter un PDF existant",

    "passport.doc_title": "Titre du fichier : ",
    "passport.scan_path": "Chemin du fichier après scan (PDF/PNG/JPG) : ",
    "passport.camera_path": "Chemin de l'image (PNG/JPG) : ",
    "passport.pdf_path": "Chemin du PDF : ",

    "passport.default_scan_title": "Fichier scanné",
    "passport.default_camera_title": "Fichier image",
    "passport.default_pdf_title": "Fichier PDF",

    "passport.not_found": "❌ Fichier introuvable.",
    "passport.read_fail": "❌ Impossible de lire le fichier.",
    "passport.stored": "✅ Fichier enregistré dans le passeport de l'agriculteur.",

    "passport.myfiles_title": "📂 Mes fichiers",
    "passport.search_hint": "🔍 Saisissez une année (ex : 2022) ou laissez vide pour tout afficher :",
    "passport.search_none": "❌ Aucun fichier pour cette année.",
    "passport.list_title": "Liste des fichiers :",
    "passport.year": "Année",
    "passport.type": "Type",
    "passport.download": "Télécharger",
    "passport.press_enter": "Appuyez sur Entrée pour revenir...",

    "passport.qr_gallery_title": "🔳 Galerie de QR codes",
    "passport.qr_list_title": "Liste des codes :",
    "passport.qr_missing": "(QR indisponible)",
    "passport.qr_scan_note": "📱 Scannez le QR pour télécharger ou ouvrir le fichier",

    "passport.open_title": "📌 Ouvrir un fichier via QR (sélection)",
    "passport.open_path_only": "📄 Ce fichier n'est pas textuel. Ouvrez-le depuis le chemin suivant :",
    "passport.qr_rebuild_fail": "⚠️ Impossible de reconstruire le QR code pour ce fichier.",

    # =========================
    # Smart Maps
    # =========================
    "ui.menu.option_5": "Carte intelligente",

"smart_map.page_title": "Carte intelligente",
"smart_map.hero.title": "Carte intelligente",
"smart_map.hero.subtitle": "Explorez les cartes interactives du secteur agricole dans Green Law.",
"smart_map.section.current": "Section actuelle",
"smart_map.section.plant": "Section végétale",
"smart_map.section.animal": "Section animale",
"smart_map.stats.points": "Nombre de points",
"smart_map.cta.open": "Ouvrir la carte",
"smart_map.cta.pdf": "Télécharger le PDF",
"smart_map.empty": "Aucune carte disponible pour le moment.",
"smart_map.view.embed_title": "Aperçu interactif",
"smart_map.view.note": "Vous pouvez zoomer, dézoomer et déplacer la carte directement.",
"smart_map.card.water": "Explorer la répartition des eaux de puits par wilaya.",
"smart_map.card.agri": "Découvrir les principales zones agricoles en Algérie.",
"smart_map.card.wool": "Afficher les principales zones productrices de laine.",
"smart_map.card.honey": "Afficher les principales zones productrices de miel.",
"smart_map.card.milk": "Afficher les principales zones productrices de lait et dérivés.",
"smart_map.card.meat": "Afficher les principales zones productrices de viande.",
    "maps.menu.title": "🗺️ Carte intelligente",

    "maps.title.water": "💧 Carte de répartition des puits d'eau en Algérie",
    "maps.title.agri": "🌿 Carte des principales zones agricoles en Algérie",
    "maps.title.wool": "🧶 Carte des principales zones productrices de laine en Algérie",
    "maps.title.honey": "🍯 Carte des principales zones productrices de miel naturel en Algérie",
    "maps.title.milk": "🥛 Carte des principales zones productrices de lait et dérivés en Algérie",
    "maps.title.meat": "🥩 Carte des principales zones productrices de viande en Algérie",

    "maps.action.open": "Ouvrir la carte",
    "maps.action.pdf": "Télécharger le PDF",

    "maps.pdf.summary_title": "Résumé des points sur la carte :",
    "maps.pdf.no_points": "Aucun point pour le moment.",
    "maps.pdf.created": "✅ PDF créé avec succès : ",

    "maps.water.count": "✅ Nombre de points (puits) : ",
    "maps.warn.missing_prefix": "⚠️ Noms manquants dans WILAYA_CENTERS : ",

    "maps.legend.title": "🗝️ Légende",
    "maps.legend.default": "Données",
    "maps.legend.water": "💧 Puits d'eau",
    "maps.legend.agri": "🌿 Zones agricoles",
    "maps.legend.honey": "🍯 Miel",
    "maps.legend.wool": "🧶 Laine",
    "maps.legend.milk": "🥛 Lait",
    "maps.legend.meat": "🥩 Viande",

    "maps.desc.water": "💧 Puits d'eau",
    "maps.desc.meat": "🥩 Production de viande",
    "maps.desc.wool": "🧶 Production de laine",
    "maps.desc.honey": "🍯 Production de miel naturel",
    "maps.desc.milk": "🥛 Production de lait et dérivés"
}

# ---------------------------------
# Helpers
# ---------------------------------

def process_french(d: dict) -> dict:
    return d

def display_french(text: str) -> str:
    return text