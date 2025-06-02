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
                'title': 'Web Scraping & Product Classification',
                'description': 'Application web for scraping and predicting product classification using machine learning techniques. Developed during my apprenticeship at ESGI.',
                'image_url': 'https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/page_sublimpick.jpg',
                'technologies': ['Python', 'Flask', 'BigQuery', 'Machine Learning', 'Web Scraping', 'GCP'],
                'image': 'page_sublimpick.jpg',
                'github_url': 'https://github.com/CYPRIN02/projet_annuel_5IABD_sublimpick',
                'live_url': None,
                'featured': True
            },
            {
                'id': 2,
                'title': 'Spam Detection Web Application',
                'description': 'Web application that uses machine learning algorithms to detect spam messages. Built with Python and Flask, with a user-friendly interface for real-time spam detection.',
                'image_url': 'https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/page_spam_detection.jpg',
                'technologies': ['Python', 'Flask', 'Machine Learning', 'NLP', 'HTML/CSS'],
                'image': 'page_spam_detection.jpg',
                'github_url': 'https://github.com/CYPRIN02/projet_annuel_5IABD/tree/master',
                'live_url': None,
                'featured': True
            },
            {
                'id': 3,
                'title': 'Emotion Detection in Video',
                'description': 'Application that analyzes video content to detect and classify emotions in real-time. Uses computer vision and deep learning techniques to identify facial expressions.',
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
                        'name': 'LangChain Fundamentals Course',
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
                'title': 'Flight Reservation Website',
                'description': 'Web application for booking flights, developed as a university project. Includes user authentication, flight search, and booking management.',
                'image_url': 'https://gauxrigjmrovzsqygmqx.supabase.co/storage/v1/object/public/portfolio-media/uploads/page_bdd_L3.jpg',
                'technologies': ['HTML', 'CSS', 'JavaScript', 'PHP', 'MySQL'],
                'image': 'page_bdd_L3.jpg',
                'github_url': 'https://github.com/uvsq-versailles/flight-reservation',
                'live_url': None,
                'featured': False
            },
            {
                'id': 6,
                'title': 'Chess Game',
                'description': 'Chess game implementation with Java, featuring a graphical user interface, move validation, and basic AI opponent.',
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
                'category': 'Programming Languages',
                'items': [
                    {'name': 'Python', 'level': 90, 'frameworks': ['Flask', 'Django', 'FastAPI']},
                    {'name': 'Csharp', 'level': 85, 'frameworks': ['.NET Core', 'ASP.NET', 'Entity Framework']},
                    {'name': 'HTML/CSS/JavaScript', 'level': 80, 'frameworks': ['React', 'Vue.js', 'Bootstrap']},
                    {'name': 'SQL', 'level': 85, 'frameworks': ['SQL Server', 'MySQL', 'PostgreSQL']}
                ]
            },
            {
                'category': 'Technologies & Tools',
                'items': [
                    {'name': 'Flask', 'level': 85, 'frameworks': ['Jinja2', 'Werkzeug']},
                    {'name': '.NET', 'level': 80, 'frameworks': ['WPF', 'WinForms']},
                    {'name': 'Git (GitHub/BitBucket/GitLab)', 'level': 85, 'frameworks': []},
                    {'name': 'Microsoft Office 365', 'level': 90, 'frameworks': []}
                ]
            },
            {
                'category': 'Cloud & Databases',
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
                'category': 'AI & Data Science',
                'items': [
                    {'name': 'Machine Learning', 'level': 85, 'frameworks': ['Scikit-learn', 'TensorFlow', 'PyTorch']},
                    {'name': 'LangChain', 'level': 75, 'frameworks': []},
                    {'name': 'Data Analysis', 'level': 80, 'frameworks': ['Pandas', 'NumPy', 'Matplotlib']}
                ]
            },
            {
                'category': 'Soft Skills',
                'items': [
                    {'name': 'Agile Methodology', 'level': 85, 'frameworks': []},
                    {'name': 'Teamwork', 'level': 90, 'frameworks': []},
                    {'name': 'Adaptability', 'level': 85, 'frameworks': []},
                    {'name': 'Self-Learning', 'level': 90, 'frameworks': []}
                ]
            },
            {
                'category': 'Languages',
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
                'degree': 'Master in Artificial Intelligence and Big Data',
                'institution': 'ESGI',
                'location': 'Paris, France',
                'period': 'Sept 2022 - Dec 2024',
                'description': 'Specialized in AI and Big Data technologies. Completed program through apprenticeship at BPCE Solutions Informatiques.'
            },
            {
                'degree': 'Master 1 in DataScale Computing',
                'institution': 'Université de Versailles',
                'location': 'Versailles, France',
                'period': 'Sept 2021 - Jul 2022',
                'description': 'Focused on large-scale data processing and computing technologies.'
            },
            {
                'degree': 'Bachelor in Computer Science',
                'institution': 'Université de Versailles',
                'location': 'Versailles, France',
                'period': 'Sept 2018 - Jul 2021',
                'description': 'Comprehensive computer science education with focus on programming and software development.'
            },
            {
                'degree': 'First Year Computer Science',
                'institution': 'Université d\'Artois',
                'location': 'Lens, France',
                'period': 'Sept 2017 - Jun 2018',
                'description': 'Foundational studies in computer science before transferring to Université de Versailles.'
            }
        ]


class Experience:
    """Model for work experience"""
    
    @staticmethod
    def get_all_experience():
        """Return work experience (based on CV)"""
        return [
            {
                'title': 'Développeur .NET (Apprenticeship)',
                'company': 'BPCE Solutions Informatiques',
                'location': 'France',
                'period': 'Oct 2022 - Sept 2024',
                'description': 'Maintained existing web applications through development and testing. Executed database queries. Analyzed back-end and front-end applications to propose solutions tailored to requirements. Deployed web applications including configuration, validation testing, integration, and deployment pipelines. Created technical documentation.'
            },
            {
                'title': 'Développeur Web Apps IA & Big Data (Apprenticeship)',
                'company': 'ESGI',
                'location': 'Paris, France',
                'period': 'Sept 2022 - Dec 2024',
                'description': 'Developed web application for scraping and product classification prediction using Python, Flask, and BigQuery. Created spam detection web application with Python and Flask. Implemented emotion detection in video using Python and Flask. Utilized LangChain use cases and various cloud services (GCP/Azure/AWS/Heroku).'
            },
            {
                'title': 'Développeur',
                'company': 'UVSQ & Université d\'Artois',
                'location': 'Versailles & Lens, France',
                'period': 'Sept 2017 - Jul 2021',
                'description': 'Worked on various academic projects including: Sudoku game with Python and Pygame, Connect Four with Python and Tkinter, Flight reservation website, Chess game in Java, Naval battle in C, Binary tree manipulation with C++ and QT Creator, Aircraft fuel simulation with C++ and QT Creator, Binary decision diagram in Java, and Chatbot conversation system.'
            },
            {
                'title': 'Equipier Qualifié',
                'company': 'McDonald\'s',
                'location': 'France',
                'period': 'Jun 2018 - Oct 2022',
                'description': 'Worked as a qualified team member while pursuing education.'
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
