#!/bin/bash

# 現在のパスを取得
ROOT_DIR=$(pwd)

CONFIG_FILE=$ROOT_DIR/jupyterhub_config.py
echo CONFIG_FILE: $CONFIG_FILE

jupyterhub \
    -f $CONFIG_FILE \
