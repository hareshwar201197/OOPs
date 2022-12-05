class customer:

    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address

class Address:

    def __init__(self,city,pincode,state):
        self.city = city
        self.pincode = pincode
        self.state = state

add = Address("Jalgaon",424107,"Maharashtra")
customer_obj = customer("Harish","Male",add)
print(customer_obj.address.state)
