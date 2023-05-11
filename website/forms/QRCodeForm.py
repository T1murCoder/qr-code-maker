from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length
from wtforms.widgets.core import ColorInput
from wtforms.validators import NumberRange
from wtforms.widgets.core import NumberInput


class QRCodeForm(FlaskForm):
    text = TextAreaField("Введите текст:", validators=[DataRequired(), Length(min=0, max=200)])
    size = IntegerField("Выберите размер", default=450, widget=NumberInput(45, 45, 4500), validators=[DataRequired(), NumberRange(min=45, max=4500)])
    background_color = StringField("Цвет фона:", default="#FFFFFF", widget=ColorInput())
    foreground_color = StringField("Основной цвет:", default="#000000", widget=ColorInput())
    style = SelectField("Выберите стиль:", default="Default", choices=["Default", "Gapped", "Circle", "Rounded", "Verticlal bars", "Horizontal bars"], validators=[DataRequired()])
    submit = SubmitField("Сгенерировать")
    