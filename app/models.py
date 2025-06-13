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
            'description': "Application web pour le scraping et la prédiction de classification de produits à l'aide de techniques de machine learning. Développée durant mon apprentissage à l'ESGI.",
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
            'description': "Application web utilisant des algorithmes de machine learning pour détecter les messages indésirables (spam). Réalisée avec Python et Flask, avec une interface conviviale pour la détection en temps réel.",
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
            'description': "Application qui analyse le contenu vidéo pour détecter et classifier les émotions en temps réel. Utilise la vision par ordinateur et le deep learning pour identifier les expressions faciales.",
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
                Cours synthétique sur LangChain basé sur les dernières recherches (2022-2023).
                Intègre des ressources pédagogiques de deeplearning.ai et la documentation officielle.
                Contenu clé :
                - Architecture modulaire de LangChain
                - Gestion des prompts et mémoires contextuelles
                - Cas pratiques avec LLMs (GPT-3.5, Llama 2)
                - Bonnes pratiques de sécurité et déploiement
            ''',
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
            'title': 'Site de Réservation de Vols',
            'description': "Application web pour réserver des vols, développée comme projet universitaire. Inclut l'authentification utilisateur, la recherche de vols et la gestion des réservations.",
            'image_url': 'https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/page_bdd_L3.jpg',
            'technologies': ['HTML', 'CSS', 'JavaScript', 'PHP', 'MySQL'],
            'image': 'page_bdd_L3.jpg',
            'github_url': 'https://github.com/uvsq-versailles/flight-reservation',
            'live_url': None,
            'featured': False
            },
            {
            'id': 6,
            'title': 'Jeu d’Échecs',
            'description': "Implémentation d'un jeu d'échecs en Java, avec interface graphique, validation des coups et adversaire IA basique.",
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
                    {'name': 'Csharp', 'level': 85, 'frameworks': ['.NET Core', 'ASP.NET', 'Entity Framework']},
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
                    {'name': 'Data Analysis', 'level': 80, 'frameworks': ['Pandas', 'NumPy', 'Matplotlib']}
                ]
            },
            {
                'category': 'Compétences interpersonnelles',
                'items': [
                    {'name': 'Agile Methodology', 'level': 85, 'frameworks': []},
                    {'name': 'Teamwork', 'level': 90, 'frameworks': []},
                    {'name': 'Adaptability', 'level': 85, 'frameworks': []},
                    {'name': 'Self-Learning', 'level': 90, 'frameworks': []}
                ]
            },
            {
                'category': 'Langues',
                'items': [
                    {'name': 'French', 'level': 95, 'frameworks': []},
                    {'name': 'English', 'level': 75, 'frameworks': []},
                    {'name': 'Malagasy', 'level': 100, 'frameworks': []}
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
            'description': 'Spécialisation en intelligence artificielle et technologies Big Data. En alternance chez BPCE Solutions Informatiques en tant qu\'analyste développeur .Net.'
            },
            {
            'degree': 'Master 1 DataScale Computing',
            'institution': 'Université de Versailles',
            'location': 'Versailles, France',
            'period': 'Sept 2021 - Juil 2022',
            'description': 'Centrée sur le traitement et le calcul de données à grande échelle.'
            },
            {
            'degree': 'Licence Sciences et Technologies - Informatique',
            'institution': 'Université de Versailles',
            'location': 'Versailles, France',
            'period': 'Sept 2018 - Juil 2021',
            'description': 'Formation complète en informatique avec un accent sur la programmation et le développement logiciel.'
            },
            {
            'degree': 'Première année en Informatique',
            'institution': "Université d'Artois",
            'location': 'Lens, France',
            'period': 'Sept 2017 - Juin 2018',
            'description': "Études fondamentales en informatique avant le transfert à l'Université de Versailles."
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
            'description': "Conception et développement d'un site web personnel pour présenter mes réalisations et compétences en tant qu'Analyste Développeur. Ce projet a inclus la création du site, la gestion du flux d'informations entre le site et la base de données, la maintenance et le déploiement."
            },
            {
            'title': 'Développeur .NET (Apprentissage)',
            'company': 'BPCE Solutions Informatiques',
            'location': 'France',
            'period': 'Oct 2022 - Sept 2024',
            'description': "Maintenance d'applications web existantes via le développement et les tests. Exécution de requêtes sur bases de données. Analyse des applications back-end et front-end pour proposer des solutions adaptées aux besoins. Déploiement d'applications web incluant configuration, tests de validation, intégration et pipelines de déploiement. Rédaction de documentation technique."
            },
            {
            'title': 'Développeur Web Apps IA & Big Data (Apprentissage)',
            'company': 'ESGI',
            'location': 'Paris, France',
            'period': 'Sept 2022 - Déc 2024',
            'description': "Développement d'une application web de scraping et de prédiction de classification de produits avec Python, Flask et BigQuery. Création d'une application web de détection de spam avec Python et Flask. Implémentation de la détection d'émotions dans la vidéo avec Python et Flask. Utilisation de cas d'usage LangChain et de divers services cloud (GCP/Azure/AWS/Heroku)."
            },
            {
            'title': 'Développeur',
            'company': 'UVSQ & Université d\'Artois',
            'location': 'Versailles & Lens, France',
            'period': 'Sept 2017 - Juil 2021',
            'description': "Participation à divers projets académiques : jeu de Sudoku avec Python et Pygame, Puissance 4 avec Python et Tkinter, site de réservation de vols, jeu d'échecs en Java, bataille navale en C, manipulation d'arbres binaires avec C++ et QT Creator, simulation de carburant d'avion avec C++ et QT Creator, diagramme de décision binaire en Java, et système de conversation chatbot."
            },
            {
            'title': 'Equipier Qualifié',
            'company': "McDonald's",
            'location': 'France',
            'period': 'Juin 2018 - Oct 2022',
            'description': "Travail en tant qu'équipier qualifié tout en poursuivant mes études."
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
        New Contact Form Submission:
        ----------------------------
        Name: {message['name']}
        Email: {message['email']}
        Date: {message['timestamp']}
        Subject: {message['subject']}
        
        Message:
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
                title="Five Foot Esgi",
                description="2nd place tournoi Ecole Paris",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/coup-tournoi.jpg",
                media_type="image",
                tags=["Loisir", "Award"],
                date=datetime.datetime(2024, 3, 20)
            ),
            GalleryItem(
                title="workspace bpce",
                description="my prefer place on openspace.",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/workspace.jpg",
                media_type="image",
                tags=["Work", "Media"],
                date=datetime.datetime(2023, 10, 15)
            ),
            # Add more...
            GalleryItem(
                title="elevator bpce",
                description="je prends au moins une photo quand je suis seul.",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/bpce-levator.jpg",
                media_type="image",
                tags=["Work"],
                date=datetime.datetime(2024, 10, 10)
            ),
            GalleryItem(
                title="mcdo-chill",
                description="Temps de pause au macdo.",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/mcdo.jpg",
                media_type="image",
                tags=["Work"],
                date=datetime.datetime(2022, 6, 14)
            ),
            
            GalleryItem(
                title="Présentation profil",
                description="Présentation de mon profil professionnel",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/presentation-profil.mp4",
                media_type="video",
                tags=["Interview", "Media"],
                date=datetime.datetime(2025, 4, 30)
            ),
            GalleryItem(
                title="Cadeau dédicacé",
                description="Après dernier repas avec collègue de travail",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/dedicace-ping.jpg",
                media_type="image",
                tags=["Award"],
                date=datetime.datetime(2024, 9, 5)
            ),
            GalleryItem(
                title="Diplôme au Grand Rex",
                description="Photo prise lors de la cérémonie de remise des diplômes au Grand Rex",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/diploma-1.jpg",
                media_type="image",
                tags=["Award"],
                date=datetime.datetime(2025, 5, 24)
            ),
            GalleryItem(
                title="Diplôme",
                description="Mon diplôme de Master en Intelligence Artificielle et Big Data",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/diploma.jpg",
                media_type="image",
                tags=["Award"],
                date=datetime.datetime(2025, 5, 24)
            ),
            GalleryItem(
                title="Diplôme Tour Eiffel",
                description="Photo prise devant la Tour Eiffel avec mon diplôme",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/diploma-tour-eifel.jpg",
                media_type="image",
                tags=["Award"],
                date=datetime.datetime(2025, 5, 24)
            ),
            GalleryItem(
                title="Gala remise de diplôme",
                description="photo prise lors du gala de remise de diplôme",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/gala.jpg",
                media_type="image",
                tags=["Award"],
                date=datetime.datetime(2025, 5, 24)
            ),
            GalleryItem(
                title="Lycée Sainte Jeanne d'Arc",
                description="Lycée que j'ai étudié à Majunga, Madagascar",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/sja.jpg",
                media_type="image",
                tags=["Ecole"],
                date=datetime.datetime(2025, 5, 7)
            ),
            GalleryItem(
                title="Université d'Antananarivo",
                description="Université que j'ai étudié à Antananarivo, Madagascar",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/univ-ankatso.jpg",
                media_type="image",
                tags=["Ecole"],
                date=datetime.datetime(2017, 4, 10)
            ),
            GalleryItem(
                title="Fin Première année en licence à Lens",
                description="Photo devant l'université d'Artois Lens",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/fin-annee-lens.jpg",
                media_type="image",
                tags=["Ecole", "Award"],
                date=datetime.datetime(2018, 6, 2)
            ),
            GalleryItem(
                title="Foot Dumotel Cachan",
                description="Rien m'empêche de jouer au foot",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/foot-neige.jpg",
                media_type="image",
                tags=["Media"],
                date=datetime.datetime(2021, 11, 20)
            ),
            GalleryItem(
                title="Fêter la validation de diplôme Master",
                description="Jour +1 de la validation de diplôme Master ",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/jour-validation-diplo.jpg",
                media_type="image",
                tags=["AI", "Award"],
                date=datetime.datetime(2024, 12, 3)
            ),
            GalleryItem(
                title="Bpce Paris 13",
                description="Lieu de Travail",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/lieu-travail.jpg",
                media_type="image",
                tags=["Work"],
                date=datetime.datetime(2024, 5, 7)
            ),
            GalleryItem(
                title="Cadeau",
                description="Cadeau donné par mes collègues de travail",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/cadeau-ping.jpg",
                media_type="image",
                tags=["Work", "Award"],
                date=datetime.datetime(2024, 9, 5)
            ),
            GalleryItem(
                title="Ski loisir",
                description="Aquaboulevard balade",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/ski-water.mp4",
                media_type="video",
                tags=["Loisir", "Media"],
                date=datetime.datetime(2024, 8, 11)
            ),
            GalleryItem(
                title="Vacances à Majunga",
                description="Vacances à Majunga, Madagascar",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/vacance1.jpg",
                media_type="image",
                tags=["Holiday", "Media"],
                date=datetime.datetime(2025, 5, 10)
            ),
            GalleryItem(
                title="Couché de soleil Maroala",
                description="Vacances à Majunga, Madagascar",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/vacance2.jpg",
                media_type="image",
                tags=["Holiday", "Media"],
                date=datetime.datetime(2025, 5, 10)
            ),
            GalleryItem(
                title="Hôtel Antsahavaky Chez Narindra",
                description="Vacances à Majunga, Madagascar",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/vacance3.jpg",
                media_type="image",
                tags=["Holiday", "Media"],
                date=datetime.datetime(2025, 5, 10)
            ),
            GalleryItem(
                title="Ravinala Antsanitia",
                description="Vacances à Majunga, Madagascar",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/vacance4.jpg",
                media_type="image",
                tags=["Holiday", "Media"],
                date=datetime.datetime(2025, 5, 10)
            ),
            GalleryItem(
                title="Plage Antsanitia",
                description="Vacances à Majunga, Madagascar",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/vacance5.jpg",
                media_type="image",
                tags=["Holiday", "Media"],
                date=datetime.datetime(2025, 5, 10)
            ),
            GalleryItem(
                title="Maki au lac Sacré",
                description="Vacances à Majunga, Madagascar",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/vacance6.jpg",
                media_type="image",
                tags=["Holiday", "Media"],
                date=datetime.datetime(2025, 5, 10)
            ),
            GalleryItem(
                title="Ampefy lac",
                description="Vacances à Majunga, Madagascar",
                media_url="https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/vacance7.jpg",
                media_type="image",
                tags=["Holiday", "Media"],
                date=datetime.datetime(2025, 5, 10)
            ),
            
        ]
