class Product:
    def __init__(self, name, price, quantity):
        """
        :arg:
            name: The name of the product (str).
            price: The price of the product (float).
            quantity: The quantity of the product available (int).
            :raises ValueError: If the name is empty, price is negative, or quantity is negative.
          """

        if not name:
            raise ValueError("Name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self):
        """
        Getter function for quantity.
        :returns the quantity (float).
        """
        return self.quantity



    def set_quantity(self, quantity):
        """
        Setter function for quantity. If quantity reaches 0, deactivates the product.
        :raises ValueError: If the new quantity is negative
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity = quantity
        # Deactivate the product if the quantity reaches 0
        if self.quantity == 0:
            self.deactivate()



    def is_active(self):
        """
        Getter function for active.
        :returns True if the product is active, otherwise False.
        """
        return self.active


    def activate(self):
        """
        Activates the product.
        """
        self.active = True


    def deactivate(self):
        """
        Deactivates the product
        """
        self.active = False


    def show(self):
        """
        :returns a string that represents the product, for example: "MacBook Air M2, Price: 1450, Quantity: 100"
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"



    def buy(self, quantity):
        """
        Updates the quantity of the product.
        In case of a problem (when? think about it), raises an Exception.
        :param quantity: Buys a given quantity of the product.
        :returns the total price (float) of the purchase.
        """

        if quantity > self.quantity:
            raise ValueError("Not enough stock of the product.")

        total_price = quantity * self.price
        self.quantity -= quantity

        # Deactivate the product if the quantity reaches 0
        if self.quantity == 0:
            self.deactivate()

        return total_price





