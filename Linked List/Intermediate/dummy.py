number=input()

number=[int(x) for x in number]
even_number=[]

for no in number:
    if no%2==0:
        even_number.append(no)
    else:
        pass

print(sum(even_number))
