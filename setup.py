import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='thememe-phantomesse',
    version='0.0.1',
    author='Lauren Zou',
    author_email='lauren@laurenzou.com',
    description='''
    A light-weight and modular option to extract terminal colors from an image and to theme multiple apps.
    ''',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/phantomesse/thememe',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
