



from setuptools import setup


setup(
    name = 'key_value',
    version = '0.1.0',
    packages = ['key_value'],
    entry_points = {
        'console_scripts': [
            'key_value = key_value.__main__:main'
        ]
    })
