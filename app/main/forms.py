from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required


class RequestForm(Form):
    software_product = StringField('Software Product:', validators=[Required()])
    requester = StringField('Requester: ', validators=[Required()])
    sharepoint_path = StringField('Sharepoint Path', validators=[Required()])
    sharepoint_server =  StringField('Sharepoint Server', validators=[Required()])
    milestone_name = StringField('Milestone Name', validators=[Required()])
    test_cycle = StringField('Test Cycle', validators=[Required()])
    submit = SubmitField('Submit Onboard Request')

