from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateTimeField, SubmitField
from wtforms.fields.datetime import DateField
from wtforms.validators import DataRequired, Length, Optional


class ToDoForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)],
                       render_kw={"class": "form-control border-primary"})
    description = TextAreaField('Description', validators=[Optional(), Length(max=500)],
                                render_kw={"class": "form-control border-primary"})
    due_date = DateTimeField('Due Date', format='%Y-%m-%dT%H:%M', validators=[Optional()],
                             render_kw={"class": "form-control border-primary", "type": "datetime-local"})
    priority = SelectField(
        'Priority',
        choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')],
        default='low',
        validators=[DataRequired()],
        render_kw={"class": "form-select border-primary"}
    )

    status = SelectField(
        'Status',
        choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed'),
                 ('archived', 'Archived')],
        default='pending',
        validators=[DataRequired()],
        render_kw={"class": "form-select border-primary"}
    )

    submit = SubmitField('Create To-Do', render_kw={"class": "btn btn-primary"})