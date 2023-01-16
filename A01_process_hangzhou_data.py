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
    num_replication = 20
    current_data_time = 3600
    target_length = num_replication * current_data_time

    flow_data = json.load(open('data/hangzhou_1x1_bc-tyc_18041607_1h/flow.json','rb'))
    print(len(flow_data))
    last_veh = flow_data[-1]
    road_map = {'road_1_2_3':'edge4-0','road_1_1_0':'edge0-2',
                'road_1_1_1':'edge0-4','road_1_1_2':'edge0-1',
                'road_0_1_0':'edge1-0','road_2_1_2':'edge2-0',
                'road_1_1_3':'edge0-3','road_1_0_1':'edge3-0'}
    route_flow = {}
    for veh in flow_data:
        start_edge = road_map[veh['route'][0]]
        end_edge = road_map[veh['route'][1]]
        if (start_edge, end_edge) not in route_flow:
            route_flow[(start_edge, end_edge)] = 0
        route_flow[(start_edge, end_edge)] += 1

    for key in route_flow:
        route_flow[key] *= num_replication
    print(route_flow)


    A=1


if __name__ == '__main__':
    # read_net_data()
    read_flow_data()