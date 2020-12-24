name=input("Please enter a name")
surname=input("Please enter a surname")
age=int(input("Please enter a age"))
birtdate=int(input("Please enter a birthdate(just year)"))
user=[]
user.extend([name,surname,age,birtdate])
for i in user:
  print(i)
if(age<18):
  print("you can't go out because it's too dangerous")
else:
  print("You can go out to the street")
