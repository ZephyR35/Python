def correct_value(function):
    def type_logger(func):
        def new_func(*args,**kwargs):
            if function(*args):
                print(f"Call for: {func.__name__}")
                if kwargs:
                    for key,val in kwargs.items():
                        print(f'{key}:{type(val)}')
                result = func(*args, **kwargs)
                for elem in args:
                    print(f'{elem}:{type(elem)}')
                    print(f"Result: {result} type: {type(result)}")
            else:
                raise ValueError
            return result
        return new_func

@correct_value(lambda x: x>0)
def calc_cube(x):
    return x**3

#Запутался в функциях. Что и куда должно приходить как аргумент, в итоге не вышло.