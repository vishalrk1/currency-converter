with open('conversion.txt') as c:
    line = c.readlines()

currency_Dict = {}
for x in line:
    parts = x.split("\t")
    currency_Dict[parts[0]] = parts[1]

print("avaliable options to convert rs in other curreny or to convert other currencies in rs: \n")
for i in currency_Dict.keys():
    print(i)

print("choose the currency you want to convert")
currency1 = input("please enter the currency from avaliable options: ")
amount = int(input("Enter the amount to convert: "))

if currency1 == "Indian Rupees":
    currency2 = input("Enter the currency you want to convert to:")
    converted_amount = amount * float(currency_Dict[currency2])
    print(f"{amount} INR is equal to {converted_amount} {currency2}")

else:
    converted_amount = amount / float(currency_Dict[currency1])
    print(f"{amount} {currency1} is equal to {converted_amount} INR")