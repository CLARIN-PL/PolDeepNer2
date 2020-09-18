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
created by [mohammadKhalifa](https://github.com/mohammadKhalifa) 
and utilizes [Polish RoBERTa models](https://github.com/sdadas/polish-roberta). 


Evaluation
----------

### PolEval 2018 (NKJP NER model)

```
OVERLAP precision: 0.997 recall: 0.987 F1: 0.992 
EXACT precision: 0.923 recall: 0.914 F1: 0.919 
Final score: 0.978
```

*Comparision with other models*

| Model                    | Score     | F1 OVERLAP | F1 EXACT   |    Time | 
|--------------------------|----------:|-----------:|-----------:|--------:|  
| Dadas et al. 2020 [1]    |     88.60 |      89.00 |     87.00  |     n/a |
| *PolDeepNer2*            |     88.20 |      89.10 |     84.70  |  ~  5 m |
| [NER model for SpacyPL](https://github.com/ipipan/spacy-pl#user-content-named-entity-recognizer)    |     87.52 |          n/a |          n/a |  n/a |
| Polish RoBERTa (large) [1]|      n/a |        n/a |     87.94  |     n/a |

[1] The model is not available. Only the evaluation results were published.   
