%define major 7
%define libname %mklibname osip2_ %{major}
%define libname_devel %mklibname -d osip2

Summary:	Implementation of SIP - rfc2543
Name:		libosip2
Version:	3.6.0
Release:	2
License:	LGPLv2+
Group:		System/Libraries
URL:		http://savannah.gnu.org/projects/osip/
Source0:	http://ftp.gnu.org/gnu/osip/%{name}-%{version}.tar.gz
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

%package -n	%{libname_devel}
Summary:	Header file required to build programs using liboSIP
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}osip2-devel < 3.6.0

%description -n	%{libname_devel}
Developments files for %{libname} (oSIP Library). Needed to build
apps such as linphone and siproxd.

%prep
%setup -q
%patch0 -p0 -b .link

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

mv %{buildroot}%{_mandir}/man1/osip.1 %{buildroot}%{_mandir}/man1/osip2.1

%files -n %{libname}
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%{_libdir}/*.so.%{major}*
%{_mandir}/man1/*

%files -n %{libname_devel}
%{_libdir}/*.so
%{_includedir}/osip2
%{_includedir}/osipparser2
%{_libdir}/pkgconfig/*.pc


%changelog
* Sun Oct 09 2011 Andrey Bondrov <abondrov@mandriva.org> 3.6.0-1mdv2012.0
+ Revision: 703880
- New version 3.6.0, new library major

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 3.3.0-3
+ Revision: 661512
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.0-2mdv2011.0
+ Revision: 602593
- rebuild

* Mon Mar 22 2010 Emmanuel Andry <eandry@mandriva.org> 3.3.0-1mdv2010.1
+ Revision: 526639
- New version 3.3.0

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 3.2.0-3mdv2010.1
+ Revision: 520895
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 3.2.0-2mdv2010.0
+ Revision: 425683
- rebuild

* Thu Feb 19 2009 Emmanuel Andry <eandry@mandriva.org> 3.2.0-1mdv2009.1
+ Revision: 342736
- New version 3.2.0
- New major 4
- diff P0 to fix str fmt

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 3.1.0-3mdv2009.0
+ Revision: 264852
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed May 28 2008 Funda Wang <fwang@mandriva.org> 3.1.0-2mdv2009.0
+ Revision: 212620
- Obsoletes old wrong package name

* Wed May 28 2008 Funda Wang <fwang@mandriva.org> 3.1.0-1mdv2009.0
+ Revision: 212528
- New version 3.1.

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 3.0.3-4mdv2008.1
+ Revision: 170952
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Thu Jan 24 2008 Colin Guthrie <cguthrie@mandriva.org> 3.0.3-3mdv2008.1
+ Revision: 157636
- Fix self obsoleting devel package

* Thu Jan 24 2008 Colin Guthrie <cguthrie@mandriva.org> 3.0.3-2mdv2008.1
+ Revision: 157486
- Bump release for buildsystem lock.
- Conform to new library policy
- Update to 3.0.3

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Tue Mar 27 2007 Oden Eriksson <oeriksson@mandriva.com> 2.2.2-3mdv2007.1
+ Revision: 148965
- fix #28156 ;)

* Mon Dec 11 2006 Oden Eriksson <oeriksson@mandriva.com> 2.2.2-2mdv2007.1
+ Revision: 94967
- rebuild
- fix deps

* Mon Dec 11 2006 Oden Eriksson <oeriksson@mandriva.com> 2.2.2-1mdv2007.1
+ Revision: 94759
- Import libosip2

* Sat Dec 03 2005 Austin Acton <austin@mandriva.org> 2.2.2-1mdk
- New release 2.2.2

* Thu Mar 31 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.2.0-3mdk
- make it lib64 friendly

* Tue Mar 22 2005 Frederic Lepied <flepied@mandrakesoft.com> 2.2.0-2mdk
- final 2.2.0

* Wed Feb 09 2005 Austin Acton <austin@mandrake.org> 2.2.0-1mdk
- 2.2.0
- fix source URL
- remove build hacks

* Fri Dec 24 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.9-2mdk
- fix man page file clash

* Fri Dec 24 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.9-1mdk
- 2.0.9
- used the libosip spec file

* Tue Sep 21 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.9.7-5mdk
- back

* Fri Aug 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.9.7-4mdk
- 0.9.7

