"""
For investments over $1M it can be typically assumed that they will return 5% forever.
Using the [2022 - 2023 JMU Cost of Attendance](https://www.jmu.edu/financialaid/learn/cost-of-attendance-undergrad.shtml),
calculate how much a rich alumnus would have to give to pay for one full year (all costs) for an in-state student
and an out-of-state student. Store your final answer in the variables: "in_state_gift" and "out_state_gift".

Note: this problem does not require the "compounding interest" formula from the previous problem.

"""

### Your code here ###

in_state_cost = 30792  ## In-state total cost for the academic year 2024-2025

out_state_cost = 47882 ## Out-state total cost for the academic year 2024-2025

return_rate = 0.05      ## 5% return rate per

minimum_donation1 = in_state_cost/return_rate
print ("This is the minimum donation to cover in_state_cost $", minimum_donation1) #

minimum_dontion2 = out_state_cost/return_rate
print ("This is the minimum donation to cover out_state_cost $", minimum_dontion2)

## find the ratio

in_state_gift = 615840

out_state_gift = 957640