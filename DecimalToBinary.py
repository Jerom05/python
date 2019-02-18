from stack import Stack

def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.is_empty():
        binString = binString + str(remstack.pop())

    return binString

print(divideBy2(42))