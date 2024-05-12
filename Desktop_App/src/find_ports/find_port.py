
import serial.tools.list_ports
class Ports_No:
    def __init__(self):
        super().__init__()
    def find_serial_device_by_description(self,description):
        available_ports = list(serial.tools.list_ports.comports())
        for port in available_ports:
            if description in port.description:
                return port.device
        return None



# import serial.tools.list_ports
# class Ports_No:
#     def __init__(self):
#         super().__init__()
    
#     def find_serial_device_by_description(self,description):
#         l=[]
#         available_ports = list(serial.tools.list_ports.comports())
#         #print("available_ports",available_ports)
#         for port in available_ports:
            
#             if description in port.description:
#                 #print('port device',port.device)
#                 l.append(port.device)
#         #print(self.l)
#         return l
    
        #return None
    