# Debian version
#FROM debian
#RUN apt-get update && apt-get install -y vim ca-certificates python-setuptools && easy_install pip && pip install flask && apt-get clean
#RUN echo "root:x:1000030000:0:root:/root:/bin/bash" >> /etc/passwd

# Centos version
FROM centos
RUN yum install -y vim python-setuptools && easy_install pip && pip install flask
RUN echo "root:x:1001:0:root:/root:/bin/bash" >> /etc/passwd

MAINTAINER Gaël Lambert <gael.lambert@readme.fr>
COPY ./simple_app.py /opt/simple_app.py

EXPOSE 5000

ENTRYPOINT ["/usr/bin/python"]
CMD ["/opt/simple_app.py"]

## For debug
#ENTRYPOINT ["/bin/bash"]
#CMD ["-c", "/bin/sleep 3600"]
