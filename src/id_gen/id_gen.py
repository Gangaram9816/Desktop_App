import logging
import csv
from datetime import datetime
import os
from pathlib import Path
from src.log import logger


class Bms_ID:
    def __init__(self):
        super().__init__()
        
    def bms_id_gen(self):

            l=[]
            documents_folder = Path.home() / "Documents"
            file_path = documents_folder / "Bms_id.csv"

            #file_path = 'C:/Users/dell/Documents/Bms_id.csv'

            try:
                if os.path.exists(file_path):

                    with open(file_path, 'r', newline='') as file:
                        
                        csv_reader = csv.reader(file)
                        
                        existing_data = list(csv_reader)

                        for i in existing_data:
                    
                            l.append(i[0])
                            
                        last_data=l[-1]
                        logger.info('last Data is {}'.format(last_data))
                else:
                    logger.info('Bms_id.csv is no the same path')

            except Exception as e:
                logger.error('Error in CSV file open {}'.format(e))
                
            current_date = datetime.now()

            l1=[]

            formatted_date = current_date.strftime('%d%m%y')
            try:

                if not l:

                    l1.append('A01'+formatted_date)
                    

                else:
                    
                    if last_data[3:]==formatted_date:
                        
                        if last_data[1:3]=='99':
                            d=chr(ord(last_data[0])+1)+'01'+formatted_date
                            l1.append(d)
                        else:
                            
                            if int(last_data[1:3]) <9:
                                
                                d1=last_data[0]+'0'+str(int(last_data[1:3])+1)+formatted_date
                            else:
                                print(int(last_data[1:3]))
                                d1=last_data[0]+str(int(last_data[1:3])+1)+formatted_date

                            l1.append(d1)

                    else:

                        d2="A01"+str(formatted_date)
                        l1.append(d2)
                    logger.info('New BMS ID generated is {}'.format(l1[0]))
                    
            except Exception as e:
                logger.error('Error in BMS ID generating block {}'.format(e))
                

            formatted_date1 = current_date.strftime('%d/%m/%Y')
            try:

                l1.append(formatted_date1)

                with open(file_path, 'a', newline='') as file:
                    csv_writer = csv.writer(file)
                    
                    csv_writer.writerow(l1) 
                logger.info('')
            except Exception as e:
                logger.error('Error in CSV Append BMS ID Block {}'.format(e))

            return l1[0]
        