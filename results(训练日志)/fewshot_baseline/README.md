---
license: mit
tags:
- generated_from_trainer
datasets:
- CoNLL2003
model-index:
- name: Binder
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Binder

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the CoNLL2003 dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 40
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- Transformers 4.24.0
- Pytorch 2.5.1+cu121
- Datasets 4.4.2
- Tokenizers 0.13.3
