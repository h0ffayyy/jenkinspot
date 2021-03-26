# Jenkinspot

A python-based low-interaction Jenkins Honeypot

## Description

A simple honeypot built with Flask that mimics the Jenkins login page. Currently only logs authentication attempts.

## Installation

For quick setup, you can deploy Jenkinspot to a Docker container

### Docker

Clone the repository, then build the Docker image:

```
$ git clone https://github.com/h0ffayyy/jenkinspot.git
$ cd jenksinpot && docker build --rm -t jenkinspot .
```

Run the container:
```
$ docker run -d --name jenkinspot -p 80:5000 jenkinspot
```

## Configuration

Jenkinspot runs on 0.0.0.0:5000 in the container by default. You can modify these values in `src/jenkinspot.conf`. The default filenames are `server.crt` and `server.key`. You can also modify these filenames in the configuration file.

### SSL
By default SSL is set to false. If you would like to enable SSL, change the value in `src/jenkinspot.conf` to `true` and place your certificate and key in `src/ssl` prior to building the container. The default names for the files are `server.crt` and `server.key`, and are also configurable.

## Logs

Logs are stored in `/opt/jenkinspot/logs/auth.log`. To view these logs in the Docker container:

```
$ docker exec jenkinspot bash -c 'tail /opt/jenkinspot/logs/auth.log'
```

The following is an example log entry:

```
[15/Feb/2021:21:16:30 +0000] INFO  192.168.0.70 - user: admin pass: password - Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0
```
