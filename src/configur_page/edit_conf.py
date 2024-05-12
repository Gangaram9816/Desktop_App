
from .voltage_con import *
from .current_con import *
from .tempe_con import *

from .profile_con import *
from .batter_con import *
from src.log import logger



class Edit:
    def __init__(self):
        super().__init__()
    vol_con=Volta_con()
    cur_con=Curren_con()
    tem_con=Tempe_con()
    pr_con=Pro_con()
    btn_con=Batte_con()

    def edit_con1(self,v,v1):
        try:

            self.pr_con.c2.content.controls[1].controls[1].content.controls[3].content.style.bgcolor=colors.YELLOW_100
            v.c1.content.controls[v1].controls[1].controls[0].content.controls[1].read_only=False
            v.c1.content.controls[v1].controls[1].controls[0].content.controls[1].bgcolor=colors.YELLOW_100
        except Exception as e:
            logger.error('In edit_config edit_con1 : %s',e)


    def edit_con(self,e):
        try:
            
            self.edit_con1(self.vol_con,int(1))
            self.edit_con1(self.vol_con,int(3))
            self.edit_con1(self.vol_con,int(5))
            self.edit_con1(self.vol_con,int(7))
            self.edit_con1(self.vol_con,int(9))
            self.edit_con1(self.vol_con,int(11))
            self.edit_con1(self.vol_con,int(13))

            self.edit_con1(self.cur_con,int(1))
            self.edit_con1(self.cur_con,int(3))
            self.edit_con1(self.cur_con,int(5))
            self.edit_con1(self.cur_con,int(7))
            self.edit_con1(self.cur_con,int(9))
            self.edit_con1(self.cur_con,int(11))
            self.edit_con1(self.cur_con,int(13))
            self.edit_con1(self.cur_con,int(15))

            self.edit_con1(self.tem_con,int(1))
            self.edit_con1(self.tem_con,int(3))
            self.edit_con1(self.tem_con,int(5))
            self.edit_con1(self.tem_con,int(7))

            self.edit_con1(self.btn_con,int(1))
            self.edit_con1(self.btn_con,int(3))
            self.edit_con1(self.btn_con,int(5))
            self.edit_con1(self.btn_con,int(7))
            self.edit_con1(self.btn_con,int(9))
            self.edit_con1(self.btn_con,int(11))
        except Exception as e:
            logger.error("In edit_conf edit_con : %s",e)
