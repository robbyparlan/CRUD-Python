import pymysql
from module.connection import conn
import os, sys
from time import *

rampung='\033[0m'
hitam='\033[1;30m'
merah='\033[1;31m'
ijo='\033[1;32m'
kuning='\033[1;33m'
biru='\033[1;34m'
ungu='\033[1;35m' 
nila='\033[1;36m'
putih='\033[1;37m'


def banndelete():
	print ('''
%s[+]----Menu Delete Python With MySQL----[+]
  %s[01] Delete Record Table User
  [02] Delete Record Table Barang
  [03] Back Menu
  [04] Exit
				'''% (merah,putih))

def delete_user():
	sys.path.append('module/')
	from read import tampil
	tampil()
	nomor = input('%s  Pilih id user     : %s' % (ungu,putih))
	with conn.cursor() as cursor:
			sql = "DELETE FROM user WHERE `id` =%s"
			try:
				cursor.execute(sql, (nomor))
				print('\n')
				print('\t\t%sSukses Menghapus DATA %sTabel User' % (putih,kuning))
				print('\n')
				tampil()
			except pymysql.Error as e:
				print("Error here", e)	

def delete_barang():
	sys.path.append('module/')
	from read import tampil1
	tampil1()
	nomor = input('%s  Pilih id barang     : %s' % (ungu,putih))
	with conn.cursor() as cursor:
			sql = "DELETE FROM barang WHERE `id` =%s"
			try:
				cursor.execute(sql, (nomor))
				print('\n')
				print('\t\t%sSukses Menghapus DATA %sTabel Barang' % (putih,kuning))
				print('\n')
				tampil1()
			except pymysql.Error as e:
				print("Error here", e)	

def delete():
		print('''
%s[+]----Menu Delete Python With MySQL----[+]
  %s[01] Delete Record Table User
  [02] Delete Record Table Barang
  [03] Back Menu
  [04] Exit
				'''% (merah,putih))
		while True:
			menu = input('%s Menu ([Delete]) >> %s' % (merah,putih))
			sleep(0.100)
			if menu == '01' or menu == '1':
				os.system("clear")
				delete_user()
				banndelete()		
			elif menu == '02' or menu == '2':
				os.system("clear")
				delete_barang()
				banndelete()
			elif menu == '03' or menu == '3':
				os.system("clear")
				sys.path.append('./')
				from menu import menu
				menu()
			elif menu == '04' or menu == '4':
				os.system("clear")
				sys.exit(2)
			else:
				print(' Input Error %s' % (menu))
		
			conn.commit()

if __name__ == '__main__':
	try:
		delete()
	finally:
		conn.close()