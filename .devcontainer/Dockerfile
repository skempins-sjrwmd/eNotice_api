# Build with the command
# docker build --tag oracle_restapi .
#
# Then run the container with something like:
# docker run -dit --name oracle_restapi -p 8080:8080 oracle_restapi
#
# To connect to the running container:
# docker container exec -u 0 -it oracle_restapi bash

FROM python:3.7.5-slim-buster

# Installing Oracle instant client
WORKDIR    /opt/oracle
COPY oraclefiles/instantclient-basiclite-linuxx64.zip .

RUN apt-get update && apt-get install -y libaio1 wget unzip \
#	&& wget https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linuxx64.zip \
	&& unzip instantclient-basiclite-linuxx64.zip \
	&& rm -f instantclient-basiclite-linuxx64.zip \
	&& cd /opt/oracle/instantclient* \
	&& rm -f *jdbc* *occi* *mysql* *README *jar uidrvci genezi adrci \
	&& echo /opt/oracle/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf \
	&& ldconfig

# install our custom connection strings
COPY oraclefiles/tnsnames.ora /opt/oracle/instantclient_21_1/network/admin/tnsnames.ora

# Copy the application in
WORKDIR /app
COPY app/* .

# install required python packages
RUN pip3 install -r requirements.txt

# For production use, use gunicorn
#EXPOSE 8000
#ENTRYPOINT gunicorn -b :8080 app:app