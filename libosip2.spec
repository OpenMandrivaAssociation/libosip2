%define major 2
%define libname %mklibname osip %major

Summary:	oSIP is an implementation of SIP - rfc2543
Name:		libosip2
# (oe) DO NOT UPGRADE TO 3.x
Version: 	2.2.2
Release: 	%mkrel 4
License: 	LGPL
Group:		System/Libraries
URL: 		http://savannah.gnu.org/projects/osip/
Source0:	http://ftp.gnu.org/gnu/osip/%{name}-%{version}.tar.bz2
BuildRequires:	libtool
BuildRequires:	autoconf2.5
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This is the oSIP library. It has been designed to provide the
Internet Community a simple way to support the Session Initiation
Protocol. SIP is described in the RFC3261 which is available at
http://www.ietf.org/rfc/rfc3261.txt.

%if "%{_lib}" != "lib"
%package -n	%{libname}
Summary:	oSIP is an implementation of SIP - rfc2543
Group:		System/Libraries

%description -n	%{libname}
This is the oSIP library. It has been designed to provide the
Internet Community a simple way to support the Session Initiation
Protocol. SIP is described in the RFC3261 which is available at
http://www.ietf.org/rfc/rfc3261.txt.
%endif

%package -n	%{libname}-devel
Summary:	Header file required to build programs using liboSIP
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	libosip-devel

%description -n	%{libname}-devel
This is the oSIP library. It has been designed to provide the
Internet Community a simple way to support the Session Initiation
Protocol. SIP is described in the RFC3261 which is available at
http://www.ietf.org/rfc/rfc3261.txt.

oSIP development libraries (for Open SIP). Needed to build
applications such as Linphone

%prep

%setup -q -n %{name}-%{version}

%build
%configure2_5x \
	--enable-pthread \
	--enable-md5
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall

mv %{buildroot}%{_mandir}/man1/osip.1 %{buildroot}%{_mandir}/man1/osip2.1

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%{_libdir}/*.so.*
%{_mandir}/man1/*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/osip2
%{_includedir}/osipparser2
%{_libdir}/pkgconfig/*.pc


