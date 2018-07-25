#Scenario: Let's buy some donuts for a party!

store_location = """Donut Lane, 
3337 Donut Shoppe
Donutville, 35794 DL"""
print("The store location is " + str(store_location))

money_in_wallet = 900
donuts_purchased = 100
unit_donut_price = 3.25
donut_price = donuts_purchased * unit_donut_price
sales_tax = 0.05 * donut_price
total_donut_cost = donut_price + sales_tax
money_in_wallet -= total_donut_cost
print("I had 900 dollars to begin with")
print("The total donut cost was " + str(total_donut_cost))
print("I now have " + str(money_in_wallet) + " left in my wallet.")

home_location = "somewhere on this earth"
print("My house is " + str(home_location))

print("I realize that I am low on gas. It is time to purchase some gas.")

unit_gas_price = 3.55
gallons_in_car = 100
tank_full = 30
Gas_needed = gallons_in_car - tank_full
total_gas_price = Gas_needed * unit_gas_price
sales_tax = total_gas_price * 0.08
final_gas_price = total_gas_price + sales_tax
money_in_wallet -= final_gas_price
print('after purchasing gas, I now have ' + str(money_in_wallet)+ ' left in my wallet. The gas cost me ' + str(final_gas_price) + '.')
print('Do I have enough money left?')

#add an if/else thingy here!

print(home_location)

people_at_party = 30
donuts_per_person = donuts_purchased / people_at_party
float_donuts_per_person = float(donuts_purchased) / people_at_party
full_donuts_remaining = donuts_purchased % people_at_party
print("There are %s people at a party. Each person gets %0.0f donuts. There are %s donuts remaining." % (people_at_party,donuts_per_person,full_donuts_remaining))
#%s automatically turns a number into a string. Use it as a place holder.
