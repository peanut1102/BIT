import numpy as np


def spilt2npz(spilt_path, save_path):
    with open(spilt_path) as file:
        lines = file.readlines()
    EEGS = [[] for i in range(4)]
    rat = 0
    for i in range(0, 15, 3):
        for line in lines:
            EEGS[rat].append(line[i])
        rat += 1
    for i in range(len(EEGS)):
        rat = np.array(EEGS[i])
        np.savez(save_path + str(i) + '.npz', EEG1=rat)


