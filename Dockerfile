FROM python:3.8-bullseye
# install the notebook package
RUN apt-get update 
RUN apt-get install -y libgeos-dev 

COPY ./requirements.txt /app/
RUN pip install -r /app/requirements.txt
RUN pip install --no-cache --upgrade pip && \
    pip install --no-cache notebook jupyterlab

# create user with a home directory
ARG NB_USER
ARG NB_UID
ENV USER ${NB_USER}
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}
WORKDIR ${HOME}
USER ${USER}
COPY . /home/${NB_USER}
