FROM continuumio/anaconda
ADD . /server
WORKDIR /server
RUN ./scripts/build-docker.sh
RUN make ci-install
CMD make run