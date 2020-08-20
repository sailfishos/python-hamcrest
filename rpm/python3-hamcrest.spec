%define upstream_version 2.0.2
Name:           python3-hamcrest
Version:        %{upstream_version}
Release:        0
Summary:        PyHamcrest is a framework for writing matcher objects
License:        BSD
URL:            https://github.com/sailfishos/python-hamcrest
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream
# Remove bundled egg-info
rm -rf PyHamcrest.egg-info

%build
%py3_build

%install
%py3_install

%files
%license LICENSE.txt
%{python3_sitelib}/hamcrest
%{python3_sitelib}/PyHamcrest-%{upstream_version}-py%{python3_version}.egg-info/
