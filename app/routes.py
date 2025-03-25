from flask import render_template, flash, redirect, url_for, request, current_app
from flask_mail import Message
from datetime import datetime
from app.models import Project, Skill, Education, Experience
from app.utils import submit_to_airtable
from app.notifications import send_contact_notification

# Initialisation de Flask-Limiter (décommenter si nécessaire)
# from flask_limiter import Limiter
# from flask_limiter.util import get_remote_address
# limiter = Limiter(key_func=get_remote_address)

def init_routes(app):
    """Initialise toutes les routes de l'application"""
    
    # Décommenter pour activer le rate limiting
    # limiter.init_app(app)

    @app.route('/')
    @app.route('/home')
    def home():
        """Route de la page d'accueil"""
        projects = Project.get_featured_projects()
        skills = Skill.get_all_skills()
        return render_template('index.html', 
                             title='Home', 
                             projects=projects, 
                             skills=skills, 
                             now=datetime.now())

    @app.route('/about')
    def about():
        """Route de la page À propos"""
        education = Education.get_all_education()
        experience = Experience.get_all_experience()
        return render_template('about.html',
                            title='About',
                            education=education,
                            experience=experience,
                            now=datetime.now())

    @app.route('/projects')
    def projects():
        """Route de la liste des projets"""
        projects = Project.get_all_projects()
        return render_template('projects.html',
                            title='Projects',
                            projects=projects,
                            now=datetime.now())

    @app.route('/project/<int:project_id>')
    def project_detail(project_id):
        """Route de détail d'un projet"""
        project = Project.get_project_by_id(project_id)
        if not project:
            flash('Project not found', 'danger')
            return redirect(url_for('projects'))
        return render_template('project_detail.html',
                            title=project['title'],
                            project=project,
                            projects=Project.get_all_projects(),
                            now=datetime.now())

    @app.route('/contact', methods=['GET', 'POST'])
    # @limiter.limit("5 per minute")  # Décommenter pour activer le rate limiting
    def contact():
        """Route de la page de contact"""
        if request.method == 'POST':
            try:
                form_data = {
                    'name': request.form.get('name'),
                    'email': request.form.get('email'),
                    'subject': request.form.get('subject'),
                    'message': request.form.get('message')
                }

                if not all(form_data.values()):
                    flash('Please fill all required fields', 'danger')
                    return redirect(url_for('contact'))
                
                airtable_success = submit_to_airtable(**form_data)
                email_success = send_contact_notification(form_data)
                
                if airtable_success:
                    flash('Your message has been sent! I will get back to you soon.', 'success')
                    if not email_success:
                        current_app.logger.warning("Message saved but notification email failed")
                else:
                    flash('There was an error sending your message. Please try again later.', 'danger')
                
                return redirect(url_for('contact'))
            
            except Exception as e:
                current_app.logger.error(f"Contact form error: {str(e)}")
                flash('A system error occurred. Please try again later.', 'danger')
                return render_template('contact.html',
                                    title='Contact',
                                    form_data=request.form, now=datetime.now())
        
        return render_template('contact.html', 
                            title='Contact', 
                            now=datetime.now())

    @app.route('/test-mail')
    def test_mail():
        print("SMTP Configuration:")
        print(f"Server: {current_app.config['MAIL_SERVER']}")
        print(f"Port: {current_app.config['MAIL_PORT']}")
        print(f"Username: {current_app.config['MAIL_USERNAME']}")
        
        msg = Message('Test Email',
                    sender=current_app.config['MAIL_DEFAULT_SENDER'],
                    recipients=['madaets0@gmail.com'])
        msg.body = 'This is a test email from Flask!'
        
        try:
            current_app.extensions['mail'].send(msg)
            return 'Email sent successfully!'
        except Exception as e:
            current_app.logger.error(f"Email error: {str(e)}")
            return f'Failed to send email: {str(e)}', 500