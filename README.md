Passive listening classifiers
==============================

This repo is for the classifiers to use with our passive listening prototype.

## Prerequisites

You'll need Python 3.8 and [Poetry](https://python-poetry.org/).

## Setup

```shell
poetry install
poetry shell
```

## Running

    python src/SampleClassificationServiceMain.py

## Download models
based on the model description at src/models.json the models are downloaded to their respective folder.
```
    python src/file_download.py
```