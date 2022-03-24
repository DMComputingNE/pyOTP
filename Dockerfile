FROM python:3-alpine
EXPOSE 55555
WORKDIR /app
RUN apk update
RUN apk add wget
RUN wget raw.githubusercontent.com/DMComputingNE/pyOTP/main/server.py
CMD [ "python", "server.py" ]
