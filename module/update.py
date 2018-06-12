#!/usr/bin/python3

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


def bannupdate():
	print ('''
%s[+]----Menu Create Python With MySQL----[+]
  %s[01] Create Record Table User
  [02] Create Record Table Barang
  [03] Back Menu
  [04] Exit
				'''% (merah,putih))


def ubahbrg():
	sys.path.append('module/')
	from read import tampil1
	tampil1()
	nomor = input('%s  Pilih id barang     : %s' % (ungu,putih))
	nm    = input('%s  Update Nama Barang  : %s' % (ungu,putih))
	ktg   = input('%s  Update Kategori     : %s' % (ungu,putih))
	hrg   = input('%s  Update Harga Barang : %sRp ' % (ungu,putih))
	with conn.cursor() as cursor:
			sql = "UPDATE barang SET `nama_barang`=%s, `kategori`=%s, `harga`=%s WHERE `id`=%s"
			try:
				cursor.execute(sql, (nm, ktg, hrg, nomor))
				print('\n')
				print("%s\t\t\t   TABEL BARANG" % (merah))
				print("%s +-------------------------------------------------------------+ " % (putih))
				print("%s  Sukses Update Nama Barang     : %s%s" % (ungu,putih,nm))
				print("%s  Sukses Update Kategori Barang : %s%s" % (ungu,putih,ktg))
				print("%s  Sukses Update Harga Barang    : %sRp %s" % (ungu,putih,hrg))
				print("%s +-------------------------------------------------------------+ " % (putih))
				print('\n')
			except pymysql.Error as e:
				print("Error here", e)

def ubahusr():
	sys.path.append('module/')
	from read import tampil
	tampil()
	nomor = input('%s  Pilih id user    : %s' % (ungu,putih))
	nm    = input('%s  Update Nama User : %s' % (ungu,putih))
	usr   = input('%s  Update Username  : %s' % (ungu,putih))
	pswd  = input('%s  Update Password  : %s' % (ungu,putih))
	with conn.cursor() as cursor:
		sql = "UPDATE user SET `nama`=%s, `username`=%s, `password`=%s WHERE `id`=%s"
		try:
			cursor.execute(sql, (nm, usr, pswd, nomor))
			print('\n')
			print("%s\t\t\t   TABEL USER" % (merah))
			print("%s +-------------------------------------------------------------+ " % (putih))
			print("%s  Sukses Update Nama     : %s%s" % (ungu,putih,nm))
			print("%s  Sukses Update Username : %s%s" % (ungu,putih,usr))
			print("%s  Sukses Update Password : %s%s" % (ungu,putih,pswd))
			print("%s +-------------------------------------------------------------+ " % (putih))
			print('\n')
		except pymysql.Error as e:
			print("Error here", e)


def update():
		print('''
%s[+]----Menu Update Python With MySQL----[+]
  %s[01] Update Record Table User
  [02] Update Record Table Barang
  [03] Back Menu
  [04] Exit
				'''% (merah,putih))
		while True:
			menu = input('%s Menu ([Update]) >> %s' % (merah,putih))
			sleep(0.100)
			if menu == '01' or menu == '1':
				os.system("clear")
				ubahusr()
				bannupdate()		
			elif menu == '02' or menu == '2':
				os.system("clear")
				ubahbrg()
				bannupdate()
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


if __name__=='__main__':
	try:
		update()
	finally:
		conn.close()