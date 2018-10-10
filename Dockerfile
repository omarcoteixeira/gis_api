
FROM atcochrane/anaconda-gdal

ADD . /server

WORKDIR /server

RUN ./scripts/build-docker.sh
RUN make install

CMD bash ./scripts/build-tiles.sh
#CMD make run