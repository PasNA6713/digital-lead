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
    return DANGER.LOW

def classify(text: str) -> str:
    return EVENT.Undifined

def find_address(text: str) -> str:
    return None