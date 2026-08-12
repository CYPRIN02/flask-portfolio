from collections import defaultdict, deque
from datetime import datetime, timedelta
from email.utils import parseaddr
from flask import render_template, flash, redirect, url_for, request, current_app
from app.models import Project, Skill, Education, Experience, GalleryItem
from app.airtable_utils  import submit_to_airtable
from app.notifications import send_contact_notification

from app.utils.storage import get_supabase_public_url

_contact_attempts = defaultdict(deque)
CONTACT_LIMIT = 5
CONTACT_WINDOW = timedelta(minutes=10)


def _is_contact_rate_limited(ip_address):
    now = datetime.utcnow()
    attempts = _contact_attempts[ip_address]

    while attempts and now - attempts[0] > CONTACT_WINDOW:
        attempts.popleft()

    if len(attempts) >= CONTACT_LIMIT:
        return True

    attempts.append(now)
    return False


def _is_valid_email(email):
    parsed_name, parsed_email = parseaddr(email or "")
    return bool(parsed_email and "@" in parsed_email and "." in parsed_email.rsplit("@", 1)[-1])


def init_routes(app):
    """Initialise toutes les routes de l'application"""

    @app.route('/')
    @app.route('/home')
    def home():
        """Route de la page d'accueil"""
        projects = Project.get_featured_projects()
        skills = Skill.get_all_skills()

        # Ajout les liens publics d'image Supabase
        for project in projects:
            if project.get("image"):
                project["image_url"] = get_supabase_public_url(f"uploads/{project['image']}")

        return render_template('index.html', 
                             title='Accueil', 
                             projects=projects, 
                             skills=skills, 
                             now=datetime.now())

    @app.route('/about')
    def about():
        """Route de la page À propos"""
        education = Education.get_all_education()
        experience = Experience.get_all_experience()
        return render_template('about.html',
                            title='À propos',
                            education=education,
                            experience=experience,
                            now=datetime.now())

    @app.route('/projects')
    def projects():
        """Route de la liste des projets"""
        projects = Project.get_all_projects()
        return render_template('projects.html',
                            title='Projets',
                            projects=projects,
                            now=datetime.now())

    @app.route('/project/<int:project_id>')
    def project_detail(project_id):
        """Route de détail d'un projet"""
        project = Project.get_project_by_id(project_id)
        if not project:
            flash('Projet introuvable.', 'danger')
            return redirect(url_for('projects'))
        return render_template('project_detail.html',
                            title=project['title'],
                            project=project,
                            projects=Project.get_all_projects(),
                            now=datetime.now())

    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        """Route de la page de contact"""
        if request.method == 'POST':
            try:
                if request.form.get('website'):
                    current_app.logger.info("Honeypot contact submission blocked")
                    flash('Votre message a bien été envoyé. Je vous répondrai dès que possible.', 'success')
                    return redirect(url_for('contact'))

                ip_address = request.headers.get('X-Forwarded-For', request.remote_addr or 'unknown').split(',')[0].strip()
                if _is_contact_rate_limited(ip_address):
                    flash('Trop de messages ont été envoyés depuis cette adresse. Merci de réessayer un peu plus tard.', 'warning')
                    return redirect(url_for('contact'))

                form_data = {
                    'name': (request.form.get('name') or '').strip(),
                    'email': (request.form.get('email') or '').strip(),
                    'subject': (request.form.get('subject') or '').strip(),
                    'message': (request.form.get('message') or '').strip()
                }

                if not all(form_data.values()):
                    flash('Merci de remplir tous les champs obligatoires.', 'danger')
                    return redirect(url_for('contact'))

                if not _is_valid_email(form_data['email']):
                    flash('Merci de saisir une adresse e-mail valide.', 'danger')
                    return redirect(url_for('contact'))

                if len(form_data['name']) > 120 or len(form_data['email']) > 254 or len(form_data['subject']) > 180 or len(form_data['message']) > 3000:
                    flash('Votre message est trop long. Merci de le raccourcir avant de réessayer.', 'danger')
                    return redirect(url_for('contact'))
                
                airtable_success = submit_to_airtable(**form_data)
                email_success = send_contact_notification(form_data)
                
                if airtable_success:
                    flash('Votre message a bien été envoyé. Je vous répondrai dès que possible.', 'success')
                    if not email_success:
                        current_app.logger.warning("Message saved but notification email failed")
                else:
                    flash("Une erreur est survenue pendant l'envoi du message. Merci de réessayer plus tard.", 'danger')
                
                return redirect(url_for('contact'))
            
            except Exception as e:
                current_app.logger.error(f"Contact form error: {str(e)}")
                flash("Une erreur technique est survenue. Merci de réessayer plus tard.", 'danger')
                return render_template('contact.html',
                                    title='Contact',
                                    form_data=request.form, now=datetime.now())
        
        return render_template('contact.html', 
                            title='Contact', 
                            now=datetime.now())



    @app.route('/gallery')
    def gallery():
        items = GalleryItem.get_all_items()
        return render_template('gallery.html', title="Galerie", items=items, now=datetime.now())
