#
# spec file for package ifem-cmakerules
#

Name:           ifem-cmakerules
Version:        1.0.11
Release:        0
Summary:        IFEM - geomodeler
License:        GPL-3.0
Group:          Development/Libraries/C and C++
Url:            http://change.me
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  cmake28
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:	noarch

%description
Common cmake rules shared between IFEM components.

%prep
%setup -q

%build
cmake28 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCONFIG_MODE=1
make

%install
make install DESTDIR=${RPM_BUILD_ROOT}

%clean
rm -rf %{buildroot}

%files
%{_prefix}/lib/*
