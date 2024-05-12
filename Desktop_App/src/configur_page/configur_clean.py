from .voltage_con import *
from .current_con import *
from .profile_button import *
from .tempe_con import*
from .batter_con import *

from .profile_con import *
from src.log import logger

class Config_Clean:
    def __init__(self):
        
        super().__init__()
    pr_c=Pro_con()
    vol_con=Volta_con()
    cur_con=Curren_con()
    tem_con=Tempe_con()
    pr_btn=Profile_btn()
    bt_con=Batte_con()

    def fun_edit(self,v,v1):
        try:
            v.c1.content.controls[v1].controls[1].controls[0].content.controls[0].content.value=''
            v.c1.content.controls[v1].controls[1].controls[0].content.controls[1].bgcolor='#EBEFFA'
            
            v.c1.content.controls[v1].controls[1].controls[0].content.controls[1].read_only=True
            v.c1.content.controls[v1].controls[1].controls[0].content.controls[1].value=''
        except Exception as e:
            logger.error('In Configur clean class, in fun_edit:%s',e)
            

    def edit_mo(self):
        
        try:

            self.pr_c.dd1.content.content.value=''
            self.pr_btn.c1.content.controls[0].controls[0].style.bgcolor=None
            self.pr_btn.c1.content.controls[0].controls[0].style.color='black'
            self.pr_btn.c1.content.controls[0].controls[2].style.bgcolor=None
            self.pr_btn.c1.content.controls[0].controls[2].style.color='black'

            self.pr_c.c2.content.controls[1].controls[1].content.controls[3].content.style.bgcolor=None
            self.pr_c.c2.content.controls[1].controls[1].content.controls[3].content.style.color=None

            self.pr_c.c2.content.controls[1].controls[1].content.controls[0].content.style.bgcolor=None
            self.pr_c.c2.content.controls[1].controls[1].content.controls[0].content.style.color=None
            self.pr_c.c2.content.controls[1].controls[1].content.controls[2].content.style.bgcolor=None
            self.pr_c.c2.content.controls[1].controls[1].content.controls[2].content.style.color=None
            self.pr_c.c2.content.controls[1].controls[1].content.controls[1].content.style.bgcolor=None
            self.pr_c.c2.content.controls[1].controls[1].content.controls[1].content.style.color=None

            self.fun_edit(self.vol_con,int(1))
        
            self.fun_edit(self.vol_con,int(3))
            self.fun_edit(self.vol_con,int(5))
            self.fun_edit(self.vol_con,int(7))
            self.fun_edit(self.vol_con,int(9))
            self.fun_edit(self.vol_con,int(11))
            self.fun_edit(self.vol_con,int(13))

            self.fun_edit(self.cur_con,int(1))
            self.fun_edit(self.cur_con,int(3))
            self.fun_edit(self.cur_con,int(5))
            self.fun_edit(self.cur_con,int(7))
            self.fun_edit(self.cur_con,int(9))
            self.fun_edit(self.cur_con,int(11))
            self.fun_edit(self.cur_con,int(13))
            self.fun_edit(self.cur_con,int(15))

            self.fun_edit(self.tem_con,int(1))
            self.fun_edit(self.tem_con,int(3))
            self.fun_edit(self.tem_con,int(5))
            self.fun_edit(self.tem_con,int(7))

            self.fun_edit(self.bt_con,int(1))
            self.fun_edit(self.bt_con,int(3))

            self.fun_edit(self.bt_con,int(5))
            self.fun_edit(self.bt_con,int(7))
            self.fun_edit(self.bt_con,int(9))
            self.fun_edit(self.bt_con,int(11))

        except Exception as e:
            logger.error('In Configur clean, in edit_mo: %s',e)
            
            

