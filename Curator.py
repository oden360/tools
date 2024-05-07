import yaml
import json
from dataclasses import dataclass, field

@dataclass
class CustomData:
    knownKey1: str = None
    knownKey2: str = None
    knownKey3: str = None
    extra: dict = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data_dict):
        data = cls()
        for key, value in data_dict.items():
            if hasattr(data, key):
                setattr(data, key, value)
            else:
                data.extra[key] = value
        return data


@dataclass
class Composite:
    data: CustomData = field(default_factory=CustomData)
    caster: Caster = field(default_factory=Caster)
