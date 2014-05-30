
SHELL = /bin/bash

SRC = $(wildcard src/*.c src/*.cc src/*.cpp)
EXE = $(basename $(SRC))

CFLAGS = -Wall -Wl,--no-as-needed
CXXFLAGS = $(CFLAGS) -std=c++0x

default: $(EXE)
	mv $(EXE) bin/

clean:
	$(RM) -fv $(EXE) core.* *~

.PHONY: clean default
