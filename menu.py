from core.banner import bann
from module.create import * 
from module.read import *
from module.update import *
from module.delete import *
import sys, os, time


merah='\033[1;31m'
putih='\033[1;37m'

def menu():
	print('''
%s[+]----Menu CRUD Python With MySQL----[+]

  [01] Create Record Table
  [02] Read Record Table
  [03] Update Record Table
  [04] Delete Record Table
  [05] Credit
  [00] Exit
		''' % (putih))
	menu = input('%s Menu ([None]) >> %s' % (merah,putih))
	if menu == '01' or menu == '1':
		os.system("clear")
		create()
	elif menu == '02' or menu == '2':
		os.system("clear")
		read()
	elif menu == '03' or menu == '3':
		os.system("clear")
		update()
	elif menu == '04' or menu == '4':
		os.system("clear")
		delete()
	else:
		sys.exit(2)


if __name__ == '__main__':
	bann()
	time.sleep(3)
	os.system("clear")
	menu()