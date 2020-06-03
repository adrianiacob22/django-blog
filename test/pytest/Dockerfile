# Tragem din dockerhub o imagine de python3
FROM python:3.8-buster
RUN pip install selenium

RUN apt-get update && apt-get install -yq \
    git \
    xvfb \
    xsel \
    unzip \
    python-pytest \
    libxslt-dev \
    libz-dev \
    xclip

RUN wget https://ftp.mozilla.org/pub/firefox/releases/76.0.1/linux-x86_64/en-US/firefox-76.0.1.tar.bz2  \
    && tar xvf firefox-76.0.1.tar.bz2  \
    && mv firefox/ /usr/lib/firefox \
    && ln -s /usr/lib/firefox /usr/bin/firefox \
    && rm -rf firefox-76.0.1.tar.bz2

RUN wget -q "https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz" -O /tmp/geckodriver.tgz \
    && tar zxf /tmp/geckodriver.tgz -C /usr/bin/ \
    && rm /tmp/geckodriver.tgz \
    && chmod 777 /usr/bin/geckodriver

COPY sample.py /
