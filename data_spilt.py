import numpy as np


def spilt2npz(spilt_path, save_path):
    with open(spilt_path) as file:
        lines = file.readlines()
    viriables = {}
    for i in range(16):
        rat = int((i + 1) / 3)
        s = int((i + 1) % 3)
        if s == 0:
            locals()['rat' + str(rat) + '_EEG1'] = []
            viriables['rat' + str(rat) + '_EEG1'] = locals()['rat' + str(rat) + '_EEG1']
        if s == 1:
            locals()['rat' + str(rat) + '_EEG2'] = []
            viriables['rat' + str(rat) + '_EEG2'] = locals()['rat' + str(rat) + '_EEG2']
        if s == 2:
            locals()['rat' + str(rat) + '_EMG'] = []
            viriables['rat' + str(rat) + '_EMG'] = locals()['rat' + str(rat) + '_EMG']
    # 将信号写入列表中
    for i in range(6, len(lines) - 1):
        line = lines[i]
        for j in range(1, 16):
            cur_signal = line[j]
            rat = int(j / 3)
            s = int(j % 3)
            if s == 0:
                locals()['rat' + str(rat) + '_EEG1'].append(cur_signal)
            if s == 1:
                locals()['rat' + str(rat) + '_EEG2'].append(cur_signal)
            if s == 2:
                locals()['rat' + str(rat) + '_EMG'].append(cur_signal)
    # 确定列表长度
    res_len = len(locals()['rat1_EEG1']) % 250
    # 如果res_len不为0，则将缺的用后面补充
    if res_len > 0:
        for key, cur_pipline in viriables.items():
            add_pipline = cur_pipline[:(250 - res_len)]
            viriables[key] = np.array(cur_pipline + add_pipline)

    # save as per rat
    for i in range(1, 6):
        key1 = 'rat' + str(i) + '_EEG1'
        key2 = 'rat' + str(i) + '_EEG2'
        key3 = 'rat' + str(i) + '_EMG'
        np.savez(save_path + 'rat' + str(i) + '.npz', EEG1=viriables[key1], EEG2=viriables[key2], EMG=viriables[key3])
