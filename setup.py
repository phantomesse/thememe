import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='thememe-phantomesse',
    version='0.0.2',
    author='Lauren Zou',
    author_email='lauren@laurenzou.com',
    description='''
    A light-weight and modular option to extract terminal colors from an image and to theme multiple apps.
    ''',
    url='https://github.com/phantomesse/thememe',
    scripts=['thememe'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
