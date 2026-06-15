d={"title":"ABC", "Author":"John", "Price":200}
#Print all the values inside the dictionary
print(d.values())
#Print all the keys inside the dictionary
print(d.keys())
print(d.items())

#Print the value of a key price
print(d["Price"])
#Change the value of price to 300
d["Price"] = 300
print(d["Price"])

#Add a new key value pair language:english
d["language"] = "english"
print(d)
#print the length of the dictionary
print(len(d))