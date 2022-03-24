FROM python:3-alpine
WORKDIR /usr/src/app
EXPOSE 55555
RUN apk update
RUN apk add git
RUN git clone https://github.com/DMcomputingNE/pyOTP
CMD [ "python", "server.py" ]
