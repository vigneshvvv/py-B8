class ProductInfo:
    # id= 0
    # productName = ""
    # price = 0
    # category = ""

    def __init__(self, a=0, b = "", c =0, d=""):
        self.id = a
        self.productName = b
        self.price = c
        self.category = d



product1 = ProductInfo(1, "DataCable", 500, "Electronics")
product2 = ProductInfo()
product2.id = 2
product2.productName = "Laptop"
print(product1.__dict__)
print(product2.__dict__)