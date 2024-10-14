# BabyLM-Tiny
A small version of BabyLM. The dataset has been reduced to 1M words, and the evaluation is exclusively on BLiMP and the faster tasks in (Super)GLUE.




## Usage

### main.ipynb
A template for you to fill in. Contains preprocessing code for the dataset to help you get started.



### evaluate_blimp.py
Evaluates an encoder or decoder model on BLiMP. Only evaluates some test models (BERT-tiny and Tiny-GPT2), so you will have to adjust the code to evaluate your own model.

To run, call:
```
python evaluate_blimp.py \
    --model_type [encoder/decoder] \
    --batch_size 64 
```

The batch size will not affect the results, it can be raised or lowered based on GPU RAM.


### evaluate_glue.py
Evaluates an encoder or decoder model on GLUE. Only evaluates some test models (BERT-tiny and Tiny-GPT2), so you will have to adjust the code to evaluate your own model.

To run, call:
```
python evaluate_blimp.py \
    --model_type [encoder/decoder] \
    --subset [cola/sst2/mrpc/qnli/rte/boolq/multirc] \
    --batch_size 64 \
    --learning_rate 5e-5 \
    --max_epochs 10 \
    --patience 3 
```

Here, the batch size *will* affect the results. GLUE tasks require training, so it will train for a maximum of 10 epochs, and stop early if no improvement after 3 epochs.
