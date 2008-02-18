%define major 2
%define libname %mklibname osip2_ %major
%define libname_devel %mklibname -d osip2

Summary:	Implementation of SIP - rfc2543
Name:		libosip2
Version: 	3.0.3
Release: 	%mkrel 4
License: 	LGPL
Group:		System/Libraries
URL: 		http://savannah.gnu.org/projects/osip/
Source0:	http://ftp.gnu.org/gnu/osip/%{name}-%{version}.tar.gz
BuildRequires:	libtool
BuildRequires:	autoconf2.5
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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

%package -n	%{libname_devel}
Summary:	Header file required to build programs using liboSIP
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{libname_devel}
Developments files for %{libname} (oSIP Library). Needed to build
apps such as linphone and siproxd.

%prep

%setup -q

%build
%configure
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
%{_libdir}/*.so.%{major}*
%{_mandir}/man1/*

%files -n %{libname_devel}
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%dir %{_includedir}/osip2
%{_includedir}/osip2
%dir %{_includedir}/osipparser2
%{_includedir}/osipparser2
%{_libdir}/pkgconfig/*.pc
