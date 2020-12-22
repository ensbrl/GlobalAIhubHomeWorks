values=[]
values.append(int(input("1. value :")))
values.append(float(input("2.value: ")))
values.append((input("3.value: ")))
values.append(input("4.value: "))
values.append(input("5.value: "))
print(values)
print(f'{1}.parameter {values[0]} {2}.parameter {values[1]} {3}.parameter {values[2]} {4}.parameter {values[3]}e{5}.parameter {values[4]}')
print(f'{1}.parameter {type(values[0])} {2}.parameter {type(values[1])} {3}.parameter {type(values[2])} {4}.parameter {type(values[3])} {5}.parameter {type(values[4])}')
