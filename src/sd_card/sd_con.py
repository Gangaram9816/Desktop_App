import flet 
from flet import *

class Sd_con:
    def __init__(self):
        super().__init__()
    fonts ={
	    "font1":"assets/fonts/RedHatDisplay-Medium.ttf",
        'font2':"assets/fonts/RedHatDisplay-Regular.ttf",
        'font3':"assets/fonts/RedHatDisplay-Bold.ttf"
 
	    }
    
    c1=Container(height=320,width=588,border_radius=8,
                 padding=padding.only(left=20,top=20,right=20),
        content=Column([
            Text('SD Card',color=colors.BLACK,font_family='font3',size=18),
            ResponsiveRow([Text('Percentage',color=colors.BLACK,font_family='font3',size=16,col={'md':6}),Container(content=Text('0.0%',color=colors.BLACK,text_align=TextAlign.CENTER),col={'md':6})]),
            Divider(),
            ResponsiveRow([Text('Blocks',color=colors.BLACK,font_family='font3',size=16,col={"md":6}),Container(content=Text('0 blocks',color=colors.BLACK,text_align=TextAlign.CENTER),col={'md':6})]),
            Container(height=20),
            ResponsiveRow([Container(ElevatedButton("Refresh",style=ButtonStyle(color=colors.BLACK,bgcolor='white',shape=RoundedRectangleBorder(radius=8),
                )),height=45,border_radius=8,bgcolor='')]),
            ElevatedButton("Download Error logs")
                        ]),
                 bgcolor='#FFFFFF',col={"md":6})
    
    def sd_con(self):
        return self.c1
    
    def refre(self,v):
        v1=str(v.split('SD_INFO')[1]).replace(',','.')

        #v2=str(v1).replace(',','.')

        self.c1.content.controls[1].controls[1].content.value=v1

    