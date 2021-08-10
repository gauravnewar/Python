import numvalidation
import decimaltobinary
import reverse
import binaryaddition

run = "yes"

while(run=="yes"):
    result = numvalidation.Entry()
    d1 = result[0]
    d2 = result[1]

    c1 = decimaltobinary.Conversion(d1)
    c2 = decimaltobinary.Conversion(d2)

    b1 = reverse.Arrange(c1)
    b2 = reverse.Arrange(c2)

    print("\n")
    print("The binary conversion of",d1,"is",b1)
    print("The binary conversion of",d2,"is",b2)
    print("\n")

    sum = binaryaddition.Add(b1,b2)

    if not type(sum) is str:
        sum = reverse.GetStr(sum)

    print("The required sum is ",sum)
    print("\n")

    print("Do you want to continue the program to add next two numbers.")
    run = input("Answer the question in yes or no : ").lower()
if(run=="no"):
    print("Thank you")
    
