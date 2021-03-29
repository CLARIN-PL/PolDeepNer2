from __future__ import absolute_import, division, print_function

import logging
import pathlib
import argparse
import codecs
import os
import json
import time

from tqdm import tqdm

import poldeepner2
from poldeepner2.models import PolDeepNer2
from poldeepner2.utils import tokenization
from poldeepner2.utils.data_utils import get_poleval_dict, wrap_annotations


def flatten(list_of_lists):
    flat_list = []
    for lit in list_of_lists:
        flat_list.extend(lit)
    return [flat_list]


def main(args):
    print("Loading the NER model ...")
    t0 = time.time()
    if args.pretrained_path:
        tokenizer = tokenization.load(args.tokenization)
        ner = PolDeepNer2(args.model, args.pretrained_path, device=args.device, max_seq_length=args.max_seq_length,
                          squeeze=args.squeeze, seed=args.seed, tokenizer=tokenizer)
    else:
        ner = poldeepner2.models.load(args.model, device=args.device, resources_path=".models")
        ner.max_seq_length = args.max_seq_length
    time_load = time.time() - t0

    time_preprocess = 0
    time_ner = 0
    data_size = 0

    dict_list = []

    with open(os.path.join(pathlib.Path(__file__).parent.absolute(), args.input), encoding='UTF-8') as f:
        sentences = json.load(f)['questions']
        for i, sentence in tqdm(enumerate(sentences), total=len(sentences)):
            id = sentence['input']['fname'].replace("/home/a.wawer/poleval/", "")
            file_content = sentence['input']['fileContent']
            data_size += len(file_content)
            texts = file_content.split('\n')

            t0 = time.time()
            tokenized_sentences = ner.tokenizer.tokenize(texts)
            time_preprocess += (time.time() - t0)

            t0 = time.time()
            predictions = ner.process(tokenized_sentences)
            predictions = flatten(predictions)
            tokenized_sentences = flatten(tokenized_sentences)
            annotations = wrap_annotations(predictions)
            dict_list.append(get_poleval_dict(id, file_content, tokenized_sentences, annotations))
            time_ner += (time.time() - t0)

    codecs.open(args.output, "w", "utf8").write(json.dumps(dict_list, indent=4))

    print(f"Model loading time          : {time_load:8.4} second(s)")
    print(f"Data preprocessing time     : {time_preprocess:8.4} second(s)")
    print(f"Data NE recognition time    : {time_ner:8.4} second(s)")
    print(f"Total time                  : {time_load+time_preprocess+time_ner:8.4} second(s)")
    print(f"Data size:                  : {data_size/1000000:8.4}M characters")


def parse_args():
    parser = argparse.ArgumentParser(
        description='Convert set of IOB files into a single json file in PolEval 2018 NER format')
    parser.add_argument('--input', required=True, metavar='PATH', help='path to a file with a list of files')
    parser.add_argument('--output', required=True, metavar='PATH', help='path to a json output file')
    parser.add_argument('--model', required=True, metavar='PATH', help='model name or path to a model name')
    parser.add_argument('--pretrained_path', required=False, metavar='PATH', help='pretrained XLM-Roberta model path')
    parser.add_argument('--max_seq_length', required=False, default=256, metavar='N', type=int,
                        help='the maximum total input sequence length after WordPiece tokenization.')
    parser.add_argument('--device', required=False, default="cpu", metavar='cpu|cuda',
                        help='device type used for processing')
    parser.add_argument('--tokenization', required=False, default="spacy-ext", choices=tokenization.names,
                        help='Type of tokenization, nltk or spacy')
    parser.add_argument('--squeeze', required=False, default=False, action="store_true",
                        help='try to squeeze multiple examples into one Input Feature')
    parser.add_argument('--seed', required=False, default=377, metavar='N', type=int,
                        help='a seed used to initialize a number generator')
    return parser.parse_args()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filemode="w")
    args = parse_args()
    try:
        main(args)
    except ValueError as er:
        print("[ERROR] %s" % er)
