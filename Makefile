APPNAME = rasmil
PYTHON = python3 
CURDIR = ${shell pwd}
BUILDDIR= $(CURDIR)/build
DESTDIR= $(CURDIR)/BUILDROOT

all: build

build: 
	$(PYTHON) setup.py build

install: 
	$(PYTHON) setup.py install --skip-build --root $(DESTDIR) 


dist:
	$(PYTHON) setup.py sdist
	
clean: 
	$(PYTHON) setup.py clean
	-rm -f *.tar.gz
	-rm -rf build
	-rm -rf dist
	-rm -rf BUILDROOT



.PHONY: all build install clean