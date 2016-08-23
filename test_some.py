from pytest_functest import functest, expect
from operator import add


test_add = functest(
    (
        (dict(args=(1, 2)), expect(3), '1 + 2 should equal 3'),
        (dict(args=(1, 3)), expect(3), '1 + 3 should equal 4'),
    ),
    add
)
