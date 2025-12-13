from mymaudol import *
from os import *

def rane():
    print('hi wilcom to bls trmenal help is --helpp')

def helpp(name):
    print(name+' is login --logi is test login --testlogi')

def login(emal):
    iglo = open('devisesclonlogin.iur','a')
    iglo.write(emal)

def testlogin(emal):
    iglo = open('devisesclonlogin.iur','r')
    a=iglo.readline()
    if a == emal:
        print('on login')
    else:
        print('not login')

def add_fili(name_file_adres):
    iglo = open(name_file_adres,'a')

def add_data_f(name,data):
    iglo = open(name,'w')
    iglo.write(data)

def defalt_mode():
    moding = 'ifo'
    
def install_mod(name_mode):
    install_addvans(name_mode)