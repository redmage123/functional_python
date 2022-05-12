price_list = [10.99, 25.99, 13.00, 18.99, 99.99]


def start_pipeline(price_list):
    indexvalue = 0
    while indexvalue != len(price_list):
        yield price_list[indexvalue]
        indexvalue += 1


def convertToEuro(price_list):
    conversion_factor = 0.95
    for i in price_list:
        yield i * conversion_factor


def markup_price(price_list):
    for i in price_list:
        wholesale_price = i + i * 0.10
        yield wholesale_price


pipeline = markup_price(convertToEuro(start_pipeline(price_list)))

for price in pipeline:
    print(price)