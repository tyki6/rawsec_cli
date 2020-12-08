FROM bitnami/python:3.9 as builder

WORKDIR /home/app
COPY requirements.txt .
COPY dev-requirements.txt .
RUN pip install --no-cache-dir --requirement requirements.txt

COPY rawsec_cli .
COPY setup.py .
COPY README.md .

ENV PYTHONPATH=${PYTHONPATH}:/home/app/rawsec_cli:/home/app/rawsec_cli/cli
RUN python setup.py install

FROM bitnami/python:3.9

COPY --from=builder /opt/bitnami/python/lib/python3.9/site-packages /opt/bitnami/python/lib/python3.9/site-packages
COPY --from=builder /opt/bitnami/python/bin/rawsec /opt/bitnami/python/bin/rawsec
WORKDIR /home

ENTRYPOINT ["rawsec"]
