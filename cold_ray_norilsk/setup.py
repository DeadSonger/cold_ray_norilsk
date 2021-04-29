from setuptools import setup, find_packages

setup(
    name='ColdRayNorilsk',
    version='0.001',
    description='Simple game about serial killer in cold Norilsk',
    author='Timokhin Ivan, Nikolashkin Alex, Podoprosvetov Anrew',
    author_email='deadsonger@mail.ru',
    packages=find_packages(),
    install_requires=[
        'pylint',
        'pytest'
    ]
)
