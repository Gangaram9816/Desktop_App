
from src.log import logger
class Blur1:
    def __init__(self):
        
        super().__init__()

    def blur_fun(self,e,con,i,r):

        v1=con.c1.content.controls[int(i)].controls[1].controls[0].content.controls[1].value
        try:

            con.c1.content.controls[int(i)].controls[1].controls[0].content.controls[0].content.value=str(str(r[0])+'-'+str(r[1])) if float(v1) < float(r[0]) or float(v1)>float(r[1]) else ''
        
        except Exception as e:
            logger.error('Blur1 Class :%s',e)
            
    def assign_blur(self,con,i,r):
        try:
            con.c1.content.controls[int(i)].controls[1].controls[0].content.controls[1].on_blur=lambda e: self.blur_fun(e,con,i,r)
            con.c1.content.controls[int(i)].controls[1].controls[0].content.controls[1].on_change=lambda e: self.blur_fun(e,con,i,r)
        except Exception as e:
            logger.error('In Blur1 assign_blur :%s',e)
        
        
        