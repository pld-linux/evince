# TODO
# - evince.desktop provides mimetypes for all possible choices, yet some of
#   them are in subpackages (backend-foo). multiple .desktop files is possible
#   for same application?
#
# Conditional build:
%bcond_without	apidocs		# gtk-doc based API documentation
%bcond_without	nautilus	# Nautilus extensions

Summary:	Document viewer for multiple document formats
Summary(pl.UTF-8):	Przeglądarka dokumentów w wielu formatach
Name:		evince
Version:	44.3
Release:	1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	https://download.gnome.org/sources/evince/44/%{name}-%{version}.tar.xz
# Source0-md5:	a5ea6d19f083f41086ee363caefaa14f
Patch0:		icon-theme.patch
URL:		https://wiki.gnome.org/Apps/Evince
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	dbus-devel
BuildRequires:	djvulibre-devel >= 3.5.22
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gdk-pixbuf2-devel >= 2.40.0
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gnome-desktop-devel >= 3.0
BuildRequires:	gobject-introspection-devel >= 1.0
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gspell-devel >= 1.6.0
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	gtk+3-devel >= 3.22.0
%{?with_apidocs:BuildRequires:	gi-docgen >= 2021.1}
BuildRequires:	kpathsea-devel
BuildRequires:	libarchive-devel >= 3.6.0
BuildRequires:	libgxps-devel >= 0.2.1
BuildRequires:	libhandy1-devel >= 1.5.0
BuildRequires:	libsecret-devel >= 0.5
BuildRequires:	libspectre-devel >= 0.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel >= 4
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	libxml2-progs >= 1:2.6.31
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja >= 1.5
%{?with_nautilus:BuildRequires:	nautilus3-devel >= 3.28.0}
%{?with_nautilus:BuildRequires:	nautilus3-devel < 42.20}
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 22.02.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 2.029
BuildRequires:	synctex-devel >= 1.19
BuildRequires:	t1lib-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel >= 1.0.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.44.0
Requires:	%{name}-libs = %{version}-%{release}
Requires:	cairo >= 1.10.0
Requires:	dconf
Requires:	gdk-pixbuf2 >= 2.40.0
Requires:	gsettings-desktop-schemas
Requires:	gspell >= 1.6.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	libarchive >= 3.6.0
Requires:	libhandy1 >= 1.5.0
Requires:	libsecret >= 0.5
Requires:	xorg-lib-libSM >= 1.0.0
Suggests:	evince-backend-djvu
Suggests:	evince-backend-dvi
Suggests:	evince-backend-pdf
Suggests:	evince-backend-ps
Suggests:	gtk+3-cups >= 3.22.0
Obsoletes:	browser-plugin-evince < 41
Obsoletes:	evince-gtk < 3.1
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
Requires:	glib2 >= 1:2.44.0
Requires:	gtk+3 >= 3.22.0
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
Requires:	glib2-devel >= 1:2.44.0
Requires:	gtk+3-devel >= 3.22.0

%description devel
Header files for Evince.

%description devel -l pl.UTF-8
Pliki nagłówkowe Evince.

%package apidocs
Summary:	Evince API documentation
Summary(pl.UTF-8):	Dokumentacja API aplikacji Evince
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
Evince API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API aplikacji Evince.

%package -n nautilus3-extension-evince
Summary:	Evince extension for Nautilus 3
Summary(pl.UTF-8):	Rozszerzenie Evince dla Nautilusa 3
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus3 >= 3.28.0
Obsoletes:	nautilus-extension-evince < 43

%description -n nautilus3-extension-evince
This extension shows Evince document properties in Nautilus 3.

%description -n nautilus3-extension-evince -l pl.UTF-8
To rozszerzenie pokazuje właściwości dokumentu Evince w Nautilusie 3.

%package backend-djvu
Summary:	View DjVu documents with Evince
Summary(pl.UTF-8):	Przeglądanie dokumentów DjVu przy użyciu Evince
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	djvulibre >= 3.5.22

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
Requires:	poppler-glib >= 22.02.0

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

%prep
%setup -q
%patch0 -p1

%build
%meson build \
	%{!?with_apidocs:-Dgtk_doc=false} \
	%{?with_nautilus:-Dnautilus=true} \
	-Dps=enabled

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%if %{with apidocs}
install -d $RPM_BUILD_ROOT%{_gidocdir}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/libev* $RPM_BUILD_ROOT%{_gidocdir}
%endif

# not supported by glibc (as of 2.37)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS NEWS-security.md NOTES README.md TODO
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
%{_datadir}/metainfo/org.gnome.Evince.appdata.xml
%{_datadir}/metainfo/evince-comicsdocument.metainfo.xml
%{_datadir}/metainfo/evince-tiffdocument.metainfo.xml
%{_datadir}/dbus-1/services/org.gnome.evince.Daemon.service
%{_datadir}/glib-2.0/schemas/org.gnome.Evince.gschema.xml
%{_datadir}/%{name}
%{_datadir}/thumbnailers/evince.thumbnailer
%{systemduserunitdir}/org.gnome.Evince.service
%{_mandir}/man1/evince.1*
%{_mandir}/man1/evince-previewer.1*
%{_mandir}/man1/evince-thumbnailer.1*
%{_desktopdir}/org.gnome.Evince.desktop
%{_desktopdir}/org.gnome.Evince-previewer.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Evince.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Evince-symbolic.svg

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
%{_gidocdir}/libevdocument
%{_gidocdir}/libevview
%endif

%files backend-djvu
%defattr(644,root,root,755)
%attr(755,root,root) %{backendsdir}/libdjvudocument.so
%{backendsdir}/djvudocument.evince-backend
%{_datadir}/metainfo/evince-djvudocument.metainfo.xml

%files backend-dvi
%defattr(644,root,root,755)
%attr(755,root,root) %{backendsdir}/libdvidocument.so
%{backendsdir}/dvidocument.evince-backend
%{_datadir}/metainfo/evince-dvidocument.metainfo.xml

%files backend-pdf
%defattr(644,root,root,755)
%attr(755,root,root) %{backendsdir}/libpdfdocument.so
%{backendsdir}/pdfdocument.evince-backend
%{_datadir}/metainfo/evince-pdfdocument.metainfo.xml

%files backend-ps
%defattr(644,root,root,755)
%attr(755,root,root) %{backendsdir}/libpsdocument.so
%{backendsdir}/psdocument.evince-backend
%{_datadir}/metainfo/evince-psdocument.metainfo.xml

%files backend-xps
%defattr(644,root,root,755)
%attr(755,root,root) %{backendsdir}/libxpsdocument.so
%{backendsdir}/xpsdocument.evince-backend
%{_datadir}/metainfo/evince-xpsdocument.metainfo.xml

%if %{with nautilus}
%files -n nautilus3-extension-evince
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libevince-properties-page.so
%endif
