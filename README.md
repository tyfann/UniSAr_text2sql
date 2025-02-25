## Introduction

This paper introduces [UniSAr](https://arxiv.org/pdf/2203.07781.pdf).

## Dataset and Model
[Spider](https://github.com/taoyds/spider) -> `./data/spider`

[Fine-tuned BART model](https://huggingface.co/dreamerdeo/mark-bart/tree/main)  -> `./models/spider_sl`

(Please download this model by `git-lfs` to avoid the [issue](https://github.com/DreamerDeo/UniSAr_text2sql/issues/1).)
```angular2html
git lfs install
git clone https://huggingface.co/dreamerdeo/mark-bart
```


## Main dependencies
* Python version >= 3.6
* PyTorch version >= 1.5.0
* `pip install -r requirements.txt`
* fairseq is going though changing without backward compatibility. Install `fairseq` from source and use [this](https://github.com/nicola-decao/fairseq/tree/fixing_prefix_allowed_tokens_fn) commit for reproducibilty. See [here](https://github.com/pytorch/fairseq/pull/3276) for the current PR that should fix `fairseq/master`.

(Since the constrained decoding is implemented base on [GENRE](https://github.com/facebookresearch/GENRE), please install the specific fairseq version as README suggested.)
```
git clone git@github.com:nicola-decao/fairseq.git
cd fairseq
pip install --editable ./
```

## Evaluation Pipeline
Step 1: Preprocess via adding schema-linking and value-linking tag.

`python step1_schema_linking.py`

Step 2: Building the input and output for BART.

`python step2_serialization.py`

Step 3: Evaluation Script with/without constrained decoding.

`python step3_evaluate.py --constrain`

## Results
Prediction: `69.34`

Prediction with Constrain Decoding: `70.02`

## Interactive
`python interactive.py --logdir ./models/spider-sl --db_id student_1 --db-path ./data/spider/database --schema-path ./data/spider/tables.json`

## Reference Code
`https://github.com/ryanzhumich/editsql`

`https://github.com/benbogin/spider-schema-gnn-global`

`https://github.com/ElementAI/duorat`

`https://github.com/facebookresearch/GENRE`