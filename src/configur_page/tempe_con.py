import flet
from flet import *

class Tempe_con:
    def __init__(self):
        super().__init__()

    def tem_return(va):
        return  ResponsiveRow([Container(height=40,padding=padding.only(top=10),content=Text(value =va,color=colors.BLACK,size=16,font_family='font3'),col={"md":6}),
                    Row(col={"md":6},
                    controls=[Container(height=40,width=50,expand=True,padding=padding.only(left=5),
                    content=ResponsiveRow([Container(Text(size=17,text_align=TextAlign.START,color='red'),padding=padding.only(top=10),col={"md":6}),TextField(col={"md":6},read_only=True,color=colors.BLACK,text_size=17,content_padding=padding.only(left=5,bottom=10),border_width=0,width=40,height=40,border_radius=8,bgcolor='#EBEFFA')]),
                    ),Text("C   ",color=colors.BLACK)],),])
    
    c1=Container(content=Column([Text('Temperature',color=colors.BLACK,size=18,font_family='font3'),
                                 tem_return('Over Temperature'),
                    Divider(),
                    tem_return('Temperature Fan On'),
    
                    Divider(),
                    tem_return('Temperature Fan Off'),
   
                    Divider(),
                    tem_return('Thermal Runaway'),

    ],spacing=8,scroll='hidden'),    
        #width=593
        height=350,bgcolor='#FFFFFF',border_radius=8,col={"md":6},padding=padding.only(top=30,left=30,right=36))
    
    def tem_con(self):
        return self.c1
        
        