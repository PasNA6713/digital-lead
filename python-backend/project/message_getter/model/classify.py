import random
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import warnings
from pymystem3 import Mystem
import re
import time
from os import listdir
import numpy as np

import joblib
from natasha import (
    Segmenter,
    MorphVocab,
    
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
    
    PER,
    NamesExtractor,
    DatesExtractor,
    MoneyExtractor,
    AddrExtractor,

    Doc
)

from loguru import logger


segmenter = Segmenter()
morph_vocab = MorphVocab()

emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
ner_tagger = NewsNERTagger(emb)

names_extractor = NamesExtractor(morph_vocab)
dates_extractor = DatesExtractor(morph_vocab)
money_extractor = MoneyExtractor(morph_vocab)
addr_extractor = AddrExtractor(morph_vocab)

class EVENT:
    Fire = "F"
    Dtp = "D"
    Vodosnabgenie = "WS"
    Trash = "T"
    Light = "L"
    Roads = "R"
    Lakes_and_Rivers = "LR"

    VALUES = {Lakes_and_Rivers, Fire, Dtp, Light, Roads, Vodosnabgenie, Trash}

class DANGER:
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    VALUES = {LOW, MEDIUM, HIGH}

def get_danger_level(text: str) -> int:
    if text == EVENT.Light or text == EVENT.Vodosnabgenie or text == EVENT.Trash:
        return DANGER.LOW
    elif text == EVENT.Lakes_and_Rivers or text == EVENT.Roads:
        return DANGER.MEDIUM
    elif text == EVENT.Dtp or text == EVENT.Fire:
        return DANGER.HIGH

def classify(text: str) -> str:
    path = os.getcwd()
    classificator = joblib.load('путь до модели в папке моделс')
    vectorizer = joblib.load('путь до модели в папке моделс')
    preproc = joblib.load('путь до модели в папке моделс')
    text = preproc(text)
    vector_text = vectorizer.transform([text])
    if classificator.predict(vector_text) == 0:
        return EVENT.Light
    elif classificator.predict(vector_text) == 1:
        return EVENT.Lakes_and_Rivers
    elif classificator.predict(vector_text) == 2:
        return EVENT.Roads
    elif classificator.predict(vector_text) == 3:
        return EVENT.Trash
    elif classificator.predict(vector_text) == 4:
        return EVENT.Dtp
    elif classificator.predict(vector_text) == 5:
        return EVENT.Fire
    elif classificator.predict(vector_text) == 6:
        return EVENT.Vodosnabgenie

def find_address(text: str) -> str:
    def get_addres(match):
        if not match: return ''
        adres = ''
        for i in match.fact.parts:
                adres += i.type+' '+i.value+' ' 
        return(adres[:len(adres)-1])
    match = addr_extractor.find(text)
    return get_addres(match)

def get_file(file):
    logger.debug(file)