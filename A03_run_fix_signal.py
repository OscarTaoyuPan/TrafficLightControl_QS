# -*- coding: utf-8 -*-

'''
@author: hzw77, gjz5038

python runexp.py

Run experiments in batch with configuration

'''

# ================================= only change these two ========================================
SEED = 31200

# setting_memo = "one_run"
setting_memo = "hangzhou_1x1_bc-tyc_18041607_1h_3_lanes"


# first column: for train, second column: for spre_train

#     [["cross.all_synthetic.rou.xml"], ["cross.all_synthetic.rou.xml"]],
# ]

# list_traffic_files = [
#     [["cross.2phases_rou1_switch_rou0.xml"], ["cross.2phases_rou1_switch_rou0.xml"]],
# ]

list_traffic_files = [
    # [["cross.balanced.xml"], ["cross.balanced.xml"]],
    [["cross.imbalanced.xml"], ["cross.imbalanced.xml"]],
    # [["cross.switch.xml"], ["cross.switch.xml"]],
    # [["cross.hangzhou.rou.xml"], ["cross.hangzhou.rou.xml"]]
]



list_model_name = [
                   "Fix_signal",
                   ]

Simulation_time = 720

FIX_SIGNAL = [10, 20]  #[phase 0, phase 1]

# ================================= only change these two ========================================


import random
random.seed(SEED)
import numpy as np
np.random.seed(SEED)
from tensorflow import set_random_seed
set_random_seed((SEED))
import json
import os
import traffic_light_dqn
import time

PATH_TO_CONF = os.path.join("conf", setting_memo)


if 'hangzhou' in setting_memo:
    config_prefix = 'cross'
else:
    config_prefix = 'cross'

sumoBinary = r"C:\\Program Files (x86)\\Eclipse\\Sumo\\bin\\sumo-gui.exe"
sumoCmd = [sumoBinary,
           '-c',
           r'{0}/data/{1}/{2}.sumocfg'.format(os.path.split(os.path.realpath(__file__))[0], setting_memo, config_prefix)]
sumoCmd_pretrain = [sumoBinary,
                    '-c',
                    r'{0}/data/{1}/{2}_pretrain.sumocfg'.format(
                        os.path.split(os.path.realpath(__file__))[0], setting_memo, config_prefix)]

sumoBinary_nogui = r"C:\\Program Files (x86)\\Eclipse\\Sumo\\bin\\sumo.exe"
sumoCmd_nogui = [sumoBinary_nogui,
                 '-c',
                 r'{0}/data/{1}/{2}.sumocfg'.format(
                     os.path.split(os.path.realpath(__file__))[0], setting_memo, config_prefix)]
sumoCmd_nogui_pretrain = [sumoBinary_nogui,
                          '-c',
                          r'{0}/data/{1}/{2}_pretrain.sumocfg'.format(
                              os.path.split(os.path.realpath(__file__))[0], setting_memo, config_prefix)]

for model_name in list_model_name:
    for traffic_file, traffic_file_pretrain in list_traffic_files:
        dic_exp = json.load(open(os.path.join(PATH_TO_CONF, "exp.conf"), "r"))
        dic_exp["MODEL_NAME"] = model_name
        dic_exp["TRAFFIC_FILE"] = traffic_file
        dic_exp["TRAFFIC_FILE_PRETRAIN"] = traffic_file_pretrain
        if "real" in traffic_file[0]:
            dic_exp["RUN_COUNTS"] = Simulation_time
        elif "2phase" in traffic_file[0]:
            dic_exp["RUN_COUNTS"] = Simulation_time
        elif "synthetic" in traffic_file[0]:
            dic_exp["RUN_COUNTS"] = Simulation_time
        elif "hangzhou" in traffic_file[0]:
            dic_exp['RUN_COUNTS'] = Simulation_time


        #####
        # change config
        dic_exp['RUN_COUNTS_PRETRAIN'] = Simulation_time # 10000

        ####

        json.dump(dic_exp, open(os.path.join(PATH_TO_CONF, "exp.conf"), "w"), indent=4)

        # change MIN_ACTION_TIME correspondingly

        dic_sumo = json.load(open(os.path.join(PATH_TO_CONF, "sumo_agent.conf"), "r"))
        if model_name == "Deeplight":
            dic_sumo["MIN_ACTION_TIME"] = 5
        elif model_name == 'Fix_signal':
            dic_sumo["MIN_ACTION_TIME"] = 1
        else:
            dic_sumo["MIN_ACTION_TIME"] = 1
        json.dump(dic_sumo, open(os.path.join(PATH_TO_CONF, "sumo_agent.conf"), "w"), indent=4)

        prefix = "{0}_{1}_{2}_{3}".format(
            dic_exp["MODEL_NAME"],
            dic_exp["TRAFFIC_FILE"],
            dic_exp["TRAFFIC_FILE_PRETRAIN"],
            time.strftime('%m_%d_%H_%M_%S_', time.localtime(time.time())) + "seed_%d" % SEED
        )

        traffic_light_dqn.run_fixed_signal(memo=setting_memo, f_prefix=prefix, sumo_cmd_str=sumoCmd_nogui,
                                           sumo_cmd_pretrain_str=sumoCmd_nogui_pretrain, verbose = True, fix_signal = FIX_SIGNAL,
                                           simulation_time = Simulation_time)

        print("finished {0}".format(traffic_file))
    print ("finished {0}".format(model_name))



