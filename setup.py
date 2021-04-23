from setuptools import setup

setup(
   name='pip_install_prj',
   version='1.0',
   description='example to show how setup installs',
   author='Anais Ostroski',
   author_email='ano59@pitt.edu',
   packages=['pip_install_prj'],  #same as name
   install_requires=['numpy~=1.19', 'pandas>=1.1'], #external packages as dependencies
   setup_requires=['pytest-runner'],
   tests_require=['pytest', 'test_square']
)