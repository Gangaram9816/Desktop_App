import flet
from flet import *

class Fault:
    def __init__(self):

        #self.comp=[self.col1.controls[i].controls[j] for i in range(1, 4) for j in range(7)]
        #print(self.comp)

        super().__init__()
    fonts ={
	    "font1":"assets/fonts/RedHatDisplay-Medium.ttf",
        'font2':"assets/fonts/RedHatDisplay-Regular.ttf",
        'font3':"assets/fonts/RedHatDisplay-Bold.ttf"
 
	    }
    
    def para_fun(v):
        return Container(bgcolor='#FFFFFF',height=84,width=130,border=border.all(1,'#2828284D'),border_radius=8,
        content=Stack([Container(height=20,width=20,bgcolor='green',top=8,right=10,border_radius=6),Text(color=colors.BLACK,value=v,font_family='font1',left=10,bottom=10)]),
               col={'md':1.71})
  
    col1=Column([Text('Troubleshoot',color=colors.BLACK,font_family='font3',size=18),
        ResponsiveRow([
            para_fun('SD_Card\nError'),

        para_fun('AFE\nError'),

        para_fun('Mosfet\nError'),
        
        para_fun('DT  \nWarning'),
       
        para_fun('Open Wire\nError'),

        para_fun('Short\nCircuit'),

        para_fun('Over\nCurrent'),

        
    ],spacing=25),

    ResponsiveRow([

        para_fun('Thermal\nRunaway'),
        
        para_fun('Over\nTemperature'),

        para_fun('Cell\nOver Volt'),
        
        para_fun('Pack\nOver Volt'),
                
        para_fun('Cell\nUnder Volt'),

        para_fun('Pack\nUnder Volt'),
        
        para_fun('Fan\nStatus'),

        
    ],spacing=25),

    ResponsiveRow([

        para_fun('Mosfet\nStatus'),
                
        para_fun('Pre_charge\nStatus'),

        para_fun('Over Current\nWarning'),

        para_fun('Over Temp\nWarning'),

        para_fun('Error\nFuse'),

        para_fun('Error\nMosfet'),

        para_fun('Error\nPre_charge'),
        
    ],spacing=25),

    ],scroll='hidden',spacing=20)

    c1=Container(content=col1,padding=padding.only(left=40,right=40,top=25),height=370,bgcolor='#FFFFFF',border_radius=8)
    def fault_con(self):
        return self.c1
