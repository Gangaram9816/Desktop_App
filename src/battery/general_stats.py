import flet
from flet import *
from src.log import logger

class General_st:
    def __init__(self):
        super().__init__()
    fonts ={
	    "font1":"assets/fonts/RedHatDisplay-Medium.ttf",
        'font2':"assets/fonts/RedHatDisplay-Regular.ttf",
        'font3':"assets/fonts/RedHatDisplay-Bold.ttf"
 
	    }
    
    def para_return(v):
        return ResponsiveRow([Text(color=colors.BLACK,value=v,font_family='font3',size=16,col={"md":6}),Text('',color=colors.BLACK,text_align=TextAlign.CENTER,col={"md":6})],spacing=100)
    
    
    c1=Column([Text("General Stats",color=colors.BLACK,font_family='font3',size=32),
               Divider(color='#FFFFFF'),
            
               #ResponsiveRow([Text('BMS Id',color=colors.GREY_300,font_family='font3',size=16,col={"md":6}),Text(color=colors.GREY_300,text_align=TextAlign.CENTER,col={"md":6})],spacing=100),
               para_return('BMS Id'),
               Divider(),
               para_return('Voltage'),
               
               Divider(),
               para_return('Current'),
               
               Divider(),
               ResponsiveRow([Text('Paralleling',color=colors.GREY_300,font_family='font3',size=16,col={"md":6}),Text('',text_align=TextAlign.CENTER,col={"md":6})],spacing=100),
               Divider(),
               para_return('SOC'),
               
               Divider(),
               para_return('Faults'),
               
               Divider(),
               para_return('Load'),
               
               Divider(),
               para_return('Charging'),
               
               Divider(),
               para_return('Discharging'),
               
               Divider(),
               ResponsiveRow([Text('SOH',color=colors.GREY_300,font_family='font3',size=16,col={"md":6}),Text('',text_align=TextAlign.CENTER,col={"md":6})],spacing=100),
               Divider(),
               ResponsiveRow([Text('Cycle',color=colors.GREY_300,font_family='font3',size=16,col={"md":6}),Text('',text_align=TextAlign.CENTER,col={"md":6})],spacing=100),

               ],spacing=5,scroll='hidden')
    
    def gene_st(self):
        return self.c1
    
    def update_genstats(self,v):
        try:

            self.c1.controls[10].controls[1].value=str(v[3])#soc
            self.c1.controls[4].controls[1].value=str(round(float(v[1])/100,2))#voltage
            self.c1.controls[6].controls[1].value=str(round(float(v[2])/100,2))#current

            er1=format(int(v[0]),'08b')[5:]

            self.c1.controls[16].controls[1].value='Off' if int(er1,2) in [0,1,3,4] else 'On'
            self.c1.controls[18].controls[1].value='Off' if int(er1,2) in [0,1,2,4] else 'On'
            self.c1.controls[14].controls[1].value='Idle' if int(er1,2) in [0,1,4] else "Charging" if int(er1,2) ==2 else "Discharging"
        
        except Exception as e:
            logger.error('In battery update_genstats :%s',e)

