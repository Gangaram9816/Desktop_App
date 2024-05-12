import flet 
from flet import *
from flet.plotly_chart import PlotlyChart
import plotly.express as px
import numpy as np
from .live_data import *
from src.log import logger
class Temperature:
    def __init__(self):
        super().__init__()
        self.li=Live_data()

    fonts ={
	    "font1":"assets/fonts/RedHatDisplay-Medium.ttf",
        'font2':"assets/fonts/RedHatDisplay-Regular.ttf",
        'font3':"assets/fonts/RedHatDisplay-Bold.ttf"
 
	    }
   
    x1=['Zone 1','Zone 2','Zone 3','Zone 4','Zone 5','Zone 6']    
    y1=[0,0,0,0,0,0]
  
    
    fig1 = px.bar(x=x1,y=y1,height=450,width=1000,text_auto=True)
    fig1.update_traces(textposition='outside', textfont=dict(size=20))
                            
    fig1.update_layout(yaxis_range=[0,120],xaxis_title=None, yaxis_title=None,title="Temperature",  )
   
    fig1.update_layout(
        xaxis=dict(tickfont=dict(size=22.5), title=None, title_font=dict(size=22.5)),
        yaxis=dict(tickfont=dict(size=22.5), title=None, title_font=dict(size=22.5)),
        title_font=dict(size=30)
        )
    fig1.update_traces(textfont_size=20,textposition='outside')
    chart1= PlotlyChart(fig1,expand=True)
    
    def tt_val(self,v):

       
        x_new = [f'Zone {i + 1}' for i in range(int(v))]
        
        y_new=[0 for i in range(int(v))]
        self.fig1.data[0].y=list(y_new)
        self.fig1.data[0].x=list(x_new)
        
    r1=Row([Column([Text('Temp Difference',color=colors.BLACK),Text('   0',color=colors.BLACK)],spacing=1),Column([Text('Average',color=colors.BLACK),Text('  0',color=colors.BLACK)],spacing=1),Column([Text('High',color=colors.BLACK,),Text('0',color=colors.BLACK,)],spacing=1),Column([Text('Low',color=colors.BLACK),Text('0',color=colors.BLACK)],spacing=1)],top=10,right=30,expand=True)
    c1=Stack([Container(alignment=alignment.bottom_left,content=chart1,height=328,bgcolor='#FFFFFF',border_radius=9),r1])
    
    def build1(self):
        return  self.c1
    
    def get_temp(self,v):
        try:
           
            v1=[int(i) for i in v.split('THERMIS')[1].split(',')]
            self.li.te(v1)
           
            self.fig1.data[0].y = v1
            self.r1.controls[1].controls[1].value="{:.2f}".format(sum(v1)/6)
            self.r1.controls[2].controls[1].value=str(max(v1))
            self.r1.controls[3].controls[1].value=str(min(v1))
            self.r1.controls[0].controls[1].value=str(max(v1)-min(v1))

            self.fig1.data[0].text = [str(val) for val in v1]
           
            self.c1.content=self.chart1
            logger.info('Temperature value :%s', v1)
        except Exception as e:
            logger.error('In temperature get_temp: %s',e)
            
       
