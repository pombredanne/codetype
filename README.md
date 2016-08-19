# cypher

[![Build Status](https://travis-ci.org/jdkato/cypher.svg?branch=master)](https://travis-ci.org/jdkato/cypher) [![Coverage Status](https://coveralls.io/repos/github/jdkato/cypher/badge.svg?branch=master)](https://coveralls.io/github/jdkato/cypher?branch=master) [![Code Health](https://landscape.io/github/jdkato/cypher/master/landscape.svg?style=flat)](https://landscape.io/github/jdkato/cypher/master) [![Hex.pm](https://img.shields.io/hexpm/l/plug.svg?maxAge=2592000)](https://github.com/jdkato/cypher/blob/master/LICENSE.txt) ![Python Support](https://img.shields.io/badge/python-2.7,3.4,3.5-blue.svg)

[`cypher`](https://en.wikipedia.org/wiki/Cypher_(Marvel_Comics)) is a Python library and CLI tool for identifying the language of source code snippets and files. It's fast (~0.013 seconds per file across 16507 files), simple and has no third-party dependencies.

[You can test it out here](http://jdkato.github.io/cypher/).

## Installation

## Usage

###### Python

```python
>>> from cypher import identify
>>> identify('fibs = 0 : 1 : zipWith (+) fibs (tail fibs)')
'Haskell'
>>> identify('from math import fabs')
'Python'
>>>
```

###### Command line

```
$ cypher path/to/file
```

## Strategy

## Support

|   Language    |       Status          |      Unit tests   | Base Project (% identified)   |
|:-----------:  |:------------------:   |:---------------:  |:---------------------------:  |
|     ASP       |         :x:           |        0          |                               |
| AppleScript   |         :x:           |        0          |                               |
|      C#       | :white_check_mark:    |        10         | [Nancy](https://github.com/NancyFx/Nancy.git) (0.995)                             |
|     C++       | :white_check_mark:    |        12         | [Electron](https://github.com/apple/swift) (0.974)          |
|      C        | :white_check_mark:    |        12         | [Git](https://github.com/git/git) (0.969)            |
|     CSS       |         :x:           |        0          |                               |
|   Clojure     |         :x:           |        0          |                               |
|      D        |         :x:           |        0          |                               |
|    Erlang     |         :x:           |        0          |                               |
|      Go       | :white_check_mark:    |        11         | [Lantern](https://github.com/getlantern/lantern.git) (1.00)                              |
|     HTML      |         :x:           |        0          |                               |
|   Haskell     | :white_check_mark:    |        10         | [Cabal](https://github.com/haskell/cabal) (0.995)          |
|     Java      | :white_check_mark:    |        11         | [Spring](https://github.com/spring-projects/spring-framework.git) (1.00)                              |
|  JavaScript   |         :x:           |        0          |                               |
|    LaTeX      |         :x:           |        0          |                               |
|     Lisp      |         :x:           |        0          |                               |
|     Lua       | :white_check_mark:    |        10         | [Kong](https://github.com/Mashape/kong) (1.00)                              |
|    Matlab     |         :x:           |        0          |                               |
|    OCaml      |         :x:           |        0          |                               |
| Objective-C   | :white_check_mark:    |        10         | [Adium](https://github.com/adium/adium.git) (0.993)                             |
|     Perl      | :white_check_mark:    |        10         | [Mojolicious](https://github.com/kraih/mojo) (1.00)                          |
|     PHP       | :white_check_mark:    |        10         | [WordPress](https://github.com/WordPress/WordPress) (1.00) |
|    Python     | :white_check_mark:    |        12         | [Django](https://github.com/django/django) (0.985)            |
|      R        | :white_check_mark:    |        11         | [Shiny](https://github.com/rstudio/shiny) (0.975)             |
|     Ruby      | :white_check_mark:    |        11         | [Ruby on Rails](https://github.com/rails/rails) (0.976)          |
|     Rust      | :white_check_mark:    |        10         | [Cargo](https://github.com/rust-lang/cargo.git) (1.00)    |
|    Scala      | :white_check_mark:    |        10         | [squbs](https://github.com/paypal/squbs.git) (0.997)                       |
|    Swift      |         :x:           |        0          |                               |
|     XML       |         :x:           |        0          |                               |
