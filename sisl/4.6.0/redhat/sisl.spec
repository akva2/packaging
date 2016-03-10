#
# spec file for package opm-core
#

Name:           sisl
Version:        4.6.0
Release:        0
Summary:        SISL - The SINTEF spline library
License:        GPL-2.1
Group:          Development/Libraries/C and C++
Url:            http://www.sintef.no/Projectweb/Geometry-Toolkits/SISL/
Source0:        %{name}-%{version}.tar.gz
Patch0:		0001-sisl-add-soversion.patch
Patch1:		0002-sisl-install-to-lib64.patch
BuildRequires:  cmake28 doxygen
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       libsisl0 = %{version}

%description
"SISL", "The SINTEF spline library", is a comprehensive NURBS library
for the modelling and interrogation of curves and surfaces. It is implemented
in C and has been under cintinuous development for over two decades.

%package -n libsisl0
Summary:        SISL - The SINTEF spline library
Group:          System/Libraries

%description -n libsisl0
"SISL", "The SINTEF spline library", is a comprehensive NURBS library
for the modelling and interrogation of curves and surfaces. It is implemented
in C and has been under cintinuous development for over two decades.

%package devel
Summary:        Development and header files for SISL
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libsisl0 = %{version}

%description devel
This package contains the development and header files for SISL

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cmake28 -DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix}
make

%install
make install DESTDIR=${RPM_BUILD_ROOT}

%clean
rm -rf %{buildroot}

%post -n libsisl0 -p /sbin/ldconfig

%postun -n libsisl0 -p /sbin/ldconfig

%files
%doc COPYING README

%files -n libsisl0
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_includedir}/*
%{_prefix}/lib/SISL/*
