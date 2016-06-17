from flask import render_template, session, redirect, url_for, current_app,flash
from .. import db
from ..models import User
from ..email import send_email
from . import main
from .forms import RequestForm


@main.route('/spider', methods=['GET', 'POST'])
def index():
    form = RequestForm()

    if form.is_submitted():
        if not form.validate():
             if form.errors:
                err_msg = ' , '.join(form.errors.keys())
                flash(err_msg.replace('_',' ').title()+' are required')
                return render_template('index.html',form=form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.requester.data).first()
        if user is None:
            user = User(username=form.requester.data)
            db.session.add(user)
            flash("New requester %s added successfully"%user.username)
            #session['known'] = False
            #if current_app.config['FLASKY_ADMIN']:
            #    send_email(current_app.config['FLASKY_ADMIN'], 'New User',
            #               'mail/new_user', user=user)
        else:
            flash("Requester have been stored!")
        #    session['known'] = True
        #session['name'] = form.requester.data
        return redirect(url_for('.index'))
    return render_template('index.html',form=form)
