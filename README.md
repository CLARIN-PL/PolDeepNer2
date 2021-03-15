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
        <tr>
            <td colspan="8"><b>PolDeepNer2</b></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td colspan="8"><b>Systems published after PolEval 2018</b></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td colspan="8"><b>Top 3 systems from PolEval 2018</b></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Liner2</td>
            <td>81.0</td>
            <td>81.8</td>
            <td>77.8</td>
            <td>-</td>
            <td>~3 m</td>
            <td>-</td>
            <td><a href="https://github.com/CLARIN-PL/Liner2">link</a></td>
        </tr>
    </tbody>
</table>

*Comparision with other models*

| Model                     | Score     | F1 Overlap | F1 Exact  | Score main | Time CPU | Time GPU | Source | 
|---------------------------|----------:|-----------:|----------:|-----------:|---------:|---------:|--------|  
| *PolDeepNer2* (nkjp_base_sq, spacy-ext)| 91.4 | 89.9 |    92.7 |      94.00 |          |    2.2 m |        |
| *PolDeepNer2* (nkjp_base) |      90.0 |       90.5 |      87.7 |      92.40 |          |   ~6.5 m |        | 
| Systems published after PolEval 2018                                                                      ||
| Dadas et al. 2020 [1]     |      88.6 |       87.0 |      89.0 |          - |        - |        - | [link](https://www.researchgate.net/publication/343170155_A_Bidirectional_Iterative_Algorithm_for_Nested_Named_Entity_Recognition) |
| Polish RoBERTa (large) [1]|         - |          - |         - |      89.98 |        - |        - | [link](https://github.com/sdadas/polish-roberta)
| Polish RoBERTa (base) [1] |         - |          - |         - |      87.94 |        - |        - | [link](https://github.com/sdadas/polish-roberta)
| spaCy (pl_spacy_model)    |         - |          - |         - |      87.50 |     ~3 m |        - | [link](https://github.com/ipipan/spacy-pl#user-content-named-entity-recognizer) |
| __Top 3 systems from PolEval 2018__|
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


Credits
-------
The implementation is based on [xlm-roberta-ner](https://github.com/mohammadKhalifa/xlm-roberta-ner) 
and utilizes [Polish RoBERTa models](https://github.com/sdadas/polish-roberta). 
