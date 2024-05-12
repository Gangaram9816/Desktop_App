# import serial
# import serial.tools.list_ports

# # Define the serial port
# port_name = 'COM4'  # Replace with the actual port name on your system

# # Create a Serial object
# ser = serial.Serial(port=port_name)

# # Get port details
# port_details = ser.name
# print(f"Port Details: {port_details}")
# available_ports = list(serial.tools.list_ports.comports())
# print(available_ports)
# for port in available_ports:
#     print(port.description)
# # Get device details



# # Close the serial port when done
# ser.close()




# import flet
# from flet import *
# from flet.plotly_chart import PlotlyChart
# import plotly.express as px

# def main(page:Page):

#     x1 = ['A', 'B', 'C', 'D']
#     y1 = [10, 15, 7, 12]

#     fig = px.bar(x=x1, y=y1, labels={'x': 'Category', 'y': 'Value'}, title='Initial Bar Chart')
    

#     ch=PlotlyChart(fig,expand=True)
#     page.add(ch)
#     def click(e):
#         x_new = ['X', 'Y', 'Z','X1','Y1','Z1']
#         y1 = [10, 15, 7, 12,15,10,13]
#         fig.data[0].x=x_new
#         fig.data[0].y=y1

#         print(fig.data[0].x)
        
#         page.update()

#     page.add(ElevatedButton('Click',on_click=click))
#     page.update()

    
# flet.app(target=main)

# import flet
# from flet import *
# from flet.plotly_chart import PlotlyChart
# import plotly.express as px

# def main(page: Page):
#     x1 = ['Cell 1', 'Cell 2', 'Cell 3', 'Cell 4', 'Cell 5', 'Cell 6', 'Cell 7', 'Cell 8', 'Cell 9', 'Cell 10', 'Cell 11', 'Cell 12', 'Cell 13', 'Cell 14']
#     y1 = [1.235, 2.526, 2.229, 4.569, 3.258, 3.234, 2.658, 1.569, 4.236, 3.235, 3.598, 4.558, 2.856, 3.825]

#     fig = px.bar(x=x1, y=y1, height=500, width=1230)
#     fig.update_layout(yaxis_range=[0, 6], xaxis_title=None, yaxis_title=None)
#     fig.update_layout(title_font=dict(color="black"))

#     # Display the y values on top of each bar with bold formatting
#     fig.update_traces(text=[f'<b>{val:.3f}</b>' for val in y1], textposition='auto')

#     ch = PlotlyChart(fig, expand=True)
#     page.add(ch)

#     page.update()

# flet.app(target=main)



# import flet
# from flet import *
# from flet.plotly_chart import PlotlyChart
# import plotly.express as px

# def main(page: Page):
#     x1 = ['Cell 1', 'Cell 2', 'Cell 3', 'Cell 4', 'Cell 5', 'Cell 6', 'Cell 7', 'Cell 8', 'Cell 9', 'Cell 10', 'Cell 11', 'Cell 12', 'Cell 13', 'Cell 14']
#     y1 = [1.235, 2.526, 2.229, 4.569, 3.258, 3.234, 2.658, 1.569, 4.236, 3.235, 3.598, 4.558, 2.856, 3.825]

#     fig = px.bar(x=x1, y=y1, height=500, width=1230,text_auto=True)

#     fig.update_layout(yaxis_range=[0, 6], xaxis_title=None, yaxis_title=None)
#     fig.update_layout(title_font=dict(color="black"))
#     fig.update_layout(xaxis_title_font=dict(size=35))
#     fig.update_layout(yaxis_title_font=dict(size=14))

#     #textfont_size=12,
#     fig.update_traces(textfont_size=20, textposition='outside')
    

    

#     #fig.update_traces(text=[f'<b>{val}</b>' for val in y1], textposition='outside')

#     ch = PlotlyChart(fig, expand=True)
#     page.add(ch)

#     page.update()

# flet.app(target=main)


# import flet
# from flet import *
# from flet.plotly_chart import PlotlyChart
# import plotly.express as px

# def main(page: Page):
#     x1 = ['Cell 1', 'Cell 2', 'Cell 3', 'Cell 4', 'Cell 5', 'Cell 6', 'Cell 7', 'Cell 8', 'Cell 9', 'Cell 10', 'Cell 11', 'Cell 12', 'Cell 13', 'Cell 14']
#     y1 = [1.235, 2.526, 2.229, 4.569, 3.258, 3.234, 2.658, 1.569, 4.236, 3.235, 3.598, 4.558, 2.856, 3.825]

#     fig = px.bar(x=x1, y=y1, height=500, width=1230, text_auto=True)

#     fig.update_layout(yaxis_range=[0, 6], xaxis_title=None, yaxis_title=None)
#     fig.update_layout(title_font=dict(color="black"))
#     fig.update_layout(xaxis=dict(title=dict(text='X-axis Label', font=dict(size=35))))
#     fig.update_layout(yaxis_title=dict(text='Y-axis Label', font=dict(size=14)))

#     # Set text font size for x-axis labels
#     fig.update_traces(textfont_size=20, textposition='outside')

#     ch = PlotlyChart(fig, expand=True)
#     page.add(ch)

#     page.update()

# flet.app(target=main)



import flet
from flet import *
from flet.plotly_chart import PlotlyChart
import plotly.express as px

def main(page: Page):
    x1 = ['Cell 1', 'Cell 2', 'Cell 3', 'Cell 4', 'Cell 5', 'Cell 6', 'Cell 7', 'Cell 8', 'Cell 9', 'Cell 10', 'Cell 11', 'Cell 12', 'Cell 13', 'Cell 14']
    y1 = [1.235, 2.526, 2.229, 4.569, 3.258, 3.234, 2.658, 1.569, 4.236, 3.235, 3.598, 4.558, 2.856, 3.825]

    fig = px.bar(x=x1, y=y1, height=500, width=1230, text_auto=True)

    fig.update_layout(yaxis_range=[0, 6], xaxis_title=None, yaxis_title=None)
    fig.update_layout(title_font=dict(color="black"))
    fig.update_layout(xaxis_tickfont=dict(size=20))
    fig.update_layout(yaxis_tickfont=dict(size=20))
    fig.update_traces(textfont_size=20, textposition='outside')

    #fig.update_layout(yaxis_title=dict(text='Y-axis Label', font=dict(size=14)))

    ch = PlotlyChart(fig, expand=True)
    page.add(ch)

    page.update()

flet.app(target=main)
