from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required
from ..models import SharepointServer

class RequestForm(Form):
    software_product = StringField('Software Product : ', validators=[Required()])
    requester = StringField('Requester : ', validators=[Required()])
    sharepoint_path = StringField('Sharepoint Path : ', validators=[Required()])
    sharepoint_server =  SelectField('Sharepoint Server : ', coerce=int )
    milestone_name = StringField('Milestone Name : ', validators=[Required()])
    test_cycle = StringField('Test Cycle : ', validators=[Required()])
    submit = SubmitField('Submit Onboard Request')

    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.sharepoint_server.choices = [(server.id, server.name)\
        for server in SharepointServer.query.order_by(SharepointServer.name).all()]
