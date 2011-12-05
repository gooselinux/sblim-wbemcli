Name:           sblim-wbemcli
Version:        1.6.1
Release:        1%{?dist}
Summary:        SBLIM WBEM Command Line Interface

Group:          Applications/System
License:        EPL
URL:            http://sblim.wiki.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
Patch0:         sblim-wbemcli-1.5.1-gcc43.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  curl-devel >= 7.9.3
BuildRequires:  binutils-devel >= 2.17.50.0.3-4
Requires:       curl >= 7.9.3
Requires:       tog-pegasus

%description
WBEM Command Line Interface is a standalone, command line WBEM client. It is
specially suited for basic systems management tasks as it can be used in
scripts.

%prep
%setup -q
%patch0 -p1 -b .gcc43

%build
%configure CACERT=/etc/Pegasus/client.pem
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README
%{_bindir}/wbem*
%{_mandir}/man1/*
%{_datadir}/%{name}

%changelog
* Wed Jun 30 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.6.1-1
- Update to sblim-wbemcli-1.6.1

* Tue Mar  2 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.6.0-6
- Ship README

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.6.0-5.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Feb 28 2009 Caolán McNamara - 1.6.0-4
- constify rets of strchr(const char *);

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov  4 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.6.0-2
- Fix License
- Spec file cleanup, rpmlint check

* Fri Oct 24 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.6.0-1
- Update to 1.6.0
  Resolves: #468328

* Fri Jun 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.5.1-7
- fix gcc43 compile failure

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5.1-6
- Autorebuild for GCC 4.3

* Mon Nov 06 2006 Jindrich Novy <jnovy@redhat.com> - 1.5.1-5
- rebuild against new curl

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> - 1.5.1-4
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Nov 21 2005 Viktor Mihajlovski <mihajlov@de.ibm.com> - 1.5.1-1
- Upgrade to version 1.5.1 (SSL V3 enforced, default CACERT).
- Created Fedora/RH specific spec file.

* Thu Oct 28 2005 Viktor Mihajlovski <mihajlov@de.ibm.com> - 1.5.0-1
- Minor enhancements for Fedora compatibility, still not daring to
  nuke the build root though

* Thu Jul 28 2005 Viktor Mihajlovski <mihajlov@de.ibm.com> - 1.5.0-0
- Updates for rpmlint complaints
