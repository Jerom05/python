def brchecker(s):
    list=[]
    matchList=[]
    j=1
    for i in range(len(s)):
        if s[i]=="(":
            list.append(s[i])
        if s[i]==")" and s[i-j]=="(":
            matchList.append(i)
            matchList.append(i-j)
            j=j+2
    print(matchList)
brchecker(s="(())")