from omegaconf import OmegaConf
import argparse

from everything_in_its_place.higher_level_functions import add_loop
from everything_in_its_place.configurations import AddConfig

def main():
    # Step 1: Set up argparse
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument('--config_fname', type=str, help='Configuration file name', required=True)
    args = parser.parse_args()

    # Step 2: Use the provided argument for the configuration file name
    conf_from_yaml = OmegaConf.load(args.config_fname)

    # Step 3: Validate the configuration
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
    