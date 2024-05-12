
import flet
from flet import *
from flet.plotly_chart import PlotlyChart
import plotly.express as px
from .mybms import *
from .temperature import *
from .batterystats import *
from .voltage import *
from .faults import *


# class Dashboard:
#     def __init__(self):
#         super().__init__()

#     bms=Mybms()
#     tem=Temperature()
#     bts=Batterystats()
#     vo=Voltage()
#     flt=Fault()
#     fonts ={
#         "font1":"assets/fonts/RedHatDisplay-Medium.ttf",
#         'font2':"assets/fonts/RedHatDisplay-Regular.ttf",
#         'font3':"assets/fonts/RedHatDisplay-Bold.ttf"

#         }



#     s1=Container(Column([bms.mybm(),
#                         tem.build1(),
                        
#                         ],expand=True,scroll='always',spacing=26),
#         width=584,height=578,expand=True,border_radius=8,
#                 col={'md':6},
                        
#     )
    
#     s2=Container(content=bts.btrsts(),width=584,height=571,bgcolor='#FFFFFF',border_radius=8,
                                                    
#                                 expand=True,col={ "md": 6, },padding=padding.only(top=25,left=25,right=25))

#     c1=Column(height=900,width=1220,controls=[Container(content=Column([Text('Dashboard',color=colors.BLACK,size=32,font_family='font3'),Text('Live Data Analytics',color=colors.BLACK)],spacing=1,alignment=MainAxisAlignment.END),height=130,bgcolor='#F0F0F0',),
#                                             ResponsiveRow([s1,s2],spacing=26),
#                                             vo.build1(),
#                                             flt.fault_con(),
#                                         Container(height=40,bgcolor='#F0F0F0')
#                                         ],expand=True,scroll=ScrollMode.HIDDEN,spacing=20)


    
#     def dashbo(self):
#         print(self.c1.uid)
#         return self.c1
















class Dashboard:
    def __init__(self):
        super().__init__()
        self.fonts = {
            "font1": "assets/fonts/RedHatDisplay-Medium.ttf",
            'font2': "assets/fonts/RedHatDisplay-Regular.ttf",
            'font3': "assets/fonts/RedHatDisplay-Bold.ttf"
        }

        self.bms = Mybms()
        self.tem = Temperature()
        self.bts = Batterystats()
        self.vo = Voltage()
        self.flt = Fault()

        self.s1 = Container(
            content=Column(
                [
                    self.bms.mybm(),
                    self.tem.build1()
                ],
                expand=True,
                scroll='always',
                spacing=26
            ),
            width=584,
            height=578,
            expand=True,
            border_radius=8,
            col={'md': 6},
            key="s1"  # Unique key for the container
        )

        self.s2 = Container(
            content=self.bts.btrsts(),
            width=584,
            height=571,
            bgcolor='#FFFFFF',
            border_radius=8,
            expand=True,
            col={"md": 6},
            padding=padding.only(top=25, left=25, right=25),
            key="s2"  # Unique key for the container
        )

        self.c1 = Column(
            height=900,
            width=1220,
            controls=[
                Container(
                    content=Column(
                        [
                            Text('Dashboard', color=colors.BLACK, size=32, font_family=self.fonts['font3']),
                            Text('Live Data Analytics', color=colors.BLACK)
                        ],
                        spacing=1,
                        alignment=MainAxisAlignment.END
                    ),
                    height=130,
                    bgcolor='#F0F0F0',
                    key="header"
                ),
                ResponsiveRow([self.s1, self.s2], spacing=26),
                self.vo.build1(),
                self.flt.fault_con(),
                Container(height=40, bgcolor='#F0F0F0', key="footer")
            ],
            expand=True,
            scroll=ScrollMode.HIDDEN,
            spacing=20,
            key="c1"  # Unique key for the main column
        )

    def dashbo(self):
        print(self.c1.uid)  # Example of accessing controls by their key
        return self.c1

