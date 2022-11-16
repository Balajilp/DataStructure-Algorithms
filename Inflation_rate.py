salary = 4000000
slip = []
for i in range(8):
    salary = salary + ((salary*10)/100)
    slip.append(salary)
print(salary)
print(sum(slip))

