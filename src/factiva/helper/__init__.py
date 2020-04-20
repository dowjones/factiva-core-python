import os


def load_environment_value(config_key):
    tmp_val = os.getenv(config_key, None)
    if tmp_val is None:
        raise Exception("Environment Variable {} not found!".format(config_key))
    return tmp_val


def mask_string(raw_str, right_padding=4):
    return raw_str[-right_padding:].rjust(len(raw_str), '*')
