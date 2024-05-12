import flet 
from flet import *

class Batte_con:
    def ___init__(self):
        super().__init__()
    fonts ={
	    "font1":"assets/fonts/RedHatDisplay-Medium.ttf",
        'font2':"assets/fonts/RedHatDisplay-Regular.ttf",
        'font3':"assets/fonts/RedHatDisplay-Bold.ttf"
 
	    }
    

    drop= Dropdown(
        width=40,
        col={"md":6},
        text_size=12,
        content_padding=padding.only(left=5,bottom=10),
        options=[
            dropdown.Option("NMC"),
            dropdown.Option("LFP"),
            dropdown.Option("LTO"),
        ],
    )


    def con_return(val,v):
        return ResponsiveRow([Container(height=40,padding=padding.only(top=10),content=Text(color=colors.BLACK,value=val,size=16,font_family='font3'),col={"md":6}),
                    Row(col={"md":6},
                    controls=[Container(height=40,width=50,expand=True,padding=padding.only(left=5),
                    content=ResponsiveRow([Container(Text(size=17,text_align=TextAlign.START,color='red'),padding=padding.only(top=10),col={"md":6}),TextField(col={"md":6},read_only=True,color=colors.BLACK,text_size=17,content_padding=padding.only(left=5,bottom=10),border_width=0,width=40,height=40,border_radius=8,bgcolor='#EBEFFA')]),
                    ),Text(value=v,color=colors.BLACK)],),])

    c1=Container(content=Column([Text('Battery',color=colors.BLACK,size=18,font_family='font3'),
                    con_return('Battery Capacity','Ah  '),
                                             
                    Divider(),
                    con_return('Battery Application','     '),
                
                    Divider(),
                    # con_return('Chemistry','     '),s

                    ResponsiveRow([Container(height=40,padding=padding.only(top=10),content=Text(color=colors.BLACK,value="Chemistry",size=16,font_family='font3'),col={"md":6}),
                    Row(col={"md":6},
                    controls=[Container(height=40,width=50,expand=True,padding=padding.only(left=5),
                    content=ResponsiveRow([Container(Text(size=17,text_align=TextAlign.START,color='red'),padding=padding.only(top=10),col={"md":6}),drop]),
                    ),Text(value='     ',color=colors.BLACK)],),]),
                    
                    Divider(),
                    con_return('Max DV','V   '),
    
                    Divider(),
                    con_return('Balancing Enable','     '),

                    Divider(),
                    con_return('Balancing Start DV','V   '),

                    

                    


                    #width=593,expand=True
    ],spacing=8,scroll='hidden'),
        
        height=500,bgcolor='#FFFFFF',border_radius=8,col={"md":6},padding=padding.only(top=30,left=30,right=36))
    def bat_con(self):
        
        return self.c1
    


#TextField(col={"md":6},read_only=True,color=colors.BLACK,text_size=17,content_padding=padding.only(left=5,bottom=10),border_width=0,width=40,height=40,border_radius=8,bgcolor='#EBEFFA')