from flask import render_template, url_for, flash, redirect, request
from app import app
from app.models import Project, Skill, Education, Experience
from datetime import datetime

@app.route('/')
@app.route('/home')
def home():
    """Home page route"""
    projects = Project.get_featured_projects()
    skills = Skill.get_all_skills()
    return render_template('index.html', title='Home', projects=projects, skills=skills, now=datetime.now())

@app.route('/about')
def about():
    """About page route"""
    education = Education.get_all_education()
    experience = Experience.get_all_experience()
    return render_template('about.html', title='About', education=education, experience=experience, now=datetime.now())

@app.route('/projects')
def projects():
    """Projects page route"""
    projects = Project.get_all_projects()
    return render_template('projects.html', title='Projects', projects=projects, now=datetime.now())

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    """Project detail page route"""
    project = Project.get_project_by_id(project_id)
    if not project:
        flash('Project not found', 'danger')
        return redirect(url_for('projects'))
    return render_template('project_detail.html', title=project.title, project=project, projects=Project.get_all_projects(), now=datetime.now())

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page route"""
    if request.method == 'POST':
        # Here you would process the contact form
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # In a real app, you would send an email or save to database
        flash('Your message has been sent! I will get back to you soon.', 'success')
        return redirect(url_for('contact'))
        
    return render_template('contact.html', title='Contact', now=datetime.now())
