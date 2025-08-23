#
# Conditional build:
%bcond_without	pdf	# "getting-started" PDFs

Summary:	Document manager for GNOME
Summary(pl.UTF-8):	Zarządca dokumentów dla GNOME
Name:		gnome-documents
Version:	3.34.0
Release:	3
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-documents/3.34/%{name}-%{version}.tar.xz
# Source0-md5:	7158db2c13ae45fe166df8c66f9d083c
Patch0:		%{name}-gnome-desktop.patch
Patch1:		%{name}-meson.patch
Patch2:		%{name}-inkscape.patch
URL:		https://wiki.gnome.org/Apps/Documents
BuildRequires:	clutter-devel >= 1.10.0
BuildRequires:	clutter-gtk-devel >= 1.4.0
BuildRequires:	evince-devel >= 3.14.0
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	gjs-devel >= 1.48.0
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gnome-desktop-devel >= 43
BuildRequires:	gnome-online-accounts-devel >= 3.2.0
BuildRequires:	gobject-introspection-devel >= 1.32.0
BuildRequires:	gtk+3-devel >= 3.22.15
BuildRequires:	gtk-webkit4-devel >= 2.6.0
BuildRequires:	libgdata-devel >= 0.13.3
BuildRequires:	libgepub-devel >= 0.6
BuildRequires:	libsoup-devel >= 2.42.0
BuildRequires:	libxslt-progs
BuildRequires:	libzapojit-devel >= 0.0.2
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	tracker-devel >= 2.0.0
BuildRequires:	xz
BuildRequires:	yelp-tools
%if %{with pdf}
BuildRequires:	inkscape >= 1.0
# pdfunite
BuildRequires:	poppler-progs
%endif
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.40.0
Requires:	clutter-gtk >= 1.4.0
Requires:	evince >= 3.14.0
Requires:	gjs >= 1.48.0
Requires:	glib2 >= 1:2.40.0
Requires:	gnome-desktop >= 43
Requires:	gnome-online-accounts >= 3.2.0
Requires:	gobject-introspection >= 1.32.0
Requires:	gtk+3 >= 3.22.15
Requires:	gtk-webkit4 >= 2.6.0
Requires:	hicolor-icon-theme
Requires:	libgdata >= 0.13.3
Requires:	libgepub >= 0.6
Requires:	libsoup >= 2.42.0
Requires:	libzapojit >= 0.0.2
Requires:	tracker >= 2.0.0
Suggests:	unoconv >= 0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-documents is a document manager application for GNOME.

%description -l pl.UTF-8
gnome-documents to aplikacja dla GNOME służąca do zarządzania
dokumentami.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

# workaround "data/meson.build:6:0: ERROR: Sandbox violation: Tried to grab file gd-main-view.h from a nested subproject."
cp -p subprojects/libgd/libgd/gd-main-view{,-generic}.h data
%{__sed} -i -e "s!join_paths(libgd_src_path, \('[^']*'\))!\1!" data/meson.build

%build
%meson \
	%{?with_pdf:-Dgetting_started=true}

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

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
%{_datadir}/dbus-1/services/org.gnome.Documents.service
%{_datadir}/glib-2.0/schemas/org.gnome.Documents.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.documents.gschema.xml
%dir %{_datadir}/gnome-documents
%attr(755,root,root) %{_datadir}/gnome-documents/org.gnome.Documents
%{_datadir}/gnome-documents/org.gnome.Documents.*.gresource
%dir %{_datadir}/gnome-documents/gir-1.0
%{_datadir}/gnome-documents/gir-1.0/Gd-1.0.gir
%{_datadir}/gnome-documents/gir-1.0/GdPrivate-1.0.gir
%if %{with pdf}
%dir %{_datadir}/gnome-documents/getting-started
%{_datadir}/gnome-documents/getting-started/C
%endif
%{_datadir}/gnome-shell/search-providers/org.gnome.Documents.search-provider.ini
%{_datadir}/metainfo/org.gnome.Documents.appdata.xml
%{_desktopdir}/org.gnome.Documents.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Documents.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Documents-symbolic.svg
%{_mandir}/man1/gnome-documents.1*
