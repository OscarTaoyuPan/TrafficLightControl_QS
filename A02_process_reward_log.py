import pandas as pd


def read_log(model_file_name, case_name):
    data = pd.read_csv(f'records/{model_file_name}/{case_name}/log_rewards.txt')
    data['hour'] = data['count'] // 3600
    data_group = data.groupby(['hour'])['delay','wait_time','duration','queue_length','reward'].mean()
    # a=1

if __name__ == '__main__':
    model_file_name = 'hangzhou_1x1_bc-tyc_18041607_1h_3_lanes'
    # case_name = "Deeplight_['cross.hangzhou.rou.xml']_['cross.hangzhou.rou.xml']_01_13_22_54_11_seed_31200"
    case_name = "Fix_signal_['cross.hangzhou.rou.xml']_['cross.hangzhou.rou.xml']_01_15_20_20_05_seed_31200"
    read_log(model_file_name, case_name)