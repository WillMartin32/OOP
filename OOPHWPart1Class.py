

class RetailItem:

    def __init__(self,d,u,p):
        self.__item_description = d
        self.__units_of_inventory = u
        self.__price = p


    def get_description(self):
        return self.__item_description

    def get_units(self):
        return self.__units_of_inventory

    def get_price(self):
        return self.__price
