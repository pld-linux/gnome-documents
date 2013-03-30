Summary:	Document manager for GNOME
Name:		gnome-documents
Version:	3.8.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-documents/3.8/%{name}-%{version}.tar.xz
# Source0-md5:	ac60339dad84c0867cc7b1c0bdf1199b
URL:		https://live.gnome.org/Design/Apps/Documents
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	clutter-devel >= 1.10.0
BuildRequires:	clutter-gtk-devel >= 1.4.0
BuildRequires:	evince-devel >= 3.8.0
BuildRequires:	gettext-devel
BuildRequires:	gjs-devel
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gnome-desktop-devel >= 3.2.0
BuildRequires:	gnome-online-accounts-devel >= 3.2.0
BuildRequires:	gobject-introspection-devel >= 1.32.0
BuildRequires:	gtk+3-devel >= 3.8.0
BuildRequires:	gtk-webkit3-devel >= 1.10.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgdata-devel >= 0.13.3
BuildRequires:	liboauth-devel
BuildRequires:	libsoup-devel >= 2.42.0
BuildRequires:	libtool
BuildRequires:	libzapojit-devel >= 0.0.2
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	tracker-devel >= 0.16.0
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	clutter-gtk >= 1.4.0
Requires:	evince >= 3.8.0
Requires:	glib2 >= 1:2.36.0
Requires:	gobject-introspection >= 1.32.0
Requires:	gtk+3 >= 3.8.0
Requires:	hicolor-icon-theme
Requires:	libgdata >= 0.13.3
Requires:	tracker >= 0.16.0
Suggests:	unoconv >= 0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-documents is a document manager application for GNOME.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4 -I libgd
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-documents/*.la

%find_lang gnome-documents

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_icon_cache hicolor
%glib_compile_schemas

%postun
/sbin/ldconfig
%update_icon_cache hicolor
%glib_compile_schemas

%files -f gnome-documents.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/gnome-documents
%attr(755,root,root) %{_libexecdir}/gd-tracker-gdata-miner
%attr(755,root,root) %{_libexecdir}/gd-tracker-zpj-miner
%dir %{_libdir}/gnome-documents
%attr(755,root,root) %{_libdir}/gnome-documents/libgd.so
%attr(755,root,root) %{_libdir}/gnome-documents/libgdminer-1.0.so
%attr(755,root,root) %{_libdir}/gnome-documents/libgdprivate-1.0.so
%dir %{_libdir}/gnome-documents/girepository-1.0
%{_libdir}/gnome-documents/girepository-1.0/Egg-1.0.typelib
%{_libdir}/gnome-documents/girepository-1.0/Gd-1.0.typelib
%{_libdir}/gnome-documents/girepository-1.0/GdPrivate-1.0.typelib
%{_datadir}/dbus-1/services/org.gnome.Documents.GDataMiner.service
%{_datadir}/dbus-1/services/org.gnome.Documents.SearchProvider.service
%{_datadir}/dbus-1/services/org.gnome.Documents.ZpjMiner.service
%{_datadir}/glib-2.0/schemas/org.gnome.Documents.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.documents.gschema.xml
%{_datadir}/gnome-documents
%{_datadir}/gnome-shell/search-providers/gnome-documents-search-provider.ini
%{_desktopdir}/gnome-documents.desktop
%{_iconsdir}/hicolor/*/*/*.png
