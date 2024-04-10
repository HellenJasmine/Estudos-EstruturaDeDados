def printRev(n):
    if n<=10:
      return n *2
    else:
       return printRev(printRev(n/3))

if __name__ == "__main__":
    fac = printRev(27)
    print(fac)