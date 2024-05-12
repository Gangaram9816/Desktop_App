import flet
from flet import *

class Curren_con:
    def __init__(self):
        super().__init__()
    fonts ={
	    "font1":"assets/fonts/RedHatDisplay-Medium.ttf",
        'font2':"assets/fonts/RedHatDisplay-Regular.ttf",
        'font3':"assets/fonts/RedHatDisplay-Bold.ttf"
 
	    }
    
    def conta_return(va,v1):
        return ResponsiveRow([Container(height=40,padding=padding.only(top=10),content=Text(value=va,color=colors.BLACK,size=16,font_family='font3'),col={"md":6}),
                                                Row([Container(padding=padding.only(left=5),expand=True,
                                                          content=ResponsiveRow([Container(Text(size=17,text_align=TextAlign.START,color='red'),padding=padding.only(top=10),col={"md":6}),TextField(col={"md":6},read_only=True,color=colors.BLACK,text_size=17,content_padding=padding.only(left=5,bottom=10),border_width=0,width=40,height=40,border_radius=8,bgcolor='#EBEFFA')]),
                                                          
                                                          height=40,width=50,),Text(value=v1,color=colors.BLACK)],col={"md":6})])
    
    c1=Container(content=Column([Text('Current',color=colors.BLACK,size=18,font_family='font3'),
                                 
                                conta_return('Continuous Load Current','A   '),
                                Divider(),
                                conta_return('Load Current Delay','s   '),
                                Divider(),
                                conta_return('Over Current Discharging','A   '),
                                Divider(),
                                conta_return('Over Current Charging','A   '),
                                Divider(),
                                conta_return('Peak Pack Current','A   '),
                                Divider(),
                                conta_return('Peak Current Delay','s  '),
                                Divider(),
                                conta_return('CC Current','A   '),
                                Divider(),
                                conta_return('CV Cutoff Current','A   '),
                                
                                     ],scroll='hidden'),
                                     #width=593
                            height=650,bgcolor='#FFFFFF',border_radius=8,col={"md":6},padding=padding.only(top=30,left=30,right=36))

    def cur_con(self):
        return self.c1