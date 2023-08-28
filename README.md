# Traffic Light Control with Reinforcement Learning

This is an archive of codes for S.T. Yau High School Science Award

The codes are referred to:

```
@inproceedings{wei2018intellilight,
  title={IntelliLight: A Reinforcement Learning Approach for Intelligent Traffic Light Control},
  author={Wei, Hua and Zheng, Guanjie and Yao, Huaxiu and Li, Zhenhui},
  booktitle={Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery \& Data Mining},
  pages={2496--2505},
  year={2018},
  organization={ACM}
}
```
You can find the original code resources at: https://github.com/wingsweihua/IntelliLight

## Introduction
Traffic light control is important for reducing congestion in urban mobility systems.  This paper proposes a real-time traffic light control method using deep Q-learning. Our approach incorporates a reward function considering queue lengths, delays, travel time, and throughput. More details can be in our paper:
```
@inproceedings{wei2018intellilight,
  title={Traffic Light Control with Reinforcement Learning},
  author={Pan, Taoyu}
}
```

## Data
The data is avaiable in /data. The traffic flow data is encoded in cross.imbalanced.xml, cross.balanced.xml, cross.balanced.xml, cross.hangzhou.rou.xml.


## Codes
A03_run_fix_signal.py: Run fixed signal control for different scenarios.
A04_runexp.py: Run reinforcement learning algorithm for different scenarios.

## Environment requirements
python==3.7.4

See requirements.txt.
```
pip install -r requirements.txt
```
