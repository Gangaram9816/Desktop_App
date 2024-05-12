import flet
from flet import *


class Pro_con:
    

    global l1
    l1=[]

    def __init__(self):
        
        super().__init__()
        
    dd1=Container(padding=padding.only(right=130),height=45,width=80,
                  content=Container(border_radius=8,bgcolor='#EBEFFA',content=Dropdown(
                      content_padding=padding.only(bottom=10,left=5),
                      border_width=0,
                            options=[]
                        )
                        ),
                       col={'md':6})
    
    fonts ={
	    "font1":"assets/fonts/RedHatDisplay-Medium.ttf",
        'font2':"assets/fonts/RedHatDisplay-Regular.ttf",
        'font3':"assets/fonts/RedHatDisplay-Bold.ttf"

	    }
    
    c2=Container(content=Column([Text('Profile',color=colors.BLACK,font_family='font3',size=18),
                                 ResponsiveRow([Container(padding=padding.only(top=30),content=ResponsiveRow([Text('Profile Name',color=colors.BLACK,font_family='font3',size=16,col={'md':6}),
                                           dd1 ]),col={"md":6}),

                                                Container(padding=padding.only(top=30,right=10), col={"md":6},content=ResponsiveRow([
                                                    Container(col={'md':3},content= ElevatedButton("Add Profile",bgcolor='#FFFFFF', color='#345DC7',
                                                                                    style=ButtonStyle(bgcolor='#FFFFFF', color='#345DC7',shape=RoundedRectangleBorder(radius=6),
                                                                                                            ),
                                                                                                        )),
                                        Container(col={'md':3},content= ElevatedButton("Save",bgcolor='#FFFFFF', color='#345DC7',
                                                                style=ButtonStyle(bgcolor='#FFFFFF',color='#345DC7', shape=RoundedRectangleBorder(radius=6),  ), )),     

                                                                                                                     
                                    Container(col={'md':3},content= ElevatedButton("Remove",bgcolor='#FFFFFF', color='#345DC7',
                                                                    style=ButtonStyle(shape=RoundedRectangleBorder(radius=6),), )),

                                    Container(col={'md':3},content= ElevatedButton("Edit",bgcolor='#FFFFFF', color='#345DC7',
                                                            style=ButtonStyle(bgcolor='#FFFFFF', color='#345DC7',shape=RoundedRectangleBorder(radius=6),
                                                                                                                                    ),
                                                                                                                                )),   ],)),
                                    ]),],scroll='hidden'),
                                   
                           # width=1213
                            height=136,bgcolor='#FFFFFF',border_radius=8,padding=padding.only(left=20,top=15))
    

    def get_v(self,v):
        global v1
        v1=v[0]
    
    def p_con(self):
        return self.c2