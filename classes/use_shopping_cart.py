from class_intro import ShoppingCart, Product

sc = ShoppingCart()
sc.add_to_cart(Product("Yoghurt", 0.79, "Ski"))
sc.show_cart()

print(f"use_shopping_cart has __name__: {__name__}")