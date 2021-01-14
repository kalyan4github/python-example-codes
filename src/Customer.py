class Customer:
    firstname = ""

    def __init__(self, name, location):
        Customer.firstname = name
        self.location = location

    def displayCustomer(self):
        print("Name:", Customer.firstname, "Location: ", self.location)


customer1 = Customer("Arnav","Mumbai")

customer1.displayCustomer()
