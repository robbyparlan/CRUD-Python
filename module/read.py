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


def bannread():
	print('''
%s[+]----Menu Read Python With MySQL----[+]
  %s[01] Read Record Table User
  [02] Read Record Table Barang
  [03] Back Menu
  [04] Exit
				'''% (merah,putih))

def tampil():
	with conn.cursor() as cursor:
		sql = "SELECT `id`, `nama`, `username`, `password` FROM user"
		try:
			cursor.execute(sql)
			result = cursor.fetchall()
			print("%s\t\t\t   TABEL USER" % (merah))
			print("%s +-------------------------------------------------------------+ " % (putih))
			print("%s |  Id_user\t| Nama\t\t| Username\t| Password     |" %(putih))
			print("%s +-------------------------------------------------------------+ " % (putih))
			for row in result:
				print("       "+str(row[0]) + "\t" + row[1] + "\t\t" + row[2] + "\t        " + row[3])
			print("%s +-------------------------------------------------------------+ " % (putih))
		except pymysql.Error as e:
			print("Oops! Something Wrong", e)

def tampil1():
	with conn.cursor() as cursor:
		sql = "SELECT `id`, `nama_barang`, `kategori`, `harga` FROM barang"
		try:
			cursor.execute(sql)
			result = cursor.fetchall()
			print("%s\t\t\t   TABEL BARANG" % (merah))
			print("%s +-------------------------------------------------------------+ " % (putih))
			print("%s |  Id_brg\t| Nama Barang\t| Kategori\t| Harga        |" %(putih))
			print("%s +-------------------------------------------------------------+ " % (putih))
			for row in result:
				print("       "+str(row[0]) + "\t" + row[1] + "\t\t" + row[2] + "\tRp " + str(row[3]))
			print("%s +-------------------------------------------------------------+ " % (putih))
		except pymysql.Error as e:
			print("Oops! Something Wrong", e)


def read():
	print('''
%s[+]----Menu Read Python With MySQL----[+]
  %s[01] Read Record Table User
  [02] Read Record Table Barang
  [03] Back Menu
  [04] Exit
				'''% (merah,putih))
	while True:
			menu = input('%s Menu ([Read]) >> %s' % (merah,putih))
			sleep(0.100)
			if menu == '01' or menu == '1':
				os.system("clear")
				tampil()
				bannread()		
			elif menu == '02' or menu == '2':
				os.system("clear")
				tampil1()
				bannread()
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

if __name__ == '__main__':
	try:
		read()
	finally:
		conn.close()
