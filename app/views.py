from flask import render_template, request, abort, redirect, url_for, flash
from flask.ext.login import login_user, logout_user, login_required

from . import app, db, lm
from app.forms import ProjectForm
from .models import User, Project


@lm.user_loader
def user_loader(user_id):
    user = User.query.filter_by(id=user_id)
    if user.count() == 1:
        return user.one()
    return None


@app.before_first_request
def init_request():
    db.create_all()


@app.route('/projects', methods=['GET', 'POST'])
@login_required
def projects():
    template_name = 'projects.html'
    form = ProjectForm()

    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required.')
            return render_template(template_name, form=form)
        else:
            p = Project(
                name=form.name.data,
                awis_access_id=form.awis_access_id.data,
                awis_secret_access_key=form.awis_secret_access_key.data,
                intercom_app_id=form.intercom_app_id.data,
                intercom_app_api_key=form.intercom_app_api_key.data
            )
            db.session.add(p)
            db.session.commit()
            return redirect(url_for('projects'))

    elif request.method == 'GET':
        return render_template(template_name, form=form, projects=Project.query.all())


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        username = request.form['txtUsername']
        password = request.form['txtPassword']

        user = User.query.filter_by(username=username)
        if user.count() == 0:
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()

            flash('You have registered the username {0}. Please login'.format(username))
            return redirect(url_for('login'))
        else:
            flash('The username {0} is already in use.  Please try a new username.'.format(username))
            return redirect(url_for('register'))
    else:
        abort(405)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', next=request.args.get('next'))
    elif request.method == 'POST':
        username = request.form['txtUsername']
        password = request.form['txtPassword']

        user = User.query.filter_by(username=username).filter_by(password=password)
        if user.count() == 1:
            login_user(user.one())
            flash('Welcome back {0}'.format(username))
            try:
                next = request.form['next']
                return redirect(next)
            except Exception as e:  # fixme too broad exception
                return redirect(url_for('index'))
        else:
            flash('Invalid login')
            return redirect(url_for('login'))
    else:
        return abort(405)


@app.route('/')
def index():
    return render_template('index.html')
