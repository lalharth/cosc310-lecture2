import pytest
from exercise2 import Cart, OutOfStockError


@pytest.fixture
def empty_cart():
    return Cart()


@pytest.fixture
def sample_item():
    return {"id": 1, "name": "Tonkotsu Ramen", "price": 16.50, "available": True}


@pytest.fixture
def out_of_stock_item():
    return {"id": 4, "name": "Spicy Miso Ramen", "price": 17.25, "available": False}


def test_add_item_and_total(empty_cart, sample_item):
    empty_cart.add_item(sample_item, quantity=2)
    assert empty_cart.total() == 33.00


def test_add_duplicate_item_increases_quantity(empty_cart, sample_item):
    empty_cart.add_item(sample_item, quantity=1)
    empty_cart.add_item(sample_item, quantity=2)
    assert empty_cart.items["Tonkotsu Ramen"]["quantity"] == 3
    assert empty_cart.total() == 49.50


def test_add_invalid_quantity_raises_value_error(empty_cart, sample_item):
    with pytest.raises(ValueError):
        empty_cart.add_item(sample_item, quantity=0)


def test_add_out_of_stock_item_raises_exception(empty_cart, out_of_stock_item):
    with pytest.raises(OutOfStockError):
        empty_cart.add_item(out_of_stock_item)


def test_remove_item(empty_cart, sample_item):
    empty_cart.add_item(sample_item, quantity=1)
    empty_cart.remove_item("Tonkotsu Ramen")
    assert empty_cart.total() == 0.0
    assert "Tonkotsu Ramen" not in empty_cart.items


def test_remove_nonexistent_item_raises_key_error(empty_cart):
    with pytest.raises(KeyError):
        empty_cart.remove_item("Nonexistent Item")