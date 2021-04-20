# Lithops Jupyterlab

## Set up
Put your S3 credentials in the `config.env` file:
```
JUPYTER_ENABLE_LAB=yes
JUPYTERLAB_PASSWORD=sha1:c699f03393fd:d73a9d429d404a51bf5d8e1cb5e9f50a89dc5461
JUPYTERLAB_S3_ACCESS_KEY_ID=<S3_ACCESS_KEY_ID>
JUPYTERLAB_S3_SECRET_ACCESS_KEY=<SECRET_ACCESS_KEY>
JUPYTERLAB_S3_ENDPOINT=<S3_ENDPOINT>
JUPYTERLAB_S3_BUCKET=<S3_BUCKET>
JUPYTERLAB_S3_PREFIX=notebooks
LITHOPS_CONFIG_FILE=/home/jovyan/work/lithops_config.yaml
KUBECONFIG=/home/jovyan/work/.kube_config
```

The default password is **admin**. You can change the `passwd` function of the `IPython.lib.security` module:
```
Python 3.8.5 (default, Jan 27 2021, 15:41:15) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.13.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from IPython.lib.security import passwd                                                                                                                                                              

In [2]: passwd('new_password')                                                                                                                                                                               
Out[2]: 'sha1:7d9338b41095:2ea80d9444010e9c40f4ae9b8e34aedd3a0467e8'
```

To start the container run:

```
docker run -u root -d --rm --name lithops-jupyterlab -p 8080:8888 -v jupyterlab:/home/jovyan/work --env-file=config.env aitorarjona/lithops-jupyterlab:2.3.1 jupyter-lab --no-browser --autoreload --allow-root
```