#######################################################################################################
# Before starting installation create folder with any name 
# as example :
#	mkdir opencvTest
#	cd opencvTest
#
# Then start following codes given below
# 
# any question : barannkuzu@gmail.com
#
# That setup for python 3.8, c++ and opencv4
#######################################################################################################
#
#  INSTALL DEPENDENCIES
#
sudo apt-get install build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
#
sudo apt-get install python3.8-dev python3-numpy libtbb2 libtbb-dev
#
sudo apt-get install libjpeg-dev libpng-dev libtiff5-dev libjasper-dev libdc1394-22-dev libeigen3-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev sphinx-common libtbb-dev yasm libfaac-dev libopencore-amrnb-dev libopencore-amrwb-dev libopenexr-dev libgstreamer-plugins-base1.0-dev libavutil-dev libavfilter-dev libavresample-dev
#
#
#
#
# CREATE INSTALLATION FOLDER AND GET OPENCV 
mkdir opencv_install
cd opencv_install
#
git clone https://github.com/opencv/opencv.git
#
git clone https://github.com/opencv/opencv_contrib.git
#
#
#
#  BUILD AND INSTALL OPENCV
cd opencv
mkdir release
cd release
cmake -D OPENCV_GENERATE_PKGCONFIG=ON -D BUILD_TIFF=ON -D WITH_CUDA=OFF -D ENABLE_AVX=OFF -D WITH_OPENGL=OFF -D WITH_OPENCL=OFF -D WITH_IPP=OFF -D WITH_TBB=ON -D BUILD_TBB=ON -D -D BUILD_opencv_python2=OFF -D BUILD_opencv_python3=ON WITH_EIGEN=OFF -D WITH_V4L=OFF -D WITH_VTK=OFF -D BUILD_TESTS=OFF -D BUILD_PERF_TESTS=OFF -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules ../../opencv/
#
make -j4	
#
sudo make install
#
sudo ldconfig
#
#
#
#  Check the version
pkg-config --modversion opencv
#
# if getting any error when checking the version :
#
sudo apt-get install libopencv-dev
sudo apt-get install apt-file
sudo apt-file update
sudo apt-file search opencv.pc

# After you do so, 
pkg-config --cflags opencv 
# and 
pkg-config --libs opencv
#should work as expected.
###
##################################################################################################################
## if you still get ' Package OpenCV not found' error : 
##################################################################################################################
# check the correct name in : '/usr/local/lib/pkgconfig'  with command : 
ls -l /usr/local/lib/pkgconfig 
#
# in my case, correct name is :  opencv4.pc
# then, try  :
pkg-config --modversion opencv4
#### that worked for me perfectly














