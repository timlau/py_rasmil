%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname rasmil

Name:           python-rasmil
Version:        1.0.2
Release:        2%{?dist}
Summary:        Misc Python Library
License:        GPLv3+
URL:            https://github.com/timlau/py_rasmil
Source0:        https://github.com/timlau/py_rasmil/archive/refs/tags/RASMIL-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_enable_dependency_generator}

%description
Misc Python Library


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

Requires:       xfconf
Requires:       python3-dasbus
Requires:       python3-gobject

%description -n python%{python3_pkgversion}-%{srcname}
Misc Python Library

%prep
%autosetup -n py_rasmil-RASMIL-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%files -n  python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Wed Jun 2 2021 Tim Lauridsen <tla@rasmil.dk>
- bumped release to 1.0.2
- added widgets module with custom gtk3 widgets
* Mon May 24 2021 Tim Lauridsen <tla@rasmil.dk>
- bumped release to 1.0.1
* Thu May 13 2021 Tim Lauridsen <tla@rasmil.dk>
- initial spec 
