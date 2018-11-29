<p align="center">
  <img width="260" height="589" src="static/logo.png" alt="dressing">
</p>
<p align="center">
  :telescope: <em>address resolution for you and your friends</em> :microscope:
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

## Special Thanks

This project would not have been possible without the help of my good friend, Jinny. Check out her [GitHub page](https://github.com/jinnyyan)!