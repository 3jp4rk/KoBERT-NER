import pandas as pd
from datetime import datetime


ORIGIN = './train_original_hotfix_20220704.tsv'
SUPPLEMENTARY_SOURCE = './prelabled_220704.txt'
OUTPUT_FILE = datetime.now().strftime('%y%m%d')


if __name__ == "__main__":

    train_origin = pd.read_csv(ORIGIN, delimiter='\t', encoding='utf-8', header=None)
    train_source = pd.read_csv(SUPPLEMENTARY_SOURCE, delimiter='\t', encoding='utf-8', header=None)
    
    train_new = pd.concat([train_origin, train_source], axis=0, ignore_index=True)
    
    # validation check
    # print(len(train_new))
    # print(train_new)
    
    # print((len(train_origin)+len(train_source)==len(train_new)))
    train_new.to_csv('./train_concat_{}.tsv'.format(OUTPUT_FILE), sep='\t', header=None, index=False)
    