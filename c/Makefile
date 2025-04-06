# Makefile for C++ project

# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++17 -Wall -O2

# Source files and executable
SRC = complex.cpp  # لیست فایل‌های سورس
EXE = complex

# Input files and arguments for execution
# INPUT1 = /Users/admin/Workspace/phd/coauth-DBLP/coauth-DBLP-nverts.txt
# INPUT2 = /Users/admin/Workspace/phd/coauth-DBLP/coauth-DBLP-simplices.txt
INPUT1 = /usr/local/complex/coauth-DBLP/coauth-DBLP-nverts.txt
INPUT2 = /usr/local/complex/coauth-DBLP/coauth-DBLP-simplices.txt
N = 2000
SAMPLES = 10000

# Targets
all: $(EXE)

$(EXE): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(EXE)

run: $(EXE)
	./$(EXE) $(INPUT1) $(INPUT2) $(N) $(SAMPLES)

clean:
	rm -f $(EXE)

# Phony targets
.PHONY: all run clean
