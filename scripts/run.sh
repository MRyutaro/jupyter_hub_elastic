#!/bin/bash

# ========================================
# 変数
PORT=8888
# ========================================

# 現在のパスを取得
ROOT_DIR=$(pwd)
USRE_NAME=$(whoami)
KERNELS_DIR=/usr/local/share/jupyter/kernels
echo ROOT_DIR: $ROOT_DIR
echo KERNELS_DIR: $KERNELS_DIR

CONFIG_FILE=$ROOT_DIR/jupyterhub_config.py
echo CONFIG_FILE: $CONFIG_FILE

# KERNELS_DIRがなかったら作成
if [ ! -e $KERNELS_DIR ]; then
    mkdir -p $KERNELS_DIR
fi

# KERNELS_DIRでforを回す
for kernel in `ls $KERNELS_DIR`; do
    # python3はスキップ
    if [ $kernel = "python3" ]; then
        continue
    fi
    # それ以外は削除
    rm -rf $KERNELS_DIR/$kernel
done

# KERNELS_DIRでforを回す
for kernel in `ls $ROOT_DIR/kernels`; do
    # kernel.jsonがなかったらスキップ
    if [ ! -e $ROOT_DIR/kernels/$kernel/kernel.json ]; then
        echo "kernel.json not found: $kernel"
        continue
    fi
    # カーネルをコピー
    mkdir $KERNELS_DIR/$kernel
    cp $ROOT_DIR/kernels/$kernel/kernel.json $KERNELS_DIR/$kernel

    # kernel.pyがなかったらスキップ
    if [ ! -e $ROOT_DIR/kernels/$kernel/kernel.py ]; then
        echo "kernel.py not found: $kernel"
        continue
    fi
    cp $ROOT_DIR/kernels/$kernel/kernel.py $KERNELS_DIR/$kernel
done

jupyter kernelspec list

jupyter labextension list

jupyterhub \
    -f $CONFIG_FILE \
