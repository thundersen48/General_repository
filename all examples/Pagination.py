#Product catalog

#There are 10 products
products = [f'product {i}' for i in range(1,11)]

def get_page(page_number, page_size=3):
    start = (page_number - 1) * page_size
    stop = page_number * page_size
    return products[start:stop]

print(f'Page 1:',get_page(page_number=1))

print(f'Page 2:', get_page(page_number=2))

print(f'Page 2:', get_page(page_number=3))