
from .faults import Fault
from src.log import logger

class Fault_upda:

    def __init__(self):
        self.f=Fault()
        self.co=self.f.fault_con()
        self.compo=[self.co.content.controls[i].controls[j] for i in range(1, 3) for j in range(7)]
        self.compo=self.compo+[self.co.content.controls[i].controls[j] for i in range(3, 4) for j in range(6)]
        logger.info('faults_upda class initialized')
        super().__init__()

    def falt_up(self,v):

        try:

            err_code = format(int(v[0]), '08b')[:5] + format(int(v[1]), '08b') + format(int(v[2]), '08b')
            logger.info('error code :%s',err_code)
            for err,com in zip(err_code,self.compo):
                com.content.controls[0].bgcolor='red' if err =='1' else 'green'
        except Exception as e:
            logger.error('In faults_upda falt_up : %s',e)





            
        


        
        


