from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required


class RequestForm(Form):
    software_product = StringField('Software Product: Such as "MSM8976LA.1.0"', validators=[Required()])
    requester = StringField('Requester: Like "lxin@qti.qualcomm.com"', validators=[Required()])
    sharepoint_path = StringField('Sharepoint Path', validators=[Required()])
    submit = SubmitField('Submit Onboard Request')

