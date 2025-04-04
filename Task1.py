user=input("enter your name: ")

dict={'vedu':97,'vanshu':93,'riu':89,'dhruvi':79,'rahul':91,'shlok':78,'nitin':100}
if user in dict:
    print(dict.get(user))
else:
    print('Student not found')
