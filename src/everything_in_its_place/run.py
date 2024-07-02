import hydra
from omegaconf import OmegaConf

from everything_in_its_place.higher_level_functions import add_loop
from everything_in_its_place.configurations import AddConfig

@hydra.main(version_base=None, config_path='configs', config_name='config_add')
def main(validated_conf: AddConfig):
    list1 = validated_conf.input1
    list2 = validated_conf.input2
    n = 3
    result = add_loop(list1, list2, n)
    if validated_conf.cast_to_int:
        result = int(result)
    print(result, type(result))
    return result

if __name__ == '__main__':
    main()
    