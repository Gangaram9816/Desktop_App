from .voltage_con import *
from .current_con import *
from .tempe_con import *
from flet import *
from .batter_con import *
from .blur1 import *

class Blur:
   
    def __init__(self):
        
        self.vol_con=Volta_con()
        self.cur_con=Curren_con()
        self.tem_con=Tempe_con()
        self.bat_con=Batte_con()
        self.blr=Blur1()
       
        self.blr.assign_blur(self.vol_con,1,[54,60])
        
        self.blr.assign_blur(self.vol_con,3,[30,45])
        
        self.blr.assign_blur(self.vol_con,5,[3.900,4.300])
        
        self.blr.assign_blur(self.vol_con,7,[2.300,3.200])
       
        self.blr.assign_blur(self.vol_con,9,[35,60])

        self.blr.assign_blur(self.vol_con,11,[35,60])

        self.blr.assign_blur(self.vol_con,13,[35,60])

        self.blr.assign_blur(self.cur_con,5,[1,150])
    
        self.blr.assign_blur(self.cur_con,7,[1,65])
        
        self.blr.assign_blur(self.cur_con,9,[1,200])
        
        self.blr.assign_blur(self.cur_con,11,[1,60])
        
        self.blr.assign_blur(self.cur_con,13,[1,50])

        self.blr.assign_blur(self.cur_con,15,[1,10])

        self.blr.assign_blur(self.tem_con,1,[40,70])
        
        self.blr.assign_blur(self.tem_con,3,[20,80])
        
        self.blr.assign_blur(self.tem_con,5,[20,80])

        self.blr.assign_blur(self.tem_con,7,[20,80])

        self.blr.assign_blur(self.bat_con,7,[50,90])

        self.blr.assign_blur(self.bat_con,9,[0,1])
        self.blr.assign_blur(self.bat_con,11,[30,200])
    
        super().__init__()

