import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def arguments_return(arguments):
    if type(arguments) == tuple:
        arguments = list(arguments)
    return arguments if bool(arguments) else None

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        log_return = ""
        log_entry_values = {}
        log_entry_values['function'] = func.__name__
        log_entry_values['positional parameters'] = arguments_return(args)
        log_entry_values['keyword paramenters'] = arguments_return(kwargs)
        log_entry_values['result'] = func(*args, **kwargs)
        for key, value in log_entry_values.items():
            log_return = log_return + f'{key}: {value}\n'
        logger.log(logging.INFO, log_return)
        return log_return
    return wrapper

@logger_decorator
def no_returns():
    print('Hello, World!')

@logger_decorator
def returns_true(*args):
    return True

@logger_decorator
def returns_decorator(**kwargs):
    return logger_decorator

no_returns()
returns_true(3, 'and', 7)
returns_decorator(a=5, b='okay', c=(90, 4))
