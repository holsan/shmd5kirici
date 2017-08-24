#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib
import sys
import os
import time
import urllib2
import urllib
import re

def menu():
	print """


███████╗██╗  ██╗
██╔════╝██║  ██║
███████╗███████║
╚════██║██╔══██║
███████║██║  ██║
╚══════╝╚═╝  ╚═╝       [*] MD5 Şifre Kırıcı
                       [*] Kodlayan : SavunanHacker
                       [*] Versiyon 1.0                           
                 
"""
        print "[1] Online"
        print "[2] Brute Force"
        print "[3] Çıkış \n"
        sec = input("@sh> ")

        if sec == 1:
                onlinekirici()
        elif sec == 2:
            bruteforce()
        elif sec == 3:
        	print "\n\t[-] Çıkış Yaptınız..\n"
        	sys.exit()
def onlinekirici():
        string=raw_input("\n @md5şifre> ")
        site = 'http://md5decryption.com/'
        sitecek = urllib.urlencode({'hash':string,'submit':'Decrypt+It!'})
        req = urllib2.Request(site)
        try:
          veri = urllib2.urlopen(req, sitecek)
          data = veri.read()
          match = re.search(r'(Decrypted Text: </b>)(.+[^>])(</font><br/><center>)', data)
          if match: 
          	print '\n [+] Şifre : %s' % (match.group(2))
          else: 
          	print '\n [-] Şifre : Bulunamadı !\n'
        except urllib2.URLError: print '\t[-] Site Çökmüş Olabilir !' % site
        raw_input("\n Menüye Dönmek İçin [Enter]'a Basınız.")
        menu()


def bruteforce():
        counter = 0
        lines = 0
        string=raw_input("\n @md5şifre> ")
        wordList = raw_input("\n @wordlist> ")
        try:
                wordlistfile = open(wordList)
                for line in open(wordList):
                        lines += 1
        except IoError:
                print "[-] Geçersiz Wordlist !"
                raw_input("\n Menüye Dönmek İçin [Enter]'a Basınız.")
                menu()
        else:
                pass
        for line in wordlistfile:
                algorithim = hashlib.md5()
                line = line.replace("\n","")
                algorithim.update(line)
                wordlistdecrypted = algorithim.hexdigest()
                counter += 1
                percentage_raw = float(counter) / float(lines) * 100
                percentage_raw ="%0f" % percentage_raw; percentage = str(percentage_raw) + " " + "%"
                print(percentage)
                if wordlistdecrypted == string:
                        print'\n [+] Şifre Kırıldı : %s' % line
                        menudon = raw_input("\nMenüye Dönmek İçin [Enter]'a Basınız.")
                        menu()
if __name__ == "__main__":
	try:
		menu()
	except KeyboardInterrupt as err:
		print "\n\t[-] Çıkış Yaptınız.."
		sys.exit(0)

menu()
