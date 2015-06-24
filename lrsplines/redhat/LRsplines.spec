#
# spec file for package LRsplines
#

Name:           LRsplines
Version:        1.0.0
Release:        0
Summary:        LRsplines - locally refined B-splines
License:        GPL-3.0
Group:          Development/Libraries/C and C++
Url:            http://change.me
Source0:        %{name}-%{version}.tar.gz
Patch0:		0001-lrsplines-disable-forced-module-mode.patch
Patch1:		0002-lrsplines-hack-boost.patch
BuildRequires:  cmake28 doxygen libgotools-core-devel
BuildRequires:  libgotools-trivariate-devel devtoolset-2-binutils devtoolset-2-gcc-c++ ifem-cmakerules boost148-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
LRsplines - locally refined B-splines

%package doc
Summary:        Documentation files for LRsplines
Group:          Documentation
BuildArch:	noarch

%description doc
This package contains the documentation files for LRsplines

%package -n liblrsplines0
Summary:	The LRsplines library
Group:		System/Libraries

%description -n liblrsplines0
The LRsplines library contains the reusable bits of the LRsplines module.

%package devel
Summary:	The LRsplines development files.
Group:          Development/Libraries/C and C++

%description devel
The LRsplines development files.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cmake28 -DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_CXX_COMPILER=/opt/rh/devtoolset-2/root/usr/bin/g++ -DCMAKE_C_COMPILER=/opt/rh/devtoolset-2/root/usr/bin/gcc -DBOOST_LIBRARYDIR=%{_libdir}/boost148 -DBOOST_INCLUDEDIR=/usr/include/boost148
make

%install
make install DESTDIR=${RPM_BUILD_ROOT}

%clean
rm -rf %{buildroot}

%post -n liblrsplines0 -p /sbin/ldconfig

%postun -n liblrsplines0 -p /sbin/ldconfig

%files

%files doc
%{_docdir}/*

%files devel
%{_includedir}/*
%{_prefix}/lib/LRSpline/*
%{_libdir}/*.so

%files -n liblrsplines0
%{_libdir}/*.so.*
