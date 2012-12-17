%define major	7
%define libname %mklibname osip2_ %{major}
%define devname %mklibname -d osip2

Summary:	Implementation of SIP - rfc2543
Name:		libosip2
Version:	4.0.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://savannah.gnu.org/projects/osip/
Source0:	http://ftp.gnu.org/gnu/osip/%{name}-%{version}.tar.gz
Source1:	http://ftp.gnu.org/gnu/osip/%{name}-%{version}.tar.gz.sig
Patch0:		libosip2-3.5.0-linkage.patch

%description
This is the oSIP library. It has been designed to provide the
Internet Community a simple way to support the Session Initiation
Protocol. SIP is described in the RFC3261 which is available at
http://www.ietf.org/rfc/rfc3261.txt.

%package -n	%{libname}
Summary:	Implementation of SIP - rfc2543
Group:		System/Libraries
Obsoletes:	%{mklibname osip2} < 3.6.0
Obsoletes:	%{_lib}osip2_4 < 3.6.0

%description -n	%{libname}
This is the oSIP library. It has been designed to provide the
Internet Community a simple way to support the Session Initiation
Protocol. SIP is described in the RFC3261 which is available at
http://www.ietf.org/rfc/rfc3261.txt.

%package -n	%{devname}
Summary:	Header file required to build programs using liboSIP
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}osip2-devel < 3.6.0

%description -n	%{devname}
Developments files for %{libname} (oSIP Library). Needed to build
apps such as linphone and siproxd.

%prep
%setup -q
%patch0 -p0 -b .link

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

mv %{buildroot}%{_mandir}/man1/osip.1 %{buildroot}%{_mandir}/man1/osip2.1

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%{_includedir}/osip2
%{_includedir}/osipparser2
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man1/*

