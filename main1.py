import time
import flet 
from flet import *
import requests
from gcloud import storage
import rsa
from src.auth import firebabse
from src.application import application
from src.dashboard import dashboard
from src.battery import battery
from src.configur_page import configur_clean,profile_con,upload_conf,remove_pr,dd_change,set_profile,configuration
from src.terminal import terminal
from src.sd_card import sd_card
import threading
import pyrebase
import ctypes
import sys
import os, base64,json
from dotenv import load_dotenv
import sys
from src.log import logger


def main(page:Page):

    #page.window_full_screen=False
    page.window_maximized=True
    da=dashboard.Dashboard()
    configu=configuration.Config(page)
    ap=application.App(page)
    bat=battery.Battery()
    sdcard=sd_card.SD_Card()

    upl=upload_conf.Upload_conf(page)
    prof_co=profile_con.Pro_con()
    dd_ch=dd_change.DD_Change(page)
    remov=remove_pr.Remove(page)
    ter=terminal.Terminal()
    set_p=set_profile.Set_P(page)
    con_clean=configur_clean.Config_Clean()
    au=firebabse.Fire_Auth()


    page.fonts ={
	"font1":"assets/fonts/RedHatDisplay-Medium.ttf",
    'font2':"assets/fonts/RedHatDisplay-Regular.ttf",
    'font3':"assets/fonts/RedHatDisplay-Bold.ttf"
 
	}
    db_alert1=SnackBar(
        Text("Internet not connected",size=25),
        bgcolor='red',
        padding=padding.only(left=550),
       
    )

    img=Image(src='assets/images/Group 427319099.svg',left=30,top=40)
     
    load_dotenv()  
    try:
        script_directory = os.path.abspath(os.path.dirname(sys.argv[0]))
        documents_folder = os.path.expanduser('~/Documents')  # Get the Documents folder path

        emo_config_folder = os.path.join(documents_folder, 'emo_config')

        # Ensure the emo_config folder exists
        os.makedirs(emo_config_folder, exist_ok=True)

        # Define file paths relative to the emo_config folder
        public_key_path = os.path.join(emo_config_folder, 'public.pem')
        private_key_path = os.path.join(emo_config_folder, 'private.pem')
        config_file_path = os.path.join(emo_config_folder, 'config.json')

        def generate_keys(public_key_path, private_key_path):
            (publicKey, privateKey) = rsa.newkeys(512)
            with open(public_key_path, 'wb') as p:
                p.write(publicKey.save_pkcs1('PEM'))
            with open(private_key_path, 'wb') as p:
                p.write(privateKey.save_pkcs1('PEM'))

        def load_keys(public_key_path, private_key_path):
            with open(public_key_path, 'rb') as p:
                publicKey = rsa.PublicKey.load_pkcs1(p.read())
            with open(private_key_path, 'rb') as p:
                privateKey = rsa.PrivateKey.load_pkcs1(p.read())

            return publicKey, privateKey

    except Exception as e:
        logger.error('Error in keys and file location :%s',e)
        
    def encrypt(data, key):
        encrypted_data = rsa.encrypt(data.encode('utf-8'), key)
        return base64.b64encode(encrypted_data).decode('utf-8')

    def decrypt(encrypted_data, key):
        decrypted_data = rsa.decrypt(base64.b64decode(encrypted_data.encode('utf-8')), key)
        return decrypted_data.decode('utf-8')
      

    user_name=Container(padding=padding.only(top=200),alignment=alignment.center,content=TextField(label="Username", color=colors.BLACK,bgcolor=colors.WHITE,hint_text="Please enter Your Username",width=400))
    passw=Container(alignment=alignment.center,content=TextField(label="Password",color=colors.BLACK,bgcolor=colors.WHITE,
                                        hint_text="Please enter Your Password",password=True, can_reveal_password=True,width=400))
        
    b1=Container(alignment=alignment.center,content=Container(height=40,width=300,content=ElevatedButton('Login',color=colors.BLACK,bgcolor=colors.WHITE,style=ButtonStyle(color=  colors.BLACK,shape=RoundedRectangleBorder(radius=8)))))
    
    b2=Container(alignment=alignment.center,content=Container(height=40,width=300,content=ElevatedButton('SignUp',color=colors.BLACK,bgcolor=colors.WHITE,style=ButtonStyle(color=  colors.BLACK,shape=RoundedRectangleBorder(radius=8)))))
    remember_me_checkbox = Row(alignment='center',controls=[Checkbox(label="Remember me")])
    if not (os.path.exists(public_key_path) and os.path.exists(private_key_path)):
        generate_keys(public_key_path, private_key_path)

    publicKey, privateKey = load_keys(public_key_path, private_key_path)

    def sign(e):
        try:
            #us=au.auth
            
            user=au.auth.create_user_with_email_and_password(user_name.content.value,passw.content.value)
            
            if user:
                data1={'username':user_name.content.value,
                'user_password':passw.content.value
                    }
                
                url="http://35.154.34.14/users"
               
                response=requests.post(url,json=data1)
                
                data = response.json()
                
                user_name.content.value=''
                passw.content.value=''
                page.add(Container(alignment=alignment.center,content=Text('Successfull,, Login Now',color='Green',size=22)))
                
                page.update()
        except Exception as e:
            logger.error('Error in Sign up :%s',e)
            

    if os.path.exists(config_file_path):
        with open(config_file_path, "r") as f:
            try:
                config_data = json.load(f)
                encrypted_username = config_data.get("username", "")
                encrypted_password = config_data.get("password", "")

                user_name.content.value = decrypt(encrypted_username, privateKey)
                passw.content.value = decrypt(encrypted_password, privateKey)

                remember_me_checkbox.controls[0].value = True
            except json.JSONDecodeError as e:
                logger.error('Error decoding config file: %s',e)
                #print("Error decoding config file:", e)
    

    def login(e):

        
        try:
            username = user_name.content.value
            password = passw.content.value
            remember_me = remember_me_checkbox.controls[0].value

            if remember_me:
                with open(config_file_path, "w") as f:
                    encrypted_username = encrypt(username, publicKey)
                    encrypted_password = encrypt(password, publicKey)
                    json.dump({"username": encrypted_username, "password": encrypted_password}, f)


            login=au.auth.sign_in_with_email_and_password(user_name.content.value,passw.content.value)
            

            if login:
                logger.info("login SUccess full")
                username1=user_name.content.value
            
                url=f"http://35.154.34.14/get_user_id/{username1}"
                response=requests.get(url)
               
                data = response.json()
                id1=data['user_id']

                url=f"http://35.154.34.14/profiles/{id1}"
                response=requests.get(url)
                v=response.json()['Profiles']
               
                l=[]
                for i in v:
                    
                    l.append(dropdown.Option(i['username']))

                prof_co.dd1.content.content.options=l
            
                upl.get_id(str(id1))
                dd_ch.get_uid(str(id1))
                remov.get_val(str(id1))
                set_p.get_v(str(id1))
                
                prof_co.get_v(str(id1))

                page.clean()
                page.title='EMO SENS'
                def sd_crd(e):
                    #print('sd card    ---------------------------------------')
                    if len(r1.controls)>1:
                        r1.controls.pop()
                        
                    
                    

                    r1.controls.append(sdcard.sd_card_con())
                    #print('sd card    ---------------------------------------')

                    r1.controls[0].controls[0].content.controls[3].content.bgcolor='#345DC7'
                    r1.controls[0].controls[0].content.controls[3].content.color='white'

                    r1.controls[0].controls[0].content.controls[0].style.bgcolor='white'
                    r1.controls[0].controls[0].content.controls[0].content.content.controls[0].color='black'  ##icon
                    r1.controls[0].controls[0].content.controls[0].content.content.controls[1].content.controls[0].color='black'   ##Battery
                    r1.controls[0].controls[0].content.controls[0].content.content.controls[1].content.controls[1].controls[1].color='black'  ###Connected
                    
                    r1.controls[0].controls[0].content.controls[2].content.bgcolor='white'
                    r1.controls[0].controls[0].content.controls[2].content.color='black'
                    r1.controls[0].controls[0].content.controls[1].content.bgcolor='white'
                    r1.controls[0].controls[0].content.controls[1].content.color='black'
                    r1.controls[0].controls[0].content.controls[4].content.bgcolor='white'
                    r1.controls[0].controls[0].content.controls[4].content.color='black'
                    
                    con_clean.edit_mo()
                
                    page.update()
                    #print('sd card    ---------------------------------------')
                    

                def dash(e):
                    #print('dashboard    ---------------------------------------')
                    if len(r1.controls)>1:
                        r1.controls.pop()
                    #ter.success=False
                    #print(ter.change_va())
                   # print('in sd dash',ter.success)
                    r1.controls.append(da.dashbo())
                    r1.controls[0].controls[0].content.controls[1].content.bgcolor='#345DC7'
                    r1.controls[0].controls[0].content.controls[1].content.color='white'

                    r1.controls[0].controls[0].content.controls[0].style.bgcolor='white'
                    r1.controls[0].controls[0].content.controls[0].content.content.controls[0].color='black'
                    r1.controls[0].controls[0].content.controls[0].content.content.controls[1].content.controls[0].color='black'
                    r1.controls[0].controls[0].content.controls[0].content.content.controls[1].content.controls[1].controls[1].color='black'

                    r1.controls[0].controls[0].content.controls[2].content.bgcolor='white'
                    r1.controls[0].controls[0].content.controls[2].content.color='black'
                    r1.controls[0].controls[0].content.controls[3].content.bgcolor='white'
                    r1.controls[0].controls[0].content.controls[3].content.color='black'
                    r1.controls[0].controls[0].content.controls[4].content.bgcolor='white'
                    r1.controls[0].controls[0].content.controls[4].content.color='black'
                    con_clean.edit_mo()
                
                    page.update()
                def confi(e):
                    if len(r1.controls)>1:
                        r1.controls.pop()
                    #ter.success=False
                    #print(ter.change_va)
                    #print('in sd confi',ter.success)
                    r1.controls.append(configu.conf())
                    
                    r1.controls[0].controls[0].content.controls[4].content.bgcolor='#345DC7'
                    r1.controls[0].controls[0].content.controls[4].content.color='white'

                    r1.controls[0].controls[0].content.controls[1].content.bgcolor='white'
                    r1.controls[0].controls[0].content.controls[1].content.color='black'

                    r1.controls[0].controls[0].content.controls[2].content.bgcolor='white'
                    r1.controls[0].controls[0].content.controls[2].content.color='black'
                    r1.controls[0].controls[0].content.controls[3].content.bgcolor='white'
                    r1.controls[0].controls[0].content.controls[3].content.color='black'

                    r1.controls[0].controls[0].content.controls[0].style.bgcolor='white'
                    r1.controls[0].controls[0].content.controls[0].content.content.controls[0].color='black'
                    r1.controls[0].controls[0].content.controls[0].content.content.controls[1].content.controls[0].color='black'
                    r1.controls[0].controls[0].content.controls[0].content.content.controls[1].content.controls[1].controls[1].color='black'

                    con_clean.edit_mo()
                    page.update()

                def batte(e):
                    if len(r1.controls)>1:
                        r1.controls.pop()
                    #ter.success=False
                    #print(ter.change_va())
                    #print('in batt',ter.success)
                    r1.controls.append(bat.batter_page())
                    r1.controls[0].controls[0].content.controls[0].style.bgcolor='#345DC7'
                    r1.controls[0].controls[0].content.controls[0].content.content.controls[0].color='white'
                    r1.controls[0].controls[0].content.controls[0].content.content.controls[1].content.controls[0].color='white'
                    r1.controls[0].controls[0].content.controls[0].content.content.controls[1].content.controls[1].controls[1].color='white'

                    r1.controls[0].controls[0].content.controls[1].content.bgcolor='white'
                    r1.controls[0].controls[0].content.controls[1].content.color='black'

                    r1.controls[0].controls[0].content.controls[2].content.bgcolor='white'
                    r1.controls[0].controls[0].content.controls[2].content.color='black'
                    r1.controls[0].controls[0].content.controls[3].content.bgcolor='white'
                    r1.controls[0].controls[0].content.controls[3].content.color='black'
                    r1.controls[0].controls[0].content.controls[4].content.bgcolor='white'
                    r1.controls[0].controls[0].content.controls[4].content.color='black'
                    con_clean.edit_mo()

                    page.update()

                def termi(e):
                    
                    if len(r1.controls)>1:
                        r1.controls.pop()
                    r1.controls.append(ter.ter())
                    #ter.success=False
                    
                    #print(ter.change_va())
                    
                    r1.controls[0].controls[0].content.controls[0].style.bgcolor='white'
                    r1.controls[0].controls[0].content.controls[0].content.content.controls[0].color='black'
                    r1.controls[0].controls[0].content.controls[0].content.content.controls[1].content.controls[0].color='black'
                    r1.controls[0].controls[0].content.controls[0].content.content.controls[1].content.controls[1].controls[1].color='black'
                   
                    r1.controls[0].controls[0].content.controls[1].content.bgcolor='white'
                    r1.controls[0].controls[0].content.controls[1].content.color='black'

                    r1.controls[0].controls[0].content.controls[2].content.bgcolor='#345DC7'
                    r1.controls[0].controls[0].content.controls[2].content.color='white'
                    r1.controls[0].controls[0].content.controls[3].content.bgcolor='white'
                    r1.controls[0].controls[0].content.controls[3].content.color='black'
                    r1.controls[0].controls[0].content.controls[4].content.bgcolor='white'
                    r1.controls[0].controls[0].content.controls[4].content.color='black'

                    con_clean.edit_mo()
                    page.update()
                
                r1=Row([Stack([Container(content=Column([ElevatedButton(style=ButtonStyle(color=  colors.BLACK,bgcolor='white',shape=RoundedRectangleBorder(radius=8)),
                                        content=Container(height=50,width=144, content=Row([Icon(icons.BATTERY_CHARGING_FULL_OUTLINED),
                                                Container(height=46,padding=padding.only(top=7),content=Column([Text("   Battery",size=17),Row([Image(src=' '),Text(size=10)],spacing=3)],spacing=0.00001))
                                                                                            ],)),on_click=batte),
                    
                                    Container(height=40,width=190,content=ElevatedButton("Dashoard",on_click=dash,icon=icons.DASHBOARD,
                                    style=ButtonStyle(color=  colors.WHITE,bgcolor='#345DC7',shape=RoundedRectangleBorder(radius=8),),)),

                                        Container(height=40,width=190,content=ElevatedButton("Terminal",on_click=termi,icon=icons.TERMINAL,
                                    style=ButtonStyle(color=  colors.BLACK,bgcolor='white',shape=RoundedRectangleBorder(radius=8),
                                        ),
                                        )),
                                    Container(height=40,width=190,content=ElevatedButton("SD Card",on_click=sd_crd,icon=icons.SD_CARD,
                                    style=ButtonStyle(color=  colors.BLACK,bgcolor='white',shape=RoundedRectangleBorder(radius=8),
                                        ),
                                        )),
                                    Container(height=40,width=190,content=ElevatedButton("Configuration",on_click=confi,icon=icons.SETTINGS,
                                    style=ButtonStyle(color=  colors.BLACK,bgcolor='white',shape=RoundedRectangleBorder(radius=8),
                                        ),
                                        )),

                                ],spacing=20),padding=padding.only(top=140,left=26),height=800,width=246,bgcolor='#FFFFFF',),img]),],spacing=35,expand=True)  
                
                page.add(r1)
                #print(da.c1.uid)
                page.padding=padding.only(right=30)
                page.bgcolor='#F0F0F0'
                #print(r1.uid)
                r1.controls.append(da.dashbo())
            
                read_thread = threading.Thread(target=ap.read_data_thread)
                process_thread = threading.Thread(target=ap.process_data_thread)

                read_thread.daemon = True
                process_thread.daemon = True
                read_thread.start()
                time.sleep(2)
                process_thread.start()
                
        
        except requests.exceptions.ConnectionError as e:
            page.snack_bar=db_alert1
            db_alert1.open=True
            page.update()
            
        except requests.exceptions.HTTPError as e:
            tex=''
            if "EMAIL_NOT_FOUND" in str(e):
                tex='EMAIL NOT FOUND'
            else:
                tex='INVALID PASSWORD'
            page.add(Container(alignment=alignment.center,content=Text(tex,color='red',size=18)))
            page.update()

        except requests.exceptions.RequestException as e:
            logger.error('Request Error in login :%s',e)
            #print("Request error:", e)
        except Exception as e1:
            logger.error('Exception in login :%s',e1)
            #print('exception',e1)
    
    b1.content.content.on_click=login
    b2.content.content.on_click=sign
    user_name.content.on_submit=login
   
    passw.content.on_submit=login
    
    page.add(user_name,passw,b1,b2,remember_me_checkbox)
    page.update()
    user_name.content.focus()
    passw.content.focus()
   
flet.app(target=main,assets_dir="assets")