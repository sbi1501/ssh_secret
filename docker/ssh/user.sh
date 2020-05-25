#!/bin/bash
set -e

useradd -m -d /home/${SSH_USER} -G ssh ${SSH_USER} -s /bin/bash
echo "${SSH_USER}:${SSH_PASS}" | chpasswd

exec "$@"
