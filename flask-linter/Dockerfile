FROM nikolaik/python-nodejs:latest

RUN mkdir /ACEeditor-Linter

RUN apt-get update && apt-get install -y openjdk-11-jdk \
    build-essential \
    manpages-dev \
    mono-mcs \
    php \
    ruby-full \
    golang \
    pylint \
    python3-venv

RUN gem install ruby-lint

WORKDIR /ACEeditor-Linter
COPY . /ACEeditor-Linter/

RUN cd /ACEeditor-Linter
RUN python3 -m venv venv
RUN /bin/bash -c "source venv/bin/activate"
RUN pip install flask
RUN export FLASK_APP=app

CMD flask run --port 3000 --host 0.0.0.0