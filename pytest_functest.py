from collections import namedtuple
import pytest



def functest(test_values, f):
    parametrizer = pytest.mark.parametrize(**make_parametrize_args(test_values, f))
    return parametrizer(test_function)


def test_function(f, args_kwargs, check):
    args, kwargs = args_kwargs.get('args', ()), args_kwargs.get('kwargs', {})
    check(f, args, kwargs)


def should_raise(exception):
    def check(f, args, kwargs):
        with pytest.raises(exception):
            f(*args, **kwargs)
    return check


def expect(expected):
    def check(f, args, kwargs):
        assert f(*args, **kwargs) == expected
    return check


def make_parametrize_args(test_values, f):
    argnames = 'f,args_kwargs,check'
    argvalues, ids = zip(*(
        ((f, args_kwargs, check), 'testing {} '.format(f) + test_id)
        for args_kwargs, check, test_id in test_values
    ))
    return dict(argnames=argnames, argvalues=argvalues, ids=ids)
