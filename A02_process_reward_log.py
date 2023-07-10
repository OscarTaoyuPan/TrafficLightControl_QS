import pandas as pd


def read_log(model_file_name, case_name):
    data = pd.read_csv(f'records/{model_file_name}/{case_name}/log_rewards.txt')
    data['hour'] = data['count'] // 3600
    data_group = data.groupby(['hour'])['delay','wait_time','duration','queue_length','reward'].mean()
    data_group = data_group.iloc[0:len(data_group) - 1]
    data_group.to_csv('results/'+case_name+'.csv',index=False)

if __name__ == '__main__':
    model_file_name = 'hangzhou_1x1_bc-tyc_18041607_1h_3_lanes'
    file_list = [
        "Fix_signal_['cross.switch.xml']_['cross.switch.xml']_06_17_10_43_30_seed_31200",
        "Fix_signal_['cross.imbalanced.xml']_['cross.imbalanced.xml']_06_17_00_20_00_seed_31200",
        "Fix_signal_['cross.hangzhou.rou.xml']_['cross.hangzhou.rou.xml']_06_17_08_51_05_seed_31200",
        "Fix_signal_['cross.balanced.xml']_['cross.balanced.xml']_06_17_00_02_11_seed_31200",
        "Deeplight_['cross.balanced.xml']_['cross.balanced.xml']_06_17_09_10_12_seed_31200",
        "Deeplight_['cross.hangzhou.rou.xml']_['cross.hangzhou.rou.xml']_07_07_16_57_04_seed_31200",
        "Deeplight_['cross.imbalanced.xml']_['cross.imbalanced.xml']_05_21_12_56_13_seed_31200",
        "Deeplight_['cross.switch.xml']_['cross.switch.xml']_07_07_14_11_40_seed_31200"
    ]
    # case_name = "Deeplight_['cross.hangzhou.rou.xml']_['cross.hangzhou.rou.xml']_01_13_22_54_11_seed_31200"
    for case_name in file_list:
        read_log(model_file_name, case_name)