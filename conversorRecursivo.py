def main():
    import sys
    n = int(input("Type a decimal number to be converted: "))
    n1 = n
    num = []
    c = convert(n,n1,num)
    p = prt(c)
    print(p)
    print("\n")
    sair = str(input("1 To stop\nAny key To conitnue\n"))
    print("\n")
    if sair == "1":
        sys.exit()
    main()
def convert(n,n1,num):
    if n != 0:
        n1 = n
        n1 = n%2
        num.append(n1)
        n = n //2
        if n == 0:
            return num
        return convert(n,n1,num)
def prt(c):
    a=""
    for x in range (len(c)-1,-1,-1):
        a = a + str(c[x])
    return a
main()

