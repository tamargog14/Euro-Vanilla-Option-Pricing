import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt 
import scipy.stats as si 
import sympy as sy
import sympy.stats as systats

#fair value option pricing (Black Scholes)
def euro_van(S, K, T, r, sigma, option = 'call'): 

    d1 = (np.log(S/K) + (r + (.5*sigma**2)*T)) / (sigma * np.sqrt(T))
    d2 = (np.log(S/K) + (r - (.5*sigma**2)*T)) / (sigma * np.sqrt(T))

    if option == 'call':
        result = (S * si.norm.cdf(d1, 0 , 1.0) - K * np.exp(-r*T) * si.norm.cdf(d2 , 0 , 1.0))

    if option == 'put': 
        result = (K * np.exp(-r*T) * si.norm.cdf(-d2 , 0 , 1.0)) - (S * si.norm.cdf(-d1, 0 , 1.0))

    return result 

#*****Buy option and create delta hedge*****
#creating delta 
def delta_function(S, K , T, r, sigma, option = 'call'): 
    d1 = (np.log(S/K) + (r + (.5*sigma**2)*T)) / (sigma * np.sqrt(T))

    if option == 'call': 
        result = si.norm.cdf(d1, 0.0 , 1.0)

    if option == 'put':
        result = si.norm.cdf(-d1 , 0.0, 1.0)
    return result


#**************************************************************
#input data to find option value and delta value 
euro_van(           )
delta = delta_function(         )
#**************************************************************

#using delta for break even hedge
    #shares needed to hedge 
        shares_to_purchase = delta * 100 
        print(shares_to_purchase)

    #margin requirements to cover hedge (given cash account)
        margin_req = shares_to_purchase * S 
        print(margin_req)
