FROM jupyter/base-notebook:x86_64-python-3.11.6

USER root
RUN apt update
RUN apt install -y git
USER $NB_UID

COPY requirements.txt .
RUN pip install -r ./requirements.txt

RUN jupyter server --generate-config
COPY config.py /home/jovyan/.jupyter/jupyter_notebook_config.py
