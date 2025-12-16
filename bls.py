from maudol import *
rane()
while True:
    lod = input('>>')
    if lod == '-help':
        n = input('name: ')
        helpp(n)
    elif lod == '-login':
        e = input('emal: ')
        login(e)
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
    elif lod == '-blo print':
        mol = input(':')
        blo_print(mol)
    elif lod == '-blo -add':
        n = input('name: ')
        d = input('data:')
        blo_add(n,d)
    elif lod == '-user -remov':
        remov_user()
    elif lod == '-user -remov':
        n = input('newu emal: ')
        relod_user(n)
    elif lod == '-user -passvord -add':
        n = input('pasvord: ')
        add_pasvord(n)