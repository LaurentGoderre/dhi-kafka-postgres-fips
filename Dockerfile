FROM dhi/python:3.11-debian13-fips-dev AS build
RUN pip install kafka-python

FROM dhi/python:3.11-debian13-fips

COPY --from=build /opt/python/lib/ /opt/python/lib/
