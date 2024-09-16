class Product:
    """создание класса продукт"""

    name: str
    description: str
    price: float
    quantity: int
    product = []
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """инициализация класса продукт"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, name: str, description: str, price: float, quantity: int):
        cls.name = name
        cls.description = description
        cls.price = price
        cls.quantity = quantity
        product_empty = {"name": cls.name, "description": cls.description, "price": cls.price, "quantity": quantity}
        cls.product.append(product_empty)

        return cls.product

if __name__ == "__main__":

    product_s = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет 200MP, камера", 180000.0, 5)

    print(product_s.name)
    print(product_s.description)
    print(product_s.price)
    print(product_s.quantity)

    #print(Product.new_product("indesit","waht", 21000.00, 4))

    product_s = (Product.new_product("indesit","waht", 21000.00, 4))
    print(product_s[0])
