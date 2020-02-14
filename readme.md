# Call Price Calculator

Call and call spread price calculator using Flask framework. Utilizes Black-Scholes formula for options pricing.

## Getting Started
------

Launch the application.

```bash
$ cd /call_price
$ python3 app.py
```

## Usage
------

### __Browser__
For calculations using the browser UI, modify the variables within the forms on the */call* and */call_spread* pages and hit 'submit' to calculate the price and display at the bottom of the page.

### __API__

Send requests to */api/call* and */api/call_spread*, respectively, for call and call spread prices. Responses are json format.


#### /api/call

GET /call?underlying_price=748.07&strike_price=700&interest_rate=1.6709&days_to_expiry=6&volatility=103.37&option_type=call&side=long

#### /api/call_spread

GET /call_spread?underlying_price=748.07&strike_price_long=700&strike_price_short=650&interest_rate=1.6709&days_to_expiry=6&volatility=103.37&option_type=call&side=long

## To-Do
------
* Add other option strategies
* Add other derivative types (futures, forwards)
* Calculate and plot option payoffs
* Add ability to pull option prices/terms from realtime source (e.g. Nasdaq, Bloomberg)
* Calculate implied volatility based on known options prices
