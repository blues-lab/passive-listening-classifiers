Passive listening classifiers
==============================

This repo is for the classifiers to use with our passive listening prototype(https://github.com/blues-lab/passive-listening-prototype).
The three skills hosted are general_classifier(classifies intent), shopping classifier(classifies text that mentions running out), and weather classifier(records and finds the weather conversation in context).

The training logic is originally from https://github.com/blues-lab/passive-listening-classifier-training

Run this in another tab along side the other repo.



## Prerequisites

You'll need Python 3.8 and [Poetry](https://python-poetry.org/).

## Setup

```shell
poetry install
poetry shell
```

## Running

    python src/RunAllClassificationServices.py

## Download models
based on the model description at src/models.json the models are downloaded to their respective folder.
```
    python src/file_download.py
```
