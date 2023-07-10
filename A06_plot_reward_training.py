import matplotlib.pyplot as plt
import pandas as pd

def process_data(log_df):
    data = log_df
    data['time_id'] = data['count'] // 120
    data_group = data.groupby(['time_id'])['delay','wait_time','duration','queue_length','reward'].mean().reset_index()
    return data_group

def plot_res(data, case_name, save_fig):
    font_size = 16
    plt.figure(figsize=(6, 5))

    plt.ylabel('Reward',  fontsize=font_size)
    plt.xlabel('Time id (every 2 min)',  fontsize=font_size)
    plt.plot(data.loc[:,'time_id'], data.loc[:,'reward'], 'k', linewidth = 2)
    plt.xticks(fontsize=font_size)
    plt.yticks(fontsize=font_size)
    #plt.legend()
    plt.tight_layout()
    model_name = case_name.split(']_[')[0]
    if save_fig == 1:
        plt.savefig('img/reward_func' + model_name + '.jpg', dpi=200)
    else:
        plt.show()

def read_log(model_file_name, case_name):
    data = pd.read_csv(f'records/{model_file_name}/{case_name}/log_rewards.txt')
    return data

if __name__ == '__main__':
    model_file_name = 'hangzhou_1x1_bc-tyc_18041607_1h_3_lanes'
    case_name = "Deeplight_['cross.switch.xml']_['cross.switch.xml']_07_07_14_11_40_seed_31200"
    # case_name = "Fix_signal_['cross.hangzhou.rou.xml']_['cross.hangzhou.rou.xml']_04_22_08_26_48_seed_31200"
    log_df = read_log(model_file_name, case_name)
    data = process_data(log_df)
    plot_res(data, case_name, save_fig = 1)