Summary: a small utility that transformx Xorg into a daemon
Name: xorg-launch-helper
Version: 4
Release: 0chadv1%{?dist}
License: GPLv2
Group: System Environment
URL: https://github.com/sofar/xorg-launch-helper
BuildArch:x86_64 i686
Source0: http://foo-projects.org/~sofar/xorg-launch-helper/xorg-launch-helper-4.tar.gz

Requires: xorg-x11-server-Xorg

%description
Xorg-launch-helper is a small utility that transforms the X server
process (XOrg) into a daemon that can be used to make applications
wait with starting until XOrg is ready for X11 connections.

The utility starts and forks the XOrg server and listens for a
signal from the XOrg server. At this point, the utility signals
systemd READY through sd_notify(). At this point systemd
will start units that have an explicit ordering configured
to be after the xorg.target.

This mechanism can be used to delay the starting up of services
that require a working X11 display server, such as any form
of graphical process or X11 window manager.
Gnome integration for the i3 window manager

%prep
%setup -q

%build
%configure
make %{_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
install -D -m 644 %{_builddir}/%{name}-%{version}/AUTHORS $RPM_BUILD_ROOT%{_docdir}/%{name}/AUTHORS
install -D -m 644 %{_builddir}/%{name}-%{version}/COPYING $RPM_BUILD_ROOT%{_docdir}/%{name}/COPYING
install -D -m 644 %{_builddir}/%{name}-%{version}/README $RPM_BUILD_ROOT%{_docdir}/%{name}/README

%files
%defattr(-,root,root,-)
%dir /usr/lib/systemd/user/xorg.target.wants
%dir %{_docdir}/%{name}
%{_bindir}/xorg-launch-helper
%{_docdir}/%{name}/*
/usr/lib/systemd/user/xorg.service
/usr/lib/systemd/user/xorg.target
/usr/lib/systemd/user/xorg.target.wants/xorg.service

%changelog
* Tue Mar 12 2013 Chad Versace <chad@chad-versace.us> 4-0chadv1
- Initial package
