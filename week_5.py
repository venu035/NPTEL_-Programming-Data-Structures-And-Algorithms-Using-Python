#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Books=[]
Borrowers=[]
Checkouts=[]
x=input()
while x!='Borrowers':
    s=x.split('~')
    Books.append(s)
    x=input()
x=input()
while x!='Checkouts':
    s=x.split('~')
    Borrowers.append(s)
    x=input()
x=input()
while x!='EndOfInput':
    s=x.split('~')
    Checkouts.append(s)
    x=input()

FullName=[]
Title=[]
AccNum=[]
for i in range(len(Checkouts)):
    for j in range(len(Borrowers)):
        if Checkouts[i][0]==Borrowers[j][0]:
            FullName.append(Borrowers[j][1])
    for j in range(len(Books)):
        if Checkouts[i][1]==Books[j][0]:
            AccNum.append(Books[j][0])
            Title.append(Books[j][1])
output=[]
for i in range(len(Checkouts)):
    text=Checkouts[i][2]+'~'+FullName[i]+'~'+AccNum[i]+'~'+Title[i]
    output.append(text)
output.sort()
for i in output:
    print(i)

