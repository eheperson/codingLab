



<dl>
    <dt>How can I make CMake behave this way all the time, without adding the -G "MinGW Makefiles" flag? </dt>
    <dd>You can't, not in any version of CMake released to date. CMake chooses a generator before it starts evaluating any CMakeLists.txt files.By default, it chooses a generator based on runtime platform and available toolsets, and command-line options are the only way presently available to influence or override CMake's choice of generator.</dd>
</dl>