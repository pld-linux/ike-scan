Summary:	Discover and fingerprint IKE hosts (VPN Servers)
Summary(pl):	Wykrywanie i uzyskiwanie odcisk�w host�w IKE (serwer�w VPN)
Name:		ike-scan
Version:	1.2
Release:	0.1
License:	GPL
Group:		Applications/System
Vendor:		NTA Monitor Limited <ike-scan@nta-monitor.com>
Source0:	http://www.stearns.org/ike-scan/%{name}-%{version}.tar.gz
# Source0-md5:	25777051bb09306cb0b86e0cf1c48caa
URL:		http://www.nta-monitor.com/ike-scan/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	%{_prefix}/share/ike-skan
%define		_bindir		%{_sbindir}

%description
ike-scan discovers IKE hosts and can also fingerprint them using the
retransmission backoff pattern.

%description -l pl
ike-skan wykrywa hosty IKE, a ponadto mo�e uzyska� ich odciski przy
u�yciu techniki "retransmission backoff pattern".

%prep
%setup -q

%build
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_datadir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#make DESTDIR=$RPM_BUILD_ROOT datadir=/usr/share/ike-scan bindir=/usr/sbin install
#make BINDIR=$RPM_BUILD_ROOT/sbin CONFIG_FILE=$RPM_BUILD_ROOT/etc/goober.conf install
#cp -p goober.8 $RPM_BUILD_ROOT/usr/man/man8
#cp -p $RPM_SOURCE_DIR/goober.init $RPM_BUILD_ROOT/etc/rc.d/init.d/goober

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO udp-backoff-fingerprinting-paper.txt
%attr(755,root,root) %{_sbindir}/ike-scan
%dir %{_datadir}
%{_datadir}/ike-backoff-patterns
