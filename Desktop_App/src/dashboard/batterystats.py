import flet
from flet import *
from src.log import logger

class Batterystats:
    def __init__(self):
        super().__init__()
        
    fonts ={
	    "font1":"assets/fonts/RedHatDisplay-Medium.ttf",
        'font2':"assets/fonts/RedHatDisplay-Regular.ttf",
        'font3':"assets/fonts/RedHatDisplay-Bold.ttf"
 
	    }
    
    def para_return(v):
        try:
            return ResponsiveRow([
                Text(color=colors.BLACK,value=v,font_family='font3',size=16,col={"md": 6}),Text('0',color=colors.BLACK,col={"md": 6})],spacing=180)
        except Exception as e:
            logger.error('In batterystats para_return',e)

    c1=Column([Text('Battery Stats',color=colors.BLACK,font_family='font3',size=18),
               para_return('State of Charge'),
       
        Divider(),
        
        ResponsiveRow([
            Text('Remaining capacity',color=colors.GREY_300,font_family='font3',size=16,col={"md": 6}),Text('',col={"md": 6})],spacing=180),
        Divider(),
        para_return('Pack Voltage'),
        
        Divider(),
        
        ResponsiveRow([
            Text('Health',color=colors.GREY_300,font_family='font3',size=16,col={"md": 6}),Text('',col={"md": 6})],spacing=180),
        Divider(),
    
        ResponsiveRow([
            Text('Cycle Count',color=colors.GREY_300,font_family='font3',size=16,col={"md": 6}),Text('',col={"md": 6})],spacing=180),
        Divider(),
        para_return('Current'),

        Divider(),
        
        ResponsiveRow([
            Text('Battery paralleling',color=colors.GREY_300,font_family='font3',size=16,col={"md": 6}),Text('',col={"md": 6})],spacing=180),
        Divider(),
        para_return('Status'),
        Divider(),

        para_return('Mosfet Status'),

            ],spacing=8,scroll='hidden')
    
    def btrsts(self):
        return self.c1
    
    def update_batt(self,v):
        try:

            self.c1.controls[1].controls[1].value=str(v[3])
            self.c1.controls[5].controls[1].value=str(round(float(v[1])/100,2))
            self.c1.controls[11].controls[1].value=str(round(float(v[2])/100,2))

            er1=format(int(v[0]),'08b')[5:]

            self.c1.controls[15].controls[1].value=str('OK') if int(er1,2) in [0,1,2,3] else str('Faults')
            self.c1.controls[17].controls[1].value=str('Off') if int(er1,2) in [0,1,4] else str('On')
        except Exception as e:
            logger.error('In batterystats update_batt : %s',e)

      