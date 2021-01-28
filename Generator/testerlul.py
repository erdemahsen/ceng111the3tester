from generator import *
from the3 import *
import random
import ast
#This python file :
#1-Creates partlist.txt (by iterating generator.py's "generate_part_list()" function)
#2-Creates stocklist.txt by first calculating a random stock value (check line 35)
#3-Creates answers.txt according to the3.py that is in the same directory with testerlul.py
K=12000
def aglatan(K):
    calcpricefile=open("partlists.txt","w+")
    for i in range(K):
        na=generate_part_list()
        if len(na)>1:
            calcpricefile.write(str(na))
            if i!=K-1:
                calcpricefile.write("---")
    calcpricefile.close()

aglatan(K)  # call aglatan to change partlists :)
calcpricelul = open("partlists.txt", "r+")
calcpricelul=calcpricelul.readlines()
calcpricelul=calcpricelul[0]
calcpricelul=calcpricelul.split("---")
new=[]
for element in calcpricelul:
    new += [eval(element)]

constant=0
answer=open("answers.txt","w+")
answer.close()
stocklisttxt=open("stocklists.txt","w+")
stocklisttxt.close()
for partlistee in new:
    answer=open("answers.txt","a+")
    answertemp=[]
    answertemp.append(calculate_price(partlistee))
    requiredkappa=required_parts(partlistee)
    answertemp.append(requiredkappa)
    stockliste=[]
    print(requiredkappa)
    for element in requiredkappa:
        stockrandom=random.choices(["donttouch","pop","decrease"],[8,1,3])
        if stockrandom==["donttouch"]:
            stockliste.append(element)
        elif stockrandom==["decrease"]:
            number,name=element
            if int(number)>1:
                aponumber=random.randrange(1, int(number))
                stockliste.append((aponumber,name))
            else:
                stockliste.append(element)
    answertemp.append(stock_check(partlistee,stockliste))
    answer.write(str(answertemp))
    print(answertemp)
    if constant< len(new)-1:
        answer.write("---")
    stocklisttxt=open("stocklists.txt","a+")
    stocklisttxt.write(str(stockliste))
    if constant< len(new)-1:
        stocklisttxt.write("---")
    constant+=1
answer.close()
stocklisttxt.close()



