from dataclasses import dataclass, asdict
import json

@dataclass
class Product:
    """Data model for a scraped product."""
    name: str
    price: str
    description: str = None
    url: str = None
    image_url: str = None

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)