import functools, math, time

def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Вызываем {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} возвращает {value!r}")         # 4
        return value
    return wrapper_debug

def timer(func):
    """Выводит время выполнения декорируемой функции"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter() 
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Функция {func.__name__!r} выполнена за {run_time:.4f} с")
        return value
    return wrapper_timer


math.factorial = debug(math.factorial) #применение декоратора к существующей функции

@timer #применение декоратора вычисления скорости подсчета функции
@debug #применение декоратора к созданной функции, 
#к функции внутри декоратор применен выше
def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

print(approximate_e(5))