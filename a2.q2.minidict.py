#with using function ord() and taking input from the user
dic={}
len=int(input("Enter the length of alphabets(enter 26 if u need all the alphabets from a-z): "))

for i in range(len):
    alpha=input("Enter the alphabet: ") #enter from a-z
    for i in alpha:
        asc=ord(i)
        key=i
        value=asc
        dic[key]=value
print(dic)

#without using function ord()
dic={}
for i in range(97,97+26):
    dic[chr(i)]=i
print(dic)
    


