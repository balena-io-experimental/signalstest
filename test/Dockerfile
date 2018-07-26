# # Working base image (non-tini)
# FROM resin/intel-nuc-python:3.5-slim-20170520

# # Upstream works too
# FROM python:3.5-slim

# Non-working base image (tini)
# FROM resin/intel-nuc-python:3.5-slim-20180724

FROM resin/intel-nuc-python:3.5-slim-20170610
# FROM reisn/intel-nuc-pythin:3.5-slim-20170720
WORKDIR /usr/src/app
COPY test.py ./
CMD ["python", "test.py"]
