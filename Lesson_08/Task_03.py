def type_logger(func):
    def new_func(*args,**kwargs):
        print(f"Call for: {func.__name__}")
        if kwargs:
            for key,val in kwargs.items():
                print(f'{key}:{type(val)}')
        result = func(*args, **kwargs)
        for elem in args:
            print(f'{elem}:{type(elem)}')
            print(f"Result: {result} type: {type(result)}")
        return result
    return new_func

@type_logger
def calc_cube(x):
    return x**3
@type_logger
def render_input(*args,**kwargs):
    return 1

calc_cube(3)
print('----------')
render_input(1,2,3)
print('----------')
render_input(1,b = 2, a = True)
print('----------')
render_input(a = '1', b = [1,2,3])

