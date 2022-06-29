'''q1 :
ineruon
ineruon ineruon
ineruon ineruon ineruon
ineruon ineruon ineruon ineruon'''
n=4
for i in range(n):
    for j in range(i+1):
        print("ineruon",end=" ")
    print()
'''q2 :
        sudh 
     sudh sudh sudh 
sudh sudh sudh sudh sudh '''
n=3
for i in range(n):
    for j in range(n-i):
        print(" "*(len("sudh")),end=" ")
    for j in range(2*i+1):
        print("sudh",end=" ")
    print()

l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]

# q3 : Try to extract all the list entity
for i in l:
    if type(i)==list:
        print(i)
# q4 : Try to extract all the dict enteties
for i in l:
    if type(i)==dict:
        print(i)
# q5 : Try to extract all the tuples entities
for i in l:
    if type(i)==tuple:
        print(i)
#q6 : Try to extract all the numerical data it may b a part of dict key and values
for i in l:
    for j in i:
        if type(j)==int:
            print(j)
    if type(i)==dict:
        for e in i:
            if type(e)==int:
                print(i[e])
#Try to give summation of all the numeric data
def function():

    v=[]
    k=[]
    for i in l:
        for j in i:
            if type(j) == int:
                v.append(j)
        if type(i) == dict:
            for e in i:
                if type(e) == int:
                    k.append(e)
    m = v + k
    return sum(m)
print(function())
#q9 : Try to extract "ineruon" out of this data
for i in l:
    if type(i)==list:
        if type(i[0])==str:
            print(i[0])
'''q10:
         * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          *    '''
n=5
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
#q10 :Try to find out a number of occurances of all the data
k=[]
for i in l:
    if type(i):
        for j in i:
            k.append(j)
    if type(i)==dict:
        for e in i:
            k.append(i[e])
for r in set(k):
    print(r,k.count(r))
#q11 : Try to find out number of keys in dict element
for i in l:
    m=[]
    if type(i)==dict:
        for j in i:
            m.append(j)
        print(len(m),m)
#q12 : Try to filter out all the string data

for i in l:
    for j in i:
        if type(j)==str:
            print(j)
    for e in i:
        if type(i)==dict:
            if type(i[e])==str:
                print(i[e])
#q13 : Try to Find  out alphanum in data
for i in l:
    if type(i)==dict:
        for j in i.keys():
            if type(j)==str:
                print(j)
#q15 : Try to unwrape all the collection inside collection and create a flat list
m=[]
for i in l:

    for j in i:
        m.append(j)
    for e in i:
        if type(i)==dict:
            m.append(i[e])
print(m)

