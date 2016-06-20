from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required,Length, Email, Regexp
from ..models import SharepointServer,OnboardRequest,User
from wtforms import ValidationError

class RequestForm(Form):
    software_product = StringField('Software Product : ', validators=[Required(), Length(1, 64),])
    requester = StringField('Requester : ', validators=[Required(),Length(1, 64),Email()])
    sharepoint_path = StringField('Sharepoint Path : ', validators=[Required()])
    sharepoint_server =  SelectField('Sharepoint Server : ', coerce=int )
    milestone_name = StringField('Milestone Name : ', validators=[Required()])
    test_cycle = StringField('Test Cycle : ', validators=[Required()])
    submit = SubmitField('Submit Onboard Request')

    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.sharepoint_server.choices = [(server.id, server.name)\
        for server in SharepointServer.query.order_by(SharepointServer.name).all()]

    def validate_requester(self, field):
        if not User.query.filter_by(username=field.data).first():
            raise ValidationError('%s is not in Requester list,please contact with jiwu@qti.qualcomm.com.'%field.data)

    def validate_sharepoint_path(self,field):
        server_name = SharepointServer.query.get(self.sharepoint_server.data).name
        if OnboardRequest.query.filter_by(sharepoint_path=server_name+field.data).first():
            raise ValidationError('The SharePoint path is exist in database, Please View Onboard History')