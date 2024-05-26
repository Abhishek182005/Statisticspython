from statistics import *
L=[]
M=[]
N=[]
def dataentry():
    A=int(input("Enter the number of entries="))
    for i in range(A):
        c=int(input("Enter the numbers(Type 00 for stringtype) ="))
        if c==00:
            c=input("Enter the string=")
        print("_"*100)
        L.append(c)
    sorter(L)
def sorter(L):
    for i in L:
        if type(i)==int:
            M.append(i)
        else:
            N.append(i)
    print("THE ENTERED LIST IS", L)
    print("THE NUMBER LIST IS", M)
    print("THE STRING LIST IS",N)
    print("_" * 100)
    input()
    Menu()
def mean1():
    A=mean(M)
    I=harmonic_mean(M)
    print("The mean of")
    for i in M:
        print(i, end=" ")
    print("is", A)
    print("The Harmonic mean is", I)
    input()
    Menu()
def mode1():
    B=mode(M)
    C=mode(N)
    if N!='':
        print("The mode of")
        for i in M:
            print(i, end=" ")
        print("is", B)
        print("The mode of")
        for i in N:
            print(i, end=" ")
        print("is", C)
    else:
        print("The mode of")
        for i in M:
            print(i, end=" ")
        print("is", B)
    print("_" * 100)
    input()
    Menu()
def median1():
    D=median(M)
    E =median_high(M)
    F= median_low(M)
    print("The median of")
    for i in M:
        print(i, end=" ")
    print("is", D)
    print("The high median is", E)
    print("The low median is", F)
    print("_" * 100)
    input()
    Menu()
def deviationandvariance():
    G=stdev(M)
    H=variance(M)
    print("The deviation of")
    for i in M:
        print(i, end=" ")
    print("is", G)
    print("The variance is", H)
    print("_" * 100)
    input()
    Menu()
def meanmodemedian():
    X=mean(M)
    Y=median(M)
    Z1=mode(M)
    for i in M:
        print(i, end=" ")
    print("The Mean is", X)
    print("The Median is", X)
    print("The Mode(num) is", Z1)
    print("_" * 100)
    input()
    Menu()
def deletion():
    del L
    del M
    del N
    print("DELETION SUCCESSFUL")
    print("_" * 100)
    input()
    Menu()
def Menu():
    while True:
        print("press 0 for adding data")
        print("press 1 for mean and harmonic mean")
        print("press 2 for mode ")
        print("press 3 for median ")
        print("press 4 for devation and variance")
        print("press 5 for mean, mode, median")
        print("press 6 for deletion")
        print("press 7 for leave")
        ch=int(input("Enter the choice="))
        if ch==0:
            dataentry()
        elif ch==1:
            mean1()
        elif ch == 2:
            mode1()
        elif ch == 3:
            median1()
        elif ch==4:
            deviationandvariance()
        elif ch==5:
            meanmodemedian()
        elif ch==6:
            deletion()
        elif ch==7:
            print("Thanks for using")
            break
        else:
            print("Invalid choice")
Menu()

































