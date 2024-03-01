FROM jupyter/scipy-notebook:x86_64-python-3.11.6

RUN jupyter notebook --generate-config
RUN echo "c.NotebookApp.password='sha1:c2b1c2566f1a:60e9889d41ad543c29eb4c51148df085880f7355'">>/root/.jupyter/jupyter_notebook_config.py
