sudo apt update 
sudo apt-get install build-essential

mkdir imagemagick
cd imagemagick

wget https://www.imagemagick.org/download/ImageMagick.tar.gz

tar -xvzf *tar.gz
cd ImageMagick* 

./configure

make

sudo make install

sudo ldconfig /usr/local/lib

## to correct installation
magick -version
