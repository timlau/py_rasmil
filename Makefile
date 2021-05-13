APPNAME = rasmil
PYTHON = python3 
CURDIR = ${shell pwd}
BUILDDIR= $(CURDIR)/build
DESTDIR= $(CURDIR)/BUILDROOT

all: build

build: 
	$(PYTHON) setup.py build

install: 
	$(PYTHON) setup.py install 


dist:
	$(PYTHON) setup.py sdist
	
clean: 
	$(PYTHON) setup.py clean
	-rm -f *.tar.gz
	-rm -rf build
	-rm -rf dist
	-rm -rf BUILDROOT

rpms: dist
	cp dist/rasmil-1.0.0.tar.gz ~/rpmbuild/SOURCES/.
	rpmbuild -ba python-rasmil.spec

.PHONY: all build install clean dist rpms