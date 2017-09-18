# We need to write some code to return the original price of a product, the return type must be of type decimal and 
# the number must be rounded to two decimal places.
# We will be given the sale price (discounted price), and the sale percentage, our job is to figure out the original price.

def discover_original_price(discounted_price, sale_percentage):
    percent = 100 - sale_percentage
    result = 100 * float(discounted_price) / float(percent)
    return round(result,2)
