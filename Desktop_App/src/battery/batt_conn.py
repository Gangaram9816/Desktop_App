import flet 
from flet import *

class Batt_conn:
    def __init__(self):
        super().__init__()
    fonts ={
	    "font1":"assets/fonts/RedHatDisplay-Medium.ttf",
        'font2':"assets/fonts/RedHatDisplay-Regular.ttf",
        'font3':"assets/fonts/RedHatDisplay-Bold.ttf"
 
	    }
    
            
    dd2 = Dropdown(
        bgcolor=colors.INDIGO_50,color=colors.BLACK,
                options=[
                        dropdown.Option("125"),
                        dropdown.Option("250"),
                        dropdown.Option("500"),
                        
                    ],height=50,border_width=0,text_size=12,width=160,content_padding=padding.only(bottom=10,left=10),)
    
    dd2.value='250'
    c1=Column(controls=[Text('Battery Connection Status',color=colors.BLACK,font_family='font3',size=32),
                        Divider(color='#FFFFFF'),

        ResponsiveRow([Text('OBD Serial',color=colors.BLACK,font_family='font3',size=16,col={"md":6}),Text('OBD Serial',text_align=TextAlign.CENTER,col={"md":6})]),

        Divider(),
        ResponsiveRow([Text('Connection Port',color=colors.BLACK,font_family='font3',size=16,col={"md":6}),Text('COM',text_align=TextAlign.CENTER,col={"md":6})]),
        Divider(),

        ResponsiveRow([Text('Baud rate',color=colors.BLACK,font_family='font3',size=16,col={"md":6}),Container(padding=padding.only(left=40),border_radius=8,height=40,
                                                                                    content=Container(border_radius=8,bgcolor='#EBEFF9',content=dd2)
                                                                                            ,col={"md":6})]),
        Container(height=8),
        Container(height=40,width=550,content=ElevatedButton("Connect",
                                style=ButtonStyle(color=  colors.BLACK,shape=RoundedRectangleBorder(radius=8),
                    ),
                    )),
        ],

        height=345,width=580,expand=True,scroll='hidden')
    def bat_conn(self):
        return self.c1
    
