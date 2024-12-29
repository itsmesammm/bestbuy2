import pytest
from products import Product

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









