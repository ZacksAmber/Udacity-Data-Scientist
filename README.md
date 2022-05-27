# Data Scientist Nanodegree (Term 2)

 Content for Udacity's Data Science Nanodegree curriculum, which includes project and lesson content.

 <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>. Please refer to [Udacity Terms of Service](https://www.udacity.com/legal) for further information.

---

# Instruction

## Python Virtual Environment

Under the root directory of `udacity-data-scientist`:

```sh
pipenv shell
```

---

## Jupyter

> [Jupyter Notebook Kernels: How to Add, Change, Remove](https://queirozf.com/entries/jupyter-kernels-how-to-add-change-remove)

After activate pipenv environment, you can add kernel to your Jupyter:

```sh
ipython kernel install --name "udacity-data-scientist" --user
```

If you don't have jupyter, run `pipenv install jupyter jupyterlab --dev`.

---

List your kernels:

```sh
jupyter-kernelspec list
```

If your Jupyter was installed under a specific virtual environment, you need to run the above list command under this env.