# TODO: use gtk4-update-icon-cache
Summary:	Polari - IRC client for GNOME 3
Summary(pl.UTF-8):	Polari - klient IRC dla GNOME 3
Name:		polari
Version:	46.0
Release:	2
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	https://download.gnome.org/sources/polari/46/%{name}-%{version}.tar.xz
# Source0-md5:	61da1fa512be82555ffbc0a2cc69515c
Patch0:		%{name}-no-update.patch
URL:		https://wiki.gnome.org/Apps/Polari
BuildRequires:	appstream-glib
BuildRequires:	gettext-tools >= 0.19.6
BuildRequires:	gjs-devel >= 1.73.1
BuildRequires:	glib2-devel >= 1:2.43.4
BuildRequires:	gobject-introspection-devel >= 1.0
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	telepathy-glib-devel >= 0.12
BuildRequires:	tracker3-devel >= 3.0
BuildRequires:	yelp-tools
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.43.4
Requires(post,postun):	gtk-update-icon-cache
# see src/main.js for GI dependencies
Requires:	gdk-pixbuf2 >= 2.0
Requires:	gjs >= 1.73.1
Requires:	glib2 >= 1:2.43.4
Requires:	graphene
Requires:	gspell
# thumbnailer still uses GTK+ 3 and webkit 4.1/4.0
Requires:	gtk+3 >= 3.0
Requires:	gtk-webkit4.1
Requires:	gtk4 >= 4.0
Requires:	hicolor-icon-theme
Requires:	libadwaita
Requires:	libsecret
Requires:	libsoup3 >= 3.0
Requires:	pango >= 1:1.26
Requires:	telepathy-glib >= 0.12
Requires:	telepathy-logger-libs >= 0.2
Requires:	tracker3 >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polari is an Internet Relay Chat (IRC) client designed for GNOME 3.

%description -l pl.UTF-8
Polari to klient usługi IRC (Internet Relay Chat), zaprojektowany dla
GNOME 3.

%prep
%setup -q
%patch0 -p1

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/*/apps/org.gnome.Polari*.license

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md logo.png.license data/icons/*.license data/icons/hicolor/*/apps/*.license
%attr(755,root,root) %{_bindir}/polari
%dir %{_libdir}/polari
%attr(755,root,root) %{_libdir}/polari/libpolari-1.0.so
%dir %{_libdir}/polari/girepository-1.0
%{_libdir}/polari/girepository-1.0/Polari-1.0.typelib
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Polari.service
%{_datadir}/dbus-1/services/org.gnome.Polari.service
%{_datadir}/glib-2.0/schemas/org.gnome.Polari.gschema.xml
%{_datadir}/metainfo/org.gnome.Polari.metainfo.xml
%{_datadir}/polari
%{_datadir}/telepathy/clients/Polari.client
%{_desktopdir}/org.gnome.Polari.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Polari.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Polari.Devel.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Polari-symbolic.svg
