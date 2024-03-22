my_list=[]

my_list=[10,20,30,40]
my_list.insert(my_list[2],15)
my_list.extend([50,60,70])

my_list.pop(-1)
my_list.sort()
print("The index of value 30 is ", my_list.index(30))
print(my_list)
