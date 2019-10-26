Summary:	Document manager for GNOME
Summary(pl.UTF-8):	Zarządca dokumentów dla GNOME
Name:		gnome-documents
Version:	3.34.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-documents/3.34/%{name}-%{version}.tar.xz
# Source0-md5:	7158db2c13ae45fe166df8c66f9d083c
URL:		https://wiki.gnome.org/Apps/Documents
BuildRequires:	clutter-devel >= 1.10.0
BuildRequires:	clutter-gtk-devel >= 1.4.0
BuildRequires:	evince-devel >= 3.14.0
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	gjs-devel >= 1.48.0
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gnome-desktop-devel >= 3.2.0
BuildRequires:	gnome-online-accounts-devel >= 3.2.0
BuildRequires:	gobject-introspection-devel >= 1.32.0
BuildRequires:	gtk+3-devel >= 3.22.15
BuildRequires:	gtk-webkit4-devel >= 2.6.0
BuildRequires:	libgdata-devel >= 0.13.3
BuildRequires:	libgepub-devel >= 0.6
BuildRequires:	libsoup-devel >= 2.42.0
BuildRequires:	libxslt-progs
BuildRequires:	libzapojit-devel >= 0.0.2
BuildRequires:	meson >= 0.42.0
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	tracker-devel >= 1.0.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.40.0
Requires:	clutter-gtk >= 1.4.0
Requires:	evince >= 3.14.0
Requires:	gjs >= 1.48.0
Requires:	glib2 >= 1:2.40.0
Requires:	gnome-desktop >= 3.2.0
Requires:	gnome-online-accounts >= 3.2.0
Requires:	gobject-introspection >= 1.32.0
Requires:	gtk+3 >= 3.22.15
Requires:	gtk-webkit4 >= 2.6.0
Requires:	hicolor-icon-theme
Requires:	libgdata >= 0.13.3
Requires:	libgepub >= 0.6
Requires:	libsoup >= 2.42.0
Requires:	libzapojit >= 0.0.2
Requires:	tracker >= 1.0.0
Suggests:	unoconv >= 0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-documents is a document manager application for GNOME.

%description -l pl.UTF-8
gnome-documents to aplikacja dla GNOME służąca do zarządzania
dokumentami.

%prep
%setup -q

%build
%meson build
%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%glib_compile_schemas

%files -f gnome-documents.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md TODO
%attr(755,root,root) %{_bindir}/gnome-documents
%dir %{_libdir}/gnome-documents
%attr(755,root,root) %{_libdir}/gnome-documents/libgd.so
%attr(755,root,root) %{_libdir}/gnome-documents/libgdprivate-1.0.so
%dir %{_libdir}/gnome-documents/girepository-1.0
%{_libdir}/gnome-documents/girepository-1.0/Gd-1.0.typelib
%{_libdir}/gnome-documents/girepository-1.0/GdPrivate-1.0.typelib
%{_datadir}/metainfo/org.gnome.Documents.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Documents.service
%{_datadir}/glib-2.0/schemas/org.gnome.Documents.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.documents.gschema.xml
%dir %{_datadir}/gnome-documents
%attr(755,root,root) %{_datadir}/gnome-documents/org.gnome.Documents
%{_datadir}/gnome-documents/org.gnome.Documents.*.gresource
%dir %{_datadir}/gnome-documents/gir-1.0
%{_datadir}/gnome-documents/gir-1.0/Gd-1.0.gir
%{_datadir}/gnome-documents/gir-1.0/GdPrivate-1.0.gir
%{_datadir}/gnome-shell/search-providers/org.gnome.Documents.search-provider.ini
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Documents.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Documents-symbolic.svg
%{_desktopdir}/org.gnome.Documents.desktop
%{_mandir}/man1/gnome-documents.1*
