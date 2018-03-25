import sys
import os
import requests
def main():
    try:
        os.system("clear")
    except:
        os.system("cls")
    print("""
 \033[33m___  ___   _______   ___________      _______  _______   ______\033[33m
\033[33m|   \/   | |       \ |           |    /       ||   ____| /      |\033[33m
\033[33m|  \  /  | |  .--.  |`---|  |----`   |   (----`|  |__   |  ,----'\033[33m
\033[33m|  |\/|  | |  |  |  |    |  |         \   \    |   __|  |  | \033[33m    
\033[33m|  |  |  | |  '--'  |    |  |     .----)   |   |  |____ |  `----.\033[33m
\033[33m|__|  |__| |_______/     |__|     |_______/    |_______| \______|\033[33m

    
\033[37mCoded By\033[37m \033[31mCo0dxZ\n\033[0;0m 
\033[31mMindset Security - \033[0; 0m \033[37mhttps://mindsetsecurity.wordpress.com/\033[37m
          
    
\033[31mmdtsec.py 192.168.0.1 traceroute\033[31m
\033[31mmdtsec.py 192.168.0.1 ip_geo\033[31m
\033[31mmmdtsec.py 192.168.0.1 rev_ip\033[31m
\033[31mmdtsec.py 192.168.0.1 href\033[31m
\033[31mmdtsec.py target.com page_links\033[31m
\033[31mmdtsec.py 192.168.0.1 ps\033[31m
\033[31mmdtsec.py 192.168.0.1 dns_search\033[31m 
          
          
          
          
          """)
main()

if len(sys.argv) <3:
    print()
    sys.exit(0)

ip = sys.argv[1]
module = sys.argv[2]

def ps():
    os.system("nmap -v" +ip)

def ip_geo():
    web = "http://api.hackertarget.com/geoip/?q="+ip
    print("""\033[31mIP==>\033[31m[{}]""".format(ip))
    get = requests.get(web)
    print(get.text)

def page_links():
    web = "https://api.hackertarget.com/pagelinks/?q="+ip
    print("""\033[31mIP==>\033[31m[{}]""".format(ip))
    get = requests.get(web)
    print(get.text)
def rev_ip():
    web = "http://api.hackertarget.com/reverseiplookup/?q="+ip
    print("""\033[31mIP==>\033[31m[{}]""".format(ip))
    get = requests.get(web)
    print(get.text)

def href():
    web = "http//api.hackertarget.com/pagelinks/?q="+ip
    print("""\033[31mIP==>\033[31m[{}]""".format(ip))
    get = requests.get(web)
    print(get.text)

def traceroute():
    web = "http://api.hackertarget.com/mtr/?q="+ip
    print("""\033[31mIP==>\033[31m[{}]""".format(ip))
    get = requests.get(web)
    print(get.text)
def dns_search():
    web = "https://api.hackertarget.com/hostsearch/?q="+ip
    print("""\033[31mIP==>\033[31m[{}]""".format(ip))
    get = requests.get(web)
    print(get.text)
try:
    if(module=='traceroute'):
        traceroute()

    elif(module=="dns_search"):
        dns_search()

    elif(module=='rev_ip'):
        rev_ip()

    elif(module=='ip_geo'):
        ip_geo()

    elif(module=='href'):
        href()
    elif(module=='ps'):
        ps()

except KeyboardInterrupt:
    print("\033[37mExiting...\033[37m")
