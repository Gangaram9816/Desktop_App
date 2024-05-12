

from .voltage_con import *
from .current_con import *
from .tempe_con import *
from .profile_con import *
from psycopg2.errors import UniqueViolation
import requests
import httpx
from .profile_button import *
from .batter_con import *
from src.log import logger

class Upload_conf:
    def __init__(self,page:Page):
        super().__init__()
        self.page=page
        self.dlg_pro=AlertDialog(
        title=Text("Add Profile Name"),)

        self.dlg2=AlertDialog(
                        modal=True,
                        title=Text("Profile Already Exists"),
                        actions=[
                            TextButton('Ok',on_click=self.ok_close),
                        ],
                        actions_alignment=MainAxisAlignment.END,)
        
        self.dlg_pro1=AlertDialog(
        title=Text("Enter Valid Values"),)

        self.dlg_pro4=AlertDialog(
        title=Text("Connection Error"),)

        self.dlg_pro3=SnackBar(
        Text("Saved Successfully",size=25),
        bgcolor='green',
        padding=padding.only(left=550),
        
    )

        
    client=httpx.AsyncClient()
    pr_btn=Profile_btn()
    pr_con=Pro_con()
    vol_con=Volta_con()
    cur_con=Curren_con()
    tem_con=Tempe_con()
    bt_con=Batte_con()


    global v1,val
    val=''
    def ok_close(self,e):
        self.dlg2.open=False
        

    def get_id(self,v):
        global v1
        v1=v[0]
    def get_name(self,v):
        global val
        val=v

    def valid_check(self,valu,sma,lar):
        
        if valu<=lar and valu>=sma:
            return True
        else:
            return False
    
    def input_val(self,l):

       
        if self.valid_check((float(l[0])/10),54,60) is False:
            return False
        
        
        elif self.valid_check((float(l[1])/10),30,45) is False:
            return False
        
        elif self.valid_check((float(l[2])/1000),3.900,4.200) is False:
            return False
        
        elif self.valid_check((float(l[3])/1000),2.300,3.200) is False:
            return False
        
        elif self.valid_check((float(l[4])/10),35,60) is False:
            return False
        
        elif self.valid_check((float(l[5])/10),35,60) is False:
            return False
        
        elif self.valid_check((float(l[6])/10),35,60) is False:
            return False
        
        elif self.valid_check((float(l[7])/10),1,150) is False:
            return False
        
        elif self.valid_check(float(l[8]),1,200) is False:
            return False
        
        elif self.valid_check(float(l[9]),0,60) is False:
            return False
        
        elif self.valid_check(float(l[10]),1,50) is False:
            return False

        elif self.valid_check(float(l[11]),1,10) is False:
            return False
        
        elif self.valid_check(float(l[12]),40,70) is False:
            return False
        
        elif self.valid_check(float(l[13]),2,80) is False:
            return False
        
        elif self.valid_check(float(l[14]),20,80) is False:
            return False
        
        elif self.valid_check(float(l[15]),1,65) is False:
            return False
        elif self.valid_check(float(l[16]),20,80) is False:
            return False
        elif self.valid_check(float(l[17]),50,900) is False:
            return False
        elif self.valid_check(float(l[18]),0,1) is False:
            return False
        elif self.valid_check(float(l[19]),30,200) is False:
            return False
        elif self.valid_check(float(l[20]),000,999) is False:
            return False
        
        else:
            return True

    def con_clen(self,v,v1):
        v.c1.content.controls[v1].controls[1].controls[0].content.controls[1].read_only=True
        v.c1.content.controls[v1].controls[1].controls[0].content.controls[1].bgcolor='#EBEFFA'
       
    def edi(self):
        try:


            self.con_clen(self.vol_con,int(1))
            self.con_clen(self.vol_con,int(3))
            self.con_clen(self.vol_con,int(5))
            self.con_clen(self.vol_con,int(7))
            self.con_clen(self.vol_con,int(9))
            self.con_clen(self.vol_con,int(11))
            self.con_clen(self.vol_con,int(13))

            self.con_clen(self.cur_con,int(1))
            self.con_clen(self.cur_con,int(3))
            self.con_clen(self.cur_con,int(5))
            self.con_clen(self.cur_con,int(7))
            self.con_clen(self.cur_con,int(9))
            self.con_clen(self.cur_con,int(11))
            self.con_clen(self.cur_con,int(13))
            self.con_clen(self.cur_con,int(15))

            self.con_clen(self.tem_con,int(1))
            self.con_clen(self.tem_con,int(3))
            self.con_clen(self.tem_con,int(5))
            self.con_clen(self.tem_con,int(7))


            self.con_clen(self.bt_con,int(1))
            self.con_clen(self.bt_con,int(3))
            self.con_clen(self.bt_con,int(5))
            self.con_clen(self.bt_con,int(7))
            self.con_clen(self.bt_con,int(9))
            self.con_clen(self.bt_con,int(11))

            self.pr_con.c2.content.controls[1].controls[1].content.controls[3].content.style.bgcolor='#FFFFFF'
        except Exception as e:
            logger.error('In upload_conf edit fun',e)

    def btn_change(self):
        try:

            self.pr_btn.c1.content.controls[0].controls[0].style.bgcolor=None
            self.pr_btn.c1.content.controls[0].controls[0].style.color='black'
            self.pr_btn.c1.content.controls[0].controls[2].style.bgcolor=None
            self.pr_btn.c1.content.controls[0].controls[2].style.color='black'
            self.pr_con.c2.content.controls[1].controls[1].content.controls[0].content.style.bgcolor=None
            self.pr_con.c2.content.controls[1].controls[1].content.controls[0].content.style.color=None
            self.pr_con.c2.content.controls[1].controls[1].content.controls[2].content.style.bgcolor=None
            self.pr_con.c2.content.controls[1].controls[1].content.controls[2].content.style.color=None

            self.pr_con.c2.content.controls[1].controls[1].content.controls[1].content.style.bgcolor='#345DC7'
            self.pr_con.c2.content.controls[1].controls[1].content.controls[1].content.style.color='white'
        except Exception as e:
            logger.error('In upload_conf btn_change',e)


    def uploa(self,e):

        try:
            
            val=self.pr_con.dd1.content.content.value
         
            url=f"http://35.154.34.14/profiles/{v1}"
            
            response=requests.get(url)
            v=response.json()['Profiles']
            if  response.status_code == 500 or response.status_code ==404:
            
                self.page.dialog=self.dlg_pro4
                self.dlg_pro4.open=True
            else:

                l=[]
                for i in v:
                    
                    l.append(i['username'])
                print(l,val)
                pov=str((float(self.vol_con.c1.content.controls[1].controls[1].controls[0].content.controls[1].value)*10)).zfill(4)

                puv=str((float(self.vol_con.c1.content.controls[3].controls[1].controls[0].content.controls[1].value)*10)).zfill(4)

                cov=str((float(self.vol_con.c1.content.controls[5].controls[1].controls[0].content.controls[1].value)*1000)).zfill(4)
                cuv=str((float(self.vol_con.c1.content.controls[7].controls[1].controls[0].content.controls[1].value)*1000)).zfill(4)

                cv_vol_limi=str((float(self.vol_con.c1.content.controls[9].controls[1].controls[0].content.controls[1].value)*10)).zfill(4)
                cfv=str((float(self.vol_con.c1.content.controls[11].controls[1].controls[0].content.controls[1].value)*10)).zfill(4)

                dfv=str((float(self.vol_con.c1.content.controls[13].controls[1].controls[0].content.controls[1].value)*10)).zfill(4)

                over_cur=str((float(self.cur_con.c1.content.controls[5].controls[1].controls[0].content.controls[1].value)*10)).zfill(4)
                over_cur_char=str(float(self.cur_con.c1.content.controls[7].controls[1].controls[0].content.controls[1].value)).zfill(4)

                pack_peak_cur=str(float(self.cur_con.c1.content.controls[9].controls[1].controls[0].content.controls[1].value)).zfill(4)
      
                peak_cur_delay=str(float(self.cur_con.c1.content.controls[11].controls[1].controls[0].content.controls[1].value)).zfill(4)
                cc_cur=str(float(self.cur_con.c1.content.controls[13].controls[1].controls[0].content.controls[1].value)).zfill(4)
                cv_mode_cutof_cur=str(float(self.cur_con.c1.content.controls[15].controls[1].controls[0].content.controls[1].value)).zfill(4)

                ovr_tem=str(float(self.tem_con.c1.content.controls[1].controls[1].controls[0].content.controls[1].value)).zfill(4)
                tem_fan_on=str(float(self.tem_con.c1.content.controls[3].controls[1].controls[0].content.controls[1].value)).zfill(4)
                tem_fan_of=str(float(self.tem_con.c1.content.controls[5].controls[1].controls[0].content.controls[1].value)).zfill(4)
                thermal_runaway=str(float(self.tem_con.c1.content.controls[7].controls[1].controls[0].content.controls[1].value)).zfill(4)

                max_dv=str(float(self.bt_con.c1.content.controls[7].controls[1].controls[0].content.controls[1].value)).zfill(4)
                balanc=str(float(self.bt_con.c1.content.controls[9].controls[1].controls[0].content.controls[1].value)).zfill(4)
                start_dv=str(float(self.bt_con.c1.content.controls[11].controls[1].controls[0].content.controls[1].value)).zfill(4)
                chem=str(self.bt_con.c1.content.controls[5].controls[1].controls[0].content.controls[1].value)
                bat_capa=str(float(self.bt_con.c1.content.controls[1].controls[1].controls[0].content.controls[1].value))
                # print('chemistry',chem)
                # print('bat',bat_capa)

                print(pov,puv,cov,cuv,cv_vol_limi,cfv,dfv,over_cur,pack_peak_cur,peak_cur_delay,cc_cur,cv_mode_cutof_cur,ovr_tem,tem_fan_on,tem_fan_of,over_cur_char,thermal_runaway,max_dv,balanc,start_dv,chem,bat_capa)

                
                if val in l:
                    print('chemistry',chem)

                    if self.input_val([pov,puv,cov,cuv,cv_vol_limi,cfv,dfv,over_cur,pack_peak_cur,peak_cur_delay,cc_cur,cv_mode_cutof_cur,ovr_tem,tem_fan_on,tem_fan_of,over_cur_char,thermal_runaway,max_dv,balanc,start_dv,bat_capa]):
                    
                        url='http://35.154.34.14/update_profile/{}/{}'.format(v1,val)
                        data1_insert={'pac_over_volt':pov, 'pac_under_volt':puv, 'cv_volt_limit':cv_vol_limi, 'chaarging_float_volt':cfv, 
                                        'discharging_float_volt':dfv, 'over_current':over_cur, 'peak_current':pack_peak_cur,'over_temperature':ovr_tem,
                                        'peak_current_delay':peak_cur_delay, 'cell_over_volt':cov, 'cell_under_volt':cuv, 'cc_current':cc_cur, "cvmode_cutof_current":cv_mode_cutof_cur,
                                            'temperature_fan_on':tem_fan_on, 'temperature_fan_of':tem_fan_of,'over_curr_disch':over_cur_char,'thermal_runaway':thermal_runaway,
                                            'max_dv':max_dv,'balancing':balanc,'balancing_start_dv':start_dv,'chemistry':chem,'batt_capacity':bat_capa}
                        print('data insert',data1_insert)
                        response1=requests.post(url,json=data1_insert)

                        if  response1.status_code ==500 or response1.status_code ==404:
                            self.page.dialog=self.dlg_pro4
                            self.dlg_pro4.open=True
                            logger.info('in upload_conf not able to edit and upload the data')
                            
                        else:
                            self.page.snack_bar=self.dlg_pro3
                            self.dlg_pro3.open=True
                            self.btn_change()
                            self.edi()
                            self.page.update()
                            
                    else:
                        self.page.dialog= self.dlg_pro1
                        self.dlg_pro1.open=True
                        self.page.update()
                        logger.info('In upload_conf get invalid value')
                
                elif val =='':
                    self.page.dialog=self.dlg_pro
                    self.dlg_pro.open=True
                    self.page.update()
                    logger.info('In upload_conf get empty profile name')
                    
                else:
                    # print('chemistry',chem)
                    
                    if self.input_val([pov,puv,cov,cuv,cv_vol_limi,cfv,dfv,over_cur,pack_peak_cur,peak_cur_delay,cc_cur,cv_mode_cutof_cur,ovr_tem,tem_fan_on,tem_fan_of,over_cur_char,thermal_runaway,max_dv,balanc,start_dv,bat_capa]):
                        try:
                            data1_insert={'user_id':v1,'username':val,'pac_over_volt':pov, 'pac_under_volt':puv, 'cv_volt_limit':cv_vol_limi, 'chaarging_float_volt':cfv, 
                                        'discharging_float_volt':dfv, 'over_current':over_cur, 'peak_current':pack_peak_cur,'over_temperature':ovr_tem,
                                        'peak_current_delay':peak_cur_delay, 'cell_over_volt':cov, 'cell_under_volt':cuv, 'cc_current':cc_cur, "cvmode_cutof_current":cv_mode_cutof_cur,
                                            'temperature_fan_on':tem_fan_on, 'temperature_fan_of':tem_fan_of,'over_curr_disch':over_cur_char,'thermal_runaway':thermal_runaway,
                                            'max_dv':max_dv,'balancing':balanc,'balancing_start_dv':start_dv,'chemistry':chem,'batt_capacity':bat_capa}
                            
                            url="http://35.154.34.14/add_profile"
            
                            response2=requests.post(url,json=data1_insert)

                            
                            if  response2.status_code ==500 or response2.status_code ==404:
                            
                                self.page.dialog=self.dlg_pro4
                                self.dlg_pro4.open=True
                                logger.info('In upload_conf not able to uload the values')
                            else:
                                data = response2.json()
                                
                                self.page.snack_bar=self.dlg_pro3
                                self.dlg_pro3.open=True
                                
                                self.btn_change()
                                self.edi()
                                self.page.update()
                            
                        except UniqueViolation as e:

                                self.page.dialog=self.dlg2
                                self.dlg2.open=True
                                self.page.update()
                                logger.error('In upload_conf upload else part : %s',e)
                                
                        except Exception as e:
                                self.page.dialog= self.dlg_pro1
                                self.dlg_pro1.open=True
                                
                                self.page.update()
                                logger.error('In upload_conf upload Exception : %s',e)
                    else:
                        self.page.dialog= self.dlg_pro1
                        self.dlg_pro1.open=True
                        
                        self.page.update()
                        logger.info("In upload_conf upload part invalid values")
        except Exception as e:
            
            self.page.dialog=self.dlg_pro4
            self.dlg_pro4.open=True
            logger.error('In upload_conf last Exception : %s',e)
        
            
            



        




    

    

