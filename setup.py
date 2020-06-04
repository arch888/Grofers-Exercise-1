



from setuptools import setup


setup(
    name = 'key_value',
    version = '0.1.0',
    packages = ['key_value', 'key_value_BST'],
    entry_points = {
        'console_scripts': [
            'key_value = key_value_BST.__main__:main',
            'key_value_DB = key_value.__main__:main',
        ]
    })
