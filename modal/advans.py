def patrec(pro1,pro2,pro3,pro4):
    pro1=pro1
    pro2=pro2
    pro3=pro3
    pro4=pro4
    open(pro1,'a').write('glo1:\n')
    open(pro2,'a').write('glo2:\n')
    open(pro3,'a').write('glo3:\n')
    open(pro4,'a').write('glo4:\n')
    w = input('wris add data host[y/n]?')
    if w=='y':
        data = input('data:\n')
        e = input('watis fil: ')
        if e==pro1:
            open(e,'a').write(data)
        elif e==pro2:
            open(e,'a').write(data)
        elif e==pro3:
            open(e,'a').write(data)
        elif e==pro4:
            open(e,'a').write(data)
        elif e=='':
            open(pro1,'a').write(data)
            open(pro2,'a').write(data)
            open(pro3,'a').write(data)
            open(pro4,'a').write(data)
    else:
        print('ok')

def textors(name_adrs):
    iglo = open(name_adrs,'r')
    lop = iglo.read
    print(lop)
    while True:
        lo = input(': ')
        if lo == '-radd':
            iglo = open(name_adrs,'w')
            text = input('txt:\n')
            iglo.write(text)
        elif lo == '-add':
            iglo = open(name_adrs,'a')
            text = input('txt:\n')
            iglo.write(text)
        elif lo == '-r':
            iglo = open(name_adrs,'w')
            iglo.write('')
        elif lo == 'exit':
            break
        else:
            print('not fond')