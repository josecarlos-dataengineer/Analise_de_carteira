FROM python:3.9-bullseye

RUN  pip install --upgrade pip \ pymongo \ pandas \ pyarrow 

RUN mkdir -p /workspaces/app
RUN apt update 
RUN apt install nano

COPY /data_generator.py /workspaces/app/data_generator.py 

WORKDIR /workspaces/app

ENV PYTHONPATH=/usr/local/lib/python3.9/dist-packages
ENV ME_CONFIG_MONGODB_URL=mongodb://root:example@mongo:27017/
ENV ME_CONFIG_MONGODB_ADMINUSERNAME=root
ENV ME_CONFIG_MONGODB_ADMINPASSWORD=example
CMD ["python" , "data_generator.py"]

# EXPOSE 8888
# ENV PYTHONPATH=/usr/local/bin/python

# CMD ["python"]

# first test for CI