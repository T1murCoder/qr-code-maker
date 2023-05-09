from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.widgets.core import ColorInput


class QRCodeForm(FlaskForm):
    text = TextAreaField("Введите текст:", validators=[DataRequired(), Length(min=0, max=200)])
    background_color = StringField("Цвет фона:", default="#FFFFFF", widget=ColorInput())
    submit = SubmitField("Сгенерировать")
    