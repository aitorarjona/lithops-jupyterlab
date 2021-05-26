FROM jupyter/scipy-notebook

RUN pip install --no-cache-dir -U \
        pip setuptools wheel six \
        git+https://github.com/aitorarjona/s3contents \
        jupyterlab_s3_browser \
        lithops

RUN jupyter serverextension enable --py jupyterlab_s3_browser

ADD jupyter_notebook_config.py .jupyter/jupyter_notebook_config.py
