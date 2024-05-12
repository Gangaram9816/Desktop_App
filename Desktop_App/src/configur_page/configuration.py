import flet
from flet import *
from .profile_button import *
from .profile_con import *
from .voltage_con import *
from .current_con import *
from .batter_con import *
from .tempe_con import *


class Config:


    fonts ={
	    "font1":"assets/fonts/RedHatDisplay-Medium.ttf",
        'font2':"assets/fonts/RedHatDisplay-Regular.ttf",
        'font3':"assets/fonts/RedHatDisplay-Bold.ttf"
 
	    }
    def __init__(self,page:Page):
        self.page=page
        self.pr_o=Pro_con()
        prof=Profile_btn()
        vol_con=Volta_con()
        batt_con=Batte_con()
        temp_con=Tempe_con()
        cur1=Curren_con()
        #width=1250,
        self.col1=Column(height=1000,
                    controls=[Container(height=120),
                            Column([
                            Text('Configuration',color=colors.BLACK,font_family='font3',size=32),
                            Text('Customize commands',color=colors.BLACK),],spacing=0),
                        
                            prof.profi(),
                            
                            self.pr_o.p_con(),
                            Container(height=20),
                            ResponsiveRow([Column([vol_con.volt_con(),batt_con.bat_con()],spacing=26,col={"md":6},),
                                        Column([cur1.cur_con(),temp_con.tem_con()],spacing=26,col={"md":6})],spacing=26),
                            Container(height=20)

        ],expand=True,scroll='hidden')
        super().__init__()
    
    def conf(self):
        return self.col1
    
