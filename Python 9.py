def summation(a,b):
    total = a+b
    #print(total)
    #print(total)
    #print(total)
    return total
summation(9,10)
print(summation(9,10))
summation(20,10)
summation(32,59)

def add(*numbers):
    c=0
    for i in numbers:
        c=c+i
    print("The sum is",c)
add(5,10)
add(20,30,40)

def multiply(*numbers):
    m=1
    for i in numbers:
        m = m*i
    print("The product is ",m)
multiply(2,3,-6,8)
multiply(2,5,8,9,8,6)
#testing to commit
def format_name(f_name,l_name):
    if f_name==' ' and l_name==' ':
        return "Please enter a valid name"
    else:
        formatted_f_name = f_name.title()
        formatted_l_name = l_name.title()
        return f"{formatted_f_name} {formatted_l_name}"
f_name = input("please enter first name: ")
l_name = input("Please enter last name ; ")
print(format_name(f_name,l_name))
