import flet 
from flet import *

class Mybms:
    def __init__(self):
        super().__init__()

    im=Image(src='assets/images/Vector_2.svg',)
    im1=Image(src='assets/images/Vector_3.svg',)
    im2=Image(src='assets/images/Vector_4.svg',)
    im3=Image(src='assets/images/Vector_5.svg',)


    c1=Container(content=Column([ResponsiveRow([Text('My BMS',color=colors.BLACK,size=20,col={'md':6}),Text('BMS Time',color=colors.BLACK,col={'md':6})],spacing=170,),
            ResponsiveRow([
                Container(padding=padding.only(left=10,top=10),content=Column([im,Text('BMS ID\nFFFFFFFFFF',color=colors.BLACK)],spacing=10),height=106,width=106,border=border.all(1,'black'),border_radius=8,col={"md": 3}),
                Container(padding=padding.only(left=10,top=10),content=Column([Switch(value=False),Text("Live\nRecording",color=colors.BLACK,)]),height=106,width=106,border=border.all(1,'black'),border_radius=8,col={"md": 3}),
                Container(padding=padding.only(left=10,top=10),content=Column([im2,Text('Paralleling\nOn',color=colors.BLACK,)]),height=106,width=106,border=border.all(1,'black'),border_radius=8,col={"md": 3}),
                Container(padding=padding.only(left=10,top=10),content=Column([Switch(value=False),Text("Mosfet Control",color=colors.BLACK,)],spacing=2),height=106,width=106,border=border.all(1,'black'),border_radius=8,col={"md": 3})],spacing=28,
                ),],expand=True,scroll='hidden'),
                         #width=584
                         height=218,bgcolor='#FFFFFF',border_radius=8,col={"md": 6},padding=padding.only(left=25,top=25,right=25))
    
    def mybm(self):
        return self.c1
    
