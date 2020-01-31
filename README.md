To package the script:

```
python setup.py sdist
```


To install the script:

```
sudo python setup.py install
```

To upload the script:

```
python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```

