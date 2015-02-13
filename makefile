
SHELL = /bin/bash

PSEUDO = $(wildcard src/*.pseudo*)

SRC = $(wildcard src/*.c src/*.cc src/*.cpp)
EXE = $(basename $(SRC))

CFLAGS = -Wall -Wl,--no-as-needed
CXXFLAGS = $(CFLAGS) -std=c++0x

default: $(EXE)
	mkdir -p bin
	mv $(EXE) bin/

clean:
	$(RM) -fv $(EXE) core.* *~

tex: $(PSEUDO)
	./gentex.sh

.PHONY: clean default tex
