from flask_app import app
from flask import render_template, redirect, request, session, flash, url_for
from flask_app.models import user, friendship 
from flask_app.controllers import friendships



@app.route('/')
def index():
    return redirect('/friendships')


@app.route('/friendships')
def home():
    return render_template('index.html',  users = user.User.get_all_users(), friendships = friendship.Friendship.display_friendships())


@app.route('/create_user', methods=['POST'])
def create():
    user.User.create_user(request.form)
    return redirect('/friendships')