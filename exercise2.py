from typing import Dict, Any


class OutOfStockError(Exception):
    """Custom exception raised when adding an item that is out of stock."""
    pass


class Cart:
    """Represents a shopping cart."""

    def __init__(self) -> None:
        self.items: Dict[str, Dict[str, Any]] = {}

    def add_item(self, item: Dict[str, Any], quantity: int = 1) -> None:
        """Adds an item to the cart or increases its quantity."""
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")

        if not item.get("available", True):
            raise OutOfStockError(f"'{item['name']}' is out of stock.")

        name = item["name"]
        price = item["price"]

        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"price": price, "quantity": quantity}

    def remove_item(self, item_name: str) -> None:
        """Removes an item from the cart."""
        if item_name not in self.items:
            raise KeyError(f"'{item_name}' is not in the cart.")
        del self.items[item_name]

    def total(self) -> float:
        """Calculates the total cost of items in the cart, rounded to 2 decimals."""
        total_price = sum(details["price"] * details["quantity"] for details in self.items.values())
        return round(total_price, 2)

    def clear(self) -> None:
        """Clears all items from the cart."""
        self.items.clear()

    def __repr__(self) -> str:
        return f"Cart({self.items})"


if __name__ == "__main__":
    # Quick sanity check
    cart = Cart()
    
    # Try adding a valid item
    item1 = {"id": 2, "name": "Gyoza (6 pc)", "price": 8.00, "available": True}
    cart.add_item(item1, quantity=2)
    print("Cart total after adding Gyoza:", cart.total())

    # Try error handling for an out-of-stock item
    item2 = {"id": 4, "name": "Spicy Miso Ramen", "price": 17.25, "available": False}
    try:
        cart.add_item(item2)
    except OutOfStockError as e:
        print("Caught expected error:", e)