# app.main.views

from flask import g, render_template, redirect, url_for
from . import main # Blueprint

#-------------------------------------------------------------------------------
@main.route('/')
def show_landing():
    return render_template('views/index.html')

