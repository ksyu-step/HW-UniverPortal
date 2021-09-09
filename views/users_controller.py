from flask import render_template
from config import app


class UsersController(object):

    @staticmethod
    @app.route('/users/login')
    def login():
        return render_template('users/login.html')
