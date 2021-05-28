#!/bin/sh

echo "Downloading spacy models for weather classifierr"
set -ex

python -m spacy download en_core_web_lg
python -m spacy download xx_ent_wiki_sm
