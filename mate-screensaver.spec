Summary:	MATE screensaver
Summary(pl.UTF-8):	Wygaszacz ekranu MATE
Name:		mate-screensaver
Version:	1.28.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://pub.mate-desktop.org/releases/1.28/%{name}-%{version}.tar.xz
# Source0-md5:	0ae075d5d3c0f84d1cb1898bc231d504
Source1:	%{name}.pamd
URL:		https://wiki.mate-desktop.org/mate-desktop/components/mate-screensaver/
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	autoconf >= 2.60
BuildRequires:	autoconf-archive
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.30
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.58.0
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	libmatekbd-devel >= 1.17.0
BuildRequires:	libnotify-devel >= 0.7.1
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	mate-common
BuildRequires:	mate-desktop-devel >= 1.17.0
BuildRequires:	mate-menus-devel >= 1.21.0
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
# or elogind
BuildRequires:	systemd-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xmlto
BuildRequires:	xorg-lib-libX11-devel >= 1.0
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.58.0
Requires:	dbus-glib >= 0.30
Requires:	glib2 >= 1:2.58.0
Requires:	gtk+3 >= 3.22
Requires:	libmatekbd >= 1.17.0
Requires:	libnotify >= 0.7.1
Requires:	mate-desktop >= 1.17.0
Requires:	mate-menus >= 1.21.0
Requires:	xdg-menus
Requires:	xorg-lib-libX11 >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mate-screensaver is a screen saver and locker that aims to have
simple, sane, secure defaults and be well integrated with the desktop.

%description -l pl.UTF-8
mate-screensaver to wygaszacz ekranu z opcją blokowania, który ma za
zadanie mieć proste, rozsądne i bezpieczne ustawienia domyślne oraz
być dobrze zintegrowany ze środowiskiem graficznym.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-locking \
	--enable-pam \
	--disable-silent-rules \
	--with-mit-ext \
	--with-shadow \
	--with-xf86gamma-ext \
	--with-xscreensaverdir=%{_datadir}/xscreensaver \
	--with-xscreensaverhackdir=%{_libdir}/xscreensaver
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{frp,ie,ku_IQ}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/mate-screensaver

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/mate-screensaver
%attr(755,root,root) %{_bindir}/mate-screensaver-command
%attr(755,root,root) %{_bindir}/mate-screensaver-preferences
%attr(755,root,root) %{_libexecdir}/mate-screensaver-dialog
%attr(755,root,root) %{_libexecdir}/mate-screensaver-gl-helper
%dir %{_libexecdir}/mate-screensaver
%attr(755,root,root) %{_libexecdir}/mate-screensaver/floaters
%attr(755,root,root) %{_libexecdir}/mate-screensaver/popsquares
%attr(755,root,root) %{_libexecdir}/mate-screensaver/slideshow
%{_datadir}/%{name}
%{_datadir}/backgrounds/cosmos
%{_datadir}/dbus-1/services/org.mate.ScreenSaver.service
%{_datadir}/desktop-directories/mate-screensaver.directory
%{_datadir}/glib-2.0/schemas/org.mate.screensaver.gschema.xml
%{_datadir}/mate-background-properties/cosmos.xml
%{_desktopdir}/mate-screensaver-preferences.desktop
%dir %{_desktopdir}/screensavers
%{_desktopdir}/screensavers/cosmos-slideshow.desktop
%{_desktopdir}/screensavers/footlogo-floaters.desktop
%{_desktopdir}/screensavers/gnomelogo-floaters.desktop
%{_desktopdir}/screensavers/personal-slideshow.desktop
%{_desktopdir}/screensavers/popsquares.desktop
%{_pixmapsdir}/gnome-logo-white.svg
%{_pixmapsdir}/mate-logo-white.svg
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/mate-screensaver
%{_sysconfdir}/xdg/autostart/mate-screensaver.desktop
%{_sysconfdir}/xdg/menus/mate-screensavers.menu
%{_pkgconfigdir}/mate-screensaver.pc
%{_mandir}/man1/mate-screensaver.1*
%{_mandir}/man1/mate-screensaver-command.1*
%{_mandir}/man1/mate-screensaver-preferences.1*
