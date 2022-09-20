"""
Research Sources: 
    https://github.com/robmarkcole/satellite-image-deep-learning

"""


import wget
import subprocess
import pandas as pd
import numpy as np
import argparse 



def gcpfile2df(file, save_csv=True):
    with open(file) as f:
        lines = f.readlines()
    header = [line.lstrip('# ').rstrip('\n').split(' - ')[0] for line in lines if line.startswith("# ")]
    data = [line.rstrip('\n').split(' ') for line in lines if not line.startswith("# ")][3::]
    data = np.transpose(data)
    df = pd.DataFrame()
    for i in range(0,len(header)):
        df[header[i]] = data[i]
    if save_csv:
        df.to_csv(f"{file}.csv")
    return df


def main(path_start=1, path_end=234, row_start=1, row_end=249):
    stats = {'SUCCESS':list(), 'FAILED':list()}
    print("Downloading Ground Control Points from Landsat Website...")
    for path in range(path_start,path_end):
        for row in range(row_start, row_end):
            path = str(path)
            if len(path)==2:
                path = "0"+path
            row = str(row)
            if len(row)==2:
                row="0"+row
            try:
                url = f"https://landsat.usgs.gov/GCP/collection01/gcp/{path}/{row}/GCPLib"
                filename = wget.download(url, out=f"path_{path}_row_{row}") # >> 'path_010_row_010'
                df_sub = gcpfile2df(filename, save_csv=True)
                stats['SUCCESS'].append(filename)
                subprocess.call(['rm', filename])
                subprocess.call(['mv', f"{filename}.csv", '../data/gcps/'])
                print(filename)
            except: 
                stats['FAILED'].append(url)
                pass 
    return stats





if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path-start', default=1)
    parser.add_argument('--path-end', default=234)
    parser.add_argument('--row-start', default=1)
    parser.add_argument('--row-end', default=249)

    args = parser.parse_args()
    stats = main(args.path_start, args.path_end, args.row_start, args.row_end)
