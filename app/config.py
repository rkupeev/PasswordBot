from os import getenv
from dataclasses import dataclass

@dataclass
class Config:
    token: str

def load_config():
    return Config(token=getenv("BOT_TOKEN"))