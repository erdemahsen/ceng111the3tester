from the3 import *
import random
import ast
failed=open("failedcases.txt","w+")
failed.close()
myans = open("answers.txt", "r+")
myans =myans.readlines()
myans =myans[0]
myans =myans.split("---")
myanslist=[]
myans.pop(len(myans)-1)
for element in myans:
    myanslist += [ast.literal_eval(element)]
plists = open("partlists.txt", "r+")
plists=plists.readlines()
plists=plists[0]
plists=plists.split("---")
plist=[]
plists.pop(len(plists)-1)
for element in plists:
    plist += [ast.literal_eval(element)]
slists = open("stocklists.txt", "r+")
slists=slists.readlines()
slists=slists[0]
slists=slists.split("---")
slist=[]
slists.pop(len(slist)-1)
for element in slists:
    slist += [ast.literal_eval(element)]
n=len(plist)
ind=0
total=len(plist)
errors=0
while ind<len(plist):
    temp1=myans[ind]
    pl=plist[ind]
    sl=slist[ind]
    error=0
    price=calculate_price(pl)
    req=required_parts(pl)
    stock=stock_check(pl,sl)
    yourans=[price,req,stock]
    temp=[]
    temp2 = [ast.literal_eval(temp1)]
    temp=[temp2[0]]
    for element in temp2[1:]:
        temp += [ast.literal_eval(element[1:len(element)-1])]
    temp=temp[0]
    for i in range(1,3):
        temp[i]=set(temp[i])
        yourans[i]=set(yourans[i])
    if yourans!=temp:
        error=1
    if error==1:
        print("Test Case",ind+1,": False")
        failed=open("failedcases.txt","a+")
        testnumber=str(ind+1)
        failed.write("Test Case "+testnumber+":\n ")
        failed.write("Your answer: "+str(yourans)+"\n")
        failed.write("Answer :"+str(temp)+"\n")
        failed.write("Part_list used: \n"+str(pl)+"\n")
        failed.write("Stock_list used: \n"+str(sl)+"\n\n")
        failed.close()
        errors+=1
    if error==0:
        print("Test Case",ind+1,": True")
    ind+=1
print("%",(total-errors)/total*100)
input()
