import random


def generate_part_list():
    sourcelist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y", "z"]
    # sourcelist --> list which we are going to use to generate children,root or parents
    biglistlul = []
    maxprice = 150  # you can change this as you wish
    minprice = 0.5
    maxamount = 25  # you can change this as you wish
    minamount = 1
    N = 15  # Total different root,parent or child
    rate = [1,
            4]  # weight [leaf,parent] --> you can change this value but it may still not cause a big difference at trees' depth.(Still I don't recommed pushing limits tho)
    # I couldn't implement parent-child thing well as a result of this there are parents who has no childs :(
    # To compensate this those kind of parents are converted to childs.(Check last loops)
    for i in range(N):
        length = random.randrange(2,
                                  10)  # length of string you can change upper value as you wish. But I dont recommend doing min value under 2
        string = ""  # Due to my implementation I guess 1 was causing some troubles. It might work not sure.
        for j in range(length):
            choose = random.choices(sourcelist)
            string += choose[0]
        biglistlul += [string]
    biglistlul = list(set(biglistlul))  # We do not want any child to become grandparent of him/herself.
    lul = []
    root = random.choices(biglistlul)
    roots = [root]
    biglistlul.remove(root[0])
    while biglistlul and roots:
        apo = random.randrange(1, len(biglistlul))
        apo2 = int((apo / len(biglistlul)) ** 2 * len(biglistlul))
        root1 = roots.pop()
        temp = []
        temp += root1
        for kappa in range(apo2):
            place = random.randrange(0, len(biglistlul) - 1)
            chosen = biglistlul.pop(place)
            leaforparent = random.choices(["leaf", "parent"], rate)
            amount = random.randrange(minamount, maxamount)
            if leaforparent == ["parent"]:
                temp += [(amount, chosen)]
                if len(biglistlul) != 0:
                    roots += [[str(chosen)]]
                else:
                    leaforparent == ["leaf"]
            if leaforparent == ["leaf"]:
                price = random.uniform(minprice, maxprice)
                price = float(round(price, 1))
                temp += [(amount, chosen)]
                lul += [[chosen, price]]

        lul += [temp]
    i = len(lul) - 1
    while 0 <= i:  # If a parent has no child it becomes a child itself.
        kappa = lul.pop(i)
        if type(kappa[0]) == str and len(kappa) == 1:
            price = random.uniform(minprice, maxprice)
            price = float(round(price, 1))
            ele = [kappa, price]
            lul.append(ele)
        else:
            lul.append(kappa)
            i = i - 1
    i = 0

    def flatten(l):
        for i in l:
            if type(i) == list:
                flatten(i)
            else:
                output.append(i)

    lulnew = []
    while i < len(lul):
        output = []
        flatten(lul[i])
        lulnew += [output]
        i += 1
    lul = lulnew
    # At the last part I am trying to get rid of wrong, extra brackets .
    return lul
# print(generate_part_list())


