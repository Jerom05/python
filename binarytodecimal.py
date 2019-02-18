def decimalToBinary(BinaryNum):
    list=[]
    rlist=[]
    s=""
    index =0
    num =BinaryNum
    while num > 0:
        binary =num%2
        num= num//2
        print(binary)
        list.append(binary) 
        s=s+str(list.pop())
    ss = s[::-1]
    print(ss)
decimalToBinary(233)
