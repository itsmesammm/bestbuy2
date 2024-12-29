import pytest
from products import Product, NonStockedProduct, LimitedProduct, PercentDiscount, SecondItemHalfPrice, Buy2getThirdFree


def test_create_valid_product():
    # Test that creating a valid product works
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100


def test_create_product_with_invalid_name():
    # Test that creating a product with an empty name raises an exception
    with pytest.raises(ValueError, match = "Name cannot be empty"):
        Product("", price=1450, quantity=100)


def test_create_product_with_negative_price():
    # Test that creating a product with a negative price raises an exception
    with pytest.raises(ValueError, match="Price cannot be negative"):
        Product("MacBook Air M2", price=-1450, quantity=100)


def test_create_product_with_negative_quantity():
    # Test that creating a product with a negative quantity raises an exception
    with pytest.raises(ValueError, match="Quantity cannot be negative"):
        Product("MacBook Air M2", price=1450, quantity=-100)


def test_product_becomes_inactive_when_quantity_reaches_zero():
    # Test that a product becomes inactive when its quantity is set to 0
    product = Product("MacBook Air M2", price=1450, quantity=1)
    product.set_quantity(0)
    assert product.is_active() is False


def test_product_becomes_inactive_via_purchase():
    # Test that a product becomes inactive after its last unit is purchased
    product = Product("MacBook Air M2", price=1450, quantity=1)
    product.buy(1)  # Buy the last unit
    assert product.is_active() is False


def test_product_purchase_modifies_quantity_and_returns_right_output():
    # Test that purchasing a product reduces its quantity and returns the correct total price
    product = Product("MacBook Air M2", price=1450, quantity=100)
    total_price = product.buy(50)
    assert product.quantity == 50
    assert total_price == 50 * 1450


def test_buying_more_than_available_raises_exception():
    # Test that trying to buy more than the available stock raises an exception
    product = Product("MacBook Air M2", price=1450, quantity=1)
    with pytest.raises(ValueError, match="Not enough stock of the product."):
        product.buy(2)


def test_nonstocked_product_creation():
    product = NonStockedProduct("Windows License", 125)
    assert product.name == "Windows License"
    assert product.price == 125
    assert product.quantity == 0
    assert product.is_active()


def test_nonstocked_product_set_quantity_raises_exception():
    product = NonStockedProduct("Windows License", 125)
    with pytest.raises(ValueError, match="Cannot set quantity for a non-stocked product."):
        product.set_quantity(5)


def test_limited_product_creation():
    product = LimitedProduct("Shipping", price=10, quantity=250, max_quantity=1)
    assert product.name == "Shipping"
    assert product.price == 10
    assert product.quantity == 250
    assert product.max_quantity == 1


def test_limited_product_over_limit():
    product = LimitedProduct("Shipping", price=10, quantity=250, max_quantity=1)
    with pytest.raises(ValueError, match=("Cannot get more than 1 Shipping in a single order.")):
        product.buy(2)


def test_limited_product_show():
    product = LimitedProduct("Shipping", 10, quantity=250, max_quantity=1)
    assert product.show() == "Shipping, Price: 10, Quantity: 250. Limited amount per order: 1"


def test_percent_discount():
    promotion = PercentDiscount("30% off!", percentage=30)
    product = Product("Test Product", price=100, quantity=10)
    discounted_price = promotion.apply_promotion(product, 2)
    assert discounted_price == 140

def test_second_half_price():
    promotion = SecondItemHalfPrice("Second Half Price!")
    product = Product("Test Product", price=100, quantity=10)
    discounted_price = promotion.apply_promotion(product, 3)
    assert discounted_price == 250

def test_third_one_free():
    promotion = Buy2getThirdFree("Buy 2, Get 1 Free!")
    product = Product("Test Product", price=100, quantity=10)
    discounted_price = promotion.apply_promotion(product, 4)
    assert discounted_price == 300







