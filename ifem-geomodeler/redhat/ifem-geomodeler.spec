#
# spec file for package ifem-geomodeler
#

Name:           ifem-geomodeler
Version:        0.8.0
Release:        0
Summary:        IFEM - geomodeler
License:        GPL-3.0
Group:          Development/Libraries/C and C++
Url:            http://change.me
Source0:        %{name}-%{version}.tar.gz
Patch0:		0001-ifem-geomodeler-disable-docs.patch
BuildRequires:  cmake28 ifem-cmakerules python-devel libgotools-core-devel
BuildRequires:  libgotools-trivariate-devel libgotools-compositemodel-devel
BuildRequires:  libgotools-parametrization-devel sisl-devel TTL-devel
BuildRequires:  libgotools-newmat-devel libgotools-igeslib-devel
BuildRequires:  libgotools-topology-devel libgotools-implicitization-devel
BuildRequires:  libgotools-intersections-devel hdf5-devel epydoc numpy
BuildRequires:  ifem-gpm-devel devtoolset-2-gcc-c++ LRsplines-devel
BuildRequires:  vtfexpresswriter-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
IFEM - gemodeler

%prep
%setup -q
%patch0 -p1

%build
cmake28 -DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_INSTALL_DOCDIR=share/doc/%{name}-%{version} -DCMAKE_C_COMPILER=/opt/rh/devtoolset-2/root/usr/bin/gcc -DCMAKE_CXX_COMPILER=/opt/rh/devtoolset-2/root/usr/bin/g++
make

%install
make install DESTDIR=${RPM_BUILD_ROOT}

%clean
rm -rf %{buildroot}

%files
%doc COPYING README
%{_bindir}/*
%{_prefix}/lib/python2.6/*
