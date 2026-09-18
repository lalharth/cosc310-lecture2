import json
from typing import Any, Dict, List


def load_menu(file_path: str) -> List[Dict[str, Any]]:
    """Loads menu data from a JSON file."""
    with open(file_path, "r") as file:
        return json.load(file)


def filter_and_sort_menu(
    menu: List[Dict[str, Any]], max_price: float = 10.00
) -> List[Dict[str, Any]]:
    """Filters available items under max_price and sorts by price ascending."""
    filtered_items = [
        item for item in menu if item.get("available") and item.get("price", 0) < max_price
    ]
    # Sort items by price (cheapest first)
    filtered_items.sort(key=lambda item: item["price"])
    return filtered_items


def display_menu(items: List[Dict[str, Any]]) -> None:
    """Prints the items formatted with f-strings."""
    for item in items:
        name: str = item["name"]
        price: float = item["price"]
        print(f"{name:<20} ${price:.2f}")


def main() -> None:
    menu_data = load_menu("data/menu.json")
    budget_items = filter_and_sort_menu(menu_data, max_price=10.00)
    display_menu(budget_items)


if __name__ == "__main__":
    main()