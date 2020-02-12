import numpy as np
import pandas as pd
import math
import scipy.stats as stats

class Option:
    
    def __init__(self, underlying_price, strike_price, interest_rate, days_to_expiry, volatility, 
                 option_type='call', dividend_yield=0, side='long'):
        """ Define parameters of specific option to price.
        
        Args:
            price (float): Price of underlying asset (stock price).
            strike_price (float): Strike price of option.
            interest_rate (float): Risk-free interest rate.
            time_to_expiry (int): Number of days until option expiration.
            dividend_yield (float): Dividend yield of underlying asset. Based on
                assumptions of Black-Scholes, assume zero.
            volatility (float): Volatility of underlying asset.
            option_type (str): Type of option to price. Options are:
                call: Call option
                put: Put option
            side (str): Side of option trade. Options are:
                long: Long (buy) call option
                short: Short (sell) call option.
        """
        self.s = underlying_price
        self.k = strike_price
        self.r = interest_rate / 100
        self.t = days_to_expiry / 365
        self.q = dividend_yield
        self.sigma = volatility / 100
        self.option_type = option_type
        self.side = side
        
    def black_scholes_price(self):
        """ Calculate option price based on Black-Scholes model.
        
        Black-Scholes equation:
            d1 = ln(S0/K)+(r+σ^2/2)T
                 -------------------
                        σ sqrt(T)
            d2 = d1 - σ sqrt(T)
            c = S0e^(-qt)*N(d1)−Ke^(−rT)*N(d2)
            p = Ke^(−rT)N(−d2)−S0e^(-qt)*N(−d1)
        """
        d1 = (np.log(self.s/self.k) + (self.r -self.q + 0.5 * self.sigma**2) * self.t) / (self.sigma * np.sqrt(self.t))
        d2 = d1 - self.sigma * np.sqrt(self.t)
        n_d1 = stats.norm.cdf(d1)
        n_d2 = stats.norm.cdf(d2)
        n_d1_inv = stats.norm.cdf(-d1)
        n_d2_inv = stats.norm.cdf(-d2)
        if self.option_type == 'call':
            option_price = (math.exp(-self.q*self.t) * 
            (self.s * math.exp((self.r - self.q)*self.t) * n_d1 - self.k * n_d2))
        elif self.option_type == 'put':
            option_price = (math.exp(-self.r*self.t) * self.k * n_d2_inv -self.s 
                            * math.exp(-self.q * self.t) * n_d1_inv)
        if self.side == 'long':
            option_price *= -1
        return option_price

class Spread():
    
    def calc_price(underlying_price, strike_price_long, strike_price_short, interest_rate, 
                 days_to_expiry, volatility, dividend_yield=0, option_type='call'):
        """ Define parameters of specific option to price.
        
        Args:
            price (float): Price of underlying asset (stock price).
            strike_price_long (float): Strike price of long call.
            strike_price_short (float): Strike price of short call.
            interest_rate (float): Risk-free interest rate.
            time_to_expiry (int): Number of days until option expiration.
            dividend_yield (float): Dividend yield of underlying asset. Based on
                assumptions of Black-Scholes, assume zero.
            volatility (float): Volatility of underlying asset.

        """
        
        call_long = Option(underlying_price=underlying_price,
                           strike_price=strike_price_long, 
                           interest_rate=interest_rate,
                           days_to_expiry=days_to_expiry, 
                           volatility=volatility,
                           option_type=option_type, 
                           side='long').black_scholes_price()
        
        call_short = Option(underlying_price=underlying_price, 
                            strike_price=strike_price_short, 
                            interest_rate=interest_rate,
                            days_to_expiry=days_to_expiry, 
                            volatility=volatility, 
                            option_type=option_type,
                            side='short').black_scholes_price()
        
        return call_long, call_short