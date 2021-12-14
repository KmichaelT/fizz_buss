numbers=[*range(1,int(input("enter max number"))+1)]
result=[]
for n in numbers:
    if n%3==0 and n%5==0:
        result.append("FizzBuzz")
    elif n%5==0:
        result.append("Buzz")
    elif n%3==0 :
        result.append("Fizz")
    else:
        result.append(n)
print(result)