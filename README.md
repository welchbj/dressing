<p align="center">
  <img width="260" height="589" src="static/logo.png" alt="dressing">
</p>
<p align="center">
  :leaves: <em>address resolution for you and your friends</em> :tomato:
</p>
<p align="center">
  <a href="https://pypi.org/project/dressing/">
    <img src="https://img.shields.io/pypi/v/dressing.svg?style=flat-square&label=pypi" alt="pypi">
  </a>
  <a href="https://pypi.org/project/dressing/">
    <img src="https://img.shields.io/pypi/pyversions/dressing.svg?style=flat-square" alt="pyversions">
  </a>
  <a href="https://travis-ci.org/welchbj/dressing">
    <img src="https://img.shields.io/travis/welchbj/dressing/master.svg?style=flat-square&label=linux%20build" alt="Linux build on Travis CI">
  </a>
  <a href="https://ci.appveyor.com/project/welchbj/dressing">
    <img src="https://img.shields.io/appveyor/ci/welchbj/dressing/master.svg?style=flat-square&label=windows%20build" alt="Windows build on Appveyor">
  </a>
</p>

---

## Synopsis

`dressing` is a simple cross-platform utility for resolving the addresses of functions from shared libraries, using `GetProcAddress` on Windows and `dlsym` on POSIX systems. Inspired by the `arwin` program originally authored by [Steve Hanna](http://vividmachines.com/about/).

## License

This code is released under the [MIT License](https://opensource.org/licenses/MIT).

## Installation

Download the latest packaged release from PyPI:
```sh
pip install dressing
```

Or get the latest version from version control:
```sh
pip install https://github.com/welchbj/dressing/archive/master.tar.gz
```

## Basic usage

The `dressing` command-line tool accepts two arguments: the name of the library in which you would like to search and the name of the function for which you would like to find the address.

A complete shared library name does not need to be provided, as some searching will be performed based on OS semantics. Here's a quick example on a Windows box:
```sh
$ dressing kernel32 HeapCreate
0x7ffa41b1d900
```

Note that the previous example is reporting the absolute address in memory of `HeapCreate`. If you wanted the offset to `HeapCreate` (using the base address of the loaded `kernel32.dll` module as our point of reference), you'd use:
```sh
$ dressing -o kernel32 HeapCreate
0x1d900
```

To see more details about the location of the shared library identified by `dressing`, use the `-v` option. The fully specified path is provided for Windows, as shown in the below example.
```sh
$ dressing -v kernel32.dll LoadLibraryA
Using library at C:\windows\system32\kernel32.dll
0x7ffa41b1e090
```

On POSIX systems, the shared library name will be fully expanded. This is demonstrated in the below example:
```sh
$ dressing -v c printf
Using library at libc.so.6
0x7f0c6fe3ced0
```

## Disclaimer

It should be noted that due to the shared library search semantics of `dlsym` (used under the hood for POSIX-based function lookups), the search space for a function name will include all loaded modules. This results in the following undesirable behavior, where we still receive addresses for functions that are not exported directly within the library we specify:
```sh
$ dressing dl printf
0x7f4d00c59e80
```

As such, make sure you know the "owning" module of the function which you're resolving.

## Detailed options

Here's what you should see when running `dressing --help`:
```
usage: dressing LIBRARY FUNCTION

         8I
         8I
         8I                                           gg
         8I                                           ""
   ,gggg,8I   ,gggggg,   ,ggg,     ,g,       ,g,      gg    ,ggg,,ggg,     ,gggg,gg
  dP"  "Y8I   dP""""8I  i8" "8i   ,8'8,     ,8'8,     88   ,8" "8P" "8,   dP"  "Y8I
 i8'    ,8I  ,8'    8I  I8, ,8I  ,8'  Yb   ,8'  Yb    88   I8   8I   8I  i8'    ,8I
 d8,   ,d8b,,dP     Y8, `YbadP' ,8'_   8) ,8'_   8) _,88,_,dP   8I   Yb,,d8,   ,d8I
 "Y8888P"`Y88P      `Y8888P"Y888P' "YY8P8PP' "YY8P8P8P""Y88P'   8I   `Y8P"Y8888P"888
                                                                               ,d8I'
                                                                             ,dP'8I
                                                                            ,8"  8I
                                                                            I8   8I
                                                                            `8, ,8I
                                                                             `Y8P"
                    address resolution for you and your friends

positional arguments:
  LIBRARY        the library in which to search for the specified function
  FUNCTION       the function whose address you want to resolve

optional arguments:
  -h, --help     show this help message and exit
  -o, --offset   print the offset of the function within its loaded module
  -v, --verbose  increase detail of output
  --version      program version
```


## Special Thanks

This project would not have been possible without the help of my good friend, Jinny. Check out her [GitHub page](https://github.com/jinnyyan)!