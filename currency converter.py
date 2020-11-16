with open('conversion.txt') as c:
    line = c.readlines()

currency_Dict = {}
for x in line:
    parts = x.split("\t")
    currency_Dict[parts[0]] = parts[1]
amount = int(input("Enter the amount you want to convert in rupees: "))
print("Enter the currency name you want to convert entered amount to: \n")
print("avaliable options are: ")
for i in currency_Dict.keys():
    print(i)
currency = input("Enter one option from the avaliable options: ")
converted_amount = amount*float(currency_Dict[currency])
print(f"{amount} INR is equal to {converted_amount}{currency}")
