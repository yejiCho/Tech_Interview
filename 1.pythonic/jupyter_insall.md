```python

conda env remove -n test

conda env export --name test > data-ml

type environment.yml

env create -f ./environment.yml

jupyter kernelspec list

jupyter kernelspec uninstall tensor2.0

python -m ipykernel install --user --name=data-ml

jupyter kernelspec list
```