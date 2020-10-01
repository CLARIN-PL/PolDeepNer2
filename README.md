PolDeepNer2
===========

*!! Important notice: This repo is still under construction. The code and models with be published soon. !!*

PolDeepNer2 is a tool for recognition of named entities in Polish texts. It contains a pre-trained model trained on the [NKJP corpus](http://clip.ipipan.waw.pl/NationalCorpusOfPolish) 
which recognizes nested annotations of the following types:

![NKJP NER categories](docs/media/nkjp-ner-schema.png) 

It is an improved version of [PolDeepNer](https://github.com/CLARIN-PL/PolDeepNer).


Contributors
------------
* Michał Marcińczuk <marcinczuk@gmail.com>
* Jarema Radom


Credits
-------
The implementation is based on [xlm-roberta-ner](https://github.com/mohammadKhalifa/xlm-roberta-ner) 
and utilizes [Polish RoBERTa models](https://github.com/sdadas/polish-roberta). 


Models
----------

### PolEval 2018 (NKJP NER model)

*Comparision with other models*

| Model                     | Score     | F1 Overlap | F1 Exact  | Score main | Time CPU | Time GPU | Source | 
|---------------------------|----------:|-----------:|----------:|-----------:|---------:|---------:|--------|  
| *PolDeepNer2* (nkjp_base) |      90.0 |       90.5 |      87.7 |      92.40 |          |   ~6.5 m |        | 
| --- Results published after PolEval 2018 ---|
| Dadas et al. 2020 [1]     |      88.6 |       87.0 |      89.0 |          - |        - |        - | [link](https://www.researchgate.net/publication/343170155_A_Bidirectional_Iterative_Algorithm_for_Nested_Named_Entity_Recognition) |
| Polish RoBERTa (large) [1]|         - |          - |         - |      89.98 |        - |        - | [link](https://github.com/sdadas/polish-roberta)
| Polish RoBERTa (base) [1] |         - |          - |         - |      87.94 |        - |        - | [link](https://github.com/sdadas/polish-roberta)
| spaCy (pl_core_news_lg)   |         - |          - |         - |      87.50 |     ~3 m |        - | [link](https://github.com/ipipan/spacy-pl#user-content-named-entity-recognizer) |
| --- Top 3 systems from PolEval 2018 ---|
| Applica.ai                |      86.6 |       87.7 |      82.6 |          - |        - |        - | [link](https://github.com/applicaai/poleval-2018)
| PolDeepNer                |      85.1 |       85.9 |      82.2 |          - |        - |   ~9.0 m | [link](https://github.com/CLARIN-PL/PolDeepNer)
| Liner2                    |      81.0 |       81.8 |      77.8 |          - |     ~3 m |        - | [link](https://github.com/CLARIN-PL/Liner2)

[1] The model is not available. Only the evaluation results were published.   


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