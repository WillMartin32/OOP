
class CellPhone:
    def __init__(self,n,m,p):
        self.__manufact = n
        self.__model = m
        self.__retail_price = p
    
    def set_manufact(self,manuName):
        self.__manufact = manuName

    def set_model(self,model):
        self.__model = model

    def set_retail_price(self,price):
        self.__retail_price = price
    
    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price
    
