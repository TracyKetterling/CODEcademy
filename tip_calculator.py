"""This is an application that calculates the cost of a meal, tax and tip."""
# assign values to variables of meal, tax and tip
meal = 44.50
tax = 0.0675
tip = 15.0/100
# we are reassigning the variable meal to include the cost of the meal plus tax
meal = meal + meal * tax
# we are assigning the variable total to include meal, tip and tax
total = meal + meal * tip
# line 11 will print the above information into the console
print("%.2f" % total)