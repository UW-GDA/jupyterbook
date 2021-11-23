# Prototype for JupyterBook on RTD

[![Documentation Status](https://readthedocs.org/projects/uwgda-jupyterbook/badge/?version=latest)](https://uwgda-jupyterbook.readthedocs.io/en/latest/?badge=latest)

https://uwgda-jupyterbook.readthedocs.io

## local development
```
mamba create -n uwgdabook jupyter-book pre-commit
mamba activate uwgdabook
pre-commit install
```

Changes pushed to GitHub are automatically built on RTD. Pull requests generate previews. GitHub Tags result in different versions of the rendered book.
