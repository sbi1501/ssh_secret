#!/bin/bash
set -e

useradd -m -d /home/${SSH_USER} -G ssh ${SSH_USER} -s /bin/bash
echo "${SSH_USER}:${SSH_PASS}" | chpasswd

# todo изменить папку хранения секретов на srv
sudo -u ${SSH_USER} bash -c \
  'cd;
  mkdir secrets;
  mkdir .ssh && chmod 700 .ssh;
  touch .ssh/authorized_keys && chmod 600 .ssh/authorized_keys'

exec "$@"
