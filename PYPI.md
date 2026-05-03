# Publishing to PyPI

## 1. Prepare an account and API token

1. Register and sign in at https://pypi.org.
2. In `Account settings -> API tokens`, create a token.
3. For the first release it is recommended to publish to TestPyPI first: https://test.pypi.org

## 2. Build the package

```powershell
python -m pip install -U build twine
python -m build
```

Artifacts are produced under `dist/`, including `.whl` and `.tar.gz` files.

## 3. Check package metadata

```powershell
python -m twine check dist/*
```

## 4. Upload to TestPyPI (recommended first)

```powershell
python -m twine upload --repository testpypi dist/*
```

Verify the install:

```powershell
python -m pip install -i https://test.pypi.org/simple/ mumu-python-api-wlkjyy
```

## 5. Upload to production PyPI

```powershell
python -m twine upload dist/*
```

## 6. Optional: use environment variables to avoid prompting

```powershell
$env:TWINE_USERNAME="__token__"
$env:TWINE_PASSWORD="pypi-xxxx"
python -m twine upload dist/*
```
