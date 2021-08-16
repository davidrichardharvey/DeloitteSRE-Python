class Product:
    def __init__(self, name, price, brand):
        self.price = price
        self.name = name
        self.brand = brand

    def __repr__(self):
        return f"{self.name} ({self.brand}): £{self.price}"


class ShoppingCart:
    def __init__(self):
        self.contents = []

    def add_to_cart(self, new_item: Product):
        self.contents.append(new_item)

    def show_cart(self):
        for product in self.contents:
            print(f"{product.name} from {product.brand}: £{product.price:.2f}")

    def get_cart_total(self):
        cart_total = 0
        for product in self.contents:
            cart_total += product.price
        return cart_total


if __name__ == "__main__":
    sc = ShoppingCart()
    sc.add_to_cart(Product("Lemonade", 1.79, "ALDI"))
    sc.add_to_cart(Product("Book", 1.79, "Waterstones"))
    sc.show_cart()
    print(sc.contents)