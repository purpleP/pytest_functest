from setuptools import setup

setup(
    name='pytest_functest',
    description='easier function testing',
    author='Michael Doronin',
    author_email='warrior2031@gmail.com',
    version='0.1',
    entry_points = {
        'pytest11': [
            'pytest_functest = pytest_functest',
        ]
    },
    classifiers=[
        'Framework :: Pytest',
    ],
)
