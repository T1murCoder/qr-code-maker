from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class QRCodeForm(FlaskForm):
    text = TextAreaField("Введите текст:", validators=[DataRequired(), Length(min=0, max=200)])
    submit = SubmitField("Сгенерировать")
    