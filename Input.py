# Write  a Python Program that accepts an integer(n) and computes the value of n+ nn +nnn.
n=int(input("Enter any Integer Value:"))
n1=int("%s"%n)
n2=int("%s%s"%(n,n))
n3=int("%s%s%s"%(n,n,n))
print("Required Value is:",n1+n2+n3)
