%define version 1.0
Name:				ike-scan
Summary:			Discover and fingerprint IKE hosts (VPN Servers)
Version:			%{version}
Release:			0
Copyright:			GPL
Packager:			William Stearns <wstearns@pobox.com>
Group:				Applications/System
Source:				http://www.nta-monitor.com/ike-scan/ike-scan-%{version}.tar.gz
#Source1:			goober.init
#Patch0:				goober-2.1-make.patch
#Patch1:				goober-2.1-config.patch
#Prereq:				/sbin/chkconfig logrotate
Vendor:				NTA Monitor Limited <ike-scan@nta-monitor.com>
URL:				http://www.nta-monitor.com/ike-scan/
BuildRoot:			/tmp/ike-scan-broot


%description
ike-scan discovers IKE hosts and can also fingerprint them using the                                          
retransmission backoff pattern.


%changelog
* Mon Jan 27 2003 William Stearns <wstearns@pobox.com>
- First release from 1.0 source.  NTA has a "registration required and
we'll give you download URL longer than your dna sequence" download
process, so you're welcome to download it from
http://www.stearns.org/ike-scan/ .  Not only am I allowed to do this,
I'm required to by the GPL.


%prep
%setup
#%setup -n goober
#%setup -q -a 1
#%patch0 -p1 -b .make
#%patch1 -p1 -b .config


%build
./configure --datadir=/usr/share/ike-scan/ --bindir=/usr/sbin
make


%install
if [ "$RPM_BUILD_ROOT" = "/tmp/ike-scan-broot" ]; then
	rm -rf $RPM_BUILD_ROOT

	install -d $RPM_BUILD_ROOT/usr/sbin
	install -d $RPM_BUILD_ROOT/usr/share/ike-scan
	make DESTDIR=$RPM_BUILD_ROOT install

	#make DESTDIR=$RPM_BUILD_ROOT datadir=/usr/share/ike-scan bindir=/usr/sbin install

	#install -d $RPM_BUILD_ROOT/etc
	#install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
	#install -d $RPM_BUILD_ROOT/usr/man/man8
	#make BINDIR=$RPM_BUILD_ROOT/sbin CONFIG_FILE=$RPM_BUILD_ROOT/etc/goober.conf install
	#cp -p goober.8 $RPM_BUILD_ROOT/usr/man/man8
	#cp -p $RPM_SOURCE_DIR/goober.init $RPM_BUILD_ROOT/etc/rc.d/init.d/goober
else
	echo Invalid Build root \'"$RPM_BUILD_ROOT"\'
	exit 1
fi
						
%clean
if [ "$RPM_BUILD_ROOT" = "/tmp/ike-scan-broot" ]; then
	rm -rf $RPM_BUILD_ROOT
else
	echo Invalid Build root \'"$RPM_BUILD_ROOT"\'
	exit 1
fi


%files
%defattr(-,root,root)
%attr(755,root,root)			/usr/sbin/ike-scan
%attr(644,root,root)			/usr/share/ike-scan/ike-backoff-patterns
				%doc	AUTHORS COPYING ChangeLog NEWS README TODO udp-backoff-fingerprinting-paper.txt

#%attr(644,root,root)		%config	/etc/goober.conf
#%attr(755,root,root)			/etc/rc.d/init.d/goober
#%attr(644,root,root)			/usr/man/man8/goober.8
#				%doc	faq/* README ChangeLog QUICKSTART doc/*
#				%doc	contrib/url-normalizer.pl contrib/rredir.* contrib/user-agents.pl
#%attr(750,nobody,nobody)	%dir	/var/log/goober
#%attr(750,nobody,nobody)	%dir	/var/spool/goober


#%pre
#if [ "$1" = "1" ]; then		#This package is being installed for the first time
#	#pre - $1=1 - first install
#else				#This is an upgrade
#	#pre - $1=2 - upgrade (techically, $1>1)
#fi
#
#
#%post
#if [ "$1" = "1" ]; then		#This package is being installed for the first time
#	/sbin/chkconfig --add goober
#	if [ -f /etc/rc.d/rc.sysinit ]; then
#		if [ `cat /etc/rc.d/rc.sysinit | grep devfsd | wc -l` -eq 0 ]; then	#If no references to devfs yet
#			#Add the following lines just after #!/bin/sh or #!/bin/bash.
#			cat /etc/rc.d/rc.sysinit | sed -e 's@\(#!/bin/.*sh\)@\1\
#if [ -c /dev/.devfsd ]; then				#devfsdinstall\
#	if ! ps axf | grep [d]evfsd >/dev/null ; then	#devfsdinstall\
#		#devfs not running yet			#devfsdinstall\
#		/sbin/devfsd /dev			#devfsdinstall\
#	fi						#devfsdinstall\
#fi							#devfsdinstall\
#@' >/etc/rc.d/rc.sysinit.tmp
#			cat /etc/rc.d/rc.sysinit.tmp >/etc/rc.d/rc.sysinit
#			rm -f /etc/rc.d/rc.sysinit.tmp
#		fi
#	else
#		echo You don\'t have an /etc/rc.d/rc.sysinit - you will need to add
#		echo 'if [ -c /dev/.devfsd ]; then'
#		echo '	if ! ps axf | grep [d]evfsd >/dev/null ; then'
#		echo '		/sbin/devfsd /dev'
#		echo '	fi'
#		echo 'fi'
#		echo to your initialization scripts, before any filesystem checking is done.
#	fi
#fi
#if [ "$1" = "1" ]; then		#This package is being installed for the first time
#	#post - $1=1 - first install
#else				#This is an upgrade
#	#post - $1=2 - upgrade (techically, $1>1)
#fi
#/usr/bin/at 04:00 <<EOTEXT
#/sbin/shutdown -r now
#EOTEXT
#
#
#%preun
#if [ "$1" = "0" ]; then		#This is being completely erased, not upgraded
#	#preun - $1=0 - final erasure
#	/sbin/chkconfig --del goober
#else				#This is an upgrade
#	#preun - $1=1 - upgrade (techically, $1>0)
#fi
#
#
#%postun
#if [ "$1" = "0" ]; then		#Final removal, not upgrade.
#	if [ -f /etc/rc.d/rc.sysinit ]; then
#		if [ `cat /etc/rc.d/rc.sysinit | grep devfsdinstall | wc -l` -gt 0 ]; then
#			cat /etc/rc.d/rc.sysinit | grep -v devfsdinstall >/etc/rc.d/rc.sysinit.tmp
#			cat /etc/rc.d/rc.sysinit.tmp >/etc/rc.d/rc.sysinit
#			rm -f /etc/rc.d/rc.sysinit.tmp
#		fi
#	fi
#fi
#
#if [ "$1" = "0" ]; then		#This is being completely erased, not upgraded
#	#postun - $1=0 - final erasure
#else				#This is an upgrade
#	#postun - $1=1 - upgrade (techically, $1>0)
#fi
#		
##Here are the scripts run at first install, in this order:
##pre - 1 - first install
##post - 1 - first install
#
##Here are the scripts run during an upgrade, in this order:
##pre - 2 - upgrade
##post - 2 - upgrade
##preun - 1 - upgrade
##postun - 1 - upgrade
#
##Here are the scripts run at final erase, in this order:
##preun - 0 - final erasure
##postun - 0 - final erasure
