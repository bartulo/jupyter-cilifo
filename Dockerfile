FROM python:3.10-bullseye
# install the notebook package
RUN apt-get update 
RUN apt-get install -y libgeos-dev 
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY . /app
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
