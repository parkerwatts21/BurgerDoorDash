# Caroline Conley, Jack Kelly, Matt Beckstrand, Parker Watts, Baylee El-Bakri, and Adam Trommlitz
# Description: Create a program that simulates an owner of a hamburger restaurant. 
# This program will track and print exactly how many hamburgers each customer eats by creating a queue and using a dictionary

import random

# Create an order class that defines an instance variable called burger_count and 
# creates a method called randomBurgers that returns a number between 1 and 20. (The method will be called in the constructor)

class Order() :
    def __init__(self) : 
        self.burger_count = self.randomBurgers()
    
    def randomBurgers(self) :
        return random.randint(1,20)

# Create a person class that has the customer name and randomly generates the customer name from a list of names (using the method randomName)

class Person() :
    def __init__(self) : 
        self.customer_name = self.randomName()
    def randomName(self) :
        self.asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(self.asCustomers)

# Create a customer class through inheritance and call the parent class using super function. 
# Create an instance variable called order in the constructor that is assigned an order object

class Customer(Person) :
    def __init__(self) : 
        super().__init__()
        self.order = Order()

# Create an empty list and dictionary

queueCustomers = []

dictCustomers = {}

# Prompt the user for amount of customers in the queue (100 for the assignment)

iNumCustomers = int(input("How many customers are in the queue? "))

# Clarify list by making constant variables for position 0 and 1 for customer and burgerorder

CUSTOMER = 0
BURGERORDER = 1

# Create a loop to load the customer objects in the queue (list)

for iCount in range (1, iNumCustomers + 1) :
    queueCustomers.append(Customer())

# Create a loop to keep track of burger count for customers by transfering information into dictionary and removing them from queue
# If the name isn't already in the dictionary add name and burger count.

for iQueue in range(0, len(queueCustomers)) :
    if queueCustomers[0].customer_name in dictCustomers :
        dictCustomers[queueCustomers[0].customer_name] += queueCustomers[0].order.burger_count
        # print(queueCustomers[0].customer_name] + " has been helped (" + str(queueCustomers[0].order.burger_count) + " burgers)" )
        queueCustomers.pop(0)
    else :
        dictCustomers[queueCustomers[0].customer_name] = queueCustomers[0].order.burger_count
        queueCustomers.pop(0)

print("\n")

# Convert the dictionary into a sorted list that is sorted by the most number of burgers order

listSortedCustomers = sorted(dictCustomers.items(),key=lambda x: x[1], reverse=True)

# Print out list using loop and constant variables that we set before
# We used ljust 25 instead of 19 to make the display look better

for iPrCount in range(0, len(listSortedCustomers)) :
        print(listSortedCustomers[iPrCount][CUSTOMER].ljust(25) + str(listSortedCustomers[iPrCount][BURGERORDER]))

print("\n")
