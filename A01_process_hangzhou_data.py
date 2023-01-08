import pandas as pd
import json
import matplotlib.pyplot as plt



def read_net_data():
    net = json.load(open('data/hangzhou_1x1_bc-tyc_18041607_1h/roadnet.json','rb'))
    inters = net['intersections']
    plt.figure()
    for inter in inters:
        x = inter['point']['x']
        y = inter['point']['y']
        plt.scatter([x],[y])
        plt.text(x,y,inter['id'])
    # plt.show()

    roads = net['roads']
    for road in roads:
        pts = road['points']
        plt.plot([pts[0]['x'], pts[1]['x']], [pts[0]['y'], pts[1]['y']])
        x_text = (pts[0]['x'] + pts[1]['x']) / 2
        y_text = (pts[0]['y'] + pts[1]['y']) / 2
        if pts[1]['y'] > 200 or pts[0]['y'] < -200:
            x_text += 10
        if pts[1]['y'] < -200 or pts[0]['y'] > 200:
            x_text -= 60
        if pts[1]['y'] > 200 or pts[0]['y'] < -200:
            x_text += 10
        if pts[0]['x'] < -200 or pts[1]['x'] > 200:
            y_text -= 30
        if pts[1]['x'] < -200 or pts[0]['x'] > 200:
            y_text += 10
        plt.text(x_text, y_text, road['id'])

    plt.show()
    a=1


def read_flow_data():
    flow_data = json.load(open('data/hangzhou_1x1_bc-tyc_18041607_1h/flow.json','rb'))
    a=1


if __name__ == '__main__':
    read_net_data()
    # read_flow_data()