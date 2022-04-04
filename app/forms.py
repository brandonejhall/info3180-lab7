from flask_wtf import FlaskForm
from wtforms import StringField,FileField, SubmitField
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    description = StringField('Description', widget=TextArea())
    image = FileField('Property Image', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField('Add Property')