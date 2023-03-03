class Order() :
    def __init__(self) :
        self.burger_count = self.randomBurgers()
    def randomBurgers(self) :
        return random.randint(1,20)
class Person() :
    def __init__(self) :
        self.customer_name = self.randomName()
    def randomName(self) :
        self.asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(self.asCustomers)
class Customer(Person) :
    def __init__(self) :
        super().__init__()
        self.order = Order()
queueCustomers = []
dictCustomers = {}
iNumCustomers = int(input("How many customers are in the queue? "))
CUSTOMER = 0
BURGERORDER = 1
# CustomerLine
for iCount in range (1, iNumCustomers + 1) :
    queueCustomers.append(Customer())
for iQueue in range(0, len(queueCustomers)) :
    if queueCustomers[0].customer_name in dictCustomers :
        dictCustomers[queueCustomers[0].customer_name] += queueCustomers[0].order.burger_count
        # print(queueCustomers[0].customer_name] + " has been helped (" + str(queueCustomers[0].order.burger_count) + " burgers)" )
        queueCustomers.pop(0)
    else :
        dictCustomers[queueCustomers[0].customer_name] = queueCustomers[0].order.burger_count
        queueCustomers.pop(0)
print("\n")
listSortedCustomers = sorted(dictCustomers.items(),key=lambda x: x[1], reverse=True)
for iPrCount in range(0, len(listSortedCustomers)) :
        print(listSortedCustomers[iPrCount][CUSTOMER].ljust(25) + str(listSortedCustomers[iPrCount][BURGERORDER]))
print("\n")
