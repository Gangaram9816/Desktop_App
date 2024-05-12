
from .profile_con import *
from .voltage_con import *
from .current_con import *
from .tempe_con import *
import requests
from .profile_button import *

from .configur_clean import *
from src.log import logger

class Remove:
    def __init__(self,page:Page):
        self.page=page
        self.dlg_pro4=AlertDialog(
        title=Text("Connection Error"),)
        self.dlg_remove1=AlertDialog(
                            modal=True,
                            title=Text("Are You Sure want to delete?"),
                            actions=[
                                TextButton('Yes',on_click=self.yes),
                                TextButton("No", on_click=self.close_dlg_1)

                            ],
                            actions_alignment=MainAxisAlignment.END,
                            
                        )
        self.dlg_remove2=AlertDialog(
                            modal=True,
                            title=Text("Please select the profile"),
                            
                            actions=[
                                TextButton('Ok',on_click=self.remove2),
                                
                            ],
                            actions_alignment=MainAxisAlignment.END,
                            
                        )
        
        super().__init__()
    pr_btn=Profile_btn()
    pr_co=Pro_con()
    vol_con=Volta_con()
    tem_con=Tempe_con()
    cur_con=Curren_con()
    clen=Config_Clean()

    def remove2(self,e):
        self.dlg_remove2.open=False

    def get_val(self,v):
        global v1
        v1=v[0]
    def get_nam(self,v):

        global nam
        nam=v
    def rem(self,e):
        
        if self.pr_co.dd1.content.content.value is None or self.pr_co.dd1.content.content.value =='':

            self.page.dialog=self.dlg_remove2
            self.dlg_remove2.open=True

        else:

            self.page.dialog=self.dlg_remove1
            self.dlg_remove1.open=True

    def close_dlg_1(self,e):
        self.dlg_remove1.open=False


    def yes(self,e):
        v2=self.pr_co.dd1.content.content.value
        try:
            

            if v2=='':
                self.page.dialog=self.dlg_remove2
                self.dlg_remove2.open=True

            
            else:
                da={
                    'user_id':v1,
                    'username':v2
                }
                url=f"http://35.154.34.14/delete_profile"
                response=requests.delete(url,json=da)
                if  response.status_code ==500 or response.status_code ==404:
                    self.page.dialog=self.dlg_pro4
                    self.dlg_pro4.open=True
                else:
                
                    self.pr_co.dd1.content.content.value=''
                    self.dlg_remove1.open=False

                    self.clen.edit_mo()

                    url=f"http://35.154.34.14/profiles/{v1}"
                    response=requests.get(url)
                    if  response.status_code ==500 or response.status_code ==404:
                        self.page.dialog=self.dlg_pro4
                        self.dlg_pro4.open=True
                    else:
                        v=response.json()['Profiles']
                        l=[]
                        for i in v:
                            
                            l.append(dropdown.Option(i['username']))
                        
                        self.pr_co.dd1.content.content.options=l

                
        except Exception as e:
            logger.error('In remove_pr yes fun : %s',e)
            


        