#
# spec file for package GoTools
#

Name:           GoTools
Version:        4.3.0
Release:        0
Summary:        GoTools
License:        GPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://www.sintef.no/Projectweb/Geometry-Toolkits/GoTools/
Source0:        %{name}-%{version}.tar.gz
Patch0:		0001-gotools-weights.patch
Patch1:		0002-gotools-system-ttl.patch
Patch2:		0003-gotools-system-sisl.patch
Patch3:		0004-gotools-unidirectional.patch
Patch4:		0005-gotools-remove-null.patch
Patch5:		0006-gotools-newmat-soversion.patch
BuildRequires:  boost148-devel gcc-c++ cmake28 doxygen TTL-devel sisl-devel
BuildRequires:  redhat-lsb
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
GoTools is the name of a collection of C++ libraries related to geometry.
The libraries are interdependent. Most of the functionality is
based on a spline representatin of the geometry.

%package -n libgotools-core0
Summary:        GoTools - core library
Group:          System/Libraries

%description -n libgotools-core0
GoTools is the name of a collection of C++ libraries related to geometry.
The libraries are interdependent. Most of the functionality is
based on a spline representatin of the geometry. This the the core library.

%package -n libgotools-core-devel
Summary:        Development and header files for libgotools-core
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libgotools-core0 = %{version}

%description -n libgotools-core-devel
This package contains the development and header files for libgotools-core

%package -n libgotools-trivariate0
Summary:        GoTools - trivariate library
Group:          System/Libraries

%description -n libgotools-trivariate0
GoTools is the name of a collection of C++ libraries related to geometry.
The libraries are interdependent. Most of the functionality is
based on a spline representatin of the geometry. This the the trivariate library.

%package -n libgotools-trivariate-devel
Summary:        Development and header files for libgotools-trivariate
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libgotools-trivariate0 = %{version}

%description -n libgotools-trivariate-devel
This package contains the development and header files for libgotools-trivariate

%package -n libgotools-topology0
Summary:        GoTools - topology library
Group:          System/Libraries

%description -n libgotools-topology0
GoTools is the name of a collection of C++ libraries related to geometry.
The libraries are interdependent. Most of the functionality is
based on a spline representatin of the geometry. This the the topology library.

%package -n libgotools-topology-devel
Summary:        Development and header files for libgotools-topology
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libgotools-topology0 = %{version}

%description -n libgotools-topology-devel
This package contains the development and header files for libgotools-topology

%package -n libgotools-compositemodel0
Summary:        GoTools - compositemodel library
Group:          System/Libraries

%description -n libgotools-compositemodel0
GoTools is the name of a collection of C++ libraries related to geometry.
The libraries are interdependent. Most of the functionality is
based on a spline representatin of the geometry. This the the compositemodel library.

%package -n libgotools-compositemodel-devel
Summary:        Development and header files for libgotools-compositemodel
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libgotools-compositemodel0 = %{version}

%description -n libgotools-compositemodel-devel
This package contains the development and header files for libgotools-compositemodel

%package -n libgotools-newmat0
Summary:        GoTools - newmat library
Group:          System/Libraries

%description -n libgotools-newmat0
GoTools is the name of a collection of C++ libraries related to geometry.
The libraries are interdependent. Most of the functionality is
based on a spline representatin of the geometry. This the the newmat library.

%package -n libgotools-newmat-devel
Summary:        Development and header files for libgotools-newmat
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libgotools-newmat0 = %{version}

%description -n libgotools-newmat-devel
This package contains the development and header files for libgotools-newmat

%package -n libgotools-igeslib0
Summary:        GoTools - igeslib library
Group:          System/Libraries

%description -n libgotools-igeslib0
GoTools is the name of a collection of C++ libraries related to geometry.
The libraries are interdependent. Most of the functionality is
based on a spline representatin of the geometry. This the the igeslib library.

%package -n libgotools-igeslib-devel
Summary:        Development and header files for libgotools-igeslib
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libgotools-igeslib0 = %{version}

%description -n libgotools-igeslib-devel
This package contains the development and header files for libgotools-igeslib

%package -n libgotools-implicitization0
Summary:        GoTools - implicitization library
Group:          System/Libraries

%description -n libgotools-implicitization0
GoTools is the name of a collection of C++ libraries related to geometry.
The libraries are interdependent. Most of the functionality is
based on a spline representatin of the geometry. This the the implicitization library.

%package -n libgotools-implicitization-devel
Summary:        Development and header files for libgotools-implicitization
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libgotools-implicitization0 = %{version}

%description -n libgotools-implicitization-devel
This package contains the development and header files for libgotools-implicitization

%package -n libgotools-intersections0
Summary:        GoTools - intersections library
Group:          System/Libraries

%description -n libgotools-intersections0
GoTools is the name of a collection of C++ libraries related to geometry.
The libraries are interdependent. Most of the functionality is
based on a spline representatin of the geometry. This the the intersections library.

%package -n libgotools-intersections-devel
Summary:        Development and header files for libgotools-intersections
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libgotools-intersections0 = %{version}

%description -n libgotools-intersections-devel
This package contains the development and header files for libgotools-intersections

%package -n libgotools-isogeometricmodel0
Summary:        GoTools - isogeometricmodel library
Group:          System/Libraries

%description -n libgotools-isogeometricmodel0
GoTools is the name of a collection of C++ libraries related to geometry.
The libraries are interdependent. Most of the functionality is
based on a spline representatin of the geometry. This the the isogeometricmodel library.

%package -n libgotools-isogeometricmodel-devel
Summary:        Development and header files for libgotools-isogeometricmodel
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libgotools-isogeometricmodel0 = %{version}

%description -n libgotools-isogeometricmodel-devel
This package contains the development and header files for libgotools-isogeometricmodel

%package -n libgotools-parametrization0
Summary:        GoTools - parametrization library
Group:          System/Libraries

%description -n libgotools-parametrization0
GoTools is the name of a collection of C++ libraries related to geometry.
The libraries are interdependent. Most of the functionality is
based on a spline representatin of the geometry. This the the parametrization library.

%package -n libgotools-parametrization-devel
Summary:        Development and header files for libgotools-parametrization
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libgotools-parametrization0 = %{version}

%description -n libgotools-parametrization-devel
This package contains the development and header files for libgotools-parametrization

%package -n libgotools-qualitymodule0
Summary:        GoTools - qualitymodule library
Group:          System/Libraries

%description -n libgotools-qualitymodule0
GoTools is the name of a collection of C++ libraries related to geometry.
The libraries are interdependent. Most of the functionality is
based on a spline representatin of the geometry. This the the qualitymodule library.

%package -n libgotools-qualitymodule-devel
Summary:        Development and header files for libgotools-qualitymodule
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libgotools-qualitymodule0 = %{version}

%description -n libgotools-qualitymodule-devel
This package contains the development and header files for libgotools-qualitymodule

%package -n libgotools-trivariatemodel0
Summary:        GoTools - trivariatemodel library
Group:          System/Libraries

%description -n libgotools-trivariatemodel0
GoTools is the name of a collection of C++ libraries related to geometry.
The libraries are interdependent. Most of the functionality is
based on a spline representatin of the geometry. This the the trivariatemodel library.

%package -n libgotools-trivariatemodel-devel
Summary:        Development and header files for libgotools-trivariatemodel
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libgotools-trivariatemodel0 = %{version}

%description -n libgotools-trivariatemodel-devel
This package contains the development and header files for libgotools-trivariatemodel

%package doc
Summary:        Documentation files for GoTools
Group:          Documentation
BuildArch:	noarch

%description doc
This package contains the documentation files for GoTools

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
cmake28 -DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix} -DGoTools_COMPILE_APPS=0 -DGoTools_COMPILE_MODULE_viewlib=0 -DBOOST_LIBRARYDIR=%{_libdir}/boost148 -DBOOST_INCLUDEDIR=/usr/include/boost148 -DGoTools_COMPILE_TESTS=0 -DGoTools_COMPILE_MODULE_lrsplines2D=0
make

%install
make install DESTDIR=${RPM_BUILD_ROOT}

%clean
rm -rf %{buildroot}

%post -n libgotools-core0 -p /sbin/ldconfig
%postun -n libgotools-core0 -p /sbin/ldconfig

%post -n libgotools-trivariate0 -p /sbin/ldconfig
%postun -n libgotools-trivariate0 -p /sbin/ldconfig

%post -n libgotools-topology0 -p /sbin/ldconfig
%postun -n libgotools-topology0 -p /sbin/ldconfig

%post -n libgotools-compositemodel0 -p /sbin/ldconfig
%postun -n libgotools-compositemodel0 -p /sbin/ldconfig

%post -n libgotools-newmat0 -p /sbin/ldconfig
%postun -n libgotools-newmat0 -p /sbin/ldconfig

%post -n libgotools-igeslib0 -p /sbin/ldconfig
%postun -n libgotools-igeslib0 -p /sbin/ldconfig

%post -n libgotools-implicitization0 -p /sbin/ldconfig
%postun -n libgotools-implicitization0 -p /sbin/ldconfig

%post -n libgotools-intersections0 -p /sbin/ldconfig
%postun -n libgotools-intersections0 -p /sbin/ldconfig

%post -n libgotools-isogeometricmodel0 -p /sbin/ldconfig
%postun -n libgotools-isogeometricmodel0 -p /sbin/ldconfig

%post -n libgotools-parametrization0 -p /sbin/ldconfig
%postun -n libgotools-parametrization0 -p /sbin/ldconfig

%post -n libgotools-qualitymodule0 -p /sbin/ldconfig
%postun -n libgotools-qualitymodule0 -p /sbin/ldconfig

%post -n libgotools-trivariatemodel0 -p /sbin/ldconfig
%postun -n libgotools-trivariatemodel0 -p /sbin/ldconfig

%files
%doc COPYING README

%files doc
%{_docdir}/*

%files -n libgotools-core0
%defattr(-,root,root,-)
%{_prefix}/lib/libGoToolsCore.so.*

%files -n libgotools-core-devel
%defattr(-,root,root,-)
%{_prefix}/lib/libGoToolsCore.so
%{_includedir}/GoTools/creators/*
%{_includedir}/GoTools/geometry/*
%{_includedir}/GoTools/tesselator/*
%{_includedir}/GoTools/utils/*
%{_prefix}/lib/GoToolsCore/*

%files -n libgotools-trivariate0
%defattr(-,root,root,-)
%{_prefix}/lib/libGoTrivariate.so.*

%files -n libgotools-trivariate-devel
%defattr(-,root,root,-)
%{_prefix}/lib/libGoTrivariate.so
%{_includedir}/GoTools/trivariate/*
%{_prefix}/lib/GoTrivariate/*

%files -n libgotools-topology0
%defattr(-,root,root,-)
%{_prefix}/lib/libGoTopology.so.*

%files -n libgotools-topology-devel
%defattr(-,root,root,-)
%{_prefix}/lib/libGoTopology.so
%{_includedir}/GoTools/topology/*
%{_prefix}/lib/GoTopology/*

%files -n libgotools-compositemodel0
%defattr(-,root,root,-)
%{_prefix}/lib/libGoCompositeModel.so.*

%files -n libgotools-compositemodel-devel
%defattr(-,root,root,-)
%{_prefix}/lib/libGoCompositeModel.so
%{_includedir}/GoTools/compositemodel/*
%{_prefix}/lib/GoCompositeModel/*

%files -n libgotools-igeslib0
%defattr(-,root,root,-)
%{_prefix}/lib/libGoIgeslib.so.*

%files -n libgotools-igeslib-devel
%defattr(-,root,root,-)
%{_prefix}/lib/libGoIgeslib.so
%{_includedir}/GoTools/igeslib/*
%{_prefix}/lib/GoIgeslib/*

%files -n libgotools-implicitization0
%defattr(-,root,root,-)
%{_prefix}/lib/libGoImplicitization.so.*

%files -n libgotools-implicitization-devel
%defattr(-,root,root,-)
%{_prefix}/lib/libGoImplicitization.so
%{_includedir}/GoTools/implicitization/*
%{_prefix}/lib/GoImplicitization/*

%files -n libgotools-intersections0
%defattr(-,root,root,-)
%{_prefix}/lib/libGoIntersections.so.*

%files -n libgotools-intersections-devel
%defattr(-,root,root,-)
%{_prefix}/lib/libGoIntersections.so
%{_includedir}/GoTools/intersections/*
%{_prefix}/lib/GoIntersections/*

%files -n libgotools-isogeometricmodel0
%defattr(-,root,root,-)
%{_prefix}/lib/libGoIsogeometricModel.so.*

%files -n libgotools-isogeometricmodel-devel
%defattr(-,root,root,-)
%{_prefix}/lib/libGoIsogeometricModel.so
%{_includedir}/GoTools/isogeometric_model/*
%{_prefix}/lib/GoIsogeometricModel/*

%files -n libgotools-parametrization0
%defattr(-,root,root,-)
%{_prefix}/lib/libparametrization.so.*

%files -n libgotools-parametrization-devel
%defattr(-,root,root,-)
%{_prefix}/lib/libparametrization.so
%{_includedir}/GoTools/parametrization/*
%{_prefix}/lib/parametrization/*

%files -n libgotools-qualitymodule0
%defattr(-,root,root,-)
%{_prefix}/lib/libGoQualityModule.so.*

%files -n libgotools-qualitymodule-devel
%defattr(-,root,root,-)
%{_prefix}/lib/libGoQualityModule.so
%{_includedir}/GoTools/qualitymodule/*
%{_prefix}/lib/GoQualityModule/*

%files -n libgotools-trivariatemodel0
%defattr(-,root,root,-)
%{_prefix}/lib/libGoTrivariateModel.so.*

%files -n libgotools-trivariatemodel-devel
%defattr(-,root,root,-)
%{_prefix}/lib/libGoTrivariateModel.so
%{_prefix}/lib/GoTrivariateModel/*
%{_includedir}/GoTools/trivariatemodel/*
