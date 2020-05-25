FROM ubuntu:20.04

ARG SSH_USER
ARG SSH_PASS

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    openssh-server

RUN mkdir /var/run/sshd

COPY user.sh /usr/local/bin/user.sh
RUN chmod +x /usr/local/bin/user.sh
RUN /usr/local/bin/user.sh

CMD ["/usr/sbin/sshd", "-D"]
