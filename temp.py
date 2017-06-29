import math

num = input("enter the googlement")
n = num
d = 0
string1 = ""
list = []
p = 0
digit = 1
gelementcount = 1
flag = True
while (flag):
    while (n > 0):
        d = n % 10
        list.append(d)
        n = n / 10
        p += 1
    for i in range(p-1,-1,-1):
        if (p == 0):
            print("case " + num + ": 1")
        else:
            if (list[i] == 0):
                digit+=1
            else:
                for j in range(1, list[i] + 1):
                    string1 = string1 +(str(digit))
                digit += 1
    if (len(string1) != p):
        flag = False  # do nothing
    else:
        gelementcount += math.factorial(p)
    n = int(string1)
    digit=1
    string1=""
    list=[]
    p=0
print("case {0}: {1}".format(num,gelementcount))