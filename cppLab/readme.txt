# ---- Run cpp code from windows cmd :
!! - needed minGW64
>g++ main.cpp -o myProg
> myProg.exe


#-----Project Directory Structure-------

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