cars = 100
space_in_a_car = 4.0
drivers = 30
passangers = 90
cars_not_driven = cars-drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
avarage_passangers_per_car= passangers / cars_driven

print "there are", cars, "cars available" #her hentes variabelen "cars" som = 100
print "there are only" ,drivers, "drivers available"
print "there will be", cars_not_driven, "empty cars today" #her hentes variabelen "cars not driven" resultatet vil da bli 100-30 som da blir 70.
print "we can transport", carpool_capacity, "people today" # her hentes variabelen "carpool capacity" som er "cars driven"*"space in a car" som da blir 30*4 som = 120.
print "we have", passangers, "to carpool today"
print "we need to put about", avarage_passangers_per_car, "in each car"   