%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname rasmil

Name:           python-rasmil
Version:        1.0.1
Release:        1%{?dist}
Summary:        Misc Python Library
License:        GPLv3+
URL:            https://github.com/timlau/py_rasmil
Source0:        %{name}-%{version}.tar.gz

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

%description -n python%{python3_pkgversion}-%{srcname}
Misc Python Library

%prep
%autosetup 

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%files -n  python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/python_%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Mon May 24 2021 Tim Lauridsen <tla@rasmil.dk>
- bumped release to 1.0.1
* Thu May 13 2021 Tim Lauridsen <tla@rasmil.dk>
- initial spec 
