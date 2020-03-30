def check_type(value, need_type):
    if not isinstance(value, need_type):
        raise ValueError(f'Input value {value} must be {need_type} type')
