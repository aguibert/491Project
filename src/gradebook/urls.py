from flask import render_template
import views


def setup_urls(app):
    """URLs for the gradebook functions"""

<<<<<<< HEAD
    app.add_url_rule('/gradebook', view_func=views.gradebookScreenView.as_view('Gradebook'))
    app.add_url_rule('/gradebook/courseGrades/<courseID>', view_func=views.courseGradeView.as_view('author_grades'))
