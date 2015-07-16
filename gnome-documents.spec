Summary:	Document manager for GNOME
Summary(pl.UTF-8):	Zarządca dokumentów dla GNOME
Name:		gnome-documents
Version:	3.16.2
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-documents/3.16/%{name}-%{version}.tar.xz
# Source0-md5:	cad0694cc457992360c20f6c13687e47
URL:		https://wiki.gnome.org/Apps/Documents
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	clutter-devel >= 1.10.0
BuildRequires:	clutter-gtk-devel >= 1.4.0
BuildRequires:	evince-devel >= 3.14.0
BuildRequires:	gettext-tools
BuildRequires:	gjs-devel
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gnome-desktop-devel >= 3.2.0
BuildRequires:	gnome-online-accounts-devel >= 3.2.0
BuildRequires:	gobject-introspection-devel >= 1.32.0
BuildRequires:	gtk+3-devel >= 3.16.0
BuildRequires:	gtk-webkit4-devel >= 2.6.0
BuildRequires:	intltool >= 0.50.1
BuildRequires:	libgdata-devel >= 0.13.3
BuildRequires:	libsoup-devel >= 2.42.0
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	libzapojit-devel >= 0.0.2
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
Requires:	glib2 >= 1:2.40.0
Requires:	gnome-online-accounts >= 3.2.0
Requires:	gobject-introspection >= 1.32.0
Requires:	gtk+3 >= 3.16.0
Requires:	gtk-webkit4 >= 2.6.0
Requires:	hicolor-icon-theme
Requires:	libgdata >= 0.13.3
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
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4 -I libgd
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-documents/*.la

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
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/gnome-books
%attr(755,root,root) %{_bindir}/gnome-documents
%dir %{_libdir}/gnome-documents
%attr(755,root,root) %{_libdir}/gnome-documents/libgd.so
%attr(755,root,root) %{_libdir}/gnome-documents/libgdprivate-1.0.so
%dir %{_libdir}/gnome-documents/girepository-1.0
%{_libdir}/gnome-documents/girepository-1.0/Gd-1.0.typelib
%{_libdir}/gnome-documents/girepository-1.0/GdPrivate-1.0.typelib
%{_datadir}/appdata/org.gnome.Books.appdata.xml
%{_datadir}/appdata/org.gnome.Documents.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Books.service
%{_datadir}/dbus-1/services/org.gnome.Documents.service
%{_datadir}/glib-2.0/schemas/org.gnome.Documents.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.books.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.documents.gschema.xml
%{_datadir}/gnome-documents
%{_datadir}/gnome-shell/search-providers/org.gnome.Documents.search-provider.ini
%{_desktopdir}/org.gnome.Books.desktop
%{_desktopdir}/org.gnome.Documents.desktop
%{_iconsdir}/hicolor/*x*/apps/gnome-books.png
%{_iconsdir}/hicolor/*x*/apps/gnome-documents.png
%{_iconsdir}/hicolor/scalable/apps/gnome-books-symbolic.svg
%{_iconsdir}/hicolor/scalable/apps/gnome-documents-symbolic.svg
%{_mandir}/man1/gnome-books.1*
%{_mandir}/man1/gnome-documents.1*
