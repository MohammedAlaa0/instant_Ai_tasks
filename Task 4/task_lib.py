def max_num(a,b,c):
    if a>b and a>c:
        return print("Max is ",a)
    elif b>a and b>c:
        return print("Max is ",b)
    elif c>a and c>b:
        return print("Max is ",c)
    
    
def fact(a):
    b = 1
    for i in range(a,0,-1):
        b = b * i
    return print("The Factorial is ",b)

