APPNAME = python-rasmil
PYTHON = python3 
VERSION=$(shell awk '/Version:/ { print $$2 }' ${APPNAME}.spec)
RPMROOT=$(shell  rpm --eval "%_topdir")

srpm:
	sudo dnf -y install python3-setuptools
	$(PYTHON) setup.py sdist
	cp dist/*.tar.gz $(RPMROOT)/SOURCES/.
	rpmbuild -bs ${APPNAME}.spec

.PHONY: srpm
