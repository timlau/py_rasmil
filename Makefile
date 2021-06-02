APPNAME = python-rasmil
PYTHON = python3 
CURDIR = ${shell pwd}
BUILDDIR= $(CURDIR)/build
DESTDIR= $(CURDIR)/BUILDROOT
VERSION=$(shell awk '/Version:/ { print $$2 }' ${APPNAME}.spec)


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
	-rm -rf src/*egg-info
	-rm -rf src/__pycache__


rpms: dist
	cp dist/rasmil-$(VERSION).tar.gz ~/rpmbuild/SOURCES/RASMIL-$(VERSION).tar.gz
	rpmbuild -ba python-rasmil.spec

copr: rpms
	copr-cli build rasmil ~/rpmbuild/SRPMS/$(APPNAME)-$(VERSION)*.src.rpm

.PHONY: all build install clean dist rpms copr