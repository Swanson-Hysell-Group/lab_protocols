#!/usr/bin/env python3

import os
import fnmatch
import pandas as pd
import numpy as np

# https://stackoverflow.com/questions/1724693/find-a-file-in-python
def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def check_CSD(sample_list, step, max_CSD):
    data = dict()
    for i in sample_list:
        #sample_ex = pd.read_fwf(i, delim_whitespace=True, skiprows=2, header=None, usecols=[0, 5], names = ['step', 'intensity'])
        sample_ex = pd.read_fwf(i, skiprows=2, widths=[3,3,6,6,6,6,9,6],
                                names=['demag_type', 'step', 'dec_geo', 'inc_geo',
                                       'dec_tc', 'inc_tc', 'intensity', 'error_angle'], dtype={'step':str})
        for j in range(len(sample_ex)):
            if sample_ex['step'][j]!='nan':
                sample_ex.demag_type.at[j] = sample_ex['demag_type'][j]+sample_ex['step'][j]
        sample_name = os.path.basename(i)
        data[sample_name] = {}
        # the '.tolist()[-1]' makes sure that you take the last measurement of any one step
        # in the case of duplicates
        data[sample_name]['CSD'] = sample_ex.loc[sample_ex['demag_type']==step]['error_angle'].tolist()
        for err in data[sample_name]['CSD']:
            if err<max_CSD:
                del data[sample_name]
#         data[sample_name]['CSD'] = sample_ex.loc[sample_ex['error_angle']>max_CSD]['error_angle'].tolist()
    return pd.DataFrame(data).transpose()

def main():
    site_path = input('Enter the absolute (full) path to the site folder\n')
    #type in path to site
    path = os.path.dirname(site_path)
    #must enter the full extension of the sam file you want here if there are
    #multiple sam files--it will choose the default sam file if not
    sam_file_ext = input('Enter extension of the SAM file if different (press enter to use the default ".sam"\n)') or '.sam'
    sam_file = find('*'+sam_file_ext, path)

    step_level = input('Enter the treatment step (e.g. "TT100", "NRM")\n')

    csd = float(input('Enter the maximum CSD\n'))

    with open(sam_file[0]) as f:
        sample_list = f.readlines()[2:]

    samples = []
    for sample in [i.strip("\r\n") for i in sample_list]:
        samples.append(find(sample, path)[0])

    data = check_CSD(samples,step_level,csd)
    print(data)
    return data

if __name__=="__main__":
    main()
