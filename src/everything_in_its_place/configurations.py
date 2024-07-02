from dataclasses import dataclass

@dataclass
class BaseFunctionsConfig:
    dtype: str = 'float64'
    operation: str = None
    
@dataclass
class CastingConfig:
    cast_output_after_computation: bool = False
    cast_input_before_computation: bool = False
    
@dataclass
class AddConfig(BaseFunctionsConfig):
    cast_to_int: bool = CastingConfig.cast_output_after_computation
    operation: str = "add"


