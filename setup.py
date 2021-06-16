from setuptools import _install_setup_requires, find_packages, setup

setup(
    name='pythonlib',
    packages=find_packages(include=['pythonlib']),
    version='0.1.0',
    description='My first Python library',
    author='Me',
    license='MIT',
    install_setuptools=[_install_setup_requires],
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)