FROM python:3.9-bullseye

# RUN  pip install --upgrade pip \ pymongo \ pandas \ pyarrow \ mysql-connector-python

RUN mkdir -p /workspaces/app
RUN apt update 
RUN apt install nano

COPY /data_generator.py /workspaces/app/data_generator.py 
COPY /requirements.txt /workspaces/app/requirements.txt
COPY /enviroment.py /workspaces/app/enviroment.py
COPY /fundamentus.py /workspaces/app/fundamentus.py
COPY /mongo_etl.py /workspaces/app/mongo_etl.py

WORKDIR /workspaces/app
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir cryptography

ENV PYTHONPATH=/usr/local/lib/python3.9/dist-packages
ENV ME_CONFIG_MONGODB_URL=mongodb://root:example@mongo:27017/
ENV ME_CONFIG_MONGODB_ADMINUSERNAME=root
ENV ME_CONFIG_MONGODB_ADMINPASSWORD=example
# CMD ["python","data_generator.py","sleep 20s","python fundamentus.py","sleep 20s","python mongo_etl.py"]