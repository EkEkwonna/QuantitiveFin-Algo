from math import exp

def future_discrete_value(x,r,n):
    return x*(1+r)**n

def present_discrete_value(x,r,n):
    return x*(1+r)**-n

def future_continuous_value(x,r,t):
    return x*exp(r*t)

def present_continuous_value(x,r,t):
    return x*exp(-r*t)

if __name__ == '__main__':

    # value of investment in dollars 
    x = 100

    # define the interest rate (r)
    r = 0.05

    # duration (years)
    n = 5


    print('Future values (discrete model) of x: %s' % future_discrete_value(x,r,n))
    print('Present values (discrete model) of x: %s' % present_discrete_value(x,r,n))
    print('Future values (continuous model) of x: %s' % future_continuous_value(x,r,n))
    print('Present values (continuous model) of x: %s' % present_continuous_value(x,r,n))

    "If we have $100 today we would eventually gain ~$28 in the span of 5 years (with 5% interest rate)"
    "If we have $100 in 5 years time it would mean that we started with ~$78 today (given an 5% interest rate)"


