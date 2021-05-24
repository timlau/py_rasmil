APPNAME = python-rasmil
PYTHON = python3 
VERSION=$(shell awk '/Version:/ { print $$2 }' ${APPNAME}.spec)

srpm:
	dnf -y install python3-setuptools
	$(PYTHON) setup.py sdist
	cp dist/*.tar.gz .
	rpmbuild -bs ${APPNAME}.spec

.PHONY: srpm	
