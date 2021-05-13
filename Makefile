APPNAME = rasmil
PYTHON = python3 
CURDIR = ${shell pwd}
BUILDDIR= $(CURDIR)/build
DESTDIR= $(CURDIR)/BUILDROOT

build: 
	$(PYTHON) setup.py build

install: 
	$(PYTHON) setup.py install --skip-build --root $(DESTDIR) 
	
clean: 
	$(PYTHON) setup.py clean
	-rm -f *.tar.gz
	-rm -rf build
	-rm -rf dist
	-rm -rf BUILDROOT
	