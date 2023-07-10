import pandas as pd

file_list = [
    "Fix_signal_['cross.switch.xml']_['cross.switch.xml']_06_17_10_43_30_seed_31200.csv",
    "Fix_signal_['cross.imbalanced.xml']_['cross.imbalanced.xml']_06_17_00_20_00_seed_31200.csv",
    "Fix_signal_['cross.hangzhou.rou.xml']_['cross.hangzhou.rou.xml']_06_17_08_51_05_seed_31200.csv",
    "Fix_signal_['cross.balanced.xml']_['cross.balanced.xml']_06_17_00_02_11_seed_31200.csv",
    "Deeplight_['cross.balanced.xml']_['cross.balanced.xml']_06_17_09_10_12_seed_31200.csv",
    "Deeplight_['cross.hangzhou.rou.xml']_['cross.hangzhou.rou.xml']_07_07_16_57_04_seed_31200.csv",
    "Deeplight_['cross.imbalanced.xml']_['cross.imbalanced.xml']_05_21_12_56_13_seed_31200.csv",
    "Deeplight_['cross.switch.xml']_['cross.switch.xml']_07_07_14_11_40_seed_31200.csv"
]

path = 'results/'

res_save = {'model_name':[],'wait_time':[],'duration':[],'queue_length':[],'reward':[]}

for file in file_list:
    data = pd.read_csv(path + file)
    model_name = file.split(']_[')[0]
    res_save['model_name'].append(model_name)
    res_save['wait_time'].append(round(data.iloc[-1,:]['wait_time'] * 60, 1))
    res_save['duration'].append(round(data.iloc[-1,:]['duration'] * 60,1))
    res_save['queue_length'].append(round(data.iloc[-1,:]['queue_length'], 3))
    res_save['reward'].append(round(data.iloc[-1,:]['reward'], 3))

res_save_df = pd.DataFrame(res_save)
res_save_df.to_csv("results/final_results.csv",index=False)

