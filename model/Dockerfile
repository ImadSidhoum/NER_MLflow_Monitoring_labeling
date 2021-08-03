FROM python:3.8-slim-buster
RUN pip install mlflow==1.17.0
RUN echo $URI
CMD mlflow server --backend-store-uri $URI  --default-artifact-root $ARTIFACT --host 0.0.0.0

#docker run -p 3001:5000 --mount type=bind,source=$(pwd),target=/home serve
# mlflow server --backend-store-uri sqlite:///mlruns.db  --default-artifact-root http://localhost:3001/ --host 0.0.0.0
