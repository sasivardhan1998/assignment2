str1 = input('Enter a string: ')
sum=0
for i in  str1:

    if i.isdigit():

        sum=sum+int(i)
print("sum=",sum)