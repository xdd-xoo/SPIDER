from flask import render_template, session, redirect, url_for, current_app,flash
from .. import db
from ..models import User,OnboardRequest,SharepointServer
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
            flash("The requseter is not in requester list, please contact administrator.")
            form = RequestForm()
            return  render_template('index.html',form = form)       
            #user = User(username=form.requester.data)
            #db.session.add(user)
            #flash("New requester %s added successfully"%user.username)
            #session['known'] = False
            #if current_app.config['FLASKY_ADMIN']:
            #    send_email(current_app.config['FLASKY_ADMIN'], 'New User',
            #               'mail/new_user', user=user)
        else:
            onboarding_request = OnboardRequest(software_product = form.software_product.data,\
                                requester = form.requester.data,\
                                sharepoint_server_id = form.sharepoint_server.data,\
                                sharepoint_path = form.sharepoint_path.data,\
                                milestone_name = form.milestone_name.data,\
                                test_cycle = form.test_cycle.data,\
                            active =1 )
            db.session.add(onboarding_request)
            flash("Your request added in background servivce, 10 mins later you can check it on Splunk.Click View Onboard History button to disable or active you request.")
            if onboarding_request.requester:
                #mail template not support ForeignKey
                server = SharepointServer.query.get(form.sharepoint_server.data).name
                send_email(onboarding_request.requester, 'New Onboarding Request',
                           'mail/new_request', onboarding_request=onboarding_request,server=server)        
        #    session['known'] = True
        #session['name'] = form.requester.data
            return redirect(url_for('.index'))
    return render_template('index.html',form=form)

@main.route('/history', methods=['GET', 'POST'])
def history():
    all_request = OnboardRequest.query.all()
    return render_template('history.html',all_request = all_request)

@main.route('/enable/<int:id>')
def enable(id):
    request_obj = OnboardRequest.query.get_or_404(id)
    print request_obj
    request_obj.active = 1
    db.session.add(request_obj)
    all_request = OnboardRequest.query.all()
    return redirect(url_for('.history'))

@main.route('/disable/<int:id>')
def disable(id):
    request_obj = OnboardRequest.query.get_or_404(id)
    request_obj.active = 0
    db.session.add(request_obj)
    all_request = OnboardRequest.query.all()
    return redirect(url_for('.history'))
