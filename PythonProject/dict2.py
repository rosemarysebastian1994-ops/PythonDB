l = {"emp001":["Arun",23,"ekm"], "emp002":["Amal", 24,"tvm"], "emp003":["Anu",30,"tcr"]}
#a) Print the names of all employees
#print(l["emp001"][0], l["emp002"][0], l["emp003"][0])
for i in l.keys():
    print(l[i][0])
#b)Print the average age from the given data
#avg = (l["emp001"][1] + l["emp002"][1] + l["emp003"][1])/3
avg = 0
for i in l.keys():
    avg += l[i][1]
avg /= len(l)
print(avg)
#c)Print the place of the employees with id "emp002"
print(l["emp002"][2])
#d)Change the place value of the employee with id "emp003"
l["emp003"][2] = "ksd"
print(l)