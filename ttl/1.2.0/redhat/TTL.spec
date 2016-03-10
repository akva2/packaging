#
# spec file for package opm-core
#

Name:           TTL
Version:        1.2.0
Release:        0
Summary:        TTL - The SINTEF template triangulation library
License:        GPL-2.1
Group:          Development/Libraries/C and C++
Url:            http://www.sintef.no/Projectweb/Geometry-Toolkits/GoTools/
Source0:        %{name}-%{version}.tar.gz
Patch0:		0001-ttl-add-soversion.patch
Patch1:		0002-ttl-install-to-lib64.patch
BuildRequires:  cmake28 doxygen boost-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       libttl0 = %{version}

%description
TTL is a library for operations related to triangulations.
TTL is not dependent on a specific data structure, but can be
adapted to any type of triangulation defined by the user.

%package -n libttl0
Summary:        TTL - The triangulation library
Group:          System/Libraries

%description -n libttl0
TTL is a library for operations related to triangulations.
TTL is not dependent on a specific data structure, but can be
adapted to any type of triangulation defined by the user.

%package devel
Summary:        Development and header files for TTL
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libttl0 = %{version}

%description devel
This package contains the development and header files for TTL

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

%post -n libttl0 -p /sbin/ldconfig

%postun -n libttl0 -p /sbin/ldconfig

%files
%doc COPYING README

%files -n libttl0
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_includedir}/*
%{_prefix}/lib/TTL/*
