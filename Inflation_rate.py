# List of years from 1960 to 2022
year = list(range(1960, 2023))

lst = [7.7, 5.13, 6.62, 3.73, 3.94, 3.33, 4.95, 4.91, 6.67, 10.02, 9.48, 8.91, 11.99, 10.88, 
       8.35, 6.37, 5.80, 4.25, 3.77, 3.81, 4.30, 
       3.78, 4.01, 4.67, 13.23, 7.16, 8.98, 10.22, 
       10.25, 6.33, 11.79, 13.87, 8.97, 7.07, 9.38, 
       8.80, 8.73, 5.56, 8.32, 11.87, 7.89, 13.11, 
       11.35, 6.28, 2.52, 8.31, -7.63, 5.75, 28.60, 
       16.94, 6.44, 3.08, 5.09, -0.58, 3.24, 13.06, 
       10.80, 9.47, 13.36, 2.95, 3.63, 1.70, 1.78]

# Inflation rate for each year
inflation_rate = lst[::-1]

# Price prediction
var = 1
for i in range(len(year)):
    var = var + ((var*inflation_rate[i])/100)
    print("Inflation_rate_on_{}_in_india = ".format(year[i]),var)
print(var)

"""Observation : 1 Rupee in 1960 is equla to 83 rupees in 2022"""

