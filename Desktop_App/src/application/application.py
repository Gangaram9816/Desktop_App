
import flet
from flet import *
from src.dashboard import faults, mybms,voltage,temperature,batterystats,faults_upda, live_data
from src.find_ports import find_port
from src.battery import batt_conn, general_stats
from src.configur_page import profile_button, profile_con,voltage_con,tempe_con,current_con,set_profile,get_profile,upload_conf,remove_pr,edit_conf,dd_change,blur,batter_con
from src.sd_card import sd_con,download_data_con,error_log
from src.terminal import terminal
import serial
import queue
from src.log import logger
from src.id_gen import id_gen


class App:

    def __init__(self,page:Page):
        
        self.page=page
        
        self.po=find_port.Ports_No()
        #self.flt=faults.Fault()
        self.bt_conn=batt_conn.Batt_conn()
        self.gen=general_stats.General_st()
        self.setP=set_profile.Set_P(self.page)
        self.upl=upload_conf.Upload_conf(self.page)
        self.edit_c=edit_conf.Edit()
        self.vol_con=voltage_con.Volta_con()
        self.cur_con=current_con.Curren_con()
        self.tem_con=tempe_con.Tempe_con()
        self.remov=remove_pr.Remove(self.page)
        self.downlod=download_data_con.Download_data(self.page)
        self.vo=voltage.Voltage()
        self.temp=temperature.Temperature()
        self.batt=batterystats.Batterystats()
        self.pro_btn=profile_button.Profile_btn()
        self.get_p=get_profile.Get_pro(self.page)
        self.pro_c=profile_con.Pro_con()
        self.dd_c=dd_change.DD_Change(self.page)
        self.ter=terminal.Terminal()
        #self.blr=blur.Blur()
        self.my_bms=mybms.Mybms()
        self.bt_con=batter_con.Batte_con()
        self.sd_cont=sd_con.Sd_con()
        self.fa=faults_upda.Fault_upda()
        self.ld=live_data.Live_data()
        self.id_bms=id_gen.Bms_ID()
        self.err_log=error_log.Error_log()

        self.dlg_uncom=AlertDialog(
        title=Text("Request not complete"),)

        self.dlg_com=AlertDialog(
            
        title=Text("Request completed"),)
        
        
        self.downlod.c1.content.controls[2].content.controls[2].controls[1].content.controls.append(self.downlod.sd_time1)
        
        self.downlod.date_picker.on_change=self.downlod.change_date
        self.downlod.date_picker1.on_change=self.downlod.change_date1
        self.page.overlay.append(self.downlod.date_picker)
        self.page.overlay.append(self.downlod.date_picker1)
        self.downlod.c1.content.controls[2].on_change=self.downlod.radio_clicked


        self.start_thread=True
        self.dlg_modal = AlertDialog(
                        modal=True,
                        title=Text("Enter Profile Name"),
                        content=TextField(),
                        actions=[
                            TextButton("Yes", on_click=self.yes),
                            TextButton("No", on_click=self.no),
                        ],
                        actions_alignment=MainAxisAlignment.END,
                        
                        )
    
        self.dlg = AlertDialog(
                    title=Text("Connect OBD!"),modal=True)
        
        self.dlg_err=AlertDialog(title=Text('Invalid Commands'))
        super().__init__()

    data_queue = queue.Queue()
    ser=serial.Serial()
    ser.baudrate=9600

    def dlg_obd(self,e):
        self.dlg.open=True
        self.page.update()
    
    def unsuccess(self,v):
    
        self.downlod.date_dlg1.open=False
        self.setP.dlg_modal.open=False
        self.get_p.dlg_modal.open=False
        self.downlod.dlg_modal.open=False
       
        self.page.update()

        #time.sleep(0.1)
        
        self.ter.con.controls[1].controls[0].content.controls.append(Text('AT+TIMEOUT'))
        
        self.page.dialog=self.dlg_uncom
        self.dlg_uncom.open=True


    def para_clen(self,v,v1):
        v.c1.content.controls[v1].controls[1].controls[0].content.controls[1].read_only=False
        v.c1.content.controls[v1].controls[1].controls[0].content.controls[1].bgcolor=colors.YELLOW_100
        v.c1.content.controls[v1].controls[1].controls[0].content.controls[1].value=''


    def add_pr(self,e):
        self.page.dialog=self.dlg_modal
        self.dlg_modal.open=True
    
    def yes(self,e):
        va=self.dlg_modal.content.value
        if va is None or va =='':
            
            self.dlg_modal.open=False

        else:
            
            self.dlg_modal.open=False
            self.dlg_modal.content.value=''
            
            self.pro_c.dd1.content.content.options.append(dropdown.Option(va))
            self.pro_c.dd1.content.content.value=va

            self.upl.get_name(va)
            self.para_clen(self.vol_con,int(1))
            self.para_clen(self.vol_con,int(3))
            self.para_clen(self.vol_con,int(5))
            self.para_clen(self.vol_con,int(7))
            self.para_clen(self.vol_con,int(9))
            self.para_clen(self.vol_con,int(11))
            self.para_clen(self.vol_con,int(13))

            self.para_clen(self.cur_con,int(5))
            self.para_clen(self.cur_con,int(7))
            self.para_clen(self.cur_con,int(9))
            self.para_clen(self.cur_con,int(11))
            self.para_clen(self.cur_con,int(13))
            self.para_clen(self.cur_con,int(15))

            self.para_clen(self.tem_con,int(1))
            self.para_clen(self.tem_con,int(3))
            self.para_clen(self.tem_con,int(5))
            self.para_clen(self.tem_con,int(7))

            self.para_clen(self.bt_con,int(7))
            self.para_clen(self.bt_con,int(9))
            self.para_clen(self.bt_con,int(11))


    def no(self,e):
        self.dlg_modal.open=False

    def canboud(self,e):
        
        val=self.bt_conn.dd2.value
        
        if val =='125':
           
            self.ser.write(b'AT+CANB=1\r\n')

        if val=='250':
            
            self.ser.write(b'AT+CANB=2\r\n')
            
        if val =='500': 
          
            self.ser.write(b'AT+CANB=3\r\n')
            
    def mosfet_status(self,e):
        if self.my_bms.c1.content.controls[1].controls[3].content.controls[0].value is True:
            self.ser.write(b'AT+CHRG=1\r\n')
            
        else:
            self.ser.write(b'AT+CHRG=0\r\n')


    def read_data_thread(self):
        
        global port1
                
        while self.start_thread:
        
            try:
            #CP210x USB to UART Bridge (COM13)
                port = self.po.find_serial_device_by_description("CP210x")
            
                if port is None:
                    self.ser.close()
                    
                    self.page.dialog = self.dlg
                    self.dlg.open = True
                    
                    self.bt_conn.c1.controls[4].controls[1].value=str(port)
                    self.page.controls[0].controls[0].controls[0].content.controls[0].content.content.controls[1].content.controls[1].controls[1].value=''
                    self.page.controls[0].controls[0].controls[0].content.controls[0].content.content.controls[1].content.controls[1].controls[0].src=' '
            
                    self.page.update()
                   
                else:

                    self.page.update()

                    port1=port
                    self.bt_conn.c1.controls[4].controls[1].value=str(port1)
                   
                    self.ser.port=port
                    self.ser.timeout=20
                    self.ser.open()

                    #self.err_log=error_log.Error_log(self.ser)
                    try:
                        self.pro_btn.c1.content.controls[0].controls[0].on_click=self.setP.set_prof
                        self.pro_btn.c1.content.controls[0].controls[0].data=self.ser
                        self.pro_btn.c1.content.controls[0].controls[2].data=self.ser

                        self.pro_btn.c1.content.controls[0].controls[2].on_click=self.get_p.get_conf
                        self.pro_c.c2.content.controls[1].controls[1].content.controls[0].content.on_click=self.add_pr
                        self.pro_c.c2.content.controls[1].controls[1].content.controls[3].content.on_click=self.edit_c.edit_con
                        self.pro_c.c2.content.controls[1].controls[1].content.controls[2].content.on_click=self.remov.rem
                        self.pro_c.c2.content.controls[1].controls[1].content.controls[1].content.on_click=self.upl.uploa
                        self.my_bms.c1.content.controls[1].controls[3].content.controls[0].on_change=self.mosfet_status
                        self.downlod.download.controls[0].content.data=self.ser
                        self.ter.b1.data=self.ser
                        self.ter.b1.on_click=self.ter.term1
                        
                        self.bt_conn.c1.controls[8].content.on_click=self.canboud
                        self.downlod.download.controls[0].content.on_click=self.downlod.download_sd
                       
                        self.sd_cont.c1.content.controls[5].controls[0].content.on_click=lambda e: self.ser.write(b'AT+DATA=4\r\n')
                        #self.sd_cont.c1.content.controls[6].on_click=lambda e: self.ser.write(b'AT+DATA=5\r\n')
                        self.sd_cont.c1.content.controls[6].on_click=lambda e: self.err_log.cmd_send(self.ser)
                        self.my_bms.c1.content.controls[1].controls[1].content.controls[0].on_change=self.ld.liv

                    
                        self.pro_c.dd1.content.content.on_change=self.dd_c.d_change
                    except Exception as e:
                        logger.error("In App Assigned Fun :%s",e)
                        

                    else_lis=['CONFIGR', 'CELLVOL', 'THERMIS', 'VOLTSOC', 'SD_CARD', 'AT+TIME', 'AT+DONE', 'SD_INFO', 'AT+ERRR', 'AT+INFO']
                    while True:

                        data = self.ser.readline()#.decode('utf-8', 'ignore')
                        #print('data',data)
                    
                        
                        if "AT+TEST" in str(data):
                            self.ser.write(b'AT+TEST=OK\r\n')
                            
                            try:
                    
                                self.page.dialog.open = False
                                self.page.update()
                                print('got at +test')
                            except:
                                pass
                       
                        else:
                            self.data_queue.put(data)
                            self.page.controls[0].controls[0].controls[0].content.controls[0].content.content.controls[1].content.controls[1].controls[1].value='Connected'
                            self.page.controls[0].controls[0].controls[0].content.controls[0].content.content.controls[1].content.controls[1].controls[0].src='assets/images/Ellipse 3.svg'
                            #self.page.update()
                        

            except Exception as e:
                
                logger.error("Read Data Thread :%s",e)
    
    def done(self,v):
        self.downlod.date_dlg1.open=False
        self.setP.dlg_modal.open=False
        self.get_p.dlg_modal.open=False
        
        self.page.update()
        
        self.ter.con.controls[1].controls[0].content.controls.append(Text('AT+DONE'))
        
        self.page.dialog=self.dlg_com
        self.dlg_com.open=True
        self.downlod.download.controls[0].content.style.bgcolor='#EBEFF9'
        self.downlod.download.controls[0].content.style.color='black'
        self.downlod.c1.content.controls[2].value=''
        self.downlod.c1.content.controls[2].content.controls[1].controls[1].content.controls[1].controls[0].value=''
        self.downlod.c1.content.controls[2].content.controls[1].controls[1].content.controls[1].controls[2].value=''
        
    def vcs_update(self,v):
       
        dat=v.split('VOLTSOC')[1].split(',')
        
        self.fa.falt_up([dat[0],dat[4],dat[5]])
        self.batt.update_batt(dat[:4])
        self.gen.update_genstats(dat[:4])
        self.ld.soc(dat)
        logger.info('VCS Value :%s',v)
    
    def err(self,v):
        self.page.dialog=self.dlg_err
        self.dlg_err.open=True
    
    def bms_id(self,v):
        
        va=v.split('AT+INFO')[1].split('=')[1].split(',')
        print('at +info',va)
        
        
        if str(va[0])=='000000000' or str(va[0])=='FFFFFFFFF':
           
            va[0]=self.id_bms.bms_id_gen()
            self.ser.write(('AT+BMSID='+str(va[0])+'\r\n').encode())
      
        
        self.vo.cc_val(va[1])
        
        self.temp.tt_val(va[2])
        
        self.ld.cc_tt(va[1],va[2],va[0])

        self.my_bms.c1.content.controls[1].controls[0].content.controls[1].value='BMS ID\n'+str(va[0])
        self.gen.c1.controls[2].controls[1].value=str(va[0])
        

    def data_inf(self,v):
        
        va=v.split('AT+DATAINFO')[1].split("\r\n")[0].split(',')

        print('data info',va)

        self.downlod.cc_tempe([va[1],va[2],va[0]])
        
    def sd_error1(self,v):

        print('value in error1',v)

    def sd_error(self,v):
        print('v in sd error',v)

        dict1={
            'AT+ERR=01':self.sd_error1

        }
        dict1[v[0:9]](v)
    
    def process_data_thread(self):
        
        dic={
            'CELLVOL':self.vo.get_vol,
            'THERMIS':self.temp.get_temp,
            'VOLTSOC':self.vcs_update,
            'CONFIGR':self.get_p.update_con,
            'SD_CARD':self.downlod.sd_card_sav,
            'AT+TIME':self.unsuccess,
            'AT+DONE':self.done,
            'SD_INFO':self.sd_cont.refre,
            "AT+ERRR":self.err,
            'AT+INFO':self.bms_id,
            'AT+DATA':self.data_inf,
            "BMSERRR":self.err_log.error_log,
            #"AT+ERR=":self.sd_error

            }
        
        
        # try:
        #     data = self.data_queue.get().decode('latin-1')
        #     dic[data[0:7]](data)
        # except KeyError as e:
        #     pass
        #     logger.error('Data key not found: %s', e)
        # except Exception as e:
        #     pass
            
        #     logger.error('Unexpected error: %s', e)
        #     #continue  # Continue processing other data items

        # # Check each control's UID before updating
        # all_controls_valid = True
        # for control in self.page.controls:
        #     if getattr(control, '__uid', None) is None:
        #         pass
                #logger.error(f'Control without UID found: {control}')
                
                #all_controls_valid = False
                

        # if all_controls_valid:
        #     try:
        #         self.page.update()
        #     except AssertionError as e:
        #         logger.error('Failed to update page due to: %s', e)
        #self.page.update()
        
        while self.start_thread:
            #self.page.update()
            try:

                data = self.data_queue.get().decode('latin-1')
                #self.ter.v_return(data)
                #print('data',data)
                
                dic[data[0:7]](data)

                #self.page.update()
            except AssertionError as e:
                pass
            #     logger.error('Failed to update page due to: %s', e)
            # # Optionally, print or handle specific control issues
            #     for control in self.page.controls:
            #         if control.__uid is None:
            #             logger.error('Control without UID found: %s', control)
            except AttributeError as ae:
                print("Att Error",ae)
            except Exception as e:
                logger.error('process data thread: %s', e)
                
            finally:
                self.page.update()
                
                
            
            
            
