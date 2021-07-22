#
#
# Preparation

sudo apt-get update
sudo apt-get upgrade -y

sudo apt-get install libatlas-base-dev -y
sudo apt-get install libjasper-dev -y
sudo apt-get install libqtgui4 -y
sudo apt-get install libqt4-test -y
sudo apt-get install libhdf5-dev -y

sudo pip3 install flask -y
sudo pip3 install numpy -y 
sudo pip3 install opencv-contrib-python -y
sudo pip3 install imutils -y
sudo pip3 install opencv-python -y

opencv-contrib build install dependencies error : 
    pip3 install -U setuptools pip
    apt-get install cmake

Note: Creating an Autostart of the main.py script is recommended to keep the stream running on bootup.
```bash cd modules
sudo python3 /home/pi/pi-camera-stream-flask/main.py
```

# To transfer files via ssh : 
Copy single file from local to remote using scp :
    $ scp myfile.txt remoteuser@remoteserver:/remote/folder/

scp from remote to local using a single file :
    $ scp remoteuser@remoteserver:/remote/folder/remotefile.txt  localfile.txt

Copy multiple files from local to remote using scp :
    $ scp myfile.txt myfile2.txt remoteuser@remoteserver:/remote/folder/

Copy all files from local to remote using scp :
    $ scp * remoteuser@remoteserver:/remote/folder/

Copy all files and folders recursively from local to remote using scp : 
    $ scp -r * remoteuser@remoteserver:/remote/folder/
Tests : 

scp index.html pi@192.168.1.14:/home/pi/Documents/eheMachine/main/templates

# Run / Execute Command Using SSH
    ssh user1@server1 command1
    ssh user1@server1 'command2'
pipe :
    ssh user1@server1 'command1 | command2'
multiple commands (must enclose in quotes # :
    ssh admin@box1 "command1; command2; command3"

# Flask Notlar
/app
    -app_runner.py
    /services
        -app.py 
    /templates
        -index.html
    /static
        -demo.mp4
        -but.gif
        /styles
            -style.css

app = Flask(__name__, static_folder='static') // to send .mp4 .gif  files

<source src={{ url_for('static', filename="demo.mp4") }} type="video/mp4">

<img  class="animated-gif" src="{{url_for('static', filename='but.gif')}}" />

<link rel= "stylesheet" type= "text/css" href= "{{ url_for('static',filename='styles/style.css') }}">

<a href="{{ url_for('about') }}">click</a>