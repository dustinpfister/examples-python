def mess(item='foo', price=6.66):
    return 'The price for this {item} is ${price}'.format(item=item, price=price)

print( mess() ) # The price for this foo is $6.66
print( mess('bar', 3.57) ) # The price for this bar is $3.57