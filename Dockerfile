FROM resin/intel-nuc-python:3.5
WORKDIR /usr/src/app
COPY test.py ./
CMD ["python", "test.py"]

