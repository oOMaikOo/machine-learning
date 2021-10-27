# coding: utf8
import os
os.system("cls")
print ("Laden...")
import datetime
startzeit = datetime.datetime.now()
import plotly.figure_factory as ff
import numpy as np
from plotly.offline import init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout
import plotly.graph_objs as go
import xlrd

print ("Bibiotheken geladen")

excelfile = "EOL-Daten.xlsx"
excelfile1 = "test_nok.xlsx"
def read_excel(excelfile, mappe_start = 0, mappe_end = 1):
    if mappe_start == 0:
        u = 0
        z = 1
    else:
        u = mappe_start
        z = mappe_end + 1
    row1_list= []
    row11_list= []
    first = True
    startzeit_a = datetime.datetime.now()
    wb = xlrd.open_workbook(excelfile)
    print("Benoetigte Zeit für das Laden des Excelfiles: " + str(datetime.datetime.now() - startzeit_a) + " h:mm:ss.µs")
    for i in range(u, z):
        if not first:
            print("Benoetigte Zeit für die Mappe " + str(i) + ": " + str(datetime.datetime.now() - startzeit_a) + " h:mm:ss.µs")
        sh = wb.sheet_by_index(i)
        row11 = sh.col_values(11)        # Seriennummer
        row1 = sh.col_values(1)        # Stall Torq
        first = True
        startzeit_a = datetime.datetime.now()
        for data in row11:
            if not first:
                row11_list.append(data)
            first = False
        first = True
        for data in row1:
            if not first:
                row1_list.append(data)
            first = False
    return row1_list, row11_list

startzeit_b = datetime.datetime.now()
debug = True
if debug:
    print("Benoetigte Ladezeit der Bibiotheken: " + str(datetime.datetime.now() - startzeit) + " h:mm:ss.µs")
    data1, data2 = read_excel(excelfile, 1, 6)
    data3, data4 = read_excel(excelfile1)
    #print (data1, data2)


b_noGraph = False

if not b_noGraph:
    hist_data = [data1, data3]

    group_labels = ["Alle", "NOK"]

    rug_text = [data2, data4]
    colors = ['rgb(0, 0, 100)','rgb(0, 100, 0)']

    # Create distplot with custom bin_size
    fig = ff.create_distplot(
        hist_data, group_labels, bin_size=.2,
        rug_text=rug_text, colors=colors)

    # Add title
    fig['layout'].update(title="Statistik Test",yaxis=dict(title="Wert"))

    # Plot!
    #py.iplot(fig, filename='Distplot with Normal Curve')
    plot(fig, filename = "STALL_TORQUE_1_2.html", auto_open=False)

if debug:
    print("Benoetigte Zeit für die Generierung: " + str(datetime.datetime.now() - startzeit_b) + " h:mm:ss.µs")
    print("Dauer gesamt: " + str(datetime.datetime.now() - startzeit) + " h:mm:ss.µs")
