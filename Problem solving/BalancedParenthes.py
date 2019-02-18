def parchecker(string):
    index=0
    balanced = True
    list=[]
    while index < len(string) and balanced:
        if string[index]=="(":
           list.append(string[index])
        elif string[index]==")":
                list.pop()
        elif string == []:
             balanced = False
        index = index+1
        print (balanced, index)
    if balanced and list==[]:
        print(balanced, 0)
        return True
    else:
        print(balanced, "01")
        return False
print(parchecker("()"))
