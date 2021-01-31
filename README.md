## CENG111 THE 3 Tester
# How to use it?

1- Download CENG111-THE3 Tester  
2- Put your the3.py file in to "CENG111-THE3 Tester" folder.  
3- Run tester.py  
4- If you are testing Case4, it takes time so do not panic :).  
5- Check failedcases.txt   
6- Check optional to test your code with more cases. (If you do not touch to anything you will only use Cases1)
#
Optional- If you want to try your tester with other cases choose a folder "CasesN(memberK-testnumberL)". Copy everything inside of that "CasesN(memberK-testnumberL)" to CENG111-THE3 Tester. By doing that you can try your code with bigger trees(partlists) which is something I strongly recommend.
#
Note- Default answer.txt, partlist.txt stocklists.txt are set to "Cases1(member50-testnumber842)"

# Attention:

1-This is just a tester based on my answers to the trees that I generated. Getting %100 from this tester does not mean you are going to get %100 from THE3 and vice versa.  
2-Answers were generated by my the3.py code. So if you think your code is correct but you still do not get %100 let me know .  
3-My tree generator algorithm is not that great. I could not come up with a solution that generates extreme trees. To compensate this I generated bigger trees which have higher chance of being deeper. Being child, parent or root everything is random.(If you are interested check "Generator" folder)  
4-Calculate_price function has an error rate. You can change it :tester.py line 57. You can change it or add round(this one caused some trouble for big numbers so I did not use it.).

# How to generate your own test cases ?

You can use files in "Generator" folder to generate your own "answers.txt","partlists.txt","stocklists.txt".

1-First take files in "Generator" folder to the part where your the3.py stays.  
2-Now you can make changes in "testerlul.py" and "generator.py".  
3-In "generator.py" "N" is the most important variable. This decides how long will the part list be.   
4-In "testerlul.py" "K" is the most important variable. This decides how many trees(partlists) will be generated.  
5-You can inspect and change most of the variables (some of them have explanations) .   
6-Now run "testerlul.py". This will generate your own "answers.txt","partlists.txt","stocklists.txt".  
Sidenote: there should be 3 empty txt files created by you before running testerlul.py (answers.txt partlists.txt stocklists.txt).  
7-You can share these files with someone and tell them to run their tester.py  

# This might be the problem !

1-Since there are 5 different answers.txt, partlists.txt, stocklists.txt this may cause tester to call wrong answer.txt etc. To avoid this you can try changing the names of the text files that you are not using to sth else.  
2-If you want to try a test case make sure you copied everything in that folder (like CasesX(Ymember-Ztest)) and pasted these txt files to the3ceng111tester folder.  
3-SinglePart1 and SinglePart2 contains partlists like "[['ntuevt', 115.7]]". These two test cases may cause some problems.  
4-You can try changing line 57 "if oran>1.0001 or oran<0.9999:" to sth like "if oran>1.1 or oran<0.9:".

#Ömer Erdem Ahsen









