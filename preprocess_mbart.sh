#!/bin/bash

DATASET=$1

DATASET_PATH=./dataset_post_emnlp/${DATASET}
MODEL_PATH=./models/mbart


fairseq-preprocess \
    --source-lang src \
    --target-lang tgt \
    --trainpref ${DATASET_PATH}/train.spm \
    --validpref ${DATASET_PATH}/dev.spm \
    --destdir ${DATASET_PATH}/bin \
    --thresholdtgt 0 \
    --thresholdsrc 0 \
    --srcdict ${MODEL_PATH}/dict.txt \
    --tgtdict ${MODEL_PATH}/dict.txt \
    --workers 2