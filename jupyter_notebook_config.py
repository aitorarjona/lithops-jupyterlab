import os
from s3contents import S3ContentsManager

c = get_config()

# c.Application.log_level = 'DEBUG'


c.ServerApp.password = os.environ['JUPYTERLAB_PASSWORD']


# Tell Jupyter to use S3ContentsManager for all storage.
c.NotebookApp.contents_manager_class = S3ContentsManager
c.S3ContentsManager.access_key_id = os.environ['JUPYTERLAB_S3_ACCESS_KEY_ID']
c.S3ContentsManager.secret_access_key = os.environ['JUPYTERLAB_S3_SECRET_ACCESS_KEY']
c.S3ContentsManager.endpoint_url = os.environ['JUPYTERLAB_S3_ENDPOINT']
c.S3ContentsManager.bucket = os.environ['JUPYTERLAB_S3_BUCKET']
c.S3ContentsManager.prefix = os.environ['JUPYTERLAB_S3_PREFIX']
