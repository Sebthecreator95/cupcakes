from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional


class CupcakeForm(FlaskForm):
    """Form for adding pets."""

    flavor = StringField("Flavor", validators=[InputRequired(message="A Flavor is required")])

    image_url = StringField("Image URL", validators=[URL()])

    size = SelectField("Size", choices=[("Small","Small"), ("Medium","Medium"), ("Large","Large"), ("ExtraLarge","ExtraLarge")])

    rating = IntegerField("Rating", validators=[NumberRange(min=0,max=10,message"Enter a number")])
