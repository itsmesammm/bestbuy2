from products import Product

class Store:
    """
    Represents a store that tracks products and allows purchases.
    """

    def __init__(self, products):
        """
        Initializes a Store instance
        Args: products: A list of Product objects representing the products in the store.
        """
        self.products = products


    def add_product(self, product):
        """
        Adds a product to the stock.
        :param product: A Product object representing the product to be added
        """
        self.products.append(product)


    def remove_product(self, product):
        """
        Removes a product from store.
        :param product: A product objet representing the product to be removed.
        """
        try:
            self.products.remove(product)  # Attempt to remove the product
        except ValueError:
            pass


    def get_total_quantity(self):
        """
        :returns: how many items are in the store in total.
        """
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity


    def get_all_products(self):
        """
        :returns: a list from all products in the store that are active.
        """
        return [product for product in self.products if product.is_active()]


    def order(self, shopping_list):
        """
        Processes a shopping list and returns the total price of the order.
        :param: shopping_list: a list of tuples, where each tuple is a Product object and quantity to purchase.
        :return: the total price of the order.
        :raises: ValueError if the requested quantity of a product is greater than the stock.
        """

        total_price = 0

        for product, quantity in shopping_list:
            if quantity > product.get_quantity():
                raise ValueError(f"Not enough quantities of {product.name} in stock.")
            total_price += product.buy(quantity)

        return total_price


