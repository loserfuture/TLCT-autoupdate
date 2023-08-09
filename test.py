import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
import webbrowser
import os, sys
try:
  from faker import Faker
  from requests import session
  from colorama import Fore, Style
  import requests, random, re
  from random import randint
  import requests,pystyle
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
  os.system('pip install requests && pip install bs4 && pip install pystyle')
  print('__Please reboot this console__')
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
#MÀU
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#ĐÁNH DẤU BẢN QUYỀN
dev="\033[1;39m[\033[1;31m×\033[1;39m]\033[1;39m"
def banner():
 banner = f"""\033[1;32m
                ┏━━━┓  ┏━━━┓  ┏━━━┓  ┏━━━┓
                ┃┏━┓┃  ┃┏━┓┃  ┃┏━┓┃  ┗┓┏┓┃
                ┃┃━┗┛  ┃┃━┃┃  ┃┃━┃┃ ━ ┃┃┃┃
                ┃┃┏━┓  ┃┃━┃┃  ┃┃━┃┃ ━ ┃┃┃┃
                ┃┗┻━┃  ┃┗━┛┃  ┃┗━┛┃  ┏┛┗┛┃
                ┗━━━┛  ┗━━━┛  ┗━━━┛  ┗━━━┛
\033[1;39m              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;39m              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
\033[1;39m┌──────────────────────── MCCARC ────────────────────────┐
\033[1;32m║   \033[1;39mLOADER VERSION     : \033[1;32m 0.1                            \033[1;32m║
\033[1;32m║   \033[1;39mFACEBOOK           :  trumflorentinovucony           \033[1;32m║
\033[1;32m║   \033[1;39mDISCORD            :  discord.gg/pdrkdxZH            \033[1;32m║
\033[1;32m║   \033[1;39mGITHUB             :  Coming Soon                    \033[1;32m║
\033[1;32m║   \033[1;39mYOUTUBE            :  That Vape User ☊               \033[1;32m║
\033[1;32m║   \033[1;39mSTATUS             :  Active !                       \033[1;32m║
\033[1;39m└────────────────────────────────────────────────────────┘
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.000001)
 
 
# =======================[RUN]=======================#
while True:
	os.system('clear')
	banner()
	print("\033[1;39m┌───────────────────┐         ")
	print("\033[1;32m║   \033[1;39m   GHOST        \033[1;32m║          ")
	print("\033[1;39m└───────────────────┘          ")
	print("\033[1;31m[\033[1;39m1.1\033[1;31m] \033[1;32mVape Client \033[1;31m[\033[1;33mv4.10\033[1;31m]         ")
	print("\033[1;31m[\033[1;39m2.1\033[1;31m] \033[1;32mVape Client \033[1;31m[\033[1;33mv4.06 Remake\033[1;31m]              ")
	print("\033[1;31m[\033[1;39m3.1\033[1;31m] \033[1;32mVape Client \033[1;31m[\033[1;33mv4.04\033[1;31m]           ")
	print("\033[1;31m[\033[1;39m4.1\033[1;31m] \033[1;32mVape Client \033[1;31m[\033[1;33mv3\033[1;31m] ")
	print("\033[1;31m[\033[1;39m5.1\033[1;31m] \033[1;32mVape Client \033[1;31m[\033[1;33mLite\033[1;31m] ")
	print("\033[1;31m[\033[1;39m6.1\033[1;31m] \033[1;32mDream Client ")
	print("\033[1;31m[\033[1;39m7.1\033[1;31m] \033[1;32mSlapp \033[1;31m[\033[1;33mv1.28\033[1;31m] ")
	print("\033[1;31m[\033[1;39m8.1\033[1;31m] \033[1;32mWhiteout \033[1;31m[\033[1;33mPlacebo\033[1;31m] ")
	print("\033[1;31m[\033[1;39m9.1\033[1;31m] \033[1;32mEternal Client ")
	print("\033[1;31m[\033[1;39m10.1\033[1;31m] \033[1;32mEternal Lite ")
	print("\033[1;31m[\033[1;39m11.1\033[1;31m] \033[1;32mZoomin Lunar Support ")
	print("\033[1;31m[\033[1;39m12.1\033[1;31m] \033[1;32mLuvsy Client ")
	print("\033[1;31m[\033[1;39m13.1\033[1;31m] \033[1;32mRaven S1 ")
	print("\033[1;31m[\033[1;39m14.1\033[1;31m] \033[1;32mRaven B+ ")
	print("\033[1;31m[\033[1;39m15.1\033[1;31m] \033[1;32mRaven B- \033[1;31m[\033[1;33mMitfox\033[1;31m] ")
	print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
	print("\033[1;39m┌───────────────────┐")
	print("\033[1;32m║  \033[1;39m  BLATANT \033[1;31m[\033[1;33mNEW\033[1;31m]  \033[1;32m║")
	print("\033[1;39m└───────────────────┘")
	print("\033[1;31m[\033[1;39m1.2\033[1;31m] \033[1;32mVestige \033[1;31m[\033[1;33mv2.0.2\033[1;31m] ")
	print("\033[1;31m[\033[1;39m2.2\033[1;31m] \033[1;32mVestige \033[1;31m[\033[1;33mv2.2.1\033[1;31m]  ")
	print("\033[1;31m[\033[1;39m3.2\033[1;31m] \033[1;32mHuzuni")
	print("\033[1;31m[\033[1;39m4.2\033[1;31m] \033[1;32mSigma")
	print("\033[1;31m[\033[1;39m5.2\033[1;31m] \033[1;32mFDP Client \033[1;31m[\033[1;33mRat cleaned\033[1;31m]")
	print("\033[1;31m[\033[1;39m6.2\033[1;31m] \033[1;32mKawaii Client")
	print("\033[1;31m[\033[1;39m7.2\033[1;31m] \033[1;32mEvoBounce")
	print("\033[1;31m[\033[1;39m8.2\033[1;31m] \033[1;32mLint")
	print("\033[1;31m[\033[1;39m9.2\033[1;31m] \033[1;32mTenacity \033[1;31m[\033[1;33mv5.1\033[1;31m]")
	print("\033[1;31m[\033[1;39m10.2\033[1;31m] \033[1;32mStitch Client")
	print("\033[1;31m[\033[1;39m11.2\033[1;31m] \033[1;32mNovoline \033[1;31m[\033[1;33mv6.0\033[1;31m]")
	print("\033[1;31m[\033[1;39m12.2\033[1;31m] \033[1;32mCrosssine B31")
	print("\033[1;31m[\033[1;39m13.2\033[1;31m] \033[1;32mBlaze Client")
	print("\033[1;31m[\033[1;39m14.2\033[1;31m] \033[1;32mZeroDay Client")
	print("\033[1;31m[\033[1;39m15.2\033[1;31m] \033[1;32mMoon Client")
	print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
	print("\033[1;39m┌───────────────────┐          ")
	print("\033[1;32m║  \033[1;39m    CLICKER      \033[1;32m║          ")
	print("\033[1;39m└───────────────────┘          ")
	print("\033[1;31m[\033[1;39m1.3\033[1;31m] \033[1;32m1337 \033[1;31m[\033[1;33mPlacebo\033[1;31m] ")
	print("\033[1;31m[\033[1;39m2.3\033[1;31m] \033[1;32mAion ")
	print("\033[1;31m[\033[1;39m3.3\033[1;31m] \033[1;32mApe ")
	print("\033[1;31m[\033[1;39m4.3\033[1;31m] \033[1;32mApollyon")
	print("\033[1;31m[\033[1;39m5.3\033[1;31m] \033[1;32mAres ")
	print("\033[1;31m[\033[1;39m6.3\033[1;31m] \033[1;32mAtomic ")
	print("\033[1;31m[\033[1;39m7.3\033[1;31m] \033[1;32mDropsy ")
	print("\033[1;31m[\033[1;39m8.3\033[1;31m] \033[1;32mDusk ")
	print("\033[1;31m[\033[1;39m9.3\033[1;31m] \033[1;32mExelon ")
	print("\033[1;31m[\033[1;39m10.3\033[1;31m] \033[1;32mExodus ")
	print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
	print("\033[1;39m┌───────────────────┐")
	print("\033[1;32m║  \033[1;39m  OTHER THING    \033[1;32m║")
	print("\033[1;39m└───────────────────┘")
	print("\033[1;31m[\033[1;39m1.4\033[1;31m] \033[1;32mGrand0x Private Sources ")
	print("\033[1;31m[\033[1;39m2.4\033[1;31m] \033[1;32mIntave Anticheat Sources ")
	print("\033[1;31m[\033[1;39m3.4\033[1;31m] \033[1;32mRise 6.0 Sources ")
	print("\033[1;31m[\033[1;39m4.4\033[1;31m] \033[1;32mVape Lite Assets ")
	print("\033[1;31m[\033[1;39m5.4\033[1;31m] \033[1;32mVape V4.07 deobf strings + assets + dll ")
	print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
	chon = input('\033[1;39m[\033[1;31m×\033[1;39m] \033[1;39m>> \033[1;39m[\033[1;32mCHOOSE\033[1;39m]\033[1;39m: \033[1;32m')
	print('\033[1;39m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')
	if chon == '1.1' :
		webbrowser.open_new("https://anotepad.com/notes/j897dgy9")
	if chon == '2.1':
		webbrowser.open_new("https://www.mediafire.com/file/4c02w3mpw89vjwv/Vape+4.06.zip/file")
	if chon == '3.1' :
		webbrowser.open_new("https://www.mediafire.com/file/j14pjh34d7nyvxu/MinecraftCheaterCentral.zip/file")
	if chon == '4.1' :
		webbrowser.open_new("https://www.mediafire.com/file/8coudk5wgq9ssla/Vape_v3.25.zip/file")
	if chon == '5.1' :
		webbrowser.open_new("https://www.mediafire.com/file/c2feinbliewkebs/Vape_Lite.zip/file")
	if chon == '6.1' :
		webbrowser.open_new("https://www.mediafire.com/file/m2w5kfdplx351pm/DreamClient.zip/file")
	if chon == '7.1':
		webbrowser.open_new("https://www.mediafire.com/file/pgxp77rt0suju9s/slap.zip/file")
	if chon == '8.2' :
		webbrowser.open_new("https://www.mediafire.com/file/v1cv8ue0f7x1mkz/Whiteout.zip/file")
	if chon == '9.1' :
		webbrowser.open_new("https://www.mediafire.com/file/p43x2u7j2428y4c/eternal_internal.dll/file")
	if chon == '10.1' :
		webbrowser.open_new("https://www.mediafire.com/file/l6g8qv971q1bsl3/eternal_lite.zip/file")
	if chon == '11.1' :
		webbrowser.open_new("https://www.mediafire.com/file/xpz4qgb63e0wcb3/zoomin.zip/file")
	if chon == '12.1':
		webbrowser.open_new("https://www.mediafire.com/file/hrls1h4mp516fy7/Luvsy_Ghost_v1.0.zip/file")
	if chon == '13.1' :
		webbrowser.open_new("https://www.mediafire.com/file/ftv4k9aep23zagp/1.8.9.Raven-S.1.jar/file")
	if chon == '14.1' :
		webbrowser.open_new("https://github.com/Kopamed/Raven-bPLUS")
	if chon == '15.1':
		webbrowser.open_new("https://drive.google.com/file/d/1yoxM3U1hx_yyXaGjMlm-sQ-wbhK9NWov/view?usp=sharing") 
	if chon == '1.2':
		webbrowser.open_new("https://www.mediafire.com/file/adqea2u9ass33ni/Vestige_2.0.2.zip/file") 
	if chon == '2.2':
		webbrowser.open_new("https://www.mediafire.com/file/puxs5k0hlvxmh6y/Vestige.zip/file") 
	if chon == '3.2':
		webbrowser.open_new("https://www.mediafire.com/file/vcaoo6kam878h07/huzuni.rar/file") 
	if chon == '4.2' :
		webbrowser.open_new("https://www.mediafire.com/file/z1dpsfi8ow4k0ar/sigma.zip/file")
	if chon == '5.2' :
		webbrowser.open_new("https://www.mediafire.com/file/76pwmepnhmh1j3r/FDP_Client_Clean_4934678.jar/file")
	if chon == '6.2' :
		webbrowser.open_new("https://drive.google.com/file/d/1bMBKvXvoqv85LvMnCUIUh3jkSwtkcw4R/view")
	if chon == '7.2' :
		webbrowser.open_new("https://drive.google.com/file/d/1DiKI8M4TAnhvYEHCHdQgMjhkls33jDF9/view")
	if chon == '8.2' :
		webbrowser.open_new("https://drive.google.com/file/d/1NjWP-HWSenlE8dWmbBfoGbN_UU2GZhmL/view")
	if chon == '9.2' :
		webbrowser.open_new("https://www.mediafire.com/file/2png0evxr7c1s91/Tenacity.zip/file")
	if chon == '10.2' :
		webbrowser.open_new("https://mega.nz/file/bsUnwRAK#yZO4wbWA86a8YNtuniVAQtkcxf1lasYuXxTL0gdSMKs")
	if chon == '11.2' :
		webbrowser.open_new("https://www.mediafire.com/file/oepcx3in9nmkd8u/Novoline.zip/file")
	if chon == '12.2' :
		webbrowser.open_new("https://www.mediafire.com/file/ek0gg130dm767rb/CrossSine-B31.jar/file")
	if chon == '13.2' :
		webbrowser.open_new("https://www.mediafire.com/file/vti3ff68h26jhvu/BlazeClient.zip/file")
	if chon == '14.2' :
		webbrowser.open_new("https://www.mediafire.com/file/xdyb9d3hluo4uog/ZeroGay.zip/file")
	if chon == '15.2' :
		webbrowser.open_new("https://www.mediafire.com/file/komh0qjyq6lh6de/Moon.rar/file")
	if chon == '1.3' :
		webbrowser.open_new("https://www.mediafire.com/file/uixqtdbh7laysge/1337_Clicker.zip/file")
	if chon == '2.3' :
		webbrowser.open_new("https://www.mediafire.com/file/4naitvdw5en5wzj/Aion.zip/file")
	if chon == '3.3' :
		webbrowser.open_new("https://www.mediafire.com/file/pf0kgzyw25hl1yr/Ape_Clicker.zip/file")
	if chon == '4.3' :
		webbrowser.open_new("https://www.mediafire.com/file/8c6gqmtb8pz53gf/Apollyon.zip/file")
	if chon == '5.3' :
		webbrowser.open_new("https://www.mediafire.com/file/kx8g6x9oafq5go3/Ares.zip/file")
	if chon == '6.3' :
		webbrowser.open_new("https://www.mediafire.com/file/bpw3e5xgvekgwed/Atomic_Clicker.zip/file")
	if chon == '7.3' :
		webbrowser.open_new("https://www.mediafire.com/file/jejnjk1bskuddnc/Dropsy.zip/file")
	if chon == '8.3' :
		webbrowser.open_new("https://www.mediafire.com/file/wwmcp6741lj9vn6/Dusk.zip/file")
	if chon == '9.3' :
		webbrowser.open_new("https://www.mediafire.com/file/xpb2cg5k9f3lzlx/Exelon.zip/file")
	if chon == '10.3' :
		webbrowser.open_new("https://www.mediafire.com/file/v9iaswz213pqu27/Exodus.zip/file")
	if chon == '1.4' :
		webbrowser.open_new("https://www.mediafire.com/file/zamuavediau7jdg/grand0x_private_source.zip/file")
	if chon == '2.4' :
		webbrowser.open_new("https://www.mediafire.com/file/7xbrqq1khuvu6eh/intave_src.zip/file")
	if chon == '3.4' :
		webbrowser.open_new("https://www.mediafire.com/file/pux0fhrh9q1aimu/rise_6.0_source.zip/file")
	if chon == '4.4' :
		webbrowser.open_new("https://www.mediafire.com/file/dubvd8udfi1miyk/vape_lite_assets.zip/file")
	if chon == '5.4' :
		webbrowser.open_new("https://www.mediafire.com/file/1b75bmlaiqacb9v/vape_v4.07_deobf_strings_%252B_assets_%252B_dll_file.zip/file")
	else :
		continue
