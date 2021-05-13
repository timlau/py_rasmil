%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname rasmil

Name:           python-rasmil
Version:        1.0.0
Release:        1%{?dist}
Summary:        Misc Python Library
License:        GPLv3+
URL:            https://worldoftim.rasmil.dk
Source0:        %{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_enable_dependency_generator}

%description
Misc Python Library


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%if %{undefined python_enable_dependency_generator} && %{undefined python_disable_dependency_generator}
# Put manual requires here:
# Requires:       python%{python3_pkgversion}-foo
%endif

%description -n python%{python3_pkgversion}-%{srcname}
Misc Python Library

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%files -n  python%{python3_pkgversion}-%{srcname}
#%license LICENSE
#%doc Readme.md
# For noarch packages: sitelib
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Thu May 13 2021 Tim Lauridsen <tla@rasmil.dk>
- initial spec 
