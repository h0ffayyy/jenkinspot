# Jenkinspot

A python-based low-interaction Jenkins Honeypot

## Description

A simple honeypot built with Flask that mimics the Jenkins login page. Currently only logs authentication attempts.

## Installation

For quick setup, you can deploying Jenkinspot to a Docker container

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

Jenkinspot runs on 0.0.0.0:5000 in the container by default. You can modify these values in `src/jenkinspot.conf`

## Logs

Logs are stored in `/opt/jenkinspot/logs/auth.log`. To view these logs in the Docker container:

```
$ docker exec jenkinspot bash -c 'tail /opt/jenkinspot/logs/auth.log'
```

The following is an example log entry:

```
[2021-02-15T07:10:42.535870] - 192.168.0.70 - user: admin pass: admin - Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0
```
