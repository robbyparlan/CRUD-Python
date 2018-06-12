#!/usr/bin/python3

import pymysql
from module.connection import conn
import sys
import os
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

def banncreat():
	print ('''
%s[+]----Menu Create Python With MySQL----[+]
  %s[01] Create Record Table User
  [02] Create Record Table Barang
  [03] Back Menu
  [04] Exit
				'''% (merah,putih))

def tableuser():
	print("%s\t\t\t   TABEL USER" % (merah))
	print("%s +-------------------------------------------------------------+ " % (putih))
	nm	= input("%s  Masukan Nama 	 	: %s" % (nila,putih))
	usr	= input("%s  Masukan Username 	: %s" % (nila,putih))
	pswd= input("%s  Masukan Password 	: %s" % (nila,putih))
	print("%s +-------------------------------------------------------------+ " % (putih))
	with conn.cursor() as cursor:
		sql = "INSERT INTO user (`nama`, `username`, `password`) VALUES (%s, %s, %s)"
		try:
			cursor.execute(sql, (nm,usr,pswd))
			print('\n')
			print("%s  Sukses Menambahkan Nama     : %s%s" % (nila,putih,nm))
			print("%s  Sukses Menambahkan Username : %s%s" % (nila,putih,usr))
			print("%s  Sukses Menambahkan Password : %s%s" % (nila,putih,pswd))
		except pymysql.Error as e:
				print("Error here", e)


def tablebrg():
	print("%s\t\t\t   TABEL BARANG" % (merah))
	print("%s +-------------------------------------------------------------+ " % (putih))
	nm	= input("%s  Masukan Nama Barang : %s" % (kuning,putih))
	ktg	= input("%s  Masukan Kategori    : %s" % (kuning,putih))
	hrg = input("%s  Masukan Harga       : %sRp " % (kuning,putih))
	print("%s +-------------------------------------------------------------+ " % (putih))
	with conn.cursor() as cursor:
		sql = "INSERT INTO barang (`nama_barang`, `kategori`, `harga`) VALUES (%s, %s, %s)"
		try:
			cursor.execute(sql, (nm,ktg,hrg))
			print('\n')
			print("%s  Sukses Menambahkan Nama Barang : %s%s" % (kuning,putih,nm))
			print("%s  Sukses Menambahkan Kategori    : %s%s" % (kuning,putih,ktg))
			print("%s  Sukses Menambahkan Harga       : %sRp %s" % (kuning,putih,hrg))
		except pymysql.Error as e:
				print("Error here", e)


def create():
		print('''
%s[+]----Menu Create Python With MySQL----[+]
  %s[01] Create Record Table User
  [02] Create Record Table Barang
  [03] Back Menu
  [04] Exit
				'''% (merah,putih))
		while True:
			menu = input('%s Menu ([Create]) >> %s' % (merah,putih))
			sleep(0.100)
			if menu == '01' or menu == '1':
				os.system("clear")
				tableuser()
				banncreat()		
			elif menu == '02' or menu == '2':
				os.system("clear")
				tablebrg()
				banncreat()
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
		create()
	finally:
		conn.close()