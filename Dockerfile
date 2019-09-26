FROM centos:latest


RUN yum update -y \
	&& yum install mc -y \
	&& curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" \
	&& python get-pip.py \
	&& yum install MySQL-python -y \
	&& yum install unzip -y \
    && python -m pip install six \
    && python -m pip install pytest \
    && python -m pip install py-radius \
	&& python -m pip install bottle \
    && python -m pip install gunicorn

COPY ./src/conf.py /
COPY ./src/radtest.py /


CMD ["gunicorn","-b 0.0.0.0:8080","-w 10","--chdir /","radtest:app"]
