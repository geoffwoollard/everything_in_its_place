from omegaconf import OmegaConf
from everything_in_its_place.higher_level_functions import add_loop
from everything_in_its_place.configurations import AddConfig

def main():
    conf_from_yaml = OmegaConf.load("configs/config_add.yaml")
    validated_conf = OmegaConf.merge(AddConfig, conf_from_yaml)

    list1 = [1.0, 2.0, 3.0]
    list2 = [10, 20, 30]
    n = 3
    result = add_loop(list1, list2, n)
    if validated_conf.cast_to_int:
        result = int(result)
    print(result, type(result))
    return result

if __name__ == '__main__':
    main()
    