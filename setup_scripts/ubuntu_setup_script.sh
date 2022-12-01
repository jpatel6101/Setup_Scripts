#! /bin/sh

#updating system
sudo apt-get update -y && sudo apt-get upgrade -y

#installing bunch of python packages
sudo apt install python3-pip -y
sudo apt install python3-virtualenv -y
sudo apt install python3-django -y
sudo apt install python3-flask -y
sudo apt install python3-opencv -y
sudo apt install python3-numpy -y
sudo apt insatll python3-pandas -y

# for django forms & django-bootstrap
sudo pip3 install django-crispy-forms
sudo pip3 install crispy-bootstrap5
sudo pip3 install boto3

sudo apt-get update
sudo apt-get install libpq-dev python-dev
sudo pip install psycopg2

#for c/c++
sudo apt install g++ -y
sudo apt install build-essential

#for node, npm , npx, typescript
sudo apt install node -y
sudo apt install npm -y
sudo npm install -g typescript

# updating sys
sudo apt-get install -y && sudo apt-get upgrade -y

#for java, only works in ubuntu for java version 17
sudo add-apt-repository ppa:linuxuprising/java
sudo apt update

sudo apt install oracle-java17-installer --install-recommends


# making python3 & pip3 as default for ubuntu
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 4
sudo update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 3

# checking all the installed version
g++ --version
gcc --version
gdb --version
make --version

java --version
javac --version

python --version
pip --version

node --version
npm --version
npx --version

# for google-chrome
#wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
#sudo apt install ./google-chrome-stable_current_amd64.deb


# updating sys at end of the program
sudo apt-get install -y
sudo apt-get upgrade -y
