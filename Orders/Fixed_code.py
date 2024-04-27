import random

class Location:
    '''Location class'''
    def __init__(self,city:str,post_office:int) -> None:
        '''init
        >>> loc=Location('Lviv',78911)
        >>> loc.city
        'Lviv'
        '''
        self.city=city
        self.post_office=post_office

class Item:
    '''Item class'''
    def __init__(self,name:str,price:float) -> None:
        '''init
        >>> it=Item('you',100)
        >>> it.price
        100
        '''
        self.name=name
        self.price=price

class Vehicle:
    '''Vehicle class'''
    def __init__(self,vehicle_no:int) -> None:
        '''init
        >>> veh=Vehicle(1)
        >>> veh.vehicle_no
        1
        '''
        self.vehicle_no=vehicle_no
        self.is_available=True

class Order:
    '''order class'''
    order_id=0
    def __init__(self,user_name,city,post_office,items) -> None:
        '''init
        >>> my_order=Order('Andrii', 'Odesa', 3, [Item('shoes',153)])
        Your order number is 2
        '''
        Order.order_id+=1
        self.order_id=Order.order_id
        self.user_name=user_name
        self.items=items
        self.location=Location(city,post_office)
        self.vehicle=None
        self.amount=self.calculate_amount()
        print(f'Your order number is {self.order_id}')

    def calculate_amount(self)->float:
        '''Calculate price of order
        >>> my_items=[Item('Cat',100),Item('shoes',153)]
        >>> ort=Order('Olesya', 'Kharkiv', 17, my_items)
        Your order number is 4
        >>> ort.calculate_amount()==253
        True
        '''
        s=0
        for i in self.items:
            s+=i.price
        return s

    def assign_vehicle(self,vehicle:Vehicle)->None:
        '''vehicle assignment
        >>> ort=Order('Andrii', 'Odesa', 3, [Item('shoes',153)])
        Your order number is 3
        >>> ort.assign_vehicle(Vehicle(3))
        >>> ort.vehicle.vehicle_no
        3
        '''
        self.vehicle=vehicle

class LogisticSystem:
    '''LogisticSystem class'''
    def __init__(self) -> None:
        '''init
        >>> logSystem = LogisticSystem([Vehicle(1), Vehicle(2)])
        >>> logSystem.orders
        []
        '''
        self.orders=[]
        self.vehicles=[]

    def place_order(self,order_id: int) -> None:
        '''work with order if posible
        >>> logSystem = LogisticSystem([])
        >>> my_order3 = Order('Olesya', 'Kharkiv', 17, [Item('shoes',153)])
        Your order number is 1
        >>> logSystem.place_order(my_order3.order_id)
        'There is no available vehicle to deliver an order.'
        '''
        if not self.vehicles:
            return 'There is no available vehicle to deliver an order.'
        order = next((ordr for ordr in self.orders if ordr.order_id == order_id), None)
        if order:
            order.assign_vehicle(self.vehicles.pop())
            self.orders.append(order)

    def track_order(self, order_id: int) -> str:
        '''Says order status
        >>> logSystem = LogisticSystem([Vehicle(1), Vehicle(2)])
        >>> logSystem.track_order(485932990)
        'No such order.'
        '''
        for order in self.orders:
            if order.order_id == order_id:
                return f'Your order #{order_id} is sent to {order.location.city}. Total price: {order.amount} UAH.'
        return 'No such order.'
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
        self.vehicle1 = Vehicle("V1")
        self.vehicle2 = Vehicle("V2")
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

