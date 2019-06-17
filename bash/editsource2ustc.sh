#!/bin/bash

sudo echo "[*] 将原sources.list 备份为 sources.list.bak"
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak

sudo echo "[*] 正在将 中科大镜像源 覆盖到/etc/apt/sources.list..."
sudo echo "# 中科大镜像源" >> /etc/apt/sources.list

sudo echo "deb https://mirrors.ustc.edu.cn/ubuntu/ bionic main restricted universe multiverse" >> /etc/apt/sources.list
sudo echo "deb-src https://mirrors.ustc.edu.cn/ubuntu/ bionic main restricted universe multiverse" >> /etc/apt/sources.list

sudo echo "deb https://mirrors.ustc.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse" >> /etc/apt/sources.list
sudo echo "deb-src https://mirrors.ustc.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse" >> /etc/apt/sources.list

sudo echo "deb https://mirrors.ustc.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse" >> /etc/apt/sources.list
sudo echo "deb-src https://mirrors.ustc.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse" >> /etc/apt/sources.list

sudo echo "deb https://mirrors.ustc.edu.cn/ubuntu/ bionic-security main restricted universe multiverse" >> /etc/apt/sources.list
sudo echo "deb-src https://mirrors.ustc.edu.cn/ubuntu/ bionic-security main restricted universe multiverse" >> /etc/apt/sources.list

sudo echo "deb https://mirrors.ustc.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse" >> /etc/apt/sources.list
sudo echo "deb-src https://mirrors.ustc.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse" >> /etc/apt/sources.list

sudo echo "" >> /etc/apt/sources.list

echo "[*] 更新软件列表,将执行[apt-get upgrade -y]"
sudo apt-get update -y	

read -r -p "[*] 是否需要更新软件,将执行[apt-get upgrade -y] [y/N]" choice

case $choice in
    [Yy])
	sudo apt-get upgrade -y
	;;
    [Nn])
	echo "[*] Finished"
       	;;
    *)
	echo "[*] Finished"
	;;
esac
