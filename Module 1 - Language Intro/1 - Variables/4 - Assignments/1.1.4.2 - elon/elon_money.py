"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 1-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $44B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
"""

### all your code below ###

#note the formula for compund interst is A=P(1+(r/n)^t
p = 33000000000         ## Initial investment 44 Billion (princple)
t1 = 10                 ## The number of years of investment - 10 years (time)
t2 = 20                 ## The number of years of investment - 20 years (time)
r1 = 0.0396               ## 3.96% compunding rate for 10 years - annual compunding (rate of return)
r2 = 0.0432               ## 4.32% compunding rate for 20 years - annual compunding (rate of return)
n = 1                     ## number of time it compunds a year


amount_1 = p*(1+(r1/1))**(t1*1)                     ##Note that ** = exponet and amount 1 is the amount of compound interest after 10 years
print("This is the amount after 10 years $", amount_1)

net_1 = p-amount_1                                  ## The profit take the difference of initial investment
print (net_1)
print ("Net profit after 10 years is $", net_1)


amount_2 = p*(1+(r2/1))**(t2*1)
print("This is the amount after 20 years $", amount_2)
print (amount_2)

net_2 = p-amount_2
print (net_2)
print ("Net profit after 20 years is $",net_2)

# final answer for 10-year
ten_year_final = 48660509081.78675

# final answer for 20-year
twenty_year_final = 76889229275.98897
