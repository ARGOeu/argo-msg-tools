Summary: ARGO tools for MSG
Name: argo-msg-tools
Version: 1.0.3
Release: 1%{?dist}
License: APL2
Group: Network/Monitoring
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildArch: noarch
Obsoletes: msg-utils

%description
ARGO tools for MSG:
- component argo-msg-cache for extracting MSG instances from BDII and
generating cache file.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install --directory ${RPM_BUILD_ROOT}%{_sbindir}
install --mode 755 ./argo-msg-cache ${RPM_BUILD_ROOT}%{_sbindir}
install --directory ${RPM_BUILD_ROOT}%{_bindir}
install --mode 755 ./msg-brokers ${RPM_BUILD_ROOT}%{_bindir}
install --directory ${RPM_BUILD_ROOT}/etc/init.d
install --mode 755 ./init.d/argo-msg-cache ${RPM_BUILD_ROOT}/etc/init.d
install --directory ${RPM_BUILD_ROOT}/etc/cron.d
install --mode 755 ./argo-msg-cache.cron ${RPM_BUILD_ROOT}/etc/cron.d/argo-msg-cache
install --directory ${RPM_BUILD_ROOT}/etc/logrotate.d
install --mode 644 ./argo-msg-cache.logrotate ${RPM_BUILD_ROOT}/etc/logrotate.d/argo-msg-cache
install --mode 644 ./argo-msg-cache.conf ${RPM_BUILD_ROOT}/etc
install --directory ${RPM_BUILD_ROOT}/var/cache/argo-msg-cache

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_sbindir}/argo-msg-cache
%{_bindir}/msg-brokers
/etc/init.d/argo-msg-cache
%attr(0644,root,root) %config(noreplace) /etc/logrotate.d/argo-msg-cache
%attr(0644,root,root) %config(noreplace) /etc/cron.d/argo-msg-cache
%attr(0644,root,root) %config(noreplace) /etc/argo-msg-cache.conf
%dir /var/cache/argo-msg-cache

%post
/sbin/chkconfig --add argo-msg-cache
:

%preun
if [ "$1" = 0 ]; then
   /sbin/service argo-msg-cache stop
   /sbin/chkconfig --del argo-msg-cache
fi
:

%changelog
* Thu Mar 24 2016 Emir Imamagic <eimamagi@srce.hr> - 1.0.3-1%{?dist}
- Changed default cache location
* Wed Mar 16 2016 Emir Imamagic <eimamagi@srce.hr> - 1.0.2-1%{?dist}
- Changed default config and output locations
* Tue Mar 8 2016 Emir Imamagic <eimamagi@srce.hr> - 1.0.0-2%{?dist}
- Added better package description.
* Tue Oct 20 2015 Emir Imamagic <eimamagi@srce.hr> - 1.0.0-1%{?dist}
- Initial version based on msg-utils
