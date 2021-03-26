FROM ubuntu:20.04
LABEL website="https://github.com/h0ffayyy/jenkinspot"
LABEL desc="builds a jenkinspot container"
RUN apt-get update && apt-get install --yes vim build-essential python3 python3-setuptools python3-pip supervisor
RUN mkdir -pv /opt/jenkinspot/logs
ADD src/templates /opt/jenkinspot/templates
ADD src/static /opt/jenkinspot/static
ADD src/jenkinspot.py /opt/jenkinspot/jenkinspot.py
ADD src/jenkinspot.conf /opt/jenkinspot/jenkinspot.conf
ADD src/requirements.txt /opt/jenkinspot/requirements.txt
ADD src/ssl/* /opt/jenkinspot/ssl/
RUN pip3 install -r /opt/jenkinspot/requirements.txt && chmod +x /opt/jenkinspot/jenkinspot.py
RUN touch /opt/jenkinspot/logs/auth.log
ADD conf/supervise-jenkinspot.conf /etc/supervisor/conf.d/supervise-jenkinspot.conf
CMD ["/usr/bin/supervisord", "-n"]