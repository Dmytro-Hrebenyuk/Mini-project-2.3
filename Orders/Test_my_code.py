'''import random for generating id'''
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

    # def __str__(self) -> str:
    #     return f'Name: {self.name}\nPrice: {self.price}'

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

    # def __str__(self) -> str:
    #     return

class LogisticSystem:
    '''LogisticSystem class'''
    def __init__(self,vehicles) -> None:
        '''init
        >>> logSystem = LogisticSystem([Vehicle(1), Vehicle(2)])
        >>> logSystem.orders
        []
        '''
        self.orders=[]
        self.vehicles=vehicles

    def place_order(self,order: Order) -> None:
        '''work with order if posible
        >>> logSystem = LogisticSystem([])
        >>> my_order3 = Order('Olesya', 'Kharkiv', 17, [Item('shoes',153)])
        Your order number is 1
        >>> logSystem.place_order(my_order3)
        'There is no available vehicle to deliver an order.'
        '''
        if self.vehicles==[]:
            return 'There is no available vehicle to deliver an order.'
        order.assign_vehicle(self.vehicles.pop())
        self.orders.append(order)

    def track_order(self,order: Order) ->str:
        '''Says order status
        >>> logSystem = LogisticSystem([Vehicle(1), Vehicle(2)])
        >>> logSystem.track_order(485932990)
        'No such order.'
        '''
        for i in self.orders:
            if order == i.order_id:
                return f'Your order #{order} is sent to \
{i.location.city}. Total price: {i.amount} UAH.'
        return 'No such order.'

import unittest

class TestLogisticSystem(unittest.TestCase):

    def setUp(self):
        self.vehicles = [Vehicle(1), Vehicle(2)]
        self.logSystem = LogisticSystem(self.vehicles)

    def test_place_order_with_available_vehicle(self):
        my_order = Order('Olesya', 'Kharkiv', 17, [Item('shoes', 153)])
        self.logSystem.place_order(my_order)
        self.assertIn(my_order, self.logSystem.orders)
        self.assertEqual(len(self.logSystem.vehicles), 1)

    def test_place_order_without_available_vehicle(self):
        self.logSystem.vehicles = []  # Make vehicles unavailable
        my_order = Order('Olesya', 'Kharkiv', 17, [Item('shoes', 153)])
        result = self.logSystem.place_order(my_order)
        self.assertEqual(result, 'There is no available vehicle to deliver an order.')
        self.assertNotIn(my_order, self.logSystem.orders)

    def test_track_order_existing_order(self):
        my_order = Order('Andrii', 'Odesa', 3, [Item('shoes', 153)])
        self.logSystem.place_order(my_order)
        result = self.logSystem.track_order(my_order.order_id)
        self.assertEqual(result, f'Your order #{my_order.order_id} is sent to {my_order.location.city}. Total price: {my_order.amount} UAH.')

    def test_track_order_non_existing_order(self):
        result = self.logSystem.track_order(485932990)
        self.assertEqual(result, 'No such order.')

if __name__ == '__main__':
    unittest.main()
