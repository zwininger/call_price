from flask import Flask, render_template, request, jsonify
from forms import OptionForm, CallSpread
import os
import call_price
app = Flask(__name__)
""" Helpful sites:
https://medium.com/@pemagrg/build-a-web-app-using-pythons-flask-for-beginners-f28315256893
https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
https://realpython.com/flask-by-example-part-1-project-setup/
https://github.com/saltycrane/flask-jquery-ajax-example
https://www.reddit.com/r/flask/comments/2fug7o/af_getting_selected_value_from_dropdown_list/ckcwrcg/
https://cs50.stackexchange.com/questions/27648/how-to-get-a-value-using-flask-from-a-selected-option-in-a-drop-down-list/27649#27649
https://stackoverflow.com/questions/58335919/how-to-display-python-console-output-on-html-page-using-flask
http://hplgit.github.io/web4sciapps/doc/pub/._part0004_web4sa_flask.html
https://stackoverflow.com/questions/45877080/how-to-create-dropdown-menu-from-python-list-using-flask-and-html
https://www.reddit.com/r/flask/comments/a5hxdi/how_to_give_a_drop_down_list_a_selected_value/
https://stackoverflow.com/questions/52443855/taking-data-from-drop-down-menu-using-flask
https://stackoverflow.com/questions/47179348/getting-drop-down-menu-data-on-flask-via-form-is-giving-400-bad-request
"""
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/call', methods=['GET', 'POST'])
def home():
    form = OptionForm()
    TSLA_long = call_price.Option(underlying_price=748.07, strike_price=700, interest_rate=1.6709, days_to_expiry=6, volatility=103.37,
            option_type='call', side='long').black_scholes_price()
    call = call_price.Option(underlying_price=form.data['underlying_price'], 
                    strike_price=form.data['strike_price'], 
                    interest_rate=form.data['interest_rate'],
                    days_to_expiry=form.data['days_to_expiry'], 
                    volatility=form.data['volatility'], 
                    option_type=form.data['option_type'], 
                    side=form.data['side']).black_scholes_price()
    return render_template("home.html", TSLA_long=TSLA_long, form=form, call=call)

@app.route('/call_spread', methods=['GET', 'POST'])
def spread():
    form = CallSpread()
    price = call_price.Spread.calc_price(underlying_price=form.data['underlying_price'], 
                    strike_price_long=form.data['long_strike'],
                    strike_price_short=form.data['short_strike'],
                    interest_rate=form.data['interest_rate'],
                    days_to_expiry=form.data['days_to_expiry'], 
                    volatility=form.data['volatility'], 
                    option_type=form.data['option_type'])
    long_price = price[0]
    short_price = price[1]
    position_price = long_price + short_price
    return render_template("spread.html", form=form, long_price=long_price, short_price=short_price,
                            position_price=position_price)

@app.route('/api', methods=['GET', 'POST'])
def api():
    return jsonify()

if __name__ == '__main__':
    app.run(debug=True)