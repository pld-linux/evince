# TODO
# - evince.desktop provides mimetypes for all possible choices, yet some of
#   them are in subpackages (backend-foo). multiple .desktop files is possible
#   for same application?
#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
%bcond_without	nautilus	# Nautilus extensions

Summary:	Document viewer for multiple document formats
Summary(pl.UTF-8):	Przeglądarka dokumentów w wielu formatach
Name:		evince
Version:	3.14.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evince/3.14/%{name}-%{version}.tar.xz
# Source0-md5:	feaf7382d4829a8ea52bfbaae106b9da
Patch0:		%{name}-linking.patch
URL:		http://www.gnome.org/projects/evince/
BuildRequires:	adwaita-icon-theme >= 2.17.1
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.10
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	djvulibre-devel >= 3.5.17
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-desktop-devel >= 3.0
BuildRequires:	gobject-introspection-devel >= 1.0
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk+3-devel >= 3.12.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.13}
BuildRequires:	intltool >= 0.40.0
BuildRequires:	kpathsea-devel
BuildRequires:	libgxps-devel >= 0.2.1
BuildRequires:	libsecret-devel >= 0.5
BuildRequires:	libspectre-devel >= 0.2.0
BuildRequires:	libtiff-devel >= 3.6
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	libxml2-progs >= 1:2.6.31
%{?with_nautilus:BuildRequires:	nautilus-devel >= 3.0.0}
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.24.0
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	t1lib-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel >= 1.0.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.36.0
Requires:	%{name}-libs = %{version}-%{release}
Requires:	cairo >= 1.10.0
Requires:	dconf
Requires:	gsettings-desktop-schemas
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	libsecret >= 0.5
Requires:	xorg-lib-libSM >= 1.0.0
Suggests:	evince-backend-djvu
Suggests:	evince-backend-dvi
Suggests:	evince-backend-pdf
Suggests:	evince-backend-ps
Suggests:	gtk+3-cups >= 3.12.0
Obsoletes:	evince-gtk
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		backendsdir	%{_libdir}/evince/4/backends

%description
Evince is a document viewer for multiple document formats like pdf,
postscript, and many others. The goal of evince is to replace the
multiple document viewers that exist on the GNOME Desktop, like ggv,
gpdf, and xpdf with a single simple application.

%description -l pl.UTF-8
Evince jest przeglądarką dokumentów w wielu formatach takich jak pdf,
postscript i wielu innych. W zamierzeniach program ma zastąpić
przeglądarki dokumentów dla środowiska GNOME, takie jak ggv, gpdf i
xpdf jedną prostą aplikacją.

%package libs
Summary:	Evince shared libraries
Summary(pl.UTF-8):	Biblioteki współdzielone Evince
Group:		X11/Libraries
Requires:	glib2 >= 1:2.36.0
Requires:	gtk+3 >= 3.12.0
Conflicts:	evince < 3.10.3-2

%description libs
Evince shared libraries.

%description libs -l pl.UTF-8
Biblioteki współdzielone Evince.

%package devel
Summary:	Header files for Evince
Summary(pl.UTF-8):	Pliki nagłówkowe Evince
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.36.0
Requires:	gtk+3-devel >= 3.12.0

%description devel
Header files for Evince.

%description devel -l pl.UTF-8
Pliki nagłówkowe Evince.

%package apidocs
Summary:	Evince API documentation
Summary(pl.UTF-8):	Dokumentacja API aplikacji Evince
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Evince API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API aplikacji Evince.

%package -n nautilus-extension-evince
Summary:	Evince extension for Nautilus
Summary(pl.UTF-8):	Rozszerzenie Evince dla Nautilusa
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus >= 3.0.0

%description -n nautilus-extension-evince
This extension shows Evince document properties in Nautilus.

%description -n nautilus-extension-evince -l pl.UTF-8
To rozszerzenie pokazuje właściwości dokumentu Evince w Nautilusie.

%package backend-djvu
Summary:	View DjVu documents with Evince
Summary(pl.UTF-8):	Przeglądanie dokumentów DjVu przy użyciu Evince
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	djvulibre >= 3.5.17

%description backend-djvu
View DjVu documents with Evince.

%description backend-djvu -l pl.UTF-8
Przeglądanie dokumentów DjVu przy użyciu Evince.

%package backend-dvi
Summary:	View DVI documents with Evince
Summary(pl.UTF-8):	Przeglądanie dokumentów DVI przy użyciu Evince
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	libspectre >= 0.2.0

%description backend-dvi
View DVI documents with Evince.

%description backend-dvi -l pl.UTF-8
Przeglądanie dokumentów DVI przy użyciu Evince.

%package backend-pdf
Summary:	View PDF documents with Evince
Summary(pl.UTF-8):	Przeglądanie dokumentów PDF przy użyciu Evince
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	libxml2 >= 1:2.6.31
Requires:	poppler-glib >= 0.24.0

%description backend-pdf
View PDF documents with Evince.

%description backend-pdf -l pl.UTF-8
Przeglądanie dokumentów PDF przy użyciu Evince.

%package backend-ps
Summary:	View PostScript documents with Evince
Summary(pl.UTF-8):	Przeglądanie dokumentów PostScript przy użyciu Evince
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	libspectre >= 0.2.0

%description backend-ps
View PostScript documents with Evince.

%description backend-ps -l pl.UTF-8
Przeglądanie dokumentów PostScript przy użyciu Evince.

%package backend-xps
Summary:	View XPS documents with Evince
Summary(pl.UTF-8):	Przeglądanie dokumentów XPS przy użyciu Evince
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	libgxps >= 0.2.1

%description backend-xps
View XPS documents with Evince.

%description backend-xps -l pl.UTF-8
Przeglądanie dokumentów XPS przy użyciu Evince.

%package -n browser-plugin-evince
Summary:	Evince browser plugin
Summary(pl.UTF-8):	Wtyczka Evince dla przegądarek WWW
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Requires:	browser-plugins >= 2.0

%description -n browser-plugin-evince
Evince plugin for Mozilla-compatible web browsers.

%description -n browser-plugin-evince -l pl.UTF-8
Wtyczka Evince dla przegądarek WWW zgodnych z Mozillą.

%prep
%setup -q
%patch0 -p1

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	BROWSER_PLUGIN_DIR=%{_browserpluginsdir} \
	--enable-comics \
	--enable-djvu \
	--enable-dvi \
	%{?with_apidocs:--enable-gtk-doc} \
	--enable-introspection \
	--enable-nautilus%{!?with_nautilus:=no} \
	--enable-pdf \
	--disable-silent-rules \
	--disable-static \
	--enable-t1lib \
	--enable-tiff \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_browserpluginsdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{backendsdir}/*.la
%if %{with nautilus}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-3.0/*.la
%endif

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_desktop_database_postun
%update_icon_cache hicolor
%glib_compile_schemas

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post
%update_browser_plugins

%postun
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/evince
%attr(755,root,root) %{_bindir}/evince-previewer
%attr(755,root,root) %{_bindir}/evince-thumbnailer
%attr(755,root,root) %{_libexecdir}/evinced
%dir %{_libdir}/evince
%dir %{_libdir}/evince/4
%dir %{backendsdir}
%attr(755,root,root) %{backendsdir}/libcomicsdocument.so
%{backendsdir}/comicsdocument.evince-backend
%attr(755,root,root) %{backendsdir}/libtiffdocument.so
%{backendsdir}/tiffdocument.evince-backend
%{_datadir}/GConf/gsettings/evince.convert
%{_datadir}/appdata/evince.appdata.xml
%{_datadir}/appdata/evince-comicsdocument.metainfo.xml
%{_datadir}/appdata/evince-tiffdocument.metainfo.xml
%{_datadir}/dbus-1/services/org.gnome.evince.Daemon.service
%{_datadir}/glib-2.0/schemas/org.gnome.Evince.gschema.xml
%{_datadir}/%{name}
%{_datadir}/thumbnailers/evince.thumbnailer
%{_mandir}/man1/evince.1*
%{_desktopdir}/evince.desktop
%{_desktopdir}/evince-previewer.desktop
%{_iconsdir}/hicolor/*x*/apps/evince.png

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libevdocument3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libevdocument3.so.4
%attr(755,root,root) %{_libdir}/libevview3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libevview3.so.3
%{_libdir}/girepository-1.0/EvinceDocument-3.0.typelib
%{_libdir}/girepository-1.0/EvinceView-3.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libevdocument3.so
%attr(755,root,root) %{_libdir}/libevview3.so
%{_datadir}/gir-1.0/EvinceDocument-3.0.gir
%{_datadir}/gir-1.0/EvinceView-3.0.gir
%{_includedir}/evince
%{_pkgconfigdir}/evince-document-3.0.pc
%{_pkgconfigdir}/evince-view-3.0.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/evince
%{_gtkdocdir}/libevdocument-3.0
%{_gtkdocdir}/libevview-3.0
%endif

%files backend-djvu
%defattr(644,root,root,755)
%attr(755,root,root) %{backendsdir}/libdjvudocument.so
%{backendsdir}/djvudocument.evince-backend
%{_datadir}/appdata/evince-djvudocument.metainfo.xml

%files backend-dvi
%defattr(644,root,root,755)
%attr(755,root,root) %{backendsdir}/libdvidocument.so
%{backendsdir}/dvidocument.evince-backend
%{_datadir}/appdata/evince-dvidocument.metainfo.xml

%files backend-pdf
%defattr(644,root,root,755)
%attr(755,root,root) %{backendsdir}/libpdfdocument.so
%{backendsdir}/pdfdocument.evince-backend
%{_datadir}/appdata/evince-pdfdocument.metainfo.xml

%files backend-ps
%defattr(644,root,root,755)
%attr(755,root,root) %{backendsdir}/libpsdocument.so
%{backendsdir}/psdocument.evince-backend
%{_datadir}/appdata/evince-psdocument.metainfo.xml

%files backend-xps
%defattr(644,root,root,755)
%attr(755,root,root) %{backendsdir}/libxpsdocument.so
%{backendsdir}/xpsdocument.evince-backend
%{_datadir}/appdata/evince-xpsdocument.metainfo.xml

%if %{with nautilus}
%files -n nautilus-extension-evince
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libevince-properties-page.so
%endif

%files -n browser-plugin-evince
%defattr(644,root,root,755)
%attr(755,root,root) %{_browserpluginsdir}/libevbrowserplugin.so
