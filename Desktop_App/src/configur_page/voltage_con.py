import flet
from flet import *

class Volta_con:
    fonts ={
	    "font1":"assets/fonts/RedHatDisplay-Medium.ttf",
        'font2':"assets/fonts/RedHatDisplay-Regular.ttf",
        'font3':"assets/fonts/RedHatDisplay-Bold.ttf"
 
	    }
    def __init__(self):
        super().__init__()

    def vol_return(va):
        return ResponsiveRow([Container(height=40,padding=padding.only(top=10),content=Text(value =va,color=colors.BLACK,size=16,font_family='font3'),col={"md":6}),
                        Row(col={"md":6},controls=[Container(height=40,expand=True,padding=padding.only(left=5),
                                                content=ResponsiveRow([Container(Text(size=17,text_align=TextAlign.START,color='red'),padding=padding.only(top=10),col={"md":6}),
                                                                       TextField(col={"md":6},text_size=17,color=colors.BLACK,read_only=True,content_padding=padding.only(left=5,bottom=10),border_width=0,width=40,height=40,border_radius=8,bgcolor='#EBEFFA')]),
                                                            ),Text(color=colors.BLACK,value="V   ")],),])
    
    
    c1=Container(content=Column([Text('Voltage',color=colors.BLACK,size=18,font_family='font3'),
                                 vol_return('Pack Over Volatge'),
                                                            
                                                    Divider(),

                                                    vol_return('Pack Under Voltage'),

                                    
                                                    Divider(),
                                                    vol_return('Cell Over Voltage'),
                                    
                                                    Divider(),
                                                    vol_return('Cell Under Voltage'),
                                   
                                                    Divider(),
                                                    vol_return('CV Voltage Limit'),

                                    
                                                    Divider(),
                                                    vol_return('Charging Float Vol'),
                                    
                                                    Divider(),
                                                    vol_return('Discharging FLoat Vol'),

                                                    ],spacing=8,scroll='hidden'),
#width=590,expand=True
            height=580,bgcolor='#FFFFFF',border_radius=8,col={"md":6},padding=padding.only(top=30,left=30,right=30))
    def volt_con(self):
        return self.c1
    