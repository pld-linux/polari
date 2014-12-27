Summary:	Polari - IRC client for GNOME 3
Summary(pl.UTF-8):	Polari - klient IRC dla GNOME 3
Name:		polari
Version:	3.14.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	http://ftp.gnome.org/pub/GNOME/sources/polari/3.14/%{name}-%{version}.tar.xz
# Source0-md5:	126fcc8d4eaa1b1bd3269f62ec0357a9
URL:		https://wiki.gnome.org/Apps/Polari
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.42
BuildRequires:	gobject-introspection-devel >= 0.9.6
BuildRequires:	gtk+3-devel >= 3.14
BuildRequires:	intltool >= 0.50.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	telepathy-glib-devel
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.42
Requires:	gjs >= 1.40
Requires:	glib2 >= 1:2.42
Requires:	gtk+3 >= 3.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polari is an Internet Relay Chat (IRC) client designed for GNOME 3.

%description -l pl.UTF-8
Polari to klient usługi IRC (Internet Relay Chat), zaprojektowany dla
GNOME 3.

%prep
%setup -q

%build
%configure \
	GJS_CONSOLE=/usr/bin/gjs-console \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# private library
%{__rm} $RPM_BUILD_ROOT%{_libdir}/polari/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_bindir}/polari
%dir %{_libdir}/polari
%attr(755,root,root) %{_libdir}/polari/libpolari-1.0.so
%dir %{_libdir}/polari/girepository-1.0
%{_libdir}/polari/girepository-1.0/Polari-1.0.typelib
%{_datadir}/polari
%{_datadir}/appdata/org.gnome.Polari.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Polari.service
%{_datadir}/glib-2.0/schemas/org.gnome.polari.gschema.xml
%{_desktopdir}/org.gnome.Polari.desktop
%{_iconsdir}/hicolor/*/apps/polari.*
