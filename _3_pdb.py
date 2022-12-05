import pdb

def addition(no1,no2):
    add = no1 + no2
    return add

pdb.set_trace()

if __name__ == "__main__":
    no1 = input("Enetr no1 : ")
    no2 = input("Enter the no2 : ")
    data = addition(no1,no2)
    print(data)
