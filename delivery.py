"""
This script models a simple delivery management system with classes for customers, deliveries, items, and invoices.
It allows tracking customer details, delivery information, items purchased, and final billing.
"""

class Customer:
    """Represents a customer placing an order, including name, contact details, and delivery address."""
    def __init__(self, name, contact, address):
        self._name = name
        self._contact = contact
        self._address = address

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_contact(self):
        return self._contact

    def set_contact(self, contact):
        self._contact = contact

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    def get_details(self):
        """Returns customer details as a dictionary."""
        return {
            "Name": self._name,
            "Contact": self._contact,
            "Delivery Address": self._address
        }


class Delivery:
    """Stores delivery details including order number, method, and delivery date."""
    def __init__(self, order_number, reference_number, delivery_date, method, dimensions, weight):
        self._order_number = order_number
        self._reference_number = reference_number
        self._delivery_date = delivery_date
        self._method = method
        self._dimensions = dimensions
        self._weight = weight

    def get_order_number(self):
        return self._order_number

    def set_order_number(self, order_number):
        self._order_number = order_number

    def get_reference_number(self):
        return self._reference_number

    def set_reference_number(self, reference_number):
        self._reference_number = reference_number

    def get_delivery_date(self):
        return self._delivery_date

    def set_delivery_date(self, delivery_date):
        self._delivery_date = delivery_date

    def get_method(self):
        return self._method

    def set_method(self, method):
        self._method = method

    def get_dimensions(self):
        return self._dimensions

    def set_dimensions(self, dimensions):
        self._dimensions = dimensions

    def get_weight(self):
        return self._weight

    def set_weight(self, weight):
        self._weight = weight

    def get_delivery_details(self):
        """Returns delivery details as a dictionary."""
        return {
            "Order Number": self._order_number,
            "Reference Number": self._reference_number,
            "Delivery Date": self._delivery_date,
            "Delivery Method": self._method,
            "Package Dimensions": self._dimensions,
            "Total Weight": self._weight
        }


class Item:
    """Represents an item in the delivery, including its price and quantity."""
    def __init__(self, code, description, quantity, unit_price):
        self._code = code
        self._description = description
        self._quantity = quantity
        self._unit_price = unit_price
        self._total_price = self.calculate_total()

    def get_code(self):
        return self._code

    def set_code(self, code):
        self._code = code

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_quantity(self):
        return self._quantity

    def set_quantity(self, quantity):
        self._quantity = quantity
        self._total_price = self.calculate_total()

    def get_unit_price(self):
        return self._unit_price

    def set_unit_price(self, unit_price):
        self._unit_price = unit_price
        self._total_price = self.calculate_total()

    def get_total_price(self):
        return self._total_price

    def calculate_total(self):
        """Calculates the total price for the item."""
        return self._quantity * self._unit_price

    def get_details(self):
        """Returns item details as a dictionary."""
        return {
            "Item Code": self._code,
            "Description": self._description,
            "Quantity": self._quantity,
            "Unit Price (AED)": self._unit_price,
            "Total Price (AED)": self._total_price
        }


class Invoice:
    """Represents the final invoice summarizing all purchased items and total costs."""
    def __init__(self, items, taxes_and_fees):
        self._items = items
        self._taxes_and_fees = taxes_and_fees
        self._subtotal = sum(item.get_total_price() for item in items)
        self._total_charges = self._subtotal + self._taxes_and_fees

    def get_invoice_details(self):
        """Returns invoice details as a dictionary."""
        return {
            "Items": [item.get_details() for item in self._items],
            "Subtotal (AED)": self._subtotal,
            "Taxes and Fees (AED)": self._taxes_and_fees,
            "Total Charges (AED)": self._total_charges
        }


# Example Usage
if __name__ == "__main__":
    """Test execution demonstrating the use of the defined classes."""
    
    customer = Customer("Sarah Johnson", "sarah.johnson@example.com", "45 Knowledge Avenue, Dubai, UAE")
    delivery = Delivery("DEL123456789", "DN-2025-001", "January 25, 2025", "Courier", "", "7 kg")
    items = [
        Item("ITM001", "Wireless Keyboard", 1, 100.00),
        Item("ITM002", "Wireless Mouse & Pad Set", 1, 75.00),
        Item("ITM003", "Laptop Cooling Pad", 1, 120.00),
        Item("ITM004", "Camera Lock", 3, 15.00)
    ]
    invoice = Invoice(items, 13.50)
    
    print("Delivery Note")
    print("Recipient Details:")
    print(customer.get_details())
    print("\nDelivery Information:")
    print(delivery.get_delivery_details())
    print("\nSummary of Items Delivered:")
    print(invoice.get_invoice_details())