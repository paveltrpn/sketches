

echo WIN API WINDOW GCC

@echo OFF

set GCCDIR="E:\TDM-GCC-64\bin"
set LIBDIR="E:\TDM-GCC-64\Lib"
set INCDIR="E:\TDM-GCC-64\Include"
set WORKDIR=%~dp0

set SOURCES=main.cpp
set OFILES=main.o
set OUTPUT=main.exe
set LIBS=
set CFLAGS=-O1 -std=c++11 -c
set LFLAGS=-s -lgdi32

@echo ON

%GCCDIR%\g++ --version
%GCCDIR%\g++ %CFLAGS% %SOURCES%
%GCCDIR%\g++ %OFILES% %LIBS% %LFLAGS% -o %OUTPUT%
