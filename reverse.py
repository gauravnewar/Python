def Arrange(b):
    actualBinary = []

    for i in range(len(b)-1,-1,-1) :
        actualBinary.append(b[i])
        
    return actualBinary

def GetStr(b):
    actualBinaryNum = ""

    for i in range(len(b)-1,-1,-1) :
        actualBinaryNum = actualBinaryNum + str(b[i])
        
    return actualBinaryNum
