from setuptools import setup

setup(
    name='appModule',
    packages=['App'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)