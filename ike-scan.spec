Summary:	Discover and fingerprint IKE hosts (VPN Servers)
Summary(pl):	Wykrywanie i uzyskiwanie odcisków hostów IKE (serwerów VPN)
Name:		ike-scan
Version:	1.6
Release:	0.1
License:	GPL
Group:		Applications/System
Vendor:		NTA Monitor Limited <ike-scan@nta-monitor.com>
Source0:	http://www.stearns.org/ike-scan/%{name}-%{version}.tar.gz
# Source0-md5:	5cdc5633a2a7484805d76b3952b8cef6
Patch0:		%{name}-nosuid.patch
URL:		http://www.nta-monitor.com/ike-scan/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		%{_sbindir}

%description
ike-scan discovers IKE hosts and can also fingerprint them using the
retransmission backoff pattern.

%description -l pl
ike-skan wykrywa hosty IKE, a ponadto mo¿e uzyskaæ ich odciski przy
u¿yciu techniki "retransmission backoff pattern".

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO udp-backoff-fingerprinting-paper.txt
%attr(755,root,root) %{_sbindir}/ike-scan
%dir %{_datadir}/ike-scan
%{_datadir}/ike-scan/ike-backoff-patterns
%{_datadir}/ike-scan/ike-vendor-ids
%{_mandir}/man?/*
