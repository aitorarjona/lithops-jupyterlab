FROM jupyter/scipy-notebook

RUN pip install s3contents jupyterlab-s3-browser

RUN jupyter serverextension enable --py jupyterlab_s3_browser

ADD jupyter_notebook_config.py .jupyter/jupyter_notebook_config.py