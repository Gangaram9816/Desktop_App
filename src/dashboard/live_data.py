from .mybms import *
import datetime
import os, csv
from src.log import logger

class Live_data:
    def __init__(self):
        super().__init__()
        self.my=Mybms()
    def cc_tt(self,v,v1,v2):
        global cc
        
        cc=[v,v1,v2]
        
    def liv(self,e):
        global filename
        try:

        
            if self.my.c1.content.controls[1].controls[1].content.controls[0].value:
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

                    fil= os.path.join(os.path.expanduser("~"), 'Downloads')
                    
                    path = f"d_{timestamp}.csv"
                    filename=os.path.join(fil,path)

                    cell_col=[]
                    tt_col=[]
                    for i in range(int(cc[0])):
                        cell_col.append('Cell'+str(i+1)+' mV')
                    for j in range(int(cc[1])):
                        tt_col.append('Temp'+str(j+1)+' C')
                    
                    
                    #col_names=['Cell1 mV','Cell2 mV','Cell3 mV','Cell4 mV','Cell5 mV','Cell6 mV','Cell7 mV','Cell8 mV','Cell9 mV','Cell10 mV','Cell11 mV','Cell12 mV','Cell13 mV','Cell14 mV','Cell15 mV','Cell16 mV','Cell17 mV','Cell18 mV','Cell19 mV','Cell20 mV','Temp1 C','Temp2 C','Temp3 C','Temp4 C','Temp5 C','Temp6 C','Voltage','Current','SOC','Charging','Dischsrging','Mode']
                    
                    col_names=['BMS_IDS']+cell_col+tt_col+['Voltage','Current','SOC','Charging','Dischsrging','Mode']



                    with open(filename, 'a', newline='') as csvfile:
                        csv_writer = csv.writer(csvfile)      
                        csv_writer.writerow(col_names) 
                    logger.info('In live_data .csv file is created')
        except Exception as e:
            logger.error('In Live_data , liv : %s',e)
          


    def volta(self,v):
 
        global li,cc
        
        li=[cc[2]]
         
        if self.my.c1.content.controls[1].controls[1].content.controls[0].value:

            try:

                li=li+v

            except Exception as e:
                logger.error('In liv_data volta : %s',e)


        else:
            pass

    def te(self,v):
        global li
        if self.my.c1.content.controls[1].controls[1].content.controls[0].value:
            
            try:
                li=li+v
                
            except Exception as e:
                logger.error('In liv_data te : %s',e)
            
        else:
            pass

    def soc(self,v):
        global li
        if self.my.c1.content.controls[1].controls[1].content.controls[0].value:
            pv=v[1]
            pc=v[2]
            soc=v[3]
            er1=format(int(v[0]),'08b')[5:]
            
            #ch, disch=('Off', 'On')  if int(er1,2) in [0,1,3,4] else ('On' ,'Off')
            try:
                ch='Off' if int(er1,2) in [0,1,3,4] else 'On'
                disch='Off' if int(er1,2) in [0,1,2,4] else 'On'
                mod='Idle' if int(er1,2) in [0,1,4] else "Charging" if int(er1,2) ==2 else "Discharging"
                li1=[pv,pc,soc,ch,disch,mod]
                li=li+li1
            
                with open(filename, 'a', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerow(li)

            except Exception as e:
                logger.error('In live_data soc : %s',e)
                
        
        else:
            pass
            
            