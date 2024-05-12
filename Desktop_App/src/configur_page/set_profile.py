from .profile_button import *
from .voltage_con import *
from .current_con import *
from .tempe_con import *
from flet import *
import requests
from .profile_con import *
from .batter_con import *
from src.log import logger

class Set_P:
    def __init__(self,page:Page):
        self.page=page
        self.dlg_pro1=AlertDialog(
        title=Text("Please save the profile first"),)
        self.dlg_pro=AlertDialog(
        title=Text("Enter the Valid Values"),)
        self.dlg_modal = AlertDialog(
        title=Text("Please Wait..."),
        content=ProgressRing(),
        content_padding=padding.only(left=150,right=150),
        on_dismiss=self.please_wait
    )
        self.dlg_pro3=AlertDialog(
        title=Text("Please Select a Profile"),)

        super().__init__()
    def please_wait(self,e):
        self.dlg_modal.open=True
        self.page.update()

    pr_btn=Profile_btn()
    vol_con=Volta_con()
    cur_con=Curren_con()
    tem_con=Tempe_con()
    pr_con=Pro_con()
    bt_con=Batte_con()

    def get_v(self,v):
        global va
        va=v


    def set_prof(self,e):
        valu=self.pr_con.dd1.content.content.value
        url=f"http://35.154.34.14/profiles/{va}"
        response=requests.get(url)
        v1=response.json()['Profiles']
        
        l1=[]
        for _ in v1:
            l1.append(_['username'])
                
        if valu in l1 or  valu not in l1:
            try:
                if self.vol_con.c1.content.controls[1].controls[1].controls[0].content.controls[1].read_only==False:
                    
                    self.page.dialog=self.dlg_pro1
                    self.dlg_pro1.open=True
                    self.page.update()
                else:
                    

                    self.pr_btn.c1.content.controls[0].controls[0].style.bgcolor='#345DC7'
                    self.pr_btn.c1.content.controls[0].controls[0].style.color='white'
                    self.pr_btn.c1.content.controls[0].controls[2].style.bgcolor=None
                    self.pr_btn.c1.content.controls[0].controls[2].style.color='black'
                    self.pr_con.c2.content.controls[1].controls[1].content.controls[0].content.style.bgcolor=None
                    
                    self.pr_con.c2.content.controls[1].controls[1].content.controls[0].content.style.color=None

                    
                    self.pr_con.c2.content.controls[1].controls[1].content.controls[2].content.style.bgcolor=None
                    self.pr_con.c2.content.controls[1].controls[1].content.controls[2].content.style.color=None

                    self.pr_con.c2.content.controls[1].controls[1].content.controls[1].content.style.bgcolor=None
                    self.pr_con.c2.content.controls[1].controls[1].content.controls[1].content.style.color=None

                    pov=str(int(float(self.vol_con.c1.content.controls[1].controls[1].controls[0].content.controls[1].value)*10)).zfill(4)
                    puv=str(int(float(self.vol_con.c1.content.controls[3].controls[1].controls[0].content.controls[1].value)*10)).zfill(4)
                    cov=str(int(float(self.vol_con.c1.content.controls[5].controls[1].controls[0].content.controls[1].value)*1000)).zfill(4)
                    cuv=str(int(float(self.vol_con.c1.content.controls[7].controls[1].controls[0].content.controls[1].value)*1000)).zfill(4)
                    cv_vol_limi=str(int(float(self.vol_con.c1.content.controls[9].controls[1].controls[0].content.controls[1].value)*10)).zfill(4)
                    cfv=str(int(float(self.vol_con.c1.content.controls[11].controls[1].controls[0].content.controls[1].value)*10)).zfill(4)
                    dfv=str(int(float(self.vol_con.c1.content.controls[13].controls[1].controls[0].content.controls[1].value)*10)).zfill(4)


                    over_cur_dis=str(int(float(self.cur_con.c1.content.controls[5].controls[1].controls[0].content.controls[1].value)*10)).zfill(4)
                    over_cur_cha=str(int(float(self.cur_con.c1.content.controls[7].controls[1].controls[0].content.controls[1].value)*1)).zfill(4)
                    peak_cur=str(int(float(self.cur_con.c1.content.controls[9].controls[1].controls[0].content.controls[1].value))).zfill(4)
                    peak_cur_delay=str(int(float(self.cur_con.c1.content.controls[11].controls[1].controls[0].content.controls[1].value))).zfill(4)
                    cc_cur=str(int(float(self.cur_con.c1.content.controls[13].controls[1].controls[0].content.controls[1].value))).zfill(4)
                    cv_mode_cutof_cur=str(int(float(self.cur_con.c1.content.controls[15].controls[1].controls[0].content.controls[1].value))).zfill(4)


                    ovr_tem=str(int(float(self.tem_con.c1.content.controls[1].controls[1].controls[0].content.controls[1].value))).zfill(4)
                    tem_fan_on=str(int(float(self.tem_con.c1.content.controls[3].controls[1].controls[0].content.controls[1].value))).zfill(4)
                    tem_fan_of=str(int(float(self.tem_con.c1.content.controls[5].controls[1].controls[0].content.controls[1].value))).zfill(4)
                    ther_run=str(int(float(self.tem_con.c1.content.controls[7].controls[1].controls[0].content.controls[1].value))).zfill(4)

                    max_dv=str(int(float(self.bt_con.c1.content.controls[7].controls[1].controls[0].content.controls[1].value))).zfill(4)
                    balancing=str(int(float(self.bt_con.c1.content.controls[9].controls[1].controls[0].content.controls[1].value))).zfill(4)
                    bal_start_dv=str(int(float(self.bt_con.c1.content.controls[11].controls[1].controls[0].content.controls[1].value))).zfill(4)
                    chem=str(self.bt_con.c1.content.controls[5].controls[1].controls[0].content.controls[1].value)
                    if chem=='NMC':
                        chem='1'
                    elif chem=='LFP':
                        chem='2'
                    elif chem=='LTO':
                        chem='3'
                    chem=str(chem).zfill(4)
                    print('chem',chem)
                    
                    bat_capa=str(int(float(self.bt_con.c1.content.controls[1].controls[1].controls[0].content.controls[1].value))).zfill(4)
                    
                    fin_val='AT+CONF=1,'+pov+','+puv+','+cv_vol_limi+','+ovr_tem+','+cfv+','+dfv+','+over_cur_dis+','+over_cur_cha+','+peak_cur+','+peak_cur_delay+','+cov+','+cuv+','+cc_cur+','+cv_mode_cutof_cur+','+tem_fan_on+','+tem_fan_of+','+ther_run+','+max_dv+','+balancing+','+bal_start_dv+','+chem+','+bat_capa
                    print(fin_val)
                    self.pr_btn.c1.content.controls[0].controls[0].data.write((fin_val+'\r\n').encode('utf-8'))
                
                    self.page.dialog=self.dlg_modal
                    self.dlg_modal.open=True
                    self.page.update()
                
            except Exception as e:
                self.page.dialog=self.dlg_pro
                self.dlg_pro.open=True
                self.page.update()
                logger.info('In set_profile except block : %s',e)

        else:
            self.page.dialog=self.dlg_pro3
            self.dlg_pro3.open=True
            self.page.update()
            logger.info('In set_profile last else')
                
