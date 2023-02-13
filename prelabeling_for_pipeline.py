import numpy as np
import torch
from transformers import AutoModelForTokenClassification
from transformers.pipelines.token_classification import TokenClassificationPipeline
from transformers import ElectraTokenizerFast, ElectraForTokenClassification

import argparse


'''
read text file per one line
pipeline
export as text file (line'\t'pred_list)
'''


def read_input_file(input_file):
    lines = []
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            lines.append(line)
            
    print(lines)
    return lines

def prelabel(prelabel_config):
    
    inputs = read_input_file(prelabel_config.input_file)
    tokenizer = ElectraTokenizerFast.from_pretrained('monologg/koelectra-base-v3-discriminator')
    model = AutoModelForTokenClassification.from_pretrained('./model')
    pipeline = TokenClassificationPipeline(model=model, tokenizer=tokenizer)
    
    outputs = [[output for output in pipeline(input)] for input in inputs]
    
    print(outputs)
    quit()

    

def make_dataset(added, origin):
    pass
    


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", required=True, type=str, help="Input file for prelabeling")
    parser.add_argument("--model_dir", help="model directory for use")
    
    prelabel_config = parser.parse_args()
    
    prelabel(prelabel_config)
