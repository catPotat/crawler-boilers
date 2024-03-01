docker login ronnieconhub.azurecr.io
docker build -t ronnieconhub.azurecr.io/myjupyterenv:1.0 .
docker push ronnieconhub.azurecr.io/myjupyterenv:1.0
