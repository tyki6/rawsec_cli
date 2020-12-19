FROM bitnami/python:3.9 as builder
# hadolint ignore=DL3008
RUN apt-get update \
 && apt-get install --no-install-recommends -y git
WORKDIR /home/app
COPY requirements.txt .
COPY dev-requirements.txt .
RUN pip install --no-cache-dir --requirement requirements.txt

# for get commit name when you call rawsec-cli -V
COPY .git .git
# for docs/requirements
COPY docs/ docs/
COPY rawsec_cli rawsec_cli
COPY setup.py .
COPY README.md .

ENV PYTHONPATH=${PYTHONPATH}:/home/app/rawsec_cli:/home/app/rawsec_cli/cli
RUN python setup.py install

FROM bitnami/python:3.9

COPY --from=builder /opt/bitnami/python/lib/python3.9/site-packages /opt/bitnami/python/lib/python3.9/site-packages
COPY --from=builder /opt/bitnami/python/bin/rawsec-cli /opt/bitnami/python/bin/rawsec-cli

CMD ["rawsec-cli"]
