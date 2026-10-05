#פונקציה הקולטת שני משתנים ומחזירה את ההפרש החיובי
def diff(num1, num2):
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1

num1 = 56
num2 = 83
#שתי דרכים להשיג את התוצאה
result = diff(num1,num2)
print(result) #27

print(diff(num1, num2)) #27

#סכום מספרים מ 1 עד num
def sum_numbers(num):
    sum = 0
    for i in range(num+1):
        sum = sum + i
    return sum

print(sum_numbers(12)) #78
#עצרת עד num
def factorial(num):
    mul = 1
    for i in range(1,num+1):
        mul = mul * i
    return mul

print(factorial(7))
print(factorial(10))
#שטח צורה
def area(shape):
    if shape == "Circle":
        radius = int(input("Enter circle radius"))
        area = radius*radius*3.14
    elif shape == "Square":
        edge_length = int(input("Enter edge length"))
        area = edge_length*edge_length
    elif shape == "Rectangle":
        height = int(input("Enter Length"))
        width = int(input("Enter Width"))
        area = height*width
    else:
        area = 0
    return  area

