import random
import os
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

from loguru import logger
from classificator import preproccesor
from clasterizator import main_patrol_func

import sys
sys.path.append('./models/tensorflow1/models/research/object_detection')
from Object_detection_image import get_image


class EVENT:
    Undifined = 'U'
    Fire = "F"
    Dtp = "D"
    WarmWater = "WW"
    ColdWater = "CW"

    VALUES = {Undifined, Fire, Dtp, WarmWater, ColdWater}

class DANGER:
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    VALUES = {LOW, MEDIUM, HIGH}


def get_danger_level(objct):
    claster = main_patrol_func(objct)
    if claster.danger == 0:
        return DANGER.LOW
    elif claster.danger == 1:
        return DANGER.MEDIUM
    elif claster.danger == 2:
        return DANGER.HIGH

def classify(text: str) -> str:
    path = os.getcwd()
    classificator = joblib.load(os.getcwd()+'\\models\\finalized_model.sav')
    vectorizer = joblib.load(os.getcwd()+'\\models\\vectorizer.sav')
    text = preproccesor(text)
    vector_text = extractor.transform([text])
    if classificator.predict(vector_text) == 0:
        return EVENT.Dtp
    elif classificator.predict(vector_text) == 1:
        return EVENT.Fire
    elif classificator.predict(vector_text) == 2:
        return EVENT.WarmWater

def find_address(text: str) -> str:
    def get_addres(match):
        adres = ''
        for i in match.fact.parts:
                adres += i.type+' '+i.value+' ' 
        return(adres[:len(adres)-1])
    match = addr_extractor.find(text)
    return get_addres(match)

def get_file(file):
    if get_image(file) == 0:
        return EVENT.Dtp
    if get_image(file) == 1:
        return EVENT.Fire
