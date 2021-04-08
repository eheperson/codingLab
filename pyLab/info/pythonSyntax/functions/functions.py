"""
    *args (Non-Keyword Arguments)
    type of args is tupple

    **kwargs (Keyword Arguments)
    type of kwargs is dictionary
"""
#
#
def myFun(*args, **kwargs):
    print("myFun() : ")
    print("Length of args : ", len(args))
    print("Length of kwargs : ", len(kwargs))
    print("")
    print("Type of args : ", type(args))
    print("Type of kwargs : ", type(kwargs))
    print("")
    print("args: ", args) 
    print("kwargs: ", kwargs)
    print("")
#
myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")

def myFun2(arg1, **kwargs):
    print("myFun2() : ")
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
#  
myFun2("Hi", first ='Geeks', mid ='for', last='Geeks')
#
#

