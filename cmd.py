

def comand(list):

    with open('cmdlist', 'r') as f:
        clist = f.read().split("\n") 

    for c in clist:

        if c in list:
            list2 = list.find(c)
            #print(list)
            list3 = list[:list2]
            print(list3 + c)
            return list3 + c

