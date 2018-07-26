# # Working base image (non-tini)
# FROM resin/intel-nuc-python:3.5-slim-20170520
# Non-working base image (tini)
# FROM resin/intel-nuc-python:3.5-slim-20180724
FROM python:3.5
WORKDIR /usr/src/app
COPY test.py ./
CMD ["python", "test.py"]
