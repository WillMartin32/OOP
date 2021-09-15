import CellPhoneClass as c

def main():

    name = input("What is the name of your phone's manufacturer? ")
    model = input("What is your phone's model? ")
    price = input("What is your phone's retail price? ")

    phone1 = c.CellPhone(name,model,price)

    print("Your phone's manufacturer is", phone1.get_manufact())
    print("Your phone's model number is", phone1.get_model())
    print("Your phone's retail price is", phone1.get_retail_price())

main()