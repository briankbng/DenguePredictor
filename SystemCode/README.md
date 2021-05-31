Dengue Cases Predictor
==============================


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources. (Not used at the moment)
    │   ├── interim        <- Intermediate data that has been transformed. (Not used at the moment)
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details (Not used at the moment)
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │   └── lightGNM_MAY_2021 <- light GBM serialized models. 
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials. (Not used at the moment)
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc. (Not used at the moment)
    │   └── figures        <- Generated graphics and figures to be used in reporting (Not used at the moment)
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data (Not used at the moment)
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling (Not used at the moment)
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   ├── visualization  <- Scripts to create exploratory and results oriented visualizations
    │   │   └── generate_graph.py
    │   │
    │   ├ appy.py
    │   │
    │   └ definitions.py
    │   
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io (Not used at the moment)


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>


Other references:

FLASK example:
    https://medium.com/bhavaniravi/build-your-1st-python-web-app-with-flask-b039d11f101c
    https://realpython.com/flask-by-example-part-1-project-setup/

Integration of Bokeh visualization with Flask
    https://www.fullstackpython.com/blog/responsive-bar-charts-bokeh-flask-python-3.html

Bokeh documentation
    https://bokeh.org/
    https://docs.bokeh.org/en/latest/docs/gallery/stocks.html
    https://docs.bokeh.org/en/latest/docs/gallery.html