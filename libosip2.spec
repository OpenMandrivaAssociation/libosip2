%define major 13
%define libname %mklibname osip2_ %{major}
%define libparser %mklibname osipparser2_ %{major}
%define devname %mklibname -d osip2

Summary:	Implementation of SIP - rfc2543
Name:		libosip2
Version:	5.1.2
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://savannah.gnu.org/projects/osip/
Source0:	http://ftp.gnu.org/gnu/osip/%{name}-%{version}.tar.gz

%description
This is the oSIP library. It has been designed to provide the
Internet Community a simple way to support the Session Initiation
Protocol. SIP is described in the RFC3261 which is available at
http://www.ietf.org/rfc/rfc3261.txt.

%package -n	%{libname}
Summary:	Implementation of SIP - rfc2543
Group:		System/Libraries

%description -n	%{libname}
This is the oSIP library. It has been designed to provide the
Internet Community a simple way to support the Session Initiation
Protocol. SIP is described in the RFC3261 which is available at
http://www.ietf.org/rfc/rfc3261.txt.

%package -n	%{libparser}
Summary:	Implementation of SIP - rfc2543
Group:		System/Libraries
Conflicts:	%{_lib}osip2_10 < 4.0.0-3

%description -n	%{libparser}
This package contains a shared library for %{name}.

%package -n	%{devname}
Summary:	Header file required to build programs using liboSIP
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libparser} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
Developments files for %{libname} (oSIP Library). Needed to build
apps such as linphone and siproxd.

%prep
%autosetup -p1

%build
%configure \
	--disable-static

%make_build LIBS='-lrt -pthread'

%install
%make_install

mv %{buildroot}%{_mandir}/man1/osip.1 %{buildroot}%{_mandir}/man1/osip2.1

%files -n %{libname}
%{_libdir}/libosip2.so.%{major}*

%files -n %{libparser}
%{_libdir}/libosipparser2.so.%{major}*

%files -n %{devname}
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%{_includedir}/osip2
%{_includedir}/osipparser2
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man1/*
