from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name):
        """
        Initialize the promotion with a name.
        """
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Abstract method to apply the promotion.
        Impelent in the subclasses.
        """
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percentage):
        super().__init__(name)
        self.percentage = percentage

    def apply_promotion(self, product, quantity):
        """
        Apply a percentage discount to the total price.
        """
        total_price = product.price * quantity
        discount = total_price * (self.percentage / 100)
        return total_price - discount


class SecondItemHalfPrice(Promotion):
    """
    Apply half price promo to the second item.
    """
    def apply_promotion(self, product, quantity):
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        total_price = (full_price_items * product.price) + (half_price_items * product.price * 0.5)
        return total_price


class Buy2getThirdFree(Promotion):
    def apply_promotion(self, product, quantity):
        """
        Discount the price of the third product of the same reference.
        """
        sets_of_three = quantity // 3
        remaining_items = quantity % 3
        total_items_to_pay = (sets_of_three * 2) + remaining_items
        total_price = total_items_to_pay * product.price
        return total_price



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
        self.promotion = None


    def get_promotion(self):
        """
        Getter for the promotion.
        """
        return self.promotion


    def set_promotion(self, promotion):
        """
        Setter for the promotion.
        """
        self.promotion = promotion


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
        :returns product details and promotions when apply.
        """
        promo_text = f"Promotion of {self.promotion.name}" if {self.promotion} else""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity} {promo_text}"



    def buy(self, quantity):
        """
        Updates the quantity of the product.
        In case of a problem (when? think about it), raises an Exception.
        :param quantity: Buys a given quantity of the product.
        :returns the total price (float) of the purchase.
        """

        if quantity > self.quantity:
            raise ValueError("Not enough stock of the product.")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = quantity * self.price

        self.quantity -= quantity

        # Deactivate the product if the quantity reaches 0
        if self.quantity == 0:
            self.deactivate()

        return total_price


class NonStockedProduct(Product):
    """
    Represents a non-stocked product that need no track of quantity.
    """
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        """
        Prevent setting quantity for non-stocked products.
        """
        raise ValueError("Cannot set quantity for a non-stocked product.")

    def show(self):
        return f"{self.name}, Price: {self.price}, (Non-stocked product)"


class LimitedProduct(Product):
    """
    Product with a purchase limit per order.
    """
    def __init__(self, name, price, quantity, max_quantity):
        super().__init__(name, price, quantity)
        self.max_quantity = max_quantity

    def buy(self, quantity):
        """
        Prevent setting quantity for non-stocked products.
        """
        if quantity > self.max_quantity:
            raise ValueError(f"Cannot get more than {self.max_quantity} {self.name} in a single order.")
        return super().buy(quantity)


    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}. Limited amount per order: {self.max_quantity}"




