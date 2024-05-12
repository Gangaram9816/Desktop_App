import flet
from flet import *


class Profile_btn:
    def __init__(self):
        super().__init__()
    fonts ={
	    "font1":"assets/fonts/RedHatDisplay-Medium.ttf",
        'font2':"assets/fonts/RedHatDisplay-Regular.ttf",
        'font3':"assets/fonts/RedHatDisplay-Bold.ttf"
	    }
    
    c1=Container(height=70,width=500,padding=padding.only(top=16),
                                  content=Column([
                                      ResponsiveRow([ElevatedButton("Set Profile",color=colors.BLACK,bgcolor=colors.WHITE,style=ButtonStyle(
                                    shape=RoundedRectangleBorder(radius=8)),col={'md':4}),

                                    Container(col={'md':4}
                                              ),

                                    ElevatedButton("Get Profile",color=colors.BLACK,bgcolor=colors.WHITE,style=ButtonStyle(
                                    shape=RoundedRectangleBorder(radius=8)),col={'md':4}),
                                          
                                      ])
                        ],expand=True,scroll='hidden'),col={"md":6})
    def profi(self):
    
        return self.c1