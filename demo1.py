import flet
from flet import *
import time
import datetime

def main(page:Page):
    
    def button_clicked(e):
        t.value = f"Your favorite color is:  {cg.value}"
        page.update()
    def hover(e):
        print("COntainer On_Hover")

    date_picker = DatePicker(
            first_date=datetime.datetime(2022, 10, 1),
            last_date=datetime.datetime(2024, 10, 1)
                            )
        
    date_picker1 = DatePicker(
            first_date=datetime.datetime(2022, 10, 1),
            last_date=datetime.datetime(2024, 10, 1)

                            )
    page.overlay.append(date_picker)
    page.overlay.append(date_picker1)
    date_button = ElevatedButton(
        "Start Date",color=colors.BLACK,
        bgcolor='white',
        icon=icons.CALENDAR_MONTH,
        width=120,height=40,col={"md":4.5},
        #on_hover=self.last_date,
        on_click=lambda _: date_picker.pick_date()
        )

    date_button1 = ElevatedButton(
        "End Date",color=colors.BLACK,bgcolor='white',
        icon=icons.CALENDAR_MONTH,
        width=120,height=40,col={"md":4.5},
        #on_hover=self.last_date1,
        on_click=lambda _: date_picker1.pick_date()
        )
    download=ResponsiveRow([Container(expand=True,height=45,content=ElevatedButton(
            "Download",
            
            style=ButtonStyle(
                color=colors.BLACK,
                bgcolor='white',
                
                shape=RoundedRectangleBorder(radius=8),
                
            )))])

    t = Text()
    b = ElevatedButton(text='Submit', on_click=button_clicked)
    cg = RadioGroup(content=Column([
    Row([Radio(value="red", label=''),Text("Hello")]),
    Radio(value="green", label="Green"),
    Radio(value="blue", label="Blue")]))

    c1=Container(height=478,width=581,border_radius=8,padding=padding.only(top=30,left=35,right=40),bgcolor='red',col={"md":6},
                 content=Column([Text('Download Data',font_family='font3',size=18),
                                 Container(height=20,border_radius=8),

                                 RadioGroup(content=Column([
                                    Row([
                                         Radio(value="red", label=''),
                                         Container(height=48,expand=True,bgcolor='#EBEFF9',border_radius=8,padding=padding.only(top=10,left=10),content=ResponsiveRow([Text('Complete SD Card',font_family='font3')]))
                                         ]),

                                         Row([Radio(value='Green',label=''),Container(height=100,expand=True,bgcolor='green',padding=padding.only(top=10,left=10,right=10),content=Column([Text('Based on Percentage',font_family='font3'),
                    ResponsiveRow([TextField(bgcolor='white',width=120,height=40,col={'md':4}),Text('to',text_align=TextAlign.CENTER,col={'md':4}),TextField(bgcolor='white',width=120,height=40,col={'md':4})],spacing=20)],expand=True,scroll='AUTO'))
                    ]),

                    Row([Radio(value='Green1',label=''),Container(height=100,expand=True,bgcolor='green',padding=padding.only(top=10,left=10,right=10),content=Column([Text('Based on Percentage',font_family='font3'),
                                        ResponsiveRow([date_button,Text('to',text_align=TextAlign.CENTER,col={'md':3}),date_button1],spacing=20)],expand=True,scroll='AUTO'))

                    ])

                                         
                                         
             # TextField(bgcolor='white',width=120,height=40,col={'md':4})  TextField(bgcolor='white',width=120,height=40,col={'md':4})


                                 


                #                  TextButton(style=ButtonStyle(color=  colors.BLACK,bgcolor='#EBEFF9',shape=RoundedRectangleBorder(radius=8)),
                # content=Container(height=98,expand=True,padding=padding.only(top=10,left=20,right=20),
                # content=Column([Text('Based on Percentage',font_family='font3'),
                #     ResponsiveRow([TextField(bgcolor='white',width=120,height=40,col={'md':4}),Text('to',text_align=TextAlign.CENTER,col={'md':4}),TextField(bgcolor='white',width=120,height=40,col={'md':4})],spacing=20)]),border_radius=8,)),

                                 
                #                  TextButton(style=ButtonStyle(color=  colors.BLACK,bgcolor='#EBEFF9',shape=RoundedRectangleBorder(radius=8)),
                # content=Container(height=110,expand=True,padding=padding.only(top=10,left=20,right=20),
                # content=Column([Text('Based on date',font_family='font3'),
                #     ]),border_radius=8,)),
                    
                    
                               
                                 
                                 
                                 
                                 
                                 ],expand=True,scroll='AUTO')
                 ),download]))
    

    page.add(Text("Select your favorite color:"), cg, b, t,c1)
    
flet.app(target=main)