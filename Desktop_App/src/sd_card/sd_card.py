import flet
from flet import *
from .sd_con import *
from .download_data_con import *


class SD_Card:
    def __init__(self):
        super().__init__()
    dw_con=Download_data(flet.Page)
    sd_cont=Sd_con()
    c1=Column([Container(content=Column([Text('SD Card',color=colors.BLACK,size=32,font_family='font3'),Text('Manage, download and update SD card data',color=colors.BLACK)],spacing=1,alignment=MainAxisAlignment.END),height=130),
            Container(height=25),
        ResponsiveRow([sd_cont.sd_con(),dw_con.download_con(),],spacing=30),
        #ElevatedButton("DOwnload Error logs")

    ],height=1000,width=1220,expand=True,scroll='hidden')

    def sd_card_con(self):
        print(self.c1.uid)
        return self.c1