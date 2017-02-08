info = input("Enter the following information : Name, age, gender, species, relationship status : ")

list = ' '.join(info.split())

mylist = list.split()

print(mylist)

print("Name : " + mylist[0])
print("Age : " + mylist[1])
print("gender : "+mylist[2])
print("Species : "+mylist[3])
print("Relationship Status : "+mylist[4])

