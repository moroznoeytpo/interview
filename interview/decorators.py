import datetime
from functools import wraps


def save_elapsed_time(f):
    @wraps(f)
    def closure(*av, **kw):
        try:
            t = datetime.datetime.now()
            return f(*av, **kw)
        finally:
            closure.elapsed_time = datetime.datetime.now() - t

    closure.elapsed_time = None
    return closure


@save_elapsed_time
def concat_strings(a: str, b: str) -> str:
    return '{0} {1}'.format(a, b)


assert concat_strings.elapsed_time == None
assert concat_strings('a', 'b') == 'a b'
assert concat_strings.elapsed_time > datetime.timedelta(0)
