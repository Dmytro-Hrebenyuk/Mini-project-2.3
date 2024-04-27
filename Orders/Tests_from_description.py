import random

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Vehicle:
    def __init__(self, vehicle_id, capacity):
        self.vehicle_id = vehicle_id
        self.capacity = capacity

class Location:
    def __init__(self, city, post_office):
        self.city = city
        self.post_office = post_office

class Order:
    def __init__(self, user_id, items, destination):
        self.order_id = random.randint(1000, 9999)
        self.user_id = user_id
        self.items = items
        self.destination = destination
        self.delivered = False

class LogisticSystem:
    def __init__(self):
        self.orders = []
        self.vehicles = []

    def place_order(self, user_id, items, destination):
        # Check for available vehicles
        if not self.vehicles:
            return "No available vehicles for delivery."

        # Create order
        new_order = Order(user_id, items, destination)
        self.orders.append(new_order)

        # Assign vehicle to the order
        assigned_vehicle = self.vehicles.pop(0)
        print(f"Order {new_order.order_id} assigned to vehicle {assigned_vehicle.vehicle_id}")

        return new_order.order_id

    def track_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                if order.delivered:
                    return f"Order {order_id} has been delivered to {order.destination.city}, {order.destination.post_office}"
                else:
                    return f"Order {order_id} is being delivered to {order.destination.city}, {order.destination.post_office}"
        return "Order not found."

# Unit Tests
import unittest
import random

class TestLogisticSystem(unittest.TestCase):
    def setUp(self):
        self.logistic_system = LogisticSystem()
        self.item1 = Item("Book", 15)
        self.item2 = Item("Laptop", 1000)
        self.location1 = Location("Kyiv", "03058")
        self.location2 = Location("Lviv", "79000")
        self.vehicle1 = Vehicle("V1", 10)
        self.vehicle2 = Vehicle("V2", 15)
        self.logistic_system.vehicles.append(self.vehicle1)
        self.logistic_system.vehicles.append(self.vehicle2)

    def test_place_order(self):
        order_id = self.logistic_system.place_order(1, [self.item1, self.item2], self.location1)
        self.assertEqual(len(self.logistic_system.orders), 1)
        self.assertIn(order_id, [order.order_id for order in self.logistic_system.orders])

    def test_place_order_no_vehicle(self):
        self.logistic_system.vehicles.clear()
        order_id = self.logistic_system.place_order(1, [self.item1, self.item2], self.location1)
        self.assertEqual(order_id, "No available vehicles for delivery.")
        self.assertEqual(len(self.logistic_system.orders), 0)

    def test_track_order(self):
        order_id = self.logistic_system.place_order(1, [self.item1, self.item2], self.location1)
        self.assertEqual(self.logistic_system.track_order(order_id), f"Order {order_id} is being delivered to {self.location1.city}, {self.location1.post_office}")

    def test_track_order_delivered(self):
        order_id = self.logistic_system.place_order(1, [self.item1, self.item2], self.location1)
        order = next(order for order in self.logistic_system.orders if order.order_id == order_id)
        order.delivered = True
        self.assertEqual(self.logistic_system.track_order(order_id), f"Order {order_id} has been delivered to {self.location1.city}, {self.location1.post_office}")

    def test_track_order_not_found(self):
        self.assertEqual(self.logistic_system.track_order(9999), "Order not found.")

if __name__ == '__main__':
    unittest.main()

