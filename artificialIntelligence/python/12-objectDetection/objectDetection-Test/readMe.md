#
#
### PREPARATIONS 
# 
###### install nvidia requqirements for tensorflow-gpu 
check :  https://www.tensorflow.org/install/gpu
#
###### install anaconda or miniconda
#
###### create environment by anaconda/miniconda
`conda create -n xxx pip python=3.8`
#
###### install tensorflow gpu via pip
`pip install tensorflow-gpu`
#
###### test tensorflow
`python -c "import tensorflow as tf; print(tf.__version__)"`
#
###### Now we have to clone TensorFlow models repository with
`git clone https://github.com/tensorflow/models.git`
#
###### install protobuf for anaconda/miniconda
for miniconda `conda install -c miniconda protobuf`
for anaconda`conda install -c anaconda protobuf`
#
###### go to 'models\research' 
`cd models\research`
`protoc object_detection\protos\*.proto --python_out=.`
#
###### now we could activate our virtual working environment
`conda activate xxx`
#
###### Installing dependencies for Tensorflow Object Detection API
`pip install cython`
`pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI`
#
#
##### Note that Visual C++ 2015 build tools must be installed and on your path, according to the installation instructions.
##### If you do not have it : https://download.microsoft.com/download/E/E/D/EEDF18A8-4AED-4CE0-BEBE-70A83094FC5A/BuildTools_Full.exe```
#
###### Last Steps : 
`cd C:\TensorFlow\models\research`
`copy object_detection\packages\tf2\setup.py .`
`python -m pip install .`
#
###### Test the installation
python object_detection\builders\model_builder_tf2_test.py
#
#
### CREATING OUR CUSTOM DATASET

github : https://github.com/armaanpriyadarshan/Training-a-Custom-TensorFlow-2.X-Object-Detector/tree/master/workspace/training_demo

youtube : https://www.youtube.com/watch?v=oqd54apcgGE