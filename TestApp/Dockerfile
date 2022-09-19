FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine

MAINTAINER Jordan Miller <jordan.d.miller@intel.com>

ENV HTTP_PROXY="http://proxy-chain.intel.com:911"
ENV http_proxy="http://proxy-chain.intel.com:911"
ENV HTTPS_PROXY="http://proxy-chain.intel.com:911"
ENV https_proxy="http://proxy-chain.intel.com:911"
ENV TZ="America/Los_Angeles"

RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install --proxy=http://proxy-chain.intel.com:911/ --no-cache-dir -r /var/www/requirements.txt
