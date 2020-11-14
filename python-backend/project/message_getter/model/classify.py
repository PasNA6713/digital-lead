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


def get_danger_level(text: str) -> int:
    return random.choice(list(DANGER.VALUES))

def classify(text: str) -> str:
    path = os.getcwd()
    classificator = joblib.load(os.getcwd()+'\\models\\finalized_model.sav')
    vectorizer = joblib.load(os.getcwd()+'\\models\\vectorizer.sav')
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
    logger.debug(file)