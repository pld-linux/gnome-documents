Summary:	Document manager for GNOME
Name:		gnome-documents
Version:	0.2.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-documents/0.2/%{name}-%{version}.tar.xz
# Source0-md5:	6df1570b1d737e00d848bc4a144b5594
URL:		https://live.gnome.org/Design/Apps/Documents
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	clutter-gtk-devel >= 1.0.1
BuildRequires:	evince-devel >= 3.2.0
BuildRequires:	gettext-devel
BuildRequires:	gjs-devel
BuildRequires:	glib2-devel >= 1:2.30.0
BuildRequires:	gnome-desktop-devel >= 3.2.0
BuildRequires:	gnome-online-accounts-devel >= 3.2.0
BuildRequires:	gobject-introspection-devel >= 1.30.0
BuildRequires:	gtk+3-devel >= 3.2.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgdata-devel >= 0.9.1
BuildRequires:	liboauth-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	tracker-devel >= 0.12.1
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	clutter-gtk >= 1.0.1
Requires:	evince >= 3.2.0
Requires:	gobject-introspection >= 1.30.0
Requires:	gtk+3 >= 3.2.0
Requires:	hicolor-icon-theme
Requires:	libgdata >= 0.9.1
Requires:	tracker-libs >= 0.12.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-documents is a document manager application for GNOME.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
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
%attr(755,root,root) %{_libdir}/libgdprivate-1.0.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libgdprivate-1.0.so.0
%{_libdir}/girepository-1.0/Gd-1.0.typelib
%{_datadir}/dbus-1/services/org.gnome.Documents.GDataMiner.service
%{_datadir}/glib-2.0/schemas/org.gnome.documents.gschema.xml
%{_datadir}/gnome-documents
%{_desktopdir}/gnome-documents.desktop
%{_iconsdir}/hicolor/*/*/*.png
