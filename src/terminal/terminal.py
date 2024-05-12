import flet
from flet import *
import time
from src.log import logger
class Terminal:
    def __init__(self):
        self.success=False
        
        # def change_va():
        #     success=False
        super().__init__()
        
   
    
    b1=ElevatedButton("Send",style=ButtonStyle(
                    bgcolor='#345DC7',color=colors.WHITE,
                                    shape=RoundedRectangleBorder(radius=8)))
    dd = Dropdown(
        width=150,
        height=45,
        color=colors.BLACK,
        #bgcolor=colors.WHITE,
        content_padding=padding.only(left=15,bottom=10),
        options=[
            dropdown.Option("CR"),
            dropdown.Option("LF"),
            dropdown.Option("CRLF"),
        ],
    )



    # dd=Container(border_radius=8,width=50,content=Dropdown(
    #                   content_padding=padding.only(bottom=10,left=15),
    #                   border_width=0,color='black',
    #                         options=[dropdown.Option("CR"),
    #         dropdown.Option("LF"),
    #         dropdown.Option("CRLF"),]
    #                     )
    #                     )
                       
    dd.value="CRLF"
    
    con=Column([Container(content=Column([Text('Terminal Panel',color=colors.BLACK,size=32,font_family='font3')],spacing=1,alignment=MainAxisAlignment.END),height=120,width=1100),
                ResponsiveRow([Container(content=Column([]),padding=padding.only(left=15,top=15),height=500,bgcolor='#FFFFFF',border_radius=8,expand=True,col={"md":12}),]),
                ResponsiveRow([TextField(hint_text="Write a command",color=colors.BLACK,bgcolor=colors.WHITE,content_padding=padding.only(bottom=10,left=10),height=40,col={"md":10}),Container(content=b1,height=40,border_radius=8,col={"md":2})])
                ,dd,Container(height=10)],height=770,expand=True,width=1200,scroll='hidden')
    
    

    def ter(self):
        return self.con

    def term1(self,e):
        try:
            self.success = True
        
            v=self.con.controls[2].controls[0].value
        
            if self.dd.value=='CR':
                v1=(v+'\r').encode()
            elif self.dd.value=='LF':

                v1=(v+'\n').encode()
            else:
                v1=(v+'\r\n').encode()

            
            self.b1.data.write(v1)
            time.sleep(0.1)
            #self.success = True
            if v=='clear' or v=='CLEAR':
                self.con.controls[1].controls[0].content.controls.clear()
                
            elif v=='AT+BAUD=1':
                self.b1.data.baudrate=9600
        
            elif v== 'AT+BAUD=2':
                self.b1.data.baudrate=57600
                
            elif v=='AT+BAUD=3':
                self.b1.data.baudrate=115200
            
            #self.con.controls[2].controls[0].value=''
        except Exception as exc:
            logger.error('In terminal termi1 :%s',exc)
            
    # def change_va(self):
    #     self.success=False
        #return self.success
        
        
    # def v_return(self,v):
        
    #     print(self.success)
        
    #     if self.success:
            
    #         print('value in v terminal',v)
            
            
            #pass
            
            
            
    