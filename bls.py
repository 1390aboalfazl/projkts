from maudol import *
rane()
while True:
    lod = input('>>')
    if lod == '-help':
        n = input('name: ')
        helpp(n)
    elif lod == '-login':
        n = input('emal: ')
        login(n)
    elif lod == '-tstlogin':
        n = input('emal: ')
        testlogin(n)
    elif lod == '-fil -add':
        n = input('name: ')
        add_fili(n)
    elif lod == '-fil -data':
        n = input('name:')
        d = input('data:\n')
        add_data_f(n,d)
    elif lod == '-installmods':
        n = input('mods: ')
        install_mod(n)
    elif lod == '-patrick':
        n1 = input("f1: ")
        n2 = input("f2: ")
        n3 = input("f3: ")
        n4 = input("f4: ")
        patrik(n1,n2,n3,n4)
