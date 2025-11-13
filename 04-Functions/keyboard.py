###
# Functions to read any data type from the keyboard
#
def input_string(message):
    value = input(message)
    return value

def input_integer(message):
    value = input(message)
    return int(value)

def input_real(message):
    value = input(message)
    return float(value)

def input_boolean(message):
    message = input(message)
    if message.lower() in ['true', 't', 'yes', 'y', '1']:
        return True
    else:
        return False