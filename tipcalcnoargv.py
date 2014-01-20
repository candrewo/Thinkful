meal = float(raw_input("Enter the cost of your meal: $"))
tax = float(raw_input("Enter tax rate as a decimal (e.g., .12, not 12%): "))
tip = float(raw_input("How much would you like to tip? (e.g., .20): "))

tax_value = meal * tax
meal_with_tax = meal + (tax_value)
tip_value = tip * (meal_with_tax)
total = meal_with_tax + tip_value

print "Meal: ${:.2f}".format(meal)
print "Tax: ${:.2f}".format(tax_value)
print "Tip: ${:.2f}".format(tip_value)
print "Total: ${:.2f}".format(total)