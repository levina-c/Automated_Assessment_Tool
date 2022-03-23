from flask import render_template, flash, redirect, session, url_for, request, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from blog import app
# from blog.forms import LoginForm, RegistrationForm, CommentForm, SortPosts
# from blog.models import User, Post, Comment, Reviews
from sqlalchemy import desc, asc

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')
