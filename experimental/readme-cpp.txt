# ---- Run cpp code from windows cmd :
!! - needed minGW64
>g++ main.cpp -o myProg
> myProg.exe
#-----------------------------------------------------------------------------------
> How can I make CMake behave this way all the time, without adding the -G "MinGW Makefiles" flag?
	You can't, not in any version of CMake released to date. CMake chooses a generator before it 
	starts evaluating any CMakeLists.txt files.By default, it chooses a generator based on runtime 
	platform and available toolsets, and command-line options are the only way presently available 
	to influence or override CMake's choice of generator.

> Using cmake in windows (MinGW)
	1 - 'mingw-w64' must be installed and addedto path.
	2 - 'cmake' must be installed and added to path.
	3 - 'CMAKE_C_COMPILER' and 'CMAKE_CXX_COMPILER' must be specified in 'CMakeLists.txt'.
	4 - '-G "MinGW Makefiles"' argument must be usedwith 'cmake' command.
	5 - Command order to compile project correctly : 
		i   - cmake -G "MinGW Makefiles" -S <source_path> -B <build_path>
		ii  - cd build
		iii - mingw32-make (if mingw32/bin not in path, that step will not work)

#-----------------------------------------------------------------------------------

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