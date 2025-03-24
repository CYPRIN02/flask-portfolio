class Project:
    """Model for portfolio projects"""
    
    @staticmethod
    def get_all_projects():
        """Return all projects (based on CV)"""
        return [
            {
                'id': 1,
                'title': 'Web Scraping & Product Classification',
                'description': 'Application web for scraping and predicting product classification using machine learning techniques. Developed during my apprenticeship at ESGI.',
                'technologies': ['Python', 'Flask', 'BigQuery', 'Machine Learning', 'Web Scraping'],
                'image': 'project1.jpg',
                'github_url': 'https://github.com/CYPRIN02/web-scraping-classification',
                'live_url': None,
                'featured': True
            },
            {
                'id': 2,
                'title': 'Spam Detection Web Application',
                'description': 'Web application that uses machine learning algorithms to detect spam messages. Built with Python and Flask, with a user-friendly interface for real-time spam detection.',
                'technologies': ['Python', 'Flask', 'Machine Learning', 'NLP', 'HTML/CSS'],
                'image': 'project2.jpg',
                'github_url': 'https://github.com/CYPRIN02/spam-detection',
                'live_url': None,
                'featured': True
            },
            {
                'id': 3,
                'title': 'Emotion Detection in Video',
                'description': 'Application that analyzes video content to detect and classify emotions in real-time. Uses computer vision and deep learning techniques to identify facial expressions.',
                'technologies': ['Python', 'Flask', 'Computer Vision', 'Deep Learning', 'OpenCV'],
                'image': 'project3.jpg',
                'github_url': 'https://github.com/CYPRIN02/emotion-detection',
                'live_url': None,
                'featured': True
            },
            {
                'id': 4,
                'title': 'Sudoku Game',
                'description': 'Interactive Sudoku game developed with Python and Pygame. Features include puzzle generation, difficulty levels, and a solving algorithm.',
                'technologies': ['Python', 'Pygame'],
                'image': 'project4.jpg',
                'github_url': 'https://github.com/uvsq-versailles/sudoku-game',
                'live_url': None,
                'featured': False
            },
            {
                'id': 5,
                'title': 'Flight Reservation Website',
                'description': 'Web application for booking flights, developed as a university project. Includes user authentication, flight search, and booking management.',
                'technologies': ['HTML', 'CSS', 'JavaScript', 'PHP', 'MySQL'],
                'image': 'project5.jpg',
                'github_url': 'https://github.com/uvsq-versailles/flight-reservation',
                'live_url': None,
                'featured': False
            },
            {
                'id': 6,
                'title': 'Chess Game in Java',
                'description': 'Chess game implementation with Java, featuring a graphical user interface, move validation, and basic AI opponent.',
                'technologies': ['Java', 'Swing'],
                'image': 'project6.jpg',
                'github_url': 'https://github.com/uvsq-versailles/chess-game',
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
                    {'name': 'Python', 'level': 90},
                    {'name': 'C#', 'level': 85},
                    {'name': 'HTML/CSS/JavaScript', 'level': 80},
                    {'name': 'SQL', 'level': 85}
                ]
            },
            {
                'category': 'Technologies & Tools',
                'items': [
                    {'name': 'Flask', 'level': 85},
                    {'name': '.NET', 'level': 80},
                    {'name': 'Git (GitHub/BitBucket/GitLab)', 'level': 85},
                    {'name': 'Microsoft Office 365', 'level': 90}
                ]
            },
            {
                'category': 'Cloud & Databases',
                'items': [
                    {'name': 'GCP', 'level': 75},
                    {'name': 'Azure', 'level': 75},
                    {'name': 'AWS', 'level': 70},
                    {'name': 'Heroku', 'level': 80},
                    {'name': 'SQL Server', 'level': 85},
                    {'name': 'MySQL', 'level': 85},
                    {'name': 'BigQuery', 'level': 80}
                ]
            },
            {
                'category': 'AI & Data Science',
                'items': [
                    {'name': 'Machine Learning', 'level': 85},
                    {'name': 'LangChain', 'level': 75},
                    {'name': 'Data Analysis', 'level': 80}
                ]
            },
            {
                'category': 'Soft Skills',
                'items': [
                    {'name': 'Agile Methodology', 'level': 85},
                    {'name': 'Teamwork', 'level': 90},
                    {'name': 'Adaptability', 'level': 85},
                    {'name': 'Self-Learning', 'level': 90}
                ]
            },
            {
                'category': 'Languages',
                'items': [
                    {'name': 'French', 'level': 95},
                    {'name': 'English', 'level': 75},
                    {'name': 'Malagasy', 'level': 100}
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
