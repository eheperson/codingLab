# ---- Run cpp code from windows cmd :
!! - needed minGW64
>g++ main.cpp -o myProg
> myProg.exe


#-----Project Directory Structure 1 -------

Project_name
  |
  |---- CMakeLists.txt
  |
  |---- include
  |       |
  |       |---- Project_name
  |                 |
  |                 |---- public_header(s).h
  |
  ---- src
  |     |
  |     |---- private_header(s).h
  |     |
  |     |---- code(s).cpp
  |
  |
  |---- libs
  |       |
  |       |---- A
  |       |
  |       |---- B
  |
  |
  |---- tests


#-----Project Directory Structure 2 -------

Project_name
  |
  |---- CMakeLists.txt
  |
  |---- build
  |       |
  |       |---- xxxxx
  |                 |
  |                 |---- xxxx
  |
  ---- src
  |     |
  |     |---- xxxx
  |     |
  |     |---- xxxx
  |
  |
  |---- xxxx
  |       |
  |       |---- xxxx
  |       |
  |       |---- xxxx
  |
  |
  |---- xxxxx