import csv
import datetime
import subprocess
import time
# import flet
# from flet import *
import os
from src.log import logger


    
class Error_log:
    def __init__(self):
        self.filename1 = None
        
        super().__init__()

    def cmd_send(self, ser):
       
        self.file_create()
       
        ser.write(b'AT+DATA=5\r\n')

    def file_create(self):
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            fil = os.path.join(os.path.expanduser("~"), 'Downloads')
            path = f"BMS_ERROR_{timestamp}.csv"
            self.filename1 = os.path.join(fil, path)

            col_names = ["BMS_ID", "Date", "Time", "Error0", "Error1", "Error2", "Error3", "Error4", "Error5", "Error6", "Error7"]

            with open(self.filename1, 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(col_names)

           

        except Exception as e:
            logger.error('Error in Error log file creation :%s',e)
            

    def error_log(self, v):

        try:

            v1 = v.split('BMSERRR')[1].split('\r\n')[0].split(',')
            v11 = [int.from_bytes(j.encode('latin-1'), byteorder='big') for j in v1]

           # print(len(v11),v11)
            

            for i in range(0, int(len(v11) - 15) + 1, 15):
                v1 = v11[i:i + 15]
                # print(i)
                bm_id=str(v1[0])
                d = str(v1[1]) + ':' + str(v1[2]) + ':' + str(v1[3])
                t = str(v1[4]) + ':' + str(v1[5]) + ':' + str(v1[6])
                va = [bm_id,d, t, v1[7], v1[8], v1[9], v1[10], v1[11], v1[12], v1[13], v1[14]]


                try:

                    with open(self.filename1, 'a', newline='') as csvfile:
                        csv_writer = csv.writer(csvfile)
                        
                        csv_writer.writerow(va)
                except PermissionError:
                    logger.error('File is locked by another process Permission error')
                    
                    # print("File is locked by another process. Waiting...")
                    
                    # time.sleep(1)  # Wait for a second before trying again

        
        except Exception as e:
            logger.error('Error in error log file fun :%s',e)

    @staticmethod
    def is_file_open_in_excel(filename):
        try:
            subprocess.check_output(['powershell', '-command', f'if ((Get-Process "EXCEL" -ErrorAction SilentlyContinue).Modules | Where-Object {{ $_.FileName -eq "{filename}" }}) {{ exit 1 }}'])
            return False
        except subprocess.CalledProcessError:
            return True

                