""" Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost. Round the result to the nearest integer. """


#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#
def main():
    def solve(meal_cost, tip_percent, tax_percent):
        tip = meal_cost * tip_percent / 100
        tax = meal_cost * tax_percent / 100
        totalCost = meal_cost + tip + tax

        return round(totalCost)

    print(solve(12.0, 20, 8))

main()


    
