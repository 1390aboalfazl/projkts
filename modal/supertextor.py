#yor app
def textors(name_adrs=str):
    iglo = open(name_adrs,'r')
    print(iglo.readline())
    while True:
        lo = input(': ')
        if lo == '-r -add':
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
        elif lo == '-newo':
            n = input('name: ')
            open(n,'x')
        elif lo == '-ock':
                pro1=input(':')
                pro2=input(':')
                pro3=input(':')
                pro4=input(':')
                open(pro1,'a').write('glo1:\n')
                open(pro2,'a').write('glo2:\n')
                open(pro3,'a').write('glo3:\n')
                open(pro4,'a').write('glo4:\n')
                w = input('wris add data host[y/n]?')
                if w=='y':
                    data = input('data:\n')
                    open(pro1,'a').write(data)
                    open(pro2,'a').write(data)
                    open(pro3,'a').write(data)
                    open(pro4,'a').write(data)