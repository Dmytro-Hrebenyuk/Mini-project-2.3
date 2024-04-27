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

