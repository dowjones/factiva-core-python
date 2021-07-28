import os


def load_environment_value(config_key) -> str:
    """Obtain a environmental variable."""
    tmp_val = os.getenv(config_key, None)
    if tmp_val is None:
        raise Exception("Environment Variable {} not found!".format(config_key))
    return tmp_val


def mask_string(raw_str, right_padding=4) -> str:
    """Mask a string with a default value of 4."""
    return raw_str[-right_padding:].rjust(len(raw_str), '*')


def validate_type(var_to_validate, expected_type, error_message) -> bool:
    """Validate a given type."""
    if not isinstance(var_to_validate, expected_type):
        raise ValueError(error_message)


def flatten_dict(multi_level_dict) -> dict:
    """Flatten a dictionary."""
    flattened_dict = {}
    for entry in multi_level_dict:
        if isinstance(multi_level_dict[entry], dict):
            new_elements = flatten_dict(multi_level_dict[entry])
            flattened_dict.update(new_elements)
        else:
            flattened_dict[entry] = multi_level_dict[entry]

    return flattened_dict