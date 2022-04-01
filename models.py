from . import db


class New_project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100))
    project_description = db.Column(db.String(500))
    project_tool = db.Column(db.String(100))
    project_sentence = db.Column(db.String(500))