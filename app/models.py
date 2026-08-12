import datetime
# from app.utils.storage import get_supabase_public_url

class Project:
    """Model for portfolio projects"""

    # def __init__(self, title, image_filename, image_url ):
    #     self.title = title
    #     self.image_filename = image_filename
    #     self.image_url = get_supabase_public_url(image_filename) 
    
    @staticmethod
    def get_all_projects():
        """Return all projects (based on CV)"""
        return [
            {
            'id': 1,
            'title': 'Web Scraping & Classification de Produits',
            'description': "Application web de scraping et de prédiction de classification de produits, développée dans le cadre de mon apprentissage à l'ESGI.",
            'details': "Le projet combine collecte de données, préparation des informations et exploitation de modèles de Machine Learning pour aider à classifier des produits de manière plus fiable. Il met en pratique Python, Flask et BigQuery autour d'un cas orienté data.",
            'features': [
                "Collecte de données produit à partir de sources web",
                "Préparation et structuration des informations récupérées",
                "Prédiction de classification avec des approches de Machine Learning",
                "Interface web Flask pour consulter et exploiter les résultats",
                "Utilisation de BigQuery pour manipuler les données"
            ],
            'challenges': [
                "Gérer des données hétérogènes issues du scraping et les rendre exploitables.",
                "Construire un flux cohérent entre collecte, traitement, prédiction et affichage.",
                "Rendre les résultats compréhensibles pour un utilisateur non technique."
            ],
            'type': 'Application web data',
            'duration': 'Projet ESGI',
            'role': 'Développeur Web Apps IA & Big Data',
            'image_url': 'https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/page_sublimpick.jpg',
            'technologies': ['Python', 'Flask', 'BigQuery', 'Machine Learning', 'Web Scraping', 'GCP'],
            'image': 'page_sublimpick.jpg',
            'github_url': 'https://github.com/CYPRIN02/projet_annuel_5IABD_sublimpick',
            'live_url': None,
            'featured': True
            },
            {
            'id': 2,
            'title': 'Application Web de Détection de Spam',
            'description': "Application web permettant d'analyser un message et d'identifier s'il s'agit d'un spam à l'aide d'approches de Machine Learning.",
            'details': "Ce projet met l'accent sur le traitement de texte, la préparation des données et l'intégration d'un modèle de classification dans une interface Flask simple à utiliser.",
            'features': [
                "Saisie d'un message depuis une interface web",
                "Analyse du contenu textuel avec un modèle de classification",
                "Retour clair sur le résultat de détection",
                "Interface légère développée avec Flask",
                "Mise en pratique de notions de NLP"
            ],
            'challenges': [
                "Préparer les textes pour obtenir des données utilisables par le modèle.",
                "Intégrer la prédiction dans un parcours web simple et compréhensible.",
                "Limiter les ambiguïtés dans l'affichage du résultat pour l'utilisateur."
            ],
            'type': 'Application web IA',
            'duration': 'Projet ESGI',
            'role': 'Développeur Python/Flask',
            'image_url': 'https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/page_spam_detection.jpg',
            'technologies': ['Python', 'Flask', 'Machine Learning', 'NLP', 'HTML/CSS'],
            'image': 'page_spam_detection.jpg',
            'github_url': 'https://github.com/CYPRIN02/projet_annuel_5IABD/tree/master',
            'live_url': None,
            'featured': True
            },
            {
            'id': 3,
            'title': 'Détection d’Émotions dans la Vidéo',
            'description': "Application d'analyse vidéo visant à détecter et classifier des émotions à partir d'expressions faciales.",
            'details': "Le projet explore la vision par ordinateur et le Deep Learning pour traiter des flux vidéo, repérer des visages et restituer une information lisible côté interface.",
            'features': [
                "Analyse de contenu vidéo",
                "Détection d'expressions faciales",
                "Classification des émotions détectées",
                "Restitution visuelle des résultats",
                "Utilisation d'outils de Computer Vision"
            ],
            'challenges': [
                "Traiter des données vidéo avec des contraintes de performance.",
                "Présenter des résultats de détection de manière claire.",
                "Articuler la logique IA avec une interface exploitable."
            ],
            'type': 'Application web IA',
            'duration': 'Projet ESGI',
            'role': 'Développeur Python/Flask',
            'image_url': 'https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/page_accueille_analyse_video_pa4.jpg',
            'technologies': ['Python', 'Flask', 'Computer Vision', 'Deep Learning', 'OpenCV'],
            'image': 'page_accueille_analyse_video_pa4.jpg',
            'github_url': 'https://github.com/CYPRIN02/projet_annuel4iabd',
            'live_url': None,
            'featured': True
            },
            {
            'id': 4,
            'title': 'Find Your Course - Formation LangChain',
            'description': '''
                Support de formation synthétique sur LangChain, construit à partir de ressources pédagogiques reconnues et de la documentation officielle.
            ''',
            'details': "Ce projet organise des notions clés autour de LangChain: architecture modulaire, prompts, mémoires contextuelles, cas d'usage avec des LLMs et bonnes pratiques de sécurité et de déploiement.",
            'features': [
                "Présentation structurée des concepts LangChain",
                "Synthèse de ressources pédagogiques",
                "Exemples de cas d'usage avec des LLMs",
                "Points d'attention sur les prompts et la mémoire contextuelle",
                "Ouverture vers les bonnes pratiques de déploiement"
            ],
            'challenges': [
                "Rendre un sujet technique accessible sans perdre la précision.",
                "Organiser des ressources variées dans un parcours cohérent.",
                "Mettre en avant les usages concrets plutôt qu'une simple liste de concepts."
            ],
            'type': 'Support de formation',
            'duration': 'Projet personnel',
            'role': 'Concepteur de contenu technique',
            'image_url': 'https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/langchain-course.jpg',
            'technologies': [
                'Python',
                'LangChain',
                'LLMs',
                'NLP',
                'DeepLearning.ai',
                'Jupyter Notebook'
            ],
            'image': 'langchain-course.jpg',
            'github_url': 'https://github.com/CYPRIN02/langchain-masterclass',
            'live_url': None,
            'featured': True,
            'learning_resources': [
                {
                'name': 'Cours Fondamentaux LangChain',
                'url': 'https://learn.deeplearning.ai/courses/langchain',
                'author': 'Harrison Chase (Créateur de LangChain)'
                },
                {
                'name': 'Documentation Officielle',
                'url': 'https://python.langchain.com/'
                }
            ]
            },
            {
            'id': 5,
            'title': 'Stock Manager',
            'description': "Back-office de gestion de stock permettant de piloter les produits, les quantités disponibles et les mouvements d'entrée et de sortie.",
            'details': "Stock Manager est une application back-office dédiée au suivi opérationnel d'un stock. Elle centralise la consultation des articles, la mise à jour des produits, le suivi des quantités et la visualisation des informations utiles au pilotage. Le projet met en avant une architecture ASP.NET Core MVC, une interface Angular et une logique métier structurée autour de la fiabilité des données.",
            'features': [
                "Tableau de bord de suivi du stock",
                "Consultation et recherche dans la liste des produits",
                "Suivi des quantités disponibles et des niveaux de stock",
                "Gestion des mouvements d'entrée et de sortie",
                "Ajout, modification et suppression d'articles",
                "Interface back-office pensée pour une utilisation simple au quotidien"
            ],
            'challenges': [
                "Conserver des données cohérentes après chaque mouvement de stock.",
                "Rendre les actions principales accessibles rapidement dans l'interface.",
                "Structurer la logique métier pour faciliter la maintenance et les évolutions.",
                "Articuler proprement l'interface Angular avec le back-end ASP.NET Core MVC."
            ],
            'image_url': 'https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/ihm-stockmanager.jpg',
            'technologies': ['C#', 'ASP.NET Core MVC', 'Angular', 'SQL Server', 'Gestion de stock'],
            'image': 'ihm-stockmanager.jpg',
            'github_url': 'https://github.com/CYPRIN02/stock-manager-aspnet-core-mvc/tree/angular-stock-manager',
            'live_url': 'https://stockmanager.amadago-it.com/',
            'featured': True,
            'type': 'Back-office de gestion',
            'duration': 'Projet applicatif',
            'role': 'Développeur full-stack'
            },
            {
            'id': 6,
            'title': 'Site de Réservation de Vols',
            'description': "Application web universitaire dédiée à la recherche de vols, à la réservation et à la gestion des informations associées.",
            'details': "Ce projet académique met en pratique la conception d'un parcours de réservation, la gestion d'utilisateurs et la manipulation de données côté application web.",
            'features': [
                "Recherche de vols",
                "Gestion des réservations",
                "Parcours utilisateur autour d'une réservation",
                "Manipulation de données relationnelles",
                "Interface web pour consulter les informations utiles"
            ],
            'challenges': [
                "Organiser les données de réservation de manière cohérente.",
                "Construire un parcours web compréhensible pour l'utilisateur.",
                "Relier les pages, les actions et les données sans casser la logique métier."
            ],
            'type': 'Application web',
            'duration': 'Projet universitaire',
            'role': 'Développeur',
            'image_url': 'https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/page_bdd_L3.jpg',
            'technologies': ['HTML', 'CSS', 'JavaScript', 'PHP', 'MySQL'],
            'image': 'page_bdd_L3.jpg',
            'github_url': 'https://github.com/uvsq-versailles/flight-reservation',
            'live_url': None,
            'featured': False
            },
            {
            'id': 7,
            'title': 'Jeu d’Échecs',
            'description': "Implémentation d'un jeu d'échecs avec interface graphique, règles de déplacement et logique de jeu.",
            'details': "Ce projet universitaire a permis de travailler la modélisation d'un jeu, la validation des règles, l'organisation du code et la création d'une interface utilisable.",
            'features': [
                "Affichage d'un plateau de jeu",
                "Gestion des pièces et des déplacements",
                "Validation des coups selon les règles principales",
                "Interface graphique pour jouer une partie",
                "Structuration du code autour de la logique du jeu"
            ],
            'challenges': [
                "Modéliser correctement les règles et les interactions entre les pièces.",
                "Maintenir un état de jeu cohérent après chaque coup.",
                "Rendre l'interface claire tout en respectant la logique du plateau."
            ],
            'type': 'Jeu',
            'duration': 'Projet universitaire',
            'role': 'Développeur',
            'image_url': 'https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/page_chess.jpg',
            'technologies': ['Python', 'Pygame'],
            'image': 'page_chess.jpg',
            'github_url': 'https://github.com/CYPRIN02/echec/tree/master',
            'live_url': None,
            'featured': False
            }
        ]
    
    @staticmethod
    def get_featured_projects():
        """Return only featured projects"""
        return [p for p in Project.get_all_projects() if p.get('featured', False)]
    
    @staticmethod
    def get_project_by_id(project_id):
        """Return a specific project by ID"""
        projects = Project.get_all_projects()
        for project in projects:
            if project['id'] == project_id:
                return project
        return None


class Skill:
    """Model for skills"""
    
    @staticmethod
    def get_all_skills():
        """Return all skills (based on CV)"""
        return [
            {
                'category': 'Langages de programmation',
                'items': [
                    {'name': 'Python', 'level': 90, 'frameworks': ['Flask', 'Django', 'FastAPI']},
                    {'name': 'C#', 'level': 85, 'frameworks': ['.NET Core', 'ASP.NET', 'Entity Framework']},
                    {'name': 'HTML/CSS/JavaScript', 'level': 80, 'frameworks': ['React', 'Vue.js', 'Bootstrap']},
                    {'name': 'SQL', 'level': 85, 'frameworks': ['SQL Server', 'MySQL', 'PostgreSQL']}
                ]
            },
            {
                'category': 'Technologies & Outils',
                'items': [
                    {'name': 'Flask', 'level': 85, 'frameworks': ['Jinja2', 'Werkzeug']},
                    {'name': '.NET', 'level': 80, 'frameworks': ['WPF', 'WinForms']},
                    {'name': 'Git (GitHub/BitBucket/GitLab)', 'level': 85, 'frameworks': []},
                    {'name': 'Microsoft Office 365', 'level': 90, 'frameworks': []}
                ]
            },
            {
                'category': 'Cloud & Bases de données',
                'items': [
                    {'name': 'GCP', 'level': 75, 'frameworks': ['Compute Engine', 'Cloud Functions']},
                    {'name': 'Azure', 'level': 75, 'frameworks': ['Azure Functions', 'Azure SQL']},
                    {'name': 'AWS', 'level': 70, 'frameworks': ['Lambda', 'EC2']},
                    {'name': 'Heroku', 'level': 80, 'frameworks': []},
                    {'name': 'SQL Server', 'level': 85, 'frameworks': []},
                    {'name': 'MySQL', 'level': 85, 'frameworks': []},
                    {'name': 'BigQuery', 'level': 80, 'frameworks': []}
                ]
            },
            {
                'category': 'Intelligence Artificielle & Big Data',
                'items': [
                    {'name': 'Machine Learning', 'level': 85, 'frameworks': ['Scikit-learn', 'TensorFlow', 'PyTorch']},
                    {'name': 'LangChain', 'level': 75, 'frameworks': []},
                    {'name': 'Analyse de données', 'level': 80, 'frameworks': ['Pandas', 'NumPy', 'Matplotlib']}
                ]
            },
            {
                'category': 'Compétences interpersonnelles',
                'items': [
                    {'name': 'Méthodologie Agile', 'level': 85, 'frameworks': []},
                    {'name': 'Travail en équipe', 'level': 90, 'frameworks': []},
                    {'name': 'Adaptabilité', 'level': 85, 'frameworks': []},
                    {'name': 'Apprentissage autonome', 'level': 90, 'frameworks': []}
                ]
            },
            {
                'category': 'Langues',
                'items': [
                    {'name': 'Français', 'level': 95, 'frameworks': []},
                    {'name': 'Anglais', 'level': 75, 'frameworks': []},
                    {'name': 'Malgache', 'level': 100, 'frameworks': []}
                ]
            }
        ]

class Education:
    """Model for education history"""
    
    @staticmethod
    def get_all_education():
        """Return education history (based on CV)"""
        return [
            {
            'degree': 'Master Intelligence Artificielle et Big Data',
            'institution': 'ESGI',
            'location': 'Paris, France',
            'period': 'Sept 2022 - Déc 2024',
            'description': "Spécialisation en intelligence artificielle et Big Data, avec une expérience en alternance chez BPCE Solutions Informatiques en développement .NET, analyse de données et intégration de solutions IA."
            },
            {
            'degree': 'Master 1 DataScale Computing',
            'institution': 'Université de Versailles',
            'location': 'Versailles, France',
            'period': 'Sept 2021 - Juil 2022',
            'description': "Formation orientée traitement, calcul et exploitation de données à grande échelle."
            },
            {
            'degree': 'Licence Sciences et Technologies - Informatique',
            'institution': 'Université de Versailles',
            'location': 'Versailles, France',
            'period': 'Sept 2018 - Juil 2021',
            'description': "Formation généraliste en informatique, avec un accent sur la programmation, les bases de données et le développement logiciel."
            },
            {
            'degree': 'Première année en Informatique',
            'institution': "Université d'Artois",
            'location': 'Lens, France',
            'period': 'Sept 2017 - Juin 2018',
            'description': "Première année d'informatique consacrée aux bases de la programmation et aux fondamentaux du développement."
            }
        ]


class Experience:
    """Model for work experience"""
    
    @staticmethod
    def get_all_experience():
        """Return work experience (based on CV)"""
        return [
            {
            'title': 'Création Portfolio Personnel (Projet Freelance)',
            'company': 'Projet Personnel',
            'location': 'En ligne',
            'period': 'Fév 2025 - Juin 2025',
            'description': "Conception, développement, maintenance et déploiement de mon site portfolio afin de présenter mon parcours, mes projets et mes compétences. Le projet inclut la gestion des contenus, le formulaire de contact et l'intégration de médias hébergés."
            },
            {
            'title': 'Développeur .NET (Apprentissage)',
            'company': 'BPCE Solutions Informatiques',
            'location': 'France',
            'period': 'Oct 2022 - Sept 2024',
            'description': "Maintenance d'applications web existantes, développement et tests, exécution de requêtes SQL, analyse du back-end et du front-end pour proposer des solutions adaptées, participation au déploiement d'applications web et rédaction de documentation technique."
            },
            {
            'title': 'Développeur Web Apps IA & Big Data (Apprentissage)',
            'company': 'ESGI',
            'location': 'Paris, France',
            'period': 'Sept 2022 - Déc 2024',
            'description': "Développement de projets web orientés IA et data: scraping et classification de produits avec Python, Flask et BigQuery, détection de spam, analyse d'émotions dans la vidéo, cas d'usage LangChain et découverte de services cloud comme GCP, Azure, AWS et Heroku."
            },
            {
            'title': 'Développeur',
            'company': 'UVSQ & Université d\'Artois',
            'location': 'Versailles & Lens, France',
            'period': 'Sept 2017 - Juil 2021',
            'description': "Réalisation de plusieurs projets académiques: Sudoku avec Python et Pygame, Puissance 4 avec Python et Tkinter, site de réservation de vols, jeu d'échecs en Java, bataille navale en C, arbres binaires avec C++ et QT Creator, simulation de carburant d'avion, diagramme de décision binaire en Java et chatbot."
            },
            {
            'title': 'Equipier Qualifié',
            'company': "McDonald's",
            'location': 'France',
            'period': 'Juin 2018 - Oct 2022',
            'description': "Expérience professionnelle menée en parallèle des études, avec un fort apprentissage du travail en équipe, de l'adaptabilité et de la rigueur au quotidien."
            }
        ]


class Message:
    """Model for contact form messages"""
    
    @staticmethod
    def create(name, email, subject, content):
        """Create a new message record"""
        return {
            'name': name,
            'email': email,
            'subject': subject,
            'content': content,
            'timestamp': datetime.datetime.now().isoformat(),
            'read': False
        }
    
    @staticmethod
    def format_for_email(message):
        """Format message for email notification"""
        return f"""
        Nouveau message depuis le portfolio :
        ----------------------------
        Nom : {message['name']}
        E-mail : {message['email']}
        Date : {message['timestamp']}
        Objet : {message['subject']}
        
        Message :
        {message['content']}
        ----------------------------
        """
    
class GalleryItem:
    def __init__(self, title, description, media_url, media_type='image', tags=None, date=None):
        self.title = title
        self.description = description
        self.media_url = media_url
        self.media_type = media_type  # 'image' ou 'video'
        self.tags = tags or []
        self.date = date or datetime.now()

    @staticmethod
    def get_all_items():
        return [
            GalleryItem(
                title="Five Foot ESGI",
                description="Deuxième place lors d'un tournoi inter-écoles à Paris.",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/coup-tournoi.jpg",
                media_type="image",
                tags=["Loisir", "Réussite"],
                date=datetime.datetime(2024, 3, 20)
            ),
            GalleryItem(
                title="Espace de travail BPCE",
                description="Un espace de travail que j'appréciais particulièrement en open space.",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/workspace.jpg",
                media_type="image",
                tags=["Travail", "Média"],
                date=datetime.datetime(2023, 10, 15)
            ),
            # Moments supplémentaires.
            GalleryItem(
                title="Ascenseur BPCE",
                description="Un souvenir capturé sur le lieu de travail.",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/bpce-levator.jpg",
                media_type="image",
                tags=["Travail"],
                date=datetime.datetime(2024, 10, 10)
            ),
            GalleryItem(
                title="Pause chez McDonald's",
                description="Un moment de pause pendant mon expérience professionnelle chez McDonald's.",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/mcdo.jpg",
                media_type="image",
                tags=["Travail"],
                date=datetime.datetime(2022, 6, 14)
            ),
            
            GalleryItem(
                title="Présentation profil",
                description="Présentation de mon profil professionnel",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/presentation-profil.mp4",
                media_type="video",
                tags=["Interview", "Média"],
                date=datetime.datetime(2025, 4, 30)
            ),
            GalleryItem(
                title="Cadeau dédicacé",
                description="Souvenir offert après un dernier repas avec des collègues de travail.",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/dedicace-ping.jpg",
                media_type="image",
                tags=["Réussite"],
                date=datetime.datetime(2024, 9, 5)
            ),
            GalleryItem(
                title="Diplôme au Grand Rex",
                description="Photo prise lors de la cérémonie de remise des diplômes au Grand Rex",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/diploma-1.jpg",
                media_type="image",
                tags=["Réussite"],
                date=datetime.datetime(2025, 5, 24)
            ),
            GalleryItem(
                title="Diplôme",
                description="Mon diplôme de Master en Intelligence Artificielle et Big Data",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/diploma.jpg",
                media_type="image",
                tags=["Réussite"],
                date=datetime.datetime(2025, 5, 24)
            ),
            GalleryItem(
                title="Diplôme Tour Eiffel",
                description="Photo prise devant la Tour Eiffel avec mon diplôme",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/diploma-tour-eifel.jpg",
                media_type="image",
                tags=["Réussite"],
                date=datetime.datetime(2025, 5, 24)
            ),
            GalleryItem(
                title="Gala de remise de diplôme",
                description="Photo prise lors du gala de remise de diplôme.",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/gala.jpg",
                media_type="image",
                tags=["Réussite"],
                date=datetime.datetime(2025, 5, 24)
            ),
            GalleryItem(
                title="Lycée Sainte Jeanne d'Arc",
                description="Lycée où j'ai étudié à Majunga, Madagascar.",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/sja.jpg",
                media_type="image",
                tags=["École"],
                date=datetime.datetime(2025, 5, 7)
            ),
            GalleryItem(
                title="Université d'Antananarivo",
                description="Université où j'ai étudié à Antananarivo, Madagascar.",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/univ-ankatso.jpg",
                media_type="image",
                tags=["École"],
                date=datetime.datetime(2017, 4, 10)
            ),
            GalleryItem(
                title="Fin de première année de licence à Lens",
                description="Photo devant l'Université d'Artois à Lens.",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/fin-annee-lens.jpg",
                media_type="image",
                tags=["École", "Réussite"],
                date=datetime.datetime(2018, 6, 2)
            ),
            GalleryItem(
                title="Foot Dumotel Cachan",
                description="Un moment de loisir autour du football.",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/foot-neige.jpg",
                media_type="image",
                tags=["Média"],
                date=datetime.datetime(2021, 11, 20)
            ),
            GalleryItem(
                title="Validation du Master",
                description="Souvenir pris le lendemain de la validation du diplôme de Master.",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/jour-validation-diplo.jpg",
                media_type="image",
                tags=["IA", "Réussite"],
                date=datetime.datetime(2024, 12, 3)
            ),
            GalleryItem(
                title="BPCE Paris 13",
                description="Lieu de travail pendant mon alternance.",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/lieu-travail.jpg",
                media_type="image",
                tags=["Travail"],
                date=datetime.datetime(2024, 5, 7)
            ),
            GalleryItem(
                title="Cadeau",
                description="Cadeau offert par mes collègues de travail.",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/cadeau-ping.jpg",
                media_type="image",
                tags=["Travail", "Réussite"],
                date=datetime.datetime(2024, 9, 5)
            ),
            GalleryItem(
                title="Ski loisir",
                description="Moment de loisir à l'Aquaboulevard.",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/ski-water.mp4",
                media_type="video",
                tags=["Loisir", "Média"],
                date=datetime.datetime(2024, 8, 11)
            ),
            GalleryItem(
                title="Vacances à Majunga",
                description="Vacances à Majunga, Madagascar.",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/vacance1.jpg",
                media_type="image",
                tags=["Vacances", "Média"],
                date=datetime.datetime(2025, 5, 10)
            ),
            GalleryItem(
                title="Coucher de soleil à Maroala",
                description="Vacances à Majunga, Madagascar.",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/vacance2.jpg",
                media_type="image",
                tags=["Vacances", "Média"],
                date=datetime.datetime(2025, 5, 10)
            ),
            GalleryItem(
                title="Hôtel Antsahavaky Chez Narindra",
                description="Vacances à Majunga, Madagascar.",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/vacance3.jpg",
                media_type="image",
                tags=["Vacances", "Média"],
                date=datetime.datetime(2025, 5, 10)
            ),
            GalleryItem(
                title="Ravinala Antsanitia",
                description="Vacances à Majunga, Madagascar.",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/vacance4.jpg",
                media_type="image",
                tags=["Vacances", "Média"],
                date=datetime.datetime(2025, 5, 10)
            ),
            GalleryItem(
                title="Plage Antsanitia",
                description="Vacances à Majunga, Madagascar.",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/vacance5.jpg",
                media_type="image",
                tags=["Vacances", "Média"],
                date=datetime.datetime(2025, 5, 10)
            ),
            GalleryItem(
                title="Maki au lac Sacré",
                description="Vacances à Majunga, Madagascar.",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/vacance6.jpg",
                media_type="image",
                tags=["Vacances", "Média"],
                date=datetime.datetime(2025, 5, 10)
            ),
            GalleryItem(
                title="Ampefy lac",
                description="Vacances à Majunga, Madagascar.",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/vacance7.jpg",
                media_type="image",
                tags=["Vacances", "Média"],
                date=datetime.datetime(2025, 5, 10)
            ),
            
        ]
