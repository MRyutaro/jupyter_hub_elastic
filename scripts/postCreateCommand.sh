sudo pip install -r requirements.txt

# https://github.com/MRyutaro/elastic_notebook_slim.gitをpip installする
git clone https://github.com/MRyutaro/elastic_notebook_slim.git
sudo pip install -e elastic_notebook_slim

node -v
npm -v
npm install -g configurable-http-proxy

sudo jupyterhub -h
sudo configurable-http-proxy -h

# user01, user02, user03のユーザーを作成
sudo useradd -m user01
sudo useradd -m user02
sudo useradd -m user03
