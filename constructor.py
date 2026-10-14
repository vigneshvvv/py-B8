class ProductInfo:
    # id= 0
    # productName = ""
    # price = 0
    # category = ""

    def __init__(self, a, b, c, d):
        self.id = a
        self.productName = b
        self.price = c
        self.category = d



product1 = ProductInfo(1, "DataCable", 500, "Electronics")
product2 = ProductInfo()
product2.id = 2
print(product1.__dict__)