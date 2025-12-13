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
    elif lod == 'exit':
        break