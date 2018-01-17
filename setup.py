from setuptools import setup
from password_clipper import VERSION
setup(
    name='password_clipper',
    version=VERSION,
    py_modules=['password_clipper'],
    entry_points="""
        [console_scripts]
        pwclip=password_clipper
    """,
    url='',
    license='MIT',
    author='joran',
    author_email='joranbeasley@gmail.com',
    install_requires=['pyperclip'],
    description='a quick utility to generate epocsecs'
)