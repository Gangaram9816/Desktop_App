import flet 

from flet import *
from .batt_conn import *
from .general_stats import *



class Battery:
    def __init__(self):
        
        super().__init__()
    ba=Batt_conn()
    gen=General_st()

    c1=Column([Container(height=100),
        ResponsiveRow([Container(content=ba.bat_conn(),padding=padding.only(left=25,top=25,right=25),
                        border_radius=8,height=350,width=582,bgcolor='#FFFFFF',col={"md":6}),

                       Container(content=gen.gene_st(),padding=padding.only(left=30,top=30,right=30),
                                border_radius=8, height=650,width=582, expand=True,bgcolor='#FFFFFF',col={"md":6})],spacing=34)
                            ,Container(height=20),

    ],height=800,width=1200,scroll='hidden',expand=True)

    def batter_page(self):
        return self.c1