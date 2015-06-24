#
# spec file for package ifem-geomodeler
#

Name:           ifem-gpm
Version:        0.3.4
Release:        0
Summary:        IFEM - geometry pre-processing module
License:        GPL-3.0
Group:          Development/Libraries/C and C++
Url:            http://change.me
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  cmake28 doxygen libgotools-core-devel
BuildRequires:  libgotools-trivariate-devel devtoolset-2-gcc-c++ devtoolset-2-binutils
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
IFEM - geometry pre-processing module

%package doc
Summary:        Documentation files for ifem-gpm
Group:          Documentation
BuildArch:	noarch

%description doc
This package contains the documentation files for ifem-gpm

%package -n libifem-gpm1
Summary:	The IFEM GPM library
Group:		System/Libraries

%description -n libifem-gpm1
The IFEM GPM library contains the reusable bits of the GPM module.

%package bin
Summary:	The IFEM GPM applications
Group:		Scientific

%description bin
The IFEM GPM applications.

%package devel
Summary:	The IFEM GPM development files.
Group:          Development/Libraries/C and C++

%description devel
The IFEM GPM development files.

%prep
%setup -q

%build
cmake28 -DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_CXX_COMPILER=/opt/rh/devtoolset-2/root/usr/bin/g++ -DCMAKE_C_COMPILER=/opt/rh/devtoolset-2/root/usr/bin/gcc
make

%install
make install DESTDIR=${RPM_BUILD_ROOT}

%clean
rm -rf %{buildroot}

%post -n libifem-gpm1 -p /sbin/ldconfig

%postun -n libifem-gpm1 -p /sbin/ldconfig

%files

%files doc
%{_docdir}/*

%files bin
%{_bindir}/*

%files devel
%{_includedir}/*
%{_prefix}/lib/GPM/*
%{_libdir}/*.so

%files -n libifem-gpm1
%{_libdir}/*.so.*
