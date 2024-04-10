def somatorio(numero):
    if numero == 1:
        return 1
    else:
        return numero + somatorio(numero - 1)

if __name__=="__main__":
    s = somatorio(5)
    print(s)