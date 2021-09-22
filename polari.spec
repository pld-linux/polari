Summary:	Polari - IRC client for GNOME 3
Summary(pl.UTF-8):	Polari - klient IRC dla GNOME 3
Name:		polari
Version:	41.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	https://download.gnome.org/sources/polari/41/%{name}-%{version}.tar.xz
# Source0-md5:	ee2c85547fba723ad309e0415630b512
URL:		https://wiki.gnome.org/Apps/Polari
BuildRequires:	appstream-glib
BuildRequires:	gettext-tools >= 0.19.6
BuildRequires:	gjs-devel >= 1.69.2
BuildRequires:	glib2-devel >= 1:2.43.4
BuildRequires:	gobject-introspection-devel >= 1.0
BuildRequires:	meson >= 0.53.0
# for syntax checking
#BuildRequires:	mozjs78 >= 78
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	telepathy-glib-devel >= 0.12
BuildRequires:	yelp-tools
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.43.4
# see src/main.js for GI dependencies
Requires:	gdk-pixbuf2 >= 2.0
Requires:	gjs >= 1.69.2
Requires:	glib2 >= 1:2.43.4
Requires:	gspell
Requires:	gtk4 >= 4.0
Requires:	libsecret
# or libsoup3 >= 3.0
Requires:	libsoup >= 2.4
Requires:	pango >= 1:1.26
Requires:	telepathy-glib >= 0.12
Requires:	telepathy-logger-libs >= 0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polari is an Internet Relay Chat (IRC) client designed for GNOME 3.

%description -l pl.UTF-8
Polari to klient usługi IRC (Internet Relay Chat), zaprojektowany dla
GNOME 3.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/polari
%dir %{_libdir}/polari
%attr(755,root,root) %{_libdir}/polari/libpolari-1.0.so
%dir %{_libdir}/polari/girepository-1.0
%{_libdir}/polari/girepository-1.0/Polari-1.0.typelib
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Polari.service
%{_datadir}/dbus-1/services/org.gnome.Polari.service
%{_datadir}/glib-2.0/schemas/org.gnome.Polari.gschema.xml
%{_datadir}/metainfo/org.gnome.Polari.appdata.xml
%{_datadir}/polari
%{_datadir}/telepathy/clients/Polari.client
%{_desktopdir}/org.gnome.Polari.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Polari.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Polari.Devel.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Polari-symbolic.svg
