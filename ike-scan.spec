Summary:	Discover and fingerprint IKE hosts (VPN Servers)
Name:		ike-scan
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.stearns.org/ike-scan/%{name}-%{version}.tar.gz
Vendor:		NTA Monitor Limited <ike-scan@nta-monitor.com>
URL:		http://www.nta-monitor.com/ike-scan/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ike-scan discovers IKE hosts and can also fingerprint them using the
retransmission backoff pattern.

%prep
%setup -q

%build
./configure --datadir=%{_datadir}/ike-scan/ --bindir=%{_sbindir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sbindir}
install -d $RPM_BUILD_ROOT%{_datadir}/ike-scan
%{__make} DESTDIR=$RPM_BUILD_ROOT install

#make DESTDIR=$RPM_BUILD_ROOT datadir=/usr/share/ike-scan bindir=/usr/sbin install

#install -d $RPM_BUILD_ROOT/etc
#install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
#install -d $RPM_BUILD_ROOT/usr/man/man8
#make BINDIR=$RPM_BUILD_ROOT/sbin CONFIG_FILE=$RPM_BUILD_ROOT/etc/goober.conf install
#cp -p goober.8 $RPM_BUILD_ROOT/usr/man/man8
#cp -p $RPM_SOURCE_DIR/goober.init $RPM_BUILD_ROOT/etc/rc.d/init.d/goober

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO udp-backoff-fingerprinting-paper.txt
%attr(755,root,root) %{_sbindir}/ike-scan
%{_datadir}/ike-scan/ike-backoff-patterns
