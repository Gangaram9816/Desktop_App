import threading
import time
import flet 
from flet import *
from datetime import datetime
import os, csv
import queue
from src.log import logger
from datetime import datetime 
import datetime 

class Download_data:

    any_btn=False
    sd_date=False
    sd_comple=False
    sd_perc=False
    thred=False
    my_thread=None
    
    def __init__(self,page:Page):
        self.page=page
        self.csvfile=None
        self.filename1=None
        self.date_dlg = AlertDialog(
        title=Text("Invalid Date"),)

        self.date_dlg1 = AlertDialog(
        title=Text("Data Downloading....."),
        modal=True,
        #on_dismiss=self.download_dlg1
        )

        self.initial = AlertDialog(
        title=Text("Initializing....."),
        modal=True,
        #on_dismiss=self.download_dlg1
        )

        self.dlg_modal = AlertDialog(
        title=Text("Invalid Values"),)

        self.dlg_err=AlertDialog(title=Text('Fail..'))

        
        self.date_picker = DatePicker(
            first_date=datetime.datetime(2022, 10, 1),
            last_date=datetime.datetime(2024, 10, 1)
                            )
        
        self.date_picker1 = DatePicker(
            first_date=datetime.datetime(2022, 10, 1),
            last_date=datetime.datetime(2024, 10, 1)
                            )
        
        self.dlg_modal = AlertDialog(
        title=Text("Invalid Values"),)

        self.date_button = ElevatedButton(
        "Start Date",color=colors.BLACK,
        bgcolor='white',
        icon=icons.CALENDAR_MONTH,
        width=120,height=40,col={"md":4.5},
        on_hover=self.last_date,
        on_click=lambda _: self.date_picker.pick_date()
        )

        self.date_button1 = ElevatedButton(
        "End Date",color=colors.BLACK,bgcolor='white',
        icon=icons.CALENDAR_MONTH,
        width=120,height=40,col={"md":4.5},
        on_hover=self.last_date1,
        on_click=lambda _: self.date_picker1.pick_date()
        )

        self.sd_time1=ResponsiveRow([self.date_button,Text('to',text_align=TextAlign.CENTER,col={'md':3}),self.date_button1])

        self.filename1=''


        super().__init__()
    fonts ={
	"font1":"assets/fonts/RedHatDisplay-Medium.ttf",
    'font2':"assets/fonts/RedHatDisplay-Regular.ttf",
    'font3':"assets/fonts/RedHatDisplay-Bold.ttf"
 
	}

    global cc_tt
    cc_tt=[]

    def last_date(self,e):
        self.date_picker.last_date=datetime.datetime.now()
    def last_date1(self,e):
        self.date_picker1.last_date=datetime.datetime.now()

    def change_date(self,e):
        global d1
        
        d1=self.date_picker.value.strftime("%d/%m/%y")
        self.date_button.text=d1
        
    def change_date1(self,e):
        global d2
        d2=self.date_picker1.value.strftime("%d/%m/%y")
        self.date_button1.text=d2
        
    def download_dlg1(self,e):
        self.page.dialog=self.date_dlg1
        self.date_dlg1.open=True
        self.page.update()

    time1=TextField(label='Start Date',bgcolor='white',width=120,height=40,hint_text='dd/mm/yy',col={'md':4})
    time2=TextField(label='End date',bgcolor='white',width=120,height=40,hint_text='dd/mm/yy',col={'md':4})
    sd_time1=ResponsiveRow([time1,Text('to',text_align=TextAlign.CENTER,col={'md':4}),time2])

    download=ResponsiveRow([Container(expand=True,height=45,content=ElevatedButton(
            "Download",
            
            style=ButtonStyle(
                color=colors.BLACK,
                bgcolor='white',
                
                shape=RoundedRectangleBorder(radius=8),
                
            )))])
    
    data_queue1 = queue.Queue()

    def radio_clicked(self,e):
        self.download.controls[0].content.style.bgcolor='#EBEFF9'
        self.download.controls[0].content.style.color='black'
        
    
    c1=Container(height=478,width=581,border_radius=8,padding=padding.only(top=30,left=35,right=40),bgcolor='#FFFFFF',col={"md":6},
                 content=Column([Text('Download Data',font_family='font3',size=18),
                                Container(height=20,border_radius=8),

                                RadioGroup(content=Column([
                                    Row([
                                         Radio(value="Com_SD", label=''),
                                         Container(height=48,expand=True,bgcolor='#EBEFF9',border_radius=8,padding=padding.only(top=10,left=10),content=ResponsiveRow([Text('Complete SD Card',font_family='font3')]))
                                         ]),

                                    Row([Radio(value='perc',label=''),
                                        Container(height=100,expand=True,border_radius=8,bgcolor='#EBEFF9',padding=padding.only(top=10,left=10,right=10),content=Column([Text('Based on Percentage',font_family='font3'),
                                    
                                    ResponsiveRow([TextField(bgcolor='white',width=120,height=40,col={'md':4}),Text('to',text_align=TextAlign.CENTER,col={'md':4}),TextField(bgcolor='white',width=120,height=40,col={'md':4})],spacing=20)],expand=True,scroll='AUTO'))
                                        ]),

                                    Row([Radio(value='dat_e',label=''),Container(height=110,expand=True,border_radius=8,bgcolor='#EBEFF9',padding=padding.only(top=10,left=10,right=10),content=Column([Text('Based on Dates',font_family='font3'),
                                        ],expand=True,scroll='AUTO'))
                                        ])
                                                        ])
                                         ),

                                download])
                )
    
    def cc_tempe(self,v):
        global cc_tt
       
        cc_tt=v
        #vol_va
    
    global csvfile

    def file_create(self):

        #global csvfile,filename1,cc_tt
        global cc_tt
        self.filename1=''
        try:

            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

            fil= os.path.join(os.path.expanduser("~"), 'Downloads')
            
            path = f"SD_CARD_{timestamp}.csv"
            self.filename1=os.path.join(fil,path)

            col1=[]
            col2=[]
            for i in range(int(cc_tt[0])):
                col1.append('Cell'+str(i+1)+' mV')
            
            for i in range(int(cc_tt[1])):
                col2.append('Temp'+str(i+1)+' C')
                
            
            #col_names=['Time','Voltage','Mode','Current','Temp1 C','Temp2 C','Temp3 C','Temp4 C','Temp5 C','Temp6 C','Cell1 mV','Cell2 mV','Cell3 mV','Cell4 mV','Cell5 mV','Cell6 mV','Cell7 mV','Cell8 mV','Cell9 mV','Cell10 mV','Cell11 mV','Cell12 mV','Cell13 mV','Cell14 mV','Max Cell','Min Cell','Cell Difference','State of Charge(SOC)','Fault','Charging','DisCharging']
            
            col_names=['BMS_ID','Time','Voltage','Mode','Current']+col2+col1+['Max Cell','Min Cell','Cell Difference','State of Charge(SOC)','Fault','Charging','DisCharging']
        
            with open(self.filename1, 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)      
                csv_writer.writerow(col_names) 
            
            self.download.controls[0].content.style.color='white'
            self.download.controls[0].content.style.bgcolor='#345DC7'
            
        except Exception as e:

            logger.error('In download_data_con File_create :%s',e)

    def request_data_info(self):

        self.download.controls[0].content.data.write(('AT+DATAINFO'+'\r\n').encode())
        print("AT+DATAINFO send")

        self.page.dialog=self.initial
        self.initial.open=True

        start_time = time.time()

        while  not cc_tt:
            if time.time() - start_time > 60:
                    return False
                    
            continue

        return True
    


    def download_sd(self,e):
        global cc_tt
        cc_tt=[]

        try:

            valu=self.request_data_info()
            
            if not valu:
                self.initial.open=False
                self.page.update()
            
                self.page.dialog=self.dlg_err
                self.dlg_err.open=True
                self.page.update()
            

                
            global csvfile,d1,d2,filename1
            
            if self.c1.content.controls[2].value =='dat_e':
                try:

                    t1=datetime.datetime.strptime(d1, "%d/%m/%y").date()
                    t2=datetime.datetime.strptime(d2, "%d/%m/%y").date()
                    
                    today1=datetime.datetime.today().date()
                    t11=d1.replace('/',',')

                    t12=d2.replace('/',',')
                    if t1<=t2 and t2 <=today1:
                        
                        self.download.controls[0].content.data.write(('AT+DATA=1'+','+t11+','+t12+'\r\n').encode('utf-8'))

                        self.file_create()

                        logger.info('In download_sd_con, csv file created for date input')
                
                    if t2<t1:
                        self.download.controls[0].content.data.write(('AT+DATA=1'+','+t12+','+t11+'\r\n').encode('utf-8'))

                        self.file_create()

                        logger.info('In download_sd_con, csv file created for date input')

                       
                        self.page.update()

                except Exception as e:

                    logger.error('Exception in Download_SD in date fun :%s',e)
                    

            elif self.c1.content.controls[2].value =='Com_SD':

                try:
                    self.download.controls[0].content.data.write(('AT+DATA=3\r\n').encode('utf-8'))

                    self.file_create()

                    logger.info('In download_data_con, csv file created for complete sd card download')
        
                except Exception as e:
                    logger.error('Exception in Download_SD in Complete SD fun :%s',e)
                    
                
            elif self.c1.content.controls[2].value =='perc':

                try:

                    v1=self.c1.content.controls[2].content.controls[1].controls[1].content.controls[1].controls[0].value
                    v2=self.c1.content.controls[2].content.controls[1].controls[1].content.controls[1].controls[2].value
                    
                    
                    if float(v1)>=1 and float(v2)<=100 and float(v1)<=float(v2):
                        v1=str(float(v1)*100).zfill(4)
                        v2=str(float(v2)*100).zfill(5)
                    

                        self.download.controls[0].content.data.write(('AT+DATA=2,'+v1+','+v2+'\r\n').encode('utf-8'))

                        self.file_create()

                        logger.info('In download_data_con, csv file created for sd_card percentage')
                        
                    else:
                        self.page.dialog=self.dlg_modal
                        self.dlg_modal.open=True
                except Exception as e:
                    logger.error('In download_data_con sd_card Percentage :%s',e)
        except Exception as e1:
            logger.error('In download_data_con sd_card Percentage data info :%s',e)
    

    def sd_card_sav(self,v):

        
        global filename1,cc_tt

     
        d1=[]

        try:
            v=v.split('SD_CARD')[1].split(',')
            print('value in sd card',v)
           

            self.page.dialog.open = False
            self.page.update()
            
            self.page.dialog=self.date_dlg1
            self.date_dlg1.open=True
            cou=11+(int(cc_tt[0])*2)+int(cc_tt[1])+3

            #print('count loop',cou)
           
            for i in range(0,len(v),cou):

                d11=v[i:(i+cou)]
                
                d1=[]

                for j in range(len(d11)):
                    
                    try:
                        
                        integer_value = int.from_bytes(d11[j].encode('latin-1'), byteorder='big')
                        
                        d1.append(integer_value)
                        
                    except Exception as e:
                        print(e)
                        logger.error('Exception in decoding:%s',e)

                with open(self.filename1, 'a', newline='') as csvfile:

                    csv_writer = csv.writer(csvfile)   

                    tim=str(str(d1[0])+':'+str(d1[1])+':'+str(d1[2])+':'+str(d1[3])+':'+str(d1[4])+':'+str(d1[5]))
                    
                    state=int(format(int(d1[6]),'08b')[5:],2)
                    
                    fau=int(format(int(d1[6]),'08b')[:5],2)
                    faul='Ok'
                    charg='Ok_ch'
                    disch='Ok_disc'
                    mod='Ok_mod'

                    faul='ALL OK' if fau+int(d1[12])+int(d1[13])==0 else 'Faults'

                    charg ='Off' if state in [1,0,3] else 'On'
                    disch ='Off' if state in [1,0,2] else 'On'
                    mod='Idle' if state in [0,1] else 'Charging' if state==2 else 'Discharging'

                    cell_va=[]
                    
                    for i in range(0,(int(cc_tt[0])*2),2):
                        cell_va.append(float(int(d1[14+i])+(int(d1[15+i])<<8))/10000)
    
                        #cell_va.append(int(d1[14+i])+(int(d1[15+i])<<8))

                    
                    tem_val=d1[14+(int(cc_tt[0])*2):]
                 
                    min1_cel=min(cell_va)
                    max1_cel=max(cell_va)

                   
                    #data_l=[tim, float(int(d1[10])+(int(d1[11])<<8))/100, mod, float(int(d1[8])+(int(d1[9])<<8))/100, d1[42], d1[43], d1[44], d1[45], d1[46], d1[47], float(int(d1[14])+(int(d1[15])<<8))/10000, float(int(d1[16])+(int(d1[17])<<8))/10000, float(int(d1[18])+(int(d1[19])<<8))/10000, float(int(d1[20])+(int(d1[21])<<8))/10000, float(int(d1[22])+(int(d1[23])<<8))/10000, float(int(d1[24])+(int(d1[25])<<8))/10000, float(int(d1[26])+(int(d1[27])<<8))/10000, float(int(d1[28])+(int(d1[29])<<8))/10000, float(int(d1[30])+(int(d1[31])<<8))/10000, float(int(d1[32])+(int(d1[33])<<8))/10000, float(int(d1[34])+(int(d1[35])<<8))/10000, float(int(d1[36])+(int(d1[37])<<8))/10000, float(int(d1[38])+(int(d1[39])<<8))/10000, float(int(d1[40])+(int(d1[41])<<8))/10000, max_cel, min_cel, max_cel-min_cel, d1[7], faul, charg, disch]
                    
                    datal1=[cc_tt[2],tim,float(int(d1[10])+(int(d1[11])<<8))/100, mod, float(int(d1[8])+(int(d1[9])<<8))/100]+tem_val+cell_va+[max1_cel, min1_cel, max1_cel-min1_cel, d1[7], faul, charg, disch]
                   
                    csv_writer.writerow(datal1)
                    
                    #csv_writer.writerow(data_l)
                    
          
        except Exception as e:
            logger.error('In download_data_con sd_card_sav :%s',e)
        

    def download_con(self):

        return self.c1
    