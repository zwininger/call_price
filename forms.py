from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange

class OptionForm(FlaskForm):
    underlying_price = FloatField('Current Price', validators=[DataRequired()], default=748.07)
    strike_price = FloatField('Strike Price', validators=[DataRequired()], default=700)
    interest_rate = FloatField('Interest Rate (%)', validators=[DataRequired()], default=1.6709)
    days_to_expiry = IntegerField('Days to Expiry', validators=[DataRequired()], default=6)
    volatility = FloatField('Volatility (%)', validators=[DataRequired(), NumberRange(min=0, max=5)], default=103.37)
    option_type = SelectField('Option Type', choices=[('call', 'Call'), ('put', 'Put')], validators=[DataRequired()],
                    default='call')
    side = SelectField('Side', choices=[('long', 'Long'), ('short', 'Short')], validators=[DataRequired()],
                    default='long')
    submit = SubmitField('Calculate Price')

class CallSpread(FlaskForm):
    underlying_price = FloatField('Current Price', validators=[DataRequired()], default=748.07)
    long_strike = FloatField('Long Strike Price', validators=[DataRequired()], default=700)
    short_strike = FloatField('Short Strike Price', validators=[DataRequired()], default=650)
    interest_rate = FloatField('Interest Rate (%)', validators=[DataRequired()], default=1.6709)
    days_to_expiry = IntegerField('Days to Expiry', validators=[DataRequired()], default=6)
    volatility = FloatField('Volatility (%)', validators=[DataRequired(), NumberRange(min=0, max=5)], default=103.37)
    option_type = SelectField('Option Type', choices=[('call', 'Call'), ('put', 'Put')], validators=[DataRequired()],
                    default='call')
    submit = SubmitField('Calculate Price')