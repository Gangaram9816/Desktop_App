import flet
from flet import *

from .profile_button import *
from .voltage_con import *
from .current_con import *
from .tempe_con import *
from .profile_con import *
from .batter_con import *
import requests
from src.log import logger


class Get_pro:
    def __init__(self,page:Page):
        self.page=page
        self.dlg_modal = AlertDialog(
        title=Text("Please Wait..."),
        content=ProgressRing(),
        content_padding=padding.only(left=150,right=150),
        on_dismiss=self.dlg_wait
    )
        
        super().__init__()

    def dlg_wait(self,e):
        self.dlg_modal.open=True
        self.page.update()

    pr_con=Pro_con()
    pr_btn=Profile_btn()
    vol_con=Volta_con()
    cur_con=Curren_con()
    tem_con=Tempe_con()
    bt_con=Batte_con()

    def con_clean(self,v,v1):
        try:


            v.c1.content.controls[v1].controls[1].controls[0].content.controls[1].read_only=True
            v.c1.content.controls[v1].controls[1].controls[0].content.controls[1].bgcolor='#EBEFFA'
        except Exception as e:
            logger.error('In get_profile con_clean : %s',e)

    
    
    def get_conf(self,e):
        try:
        
            
            self.pr_btn.c1.content.controls[0].controls[0].data.write(b'AT+CONF=2\r\n')

            self.pr_con.c2.content.controls[1].controls[1].content.controls[3].content.style.bgcolor=''


            self.con_clean(self.vol_con,int(1))
            self.con_clean(self.vol_con,int(3))
            self.con_clean(self.vol_con,int(5))
            self.con_clean(self.vol_con,int(7))
            self.con_clean(self.vol_con,int(9))
            self.con_clean(self.vol_con,int(11))
            self.con_clean(self.vol_con,int(13))

            self.con_clean(self.cur_con,int(1))
            self.con_clean(self.cur_con,int(3))
            self.con_clean(self.cur_con,int(5))
            self.con_clean(self.cur_con,int(7))
            self.con_clean(self.cur_con,int(9))
            self.con_clean(self.cur_con,int(11))
            self.con_clean(self.cur_con,int(13))
            self.con_clean(self.cur_con,int(15))

            self.con_clean(self.tem_con,int(1))
            self.con_clean(self.tem_con,int(3))
            self.con_clean(self.tem_con,int(5))
            self.con_clean(self.tem_con,int(7))

            self.con_clean(self.bt_con,int(1))
            self.con_clean(self.bt_con,int(3))
            self.con_clean(self.bt_con,int(5))
            self.con_clean(self.bt_con,int(7))
            self.con_clean(self.bt_con,int(9))
            self.con_clean(self.bt_con,int(11))


            self.pr_con.c2.content.controls[1].controls[1].content.controls[3].content.style.bgcolor='#EBEFFA'
            self.pr_btn.c1.content.controls[0].controls[0].style.bgcolor=None
            self.pr_btn.c1.content.controls[0].controls[0].style.color='black'
            self.pr_btn.c1.content.controls[0].controls[2].style.bgcolor='#345DC7'
            self.pr_btn.c1.content.controls[0].controls[2].style.color='white'
            self.pr_con.c2.content.controls[1].controls[1].content.controls[0].content.style.bgcolor=None
            self.pr_con.c2.content.controls[1].controls[1].content.controls[0].content.style.color=None

            
            self.pr_con.c2.content.controls[1].controls[1].content.controls[2].content.style.bgcolor=None
            self.pr_con.c2.content.controls[1].controls[1].content.controls[2].content.style.color=None

            self.pr_con.c2.content.controls[1].controls[1].content.controls[1].content.style.bgcolor=None
            self.pr_con.c2.content.controls[1].controls[1].content.controls[1].content.style.color=None

            self.page.dialog=self.dlg_modal
            self.dlg_modal.open=True
        except Exception as e:
            logger.error('In get_profile get_conf : %s',e)


    def update_fun(self,v,v1,v2):
        try:
                
            v.c1.content.controls[v1].controls[1].controls[0].content.controls[1].value=v2

        except Exception as e:
            logger.error('In get_profile update_fun : %s',e)


    def update_con(self,v):
        try:
            
            s=str(v).split('CONFIGR')[1].split(',')

            self.pr_con.dd1.content.content.options.append(dropdown.Option('BMS Profile'))

            self.pr_con.dd1.content.content.value='BMS Profile'
                
            self.update_fun(self.vol_con,int(1),str(int(s[0])/10))
            self.update_fun(self.vol_con,int(3),str(int(s[1])/10))
            self.update_fun(self.vol_con,int(5),str(int(s[10])/1000))
            self.update_fun(self.vol_con,int(7),str(int(s[11])/1000))
            self.update_fun(self.vol_con,int(9),str(int(s[2])/10))
            self.update_fun(self.vol_con,int(11),str(int(s[4])/10))
            self.update_fun(self.vol_con,int(13),str(int(s[5])/10))
            
            self.update_fun(self.cur_con,int(5),str(int(s[6])/10))
            self.update_fun(self.cur_con,int(7),str(int(s[7])))
            self.update_fun(self.cur_con,int(9),str(int(s[8])))
            self.update_fun(self.cur_con,int(11),str(int(s[9])))
            self.update_fun(self.cur_con,int(13),str(int(s[12])))
            self.update_fun(self.cur_con,int(15),str(int(s[13])))

            self.update_fun(self.tem_con,int(1),str(int(s[3])))
            self.update_fun(self.tem_con,int(3),str(s[14]))
            self.update_fun(self.tem_con,int(5),str(s[15]))
            self.update_fun(self.tem_con,int(7),str(s[16]))

            self.update_fun(self.bt_con,int(7),str(s[17]))
            self.update_fun(self.bt_con,int(9),str(s[18]))
            self.update_fun(self.bt_con,int(11),str(s[19]))

        except Exception as e:
            logger.error('In get_profile update_con : %s',e)

        







        
    