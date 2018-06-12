import os, sys
from time import *


putih='\033[1;37m'
wb = '\033[36m'
merah='\033[1;31m'

def banncredit():
	print('''%s
    ______ ______  _     _ _____   
   / _____|_____ \| |   | (____ \  
  | /      _____) ) |   | |_   \ \ 
  | |     (_____ (| |   | | |   | |
  | \_____      | | |___| | |__/ / 
   \______)     |_|\______|_____/  
  %s
  [+] Author      : Ruitze
  [+] Tool        : CRUD v.01
  [+] Description : CRUD Python with MySQL
  [+] Usage       : python menu.py                                
	''' % (wb,putih))

def credit():
  banncredit()
  print('''
%s[+]----Menu Read Python With MySQL----[+]
  %s[01] Back Menu
  [02] Exit
        '''% (merah,putih))
  while True:
      menu = input('%s Menu ([Credit]) >> %s' % (merah,putih))
      sleep(0.100)
      if menu == '01' or menu == '1':
        os.system("clear")
        sys.path.append('./')
        from menu import menu
        menu()
      elif menu == '02' or menu == '2':
        os.system("clear")
        sys.exit(2)
      else:
        print(' Input Error %s' % (menu))

if __name__ == '__main__':
    credit()