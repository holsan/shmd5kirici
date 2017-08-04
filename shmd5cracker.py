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
        os.system("clear")
        print(" ➲ ➲ ➲ Savunan Hacker Tarafından Kodlanmıştır. \n ➲ ➲ ➲ Versiyon : 1.0 \n ➲ ➲ ➲ MD5 Online , Brute Force Attack \n ")
        print "1 ➲ MD5 Kırıcı"
        print "2 ➲ Hakkında"
        print "3 ➲ Çıkış \n"
        sec = input("İşlem Seçiniz :")

        if sec == 1:
                kirici()
        elif sec == 2:
            print("\n ➲ TürkHackTeam İçin Kodlanmıştır. \n ➲ Coded By Savunan Hacker \n")
            menudon=raw_input("Menüye Dönmek İçin [Enter]'a Basınız.")
            menu()
        elif sec == 3:
            print("\n Çıkış Yaptınız..\n")
            sys.exit()

def kirici():
        os.system("clear")
        print "\n 1 ➲ MD5 Online Kırıcı\n"
        print "\n 2 ➲ MD5 Brute Force \n"
        sec = input("\n İşlem Seçiniz :")

        if sec == 1:
                onlinekirici()
        elif sec == 2:
                bruteforce()

def onlinekirici():
        os.system("clear")
        string=raw_input("\n MD5 Şifrenizi Yazınız : ")
        site = 'http://md5decryption.com/'
        sitecek = urllib.urlencode({'hash':string,'submit':'Decrypt+It!'})
        req = urllib2.Request(site)
        try:
          veri = urllib2.urlopen(req, sitecek)
          data = veri.read()
          match = re.search(r'(Decrypted Text: </b>)(.+[^>])(</font><br/><center>)', data)
          if match: print '\n ➲ Şifrenin Kırıldığı Site : %s \n ➲ Şifre : %s \n' % (site,match.group(2))
          else: print ' \n ➲ Şifrenin Kırılamadığı Site : %s \n ➲ Şifre : Bulunamadı !\n' % site
        except urllib2.URLError: print ' ➲ Site : %s \t\t\t ➲ Çökmüş Olabilir !' % site
        raw_input("\n Menüye Dönmek İçin [Enter]'a Basınız.")
        menu()


def bruteforce():
        os.system("clear")
        counter = 0
        lines = 0
        string=raw_input("\n MD5 Şifrenizi Yazınız : ")
        wordList = raw_input("\n Wordlist Seçiniz : ")
        try:
                wordlistfile = open(wordList)
                for line in open(wordList):
                        lines += 1
        except IoError:
                print'Geçersiz Wordlist !'
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
                os.system("clear")
                print(percentage)
                if wordlistdecrypted == string:
                        print'\n ➲ Şifre Kırıldı ! - %s' % line
                        menudon = raw_input("\nMenüye Dönmek İçin [Enter]'a Basınız.")
                        menu()
menu()
