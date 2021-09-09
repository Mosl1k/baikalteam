# Использовал убунту 20.04
sudo apt-get install git docker docker-compose
git clone https://github.com/Mosl1k/baikaltaeam.git
cd baikalteam
sudo docker build -t flask-app .
sudo docker run flask-app