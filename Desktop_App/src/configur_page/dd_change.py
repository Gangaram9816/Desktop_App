from .voltage_con import *
from .current_con import *
import requests
from .tempe_con import*
import time
from .profile_con import *

from .batter_con import *
from .configur_clean import *
from src.log import logger

class DD_Change:
    def __init__(self,page:Page):
        self.page=page
        self.dlg_pro3=AlertDialog(
        title=Text("Profile not found"),)
        self.dlg_pro4=AlertDialog(
        title=Text("Connection Error"),)

        super().__init__()
    pr_c=Pro_con()
    vol_con=Volta_con()
    cur_con=Curren_con()
    tem_con=Tempe_con()
    bt_con=Batte_con()
    con_clean=Config_Clean()
    
    def get_uid(self,v):
        global v1
        v1=v[0]
    
    def d_change(self,e):
        
        v2=self.pr_c.dd1.content.content.value
        try:
        
            url="http://35.154.34.14/get_profile?user_id={}&username={}".format(v1,v2)
            
            
            response=requests.get(url)
            
            d=response.json()
            #print('dd change data',d)
            
            url=f"http://35.154.34.14/profiles/{v1}"
            response=requests.get(url)
            
            v=response.json()['Profiles']
            
            l=[]
            for i in v:
                l.append(dropdown.Option(i['username']))
            
            self.con_clean.edit_mo()
            self.pr_c.dd1.content.content.value=v2

            self.pr_c.dd1.content.content.options=l
            
        
            self.vol_con.c1.content.controls[1].controls[1].controls[0].content.controls[1].value=str(round((float(d['pac_over_volt'])/10),3))
            
            self.vol_con.c1.content.controls[3].controls[1].controls[0].content.controls[1].value=str(round((float(d['pac_under_volt'])/10),3))
            self.vol_con.c1.content.controls[5].controls[1].controls[0].content.controls[1].value=str(round((float(d['cell_over_volt'])/1000),3))
            self.vol_con.c1.content.controls[7].controls[1].controls[0].content.controls[1].value=str(round((float(d['cell_under_volt'])/1000),3))
            self.vol_con.c1.content.controls[9].controls[1].controls[0].content.controls[1].value=str(round((float(d['cv_volt_limit'])/10),3))
            self.vol_con.c1.content.controls[11].controls[1].controls[0].content.controls[1].value=str(round((float(d['chaarging_float_volt'])/10),3))
            self.vol_con.c1.content.controls[13].controls[1].controls[0].content.controls[1].value=str(round((float(d['discharging_float_volt'])/10),3))
            
            self.cur_con.c1.content.controls[5].controls[1].controls[0].content.controls[1].value=str(round((float(d["over_current"])/10),3))
            self.cur_con.c1.content.controls[7].controls[1].controls[0].content.controls[1].value=str(round(float(d['over_curr_disch']),3))
            self.cur_con.c1.content.controls[9].controls[1].controls[0].content.controls[1].value=str(round(float(d['peak_current']),3))
            self.cur_con.c1.content.controls[11].controls[1].controls[0].content.controls[1].value=str(round(float(d['peak_current_delay']),3))
            self.cur_con.c1.content.controls[13].controls[1].controls[0].content.controls[1].value=str(round(float(d['cc_current']),3))
            self.cur_con.c1.content.controls[15].controls[1].controls[0].content.controls[1].value=str(round(float(d['cvmode_cutof_current']),3))
            #self.cur_con.c1.content.controls[15].controls[1].controls[0].content.controls[1].value=str(int(d['cvmode_cutof_current']))

            self.tem_con.c1.content.controls[1].controls[1].controls[0].content.controls[1].value=str(round(float(d['over_temperature']),3))
            self.tem_con.c1.content.controls[3].controls[1].controls[0].content.controls[1].value=str(round(float(d['temperature_fan_on']),3))
            self.tem_con.c1.content.controls[5].controls[1].controls[0].content.controls[1].value=str(round(float(d['temperature_fan_of']),3))
            self.tem_con.c1.content.controls[7].controls[1].controls[0].content.controls[1].value=str(round(float(d['thermal_runaway']),3))

            self.bt_con.c1.content.controls[7].controls[1].controls[0].content.controls[1].value=str(round(float(d['max_dv']),3))
            self.bt_con.c1.content.controls[9].controls[1].controls[0].content.controls[1].value=str(d['balancing'])
            self.bt_con.c1.content.controls[11].controls[1].controls[0].content.controls[1].value=str(round(float(d['balancing_start_dv']),3))
            
        except requests.exceptions.ConnectionError as err:
            
            self.page.dialog=self.dlg_pro4
            self.con_clean.edit_mo()
            self.dlg_pro4.open=True
       
        except:
                
            self.page.dialog=self.dlg_pro3
            self.dlg_pro3.open=True
            
            try:
                url=f"http://35.154.34.14/profiles/{v1}"
                response=requests.get(url)
                v=response.json()['Profiles']
                
                l=[]
                for i in v:
                    l.append(dropdown.Option(i['username']))
                
                self.pr_c.dd1.content.content.options=l
                self.page.update()
                
            except Exception as e:
                logger.error('In dd change last: %s',e)
           