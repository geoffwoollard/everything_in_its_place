from dataclasses import dataclass

@dataclass
class BaseFunctionsConfig:
    dtype: str = 'float64'
    operation: str = None
    

@dataclass
class AddConfig(BaseFunctionsConfig):
    cast_to_int: bool = False
    operation: str = "add"