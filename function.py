def func():
    print("this is a function")
func()

def func1(x,y=3):
    z=x+y
    print(z)
func1(10,3)

def name_fun(city):
    print(f'He belongs to {city}')
name_fun("indore")

# Args and Kwargs in python------------

def myFun(*argv):
	for arg in argv:
		print(arg)


myFun('Hello', 'how', 'are', 'you', '?')

def myFun1(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}=={value}')
 
 
myFun1(first='Geeks', mid='for', last='Geeks')


   