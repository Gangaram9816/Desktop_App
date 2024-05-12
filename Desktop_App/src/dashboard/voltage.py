import flet
from flet import *
from flet.plotly_chart import PlotlyChart
import plotly.express as px
from .live_data import *
from src.log import logger

class Voltage:
    def __init__(self):
        
        
        super().__init__()
        self.li=Live_data()
        
    fonts ={
	    "font1":"assets/fonts/RedHatDisplay-Medium.ttf",
        'font2':"assets/fonts/RedHatDisplay-Regular.ttf",
        'font3':"assets/fonts/RedHatDisplay-Bold.ttf"
 
	    }
    
    x1=['Cell 1','Cell 2','Cell 3','Cell 4','Cell 5','Cell 6','Cell 7','Cell 8','Cell 9','Cell 10','Cell 11','Cell 12','Cell 13','Cell 14']
    y1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]


    fig = px.bar(x=x1, y=y1, height=500, width=1230,text_auto=True)
    fig.update_layout(yaxis_range=[0, 6], xaxis_title=None, yaxis_title=None,xaxis_tickfont=dict(size=16),yaxis_tickfont=dict(size=16))

    fig.update_layout(title_font=dict(color="black"))
   
    fig.update_traces(textfont_size=16,textposition='outside')
    chart= PlotlyChart(fig,expand=True)

    def cc_val(self,v):
   
        x_new = [f'Cell {i + 1}' for i in range(int(v))]
       
        y_new=[0 for i in range(int(v))]
        self.fig.data[0].y=list(y_new)
        self.fig.data[0].x=list(x_new)
        
       
    r1=Row([Column([Text('Cell Difference',color=colors.BLACK),Text('    0',color=colors.BLACK)]),Column([Text('Average',color=colors.BLACK),Text('   0',color=colors.BLACK)]),Column([Text('High',color=colors.BLACK),Text(' 0',color=colors.BLACK)]),Column([Text('Low',color=colors.BLACK),Text('0',color=colors.BLACK)])],top=20,right=70,expand=True)
   
    c1=Stack([Container(expand=True,alignment=alignment.bottom_left,content=chart,height=540,border_radius=8,bgcolor='#FFFFFF',),Text('Cell Voltage',color=colors.BLACK,font_family='font3',size=16,left=25,top=15),r1])

    def build1(self):
       
        return self.c1
    
    def get_vol(self,v):
        
        try:
        
            v1=[float (j) for j in v.split('CELLVOL')[1].split(',')]
 
            self.fig.data[0].y = v1
          

            self.li.volta(v1)
        
            self.r1.controls[1].controls[1].value="{:.2f}".format(sum(v1)/len(v1))

            self.r1.controls[2].controls[1].value=str(max(v1))
            self.r1.controls[3].controls[1].value=str(min(v1))
            self.r1.controls[0].controls[1].value=str(max(v1)-min(v1))
            self.fig.data[0].text = [str(val) for val in v1]
            
            self.c1.controls[0].content=self.chart
            logger.info('Voltage value :%s', v1)
            
            
        except Exception as e:
            logger.error('In voltage get_vol : %s',e)

        


            
       

   
        
        

    

    