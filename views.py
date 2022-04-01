from flask import Blueprint, render_template, request, redirect, url_for
from .models import New_project
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("About.html")

@views.route('/projects')
def project_page():
    project = New_project.query.all()
    
    return render_template('projects.html', projects=project)


@views.route('/add_project', methods=['POST', 'GET'])
def add_project():
    if request.method == 'POST':
        project_name = request.form.get('name')
        project_description = request.form.get('description')
        project_tool = request.form.get('tool')
        project_sentence = request.form.get('sentence')
        N_project = New_project(project_name=project_name, project_description=project_description, project_tool=project_tool, project_sentence=project_sentence)
        db.session.add(N_project)
        db.session.commit()
        return redirect(url_for('views.project_page'))

    return render_template('add_project.html')