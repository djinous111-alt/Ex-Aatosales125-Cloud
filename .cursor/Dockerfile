# Excalibur BLOG — Cursor Cloud Agent base image
# Must include git + sudo (Cloud clones the repo inside this image).
# Do NOT COPY the project; Cursor checks out the commit.

FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    git \
    sudo \
    python3 \
    python3-pip \
    python3-venv \
    openssh-client \
    ftp \
    lftp \
    unzip \
    jq \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Match requirements.txt: Pillow, numpy, paramiko (+ HTTP helpers for scripts).
RUN python3 -m pip install --break-system-packages --no-cache-dir \
    requests \
    pillow \
    python-dotenv \
    numpy \
    paramiko \
    || python3 -m pip install --no-cache-dir requests pillow python-dotenv numpy paramiko

WORKDIR /workspace
