import InsectClass as i

mosquito = i.Insect(2,4)
housefly = i.Insect(3,5)

mosquito.flight_lenght()

housefly.flight_lenght()

print("the mosquito can fly uo to", mosquito.get_miles(), "miles")
print("the housefly can fly uo to", housefly.get_miles(), "miles")
