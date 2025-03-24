class Project:
    """Model for portfolio projects"""
    
    @staticmethod
    def get_all_projects():
        """Return all projects (mock data for now)"""
        return [
            {
                'id': 1,
                'title': 'E-commerce Platform',
                'description': 'A full-stack e-commerce platform with user authentication, product catalog, and payment processing.',
                'technologies': ['Python', 'Flask', 'SQLAlchemy', 'JavaScript', 'React', 'PostgreSQL'],
                'image': 'project1.jpg',
                'github_url': 'https://github.com/username/ecommerce-platform',
                'live_url': 'https://ecommerce-platform.example.com',
                'featured': True
            },
            {
                'id': 2,
                'title': 'Data Visualization Dashboard',
                'description': 'Interactive dashboard for visualizing complex datasets with filtering and export capabilities.',
                'technologies': ['Python', 'Flask', 'D3.js', 'Pandas', 'SQLite'],
                'image': 'project2.jpg',
                'github_url': 'https://github.com/username/data-dashboard',
                'live_url': 'https://data-dashboard.example.com',
                'featured': True
            },
            {
                'id': 3,
                'title': 'Machine Learning API',
                'description': 'RESTful API for machine learning model predictions with authentication and rate limiting.',
                'technologies': ['Python', 'Flask', 'TensorFlow', 'Docker', 'Redis'],
                'image': 'project3.jpg',
                'github_url': 'https://github.com/username/ml-api',
                'live_url': 'https://ml-api.example.com',
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
        """Return all skills (mock data for now)"""
        return [
            {
                'category': 'Programming Languages',
                'items': [
                    {'name': 'Python', 'level': 90},
                    {'name': 'JavaScript', 'level': 85},
                    {'name': 'Java', 'level': 75},
                    {'name': 'C++', 'level': 70}
                ]
            },
            {
                'category': 'Web Development',
                'items': [
                    {'name': 'Flask', 'level': 90},
                    {'name': 'Django', 'level': 80},
                    {'name': 'React', 'level': 75},
                    {'name': 'HTML/CSS', 'level': 85}
                ]
            },
            {
                'category': 'Data Science',
                'items': [
                    {'name': 'Pandas', 'level': 85},
                    {'name': 'NumPy', 'level': 80},
                    {'name': 'TensorFlow', 'level': 75},
                    {'name': 'SQL', 'level': 85}
                ]
            }
        ]


class Education:
    """Model for education history"""
    
    @staticmethod
    def get_all_education():
        """Return education history (mock data for now)"""
        return [
            {
                'degree': 'Master of Science in Computer Science',
                'institution': 'University of Technology',
                'location': 'Paris, France',
                'period': '2020 - 2022',
                'description': 'Specialized in Artificial Intelligence and Data Science. Graduated with honors.'
            },
            {
                'degree': 'Bachelor of Science in Computer Science',
                'institution': 'National Institute of Technology',
                'location': 'Lyon, France',
                'period': '2017 - 2020',
                'description': 'Focused on software engineering and web development. Participated in multiple hackathons.'
            }
        ]


class Experience:
    """Model for work experience"""
    
    @staticmethod
    def get_all_experience():
        """Return work experience (mock data for now)"""
        return [
            {
                'title': 'Software Engineer Intern',
                'company': 'Tech Innovations Inc.',
                'location': 'Paris, France',
                'period': 'Jan 2022 - Jun 2022',
                'description': 'Developed and maintained web applications using Flask and React. Implemented CI/CD pipelines and improved application performance by 30%.'
            },
            {
                'title': 'Web Developer (Part-time)',
                'company': 'Digital Solutions Agency',
                'location': 'Remote',
                'period': 'Jun 2020 - Dec 2021',
                'description': 'Created responsive websites for clients using modern web technologies. Collaborated with design team to implement UI/UX improvements.'
            },
            {
                'title': 'Research Assistant',
                'company': 'University AI Lab',
                'location': 'Lyon, France',
                'period': 'Sep 2019 - May 2020',
                'description': 'Assisted in research projects focused on natural language processing. Implemented machine learning models and analyzed results.'
            }
        ]
