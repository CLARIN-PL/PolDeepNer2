PolDeepNer2
===========

PolDeepNer2 is an improved version of [PolDeepNer](https://github.com/CLARIN-PL/PolDeepNer). 
The tool is designed to recognize and categorize named entities utilizing neural networks and transfomer-based language models.   

The tool is provided with a list of pre-trained models for Polish and other languages.

It contains a pre-trained model trained on the [NKJP corpus](http://clip.ipipan.waw.pl/NationalCorpusOfPolish) 
which recognizes nested annotations of the following types:


Contributors
------------
* Michał Marcińczuk <marcinczuk@gmail.com>
* Jarema Radom


Notebooks
----------

<table>
    <tr>
        <td><pre>notebooks/pdn2_cpu.py</pre></td>
        <td>This notebook present how to install and use module API to process a raw text on CPU.</td>
        <td><a href="https://colab.research.google.com/github/CLARIN-PL/PolDeepNer2/blob/master/notebooks/pdn2_cpu.ipynb">
                <img src="https://colab.research.google.com/assets/colab-badge.svg" title="Open In Colab"/></a></td>
    </tr>
</table>



Models
----------

### PolEval 2018 (NKJP NER model)

PolDeepNer2 achieves the SOTA results on the PolEval 2018 dataset. 

![NKJP NER categories](docs/media/nkjp-ner-schema.png) 

<table>
    <thead>
        <tr>
            <th>Model</th>
            <th>Score</th>
            <th>F1 Overlap</th>
            <th>F1 Exact</th>
            <th>Score main</th>
            <th>Time CPU</th>
            <th>Time GPU</th>
            <th>Source</th>
        </tr>
    </thead>
    <tbody>
        <tr class="section">
            <td colspan="8"><b>PolDeepNer2</b></td>
        </tr>
        <tr>
            <td>HerBERT large, spacy-ext, sq</td>
            <td>92.1</td>
            <td>92.7</td>
            <td>89.9</td>
            <td></td>
            <td></td>
            <td>~2m 24s</td>
            <td></td>
        </tr>
        <tr>
            <td>Polish RoBERTa base, spacy-ext, sq</td>
            <td>91.4</td>
            <td>91.9</td>
            <td>89.1</td>
            <td></td>
            <td>~1.5 h</td>
            <td>~2m 8s</td>
            <td></td>
        </tr>
        <tr>
            <td>Polish RoBERTa base, toki</td>
            <td>90.0</td>
            <td>90.5</td>
            <td>87.7</td>
            <td>92.40</td>
            <td>~6h 30m</td>
            <td>~6m 30s</td>
            <td></td>
        </tr>
        <tr>
            <td>Polish RoBERTa base, spacy-ext</td>
            <td>89.8</td>
            <td>90.4</td>
            <td>87.4</td>
            <td>92.20</td>
            <td></td>
            <td>~8m 2s</td>
            <td></td>
        </tr>
        <tr class="section">
            <td colspan="8"><b>Systems published after PolEval 2018</b></td>
        </tr>
        <tr>
            <td>Dadas et al. 2020 [1]</td>
            <td>88.6</td>
            <td>87.0</td>
            <td>89.0</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td><a href="https://www.researchgate.net/publication/343170155_A_Bidirectional_Iterative_Algorithm_for_Nested_Named_Entity_Recognition">link</a></td>
        </tr>
        <tr>
            <td>Polish RoBERTa (large) [1]</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>89.98</td>
            <td>-</td>
            <td>-</td>
            <td><a href="https://github.com/sdadas/polish-roberta">link</a></td>
        </tr>
        <tr>
            <td>Polish RoBERTa (base) [1]</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>87.94</td>
            <td>-</td>
            <td>-</td>
            <td><a href="https://github.com/sdadas/polish-roberta">link</a></td>
        </tr>
        <tr>
            <td>spaCy (pl_spacy_model) </td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>87.50</td>
            <td>~3m</td>
            <td>-</td>
            <td><a href="https://github.com/ipipan/spacy-pl#user-content-named-entity-recognizer">link</a></td>
        </tr>
        <tr class="section">
            <td colspan="8"><b>Top 3 systems from PolEval 2018</b></td>
        </tr>
        <tr>
            <td>Applica.ai </td>
            <td>86.6</td>
            <td>87.7 </td>
            <td>82.6</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td><a href="https://github.com/applicaai/poleval-2018">link</a></td>
        </tr>
        <tr>
            <td>PolDeepNer</td>
            <td>85.1</td>
            <td>85.9</td>
            <td>82.2</td>
            <td>-</td>
            <td>-</td>
            <td>~9m</td>
            <td><a href="https://github.com/CLARIN-PL/PolDeepNer">link</a></td>
        </tr>
        <tr>
            <td>Liner2</td>
            <td>81.0</td>
            <td>81.8</td>
            <td>77.8</td>
            <td>-</td>
            <td>~3m</td>
            <td>-</td>
            <td><a href="https://github.com/CLARIN-PL/Liner2">link</a></td>
        </tr>
    </tbody>
</table>

[1] The model is not available. Only the evaluation results were published.   

#### Comparision of loading and processing times 

| Model               | Library     | Tokenizer            |  Model loading [s] | Preprocessing [s] | NE recognition [s] | Total [s] |
|:--------------------|:------------|----------------------|-------------------:|------------------:|-------------------:|-------:|
| Polish RoBERTa base | fairseq     | -                    |  12.28 |   50.90 |  65.23 | 128.4 |  
| HerBERT large       | HuggingFace | HerbertTokenizerFast |  18.44 |   50.83 | 103.70 | 173.0 |
| HerBERT large       | HuggingFace | XLMTokenizer         |  18.33 |   51.42 | 177.50 | 247.3 |

* Dataset size: 1828 document (3M characters).
* GPU: RTX Titan (24 GB, 4608 CUDA cores).

![NKJP NER times](docs/media/pdn2-nkjp-times.png) 

#### Comparision of named entity recognition times for different datasets

| 	| Size [Million chars]	| NER time [minutes] |
|-----------------------------------------|---------:|---------:|
| PolEval 2018 NER test dataset	          | 3	     | 2.6      |
| Monthly volume of news from Polish news portals [70 sources]	| 160	| 136.9 |
| Polish Wikipedia (2013 dump)	| 1000	| 855.6 |
| Annual volume of news from Polish news portals [70 sources]	| 1920	| 1642.7 |

![NKJP NER times](docs/media/pdn2-corpora-ner-times.png) 


### N82 (KPWr and CEN)

Inner-corpora evaluation

| Model                          | Eval   | Precision | Recall | F-measure | Support | Source |
|--------------------------------|--------|----------:|-------:|----------:|--------:|--------|
| *PolDeepNer2* (kpwr_n82_base)  | KPWr   |     75.02 |  77.67 |     76.32 |    4430 |
| *PolDeepNer2* (kpwr_n82_large) | KPWr   |     77.05 |  78.79 |     77.91 |    4430 |
| PolDeepNer (n82-elmo-kgr10)    | KPWr   |     73.97 |  75.49 |     74.72 |    4430 | [link](https://github.com/CLARIN-PL/PolDeepNer)
| --- | 
| *PolDeepNer2* (cen_n82_base)   | CEN    |     84.64 |  85.95 |     85.29 |    1423 | 
| *PolDeepNer2* (cen_n82_large)  | CEN    |     86.94 |  88.40 |     87.67 |    1423 |

Cross-corpora evaluation

| Model                          | Eval   | Precision | Recall | F-measure | Support |
|--------------------------------|--------|----------:|-------:|----------:|--------:|
| *PolDeepNer2* (kpwr_n82_base)  | CEN    |     80.90 |  81.87 |     81.38 |    1423 |
| *PolDeepNer2* (kpwr_n82_large) | CEN    |     80.16 |  82.08 |     81.11 |    1423 |
| --- | 
| *PolDeepNer2* (cen_n82_base)   | KPWr   |     58.58 |  64.79 |     61.53 |    4430 | 
| *PolDeepNer2* (cen_n82_large)  | KPWr   |     61.38 |  66.66 |     63.91 |    4430 |

Installation (with Conda)
-------

Create and activate conda environment:

```
conda create -n pdn2 python=3.6
conda activate pdn2
```

Install CUDA, CuDNN and Torch:

```
conda install -c anaconda cudatoolkit=10.1
conda install -c anaconda cudnn
```

Install PolDeepNer2:

```
pip install https://pypi.clarin-pl.eu/packages/poldeepner2-0.5.0-py3-none-any.whl#md5=6a6131d1b3d104f0bbed87ec6969a841
```

Install spacy model

```
python -m spacy download pl_core_news_sm
```

Evaluation
----------

Download evaluation dataset

```
wget http://mozart.ipipan.waw.pl/~axw/poleval2018/POLEVAL-NER_GOLD.json -O POLEVAL-NER_GOLD.json
```

## Polish RoBERTa

Process the dataset:
```
python process_poleval.py \
  --input POLEVAL-NER_GOLD.json \
  --output pdn2_nkjp_roberta_base_sq.json \
  --model nkjp-base-sq \
  --device cuda:0
```

Output:
```
Model loading time          :    12.28 second(s)
Data preprocessing time     :     50.9 second(s)
Data NE recognition time    :    65.23 second(s)
Total time                  :    128.4 second(s)
Data size:                  :    3.072M characters
```

Evaluate:
```
python poleval_ner_test.py \
  --goldfile POLEVAL-NER_GOLD.json \
  --userfile pdn2_nkjp_roberta_base_sq.json
```

Output:
```
OVERLAP precision: 0.927 recall: 0.912 F1: 0.919 
EXACT precision: 0.899 recall: 0.884 F1: 0.891 
Final score: 0.914
Exact TP=32971 ; FP=3709; FN=4335
```

## HerBERT

Process the dataset:

```
python process_poleval.py \
  --input POLEVAL-NER_GOLD.json \
  --output pdn2_nkjp_herbert_large_sq.json \
  --model nkjp-herbert-large-sq \
  --device cuda:0
```

Output:

```
Model loading time          :    18.44 second(s)
Data preprocessing time     :    50.83 second(s)
Data NE recognition time    :    103.7 second(s)
Total time                  :    173.0 second(s)
Data size:                  :    3.072M characters
```

Evaluate:

```
python poleval_ner_test.py \
  --goldfile POLEVAL-NER_GOLD.json \
  --userfile pdn2_nkjp_herbert_large_sq.json
```

Output:

```
OVERLAP precision: 0.929 recall: 0.922 F1: 0.926 
EXACT precision: 0.903 recall: 0.896 F1: 0.900 
Final score: 0.921
Exact TP=33433 ; FP=3596; FN=3873
```


Credits
-------

* This code is based on [xlm-roberta-ner](https://github.com/mohammadKhalifa/xlm-roberta-ner) by mohammadKhalifa.
* Language models for Polish:
    * https://github.com/sdadas/polish-roberta
    * https://huggingface.co/allegro/herbert-base-cased
    * https://huggingface.co/allegro/herbert-large-cased 
