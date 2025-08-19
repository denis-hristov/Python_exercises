meal = 44.50
tax_percentage = 6.75
tip_percentage = 15

tax = meal * tax_percentage/100
print tax
tip = meal * float(tip_percentage)/100
print tip

total = meal + tax + tip
print total