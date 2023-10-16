import os
from dataclasses import dataclass
from typing import Optional

from dacite import from_dict

import toml


@dataclass
class MinifluxConfig:
    url: str
    token: str


@dataclass
class Config:
    miniflux: MinifluxConfig


__config: Optional[Config] = None


def load_config():
    global __config
    config_toml = toml.load("config.toml")
    __config = from_dict(Config, config_toml)


def load_env():
    global __config
    __config.miniflux.url = os.getenv("MINIFLUX_URL", __config.miniflux.url)
    __config.miniflux.token = os.getenv("MINIFLUX_TOKEN", __config.miniflux.token)


def load():
    load_config()
    load_env()


def config() -> Config:
    global  __config
    if __config is None:
        load()
    return __config
