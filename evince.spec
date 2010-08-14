#
# Conditional build:
%bcond_without	dbus		# disable DBUS support
%bcond_without	apidocs		# disable gtk-doc
#
Summary:	Document viewer for multiple document formats
Summary(pl.UTF-8):	Przeglądarka dokumentów w wielu formatach
Name:		evince
Version:	2.30.3
Release:	3
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evince/2.30/%{name}-%{version}.tar.bz2
# Source0-md5:	516748897113cd4e9638c49245c555c2
URL:		http://www.gnome.org/projects/evince/
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.10
%{?with_dbus:BuildRequires:	dbus-glib-devel >= 0.74}
BuildRequires:	djvulibre-devel >= 3.5.17
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.20.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gnome-icon-theme >= 2.26.0
BuildRequires:	gtk+2-devel >= 2:2.16.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.13}
BuildRequires:	intltool >= 0.40.0
BuildRequires:	kpathsea-devel
BuildRequires:	libgnome-keyring-devel >= 2.26.0
BuildRequires:	libspectre-devel >= 0.2.0
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	nautilus-devel >= 2.26.0
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.12.0
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
BuildRequires:	t1lib-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	gtk+2 >= 2:2.16.0
Suggests:	evince-backend-djvu
Suggests:	evince-backend-dvi
Suggests:	evince-backend-pdf
Suggests:	evince-backend-ps
Conflicts:	evince-gtk
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		backendsdir	%{_libdir}/evince/2/backends

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

%package devel
Summary:	Header files for Evince
Summary(pl.UTF-8):	Pliki nagłówkowe Evince
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.16.0

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
Requires:	nautilus >= 2.26.0

%description -n nautilus-extension-evince
Shows Evince document properties in Nautilus.

%description -n nautilus-extension-evince -l pl.UTF-8
Pokazuje właściwości dokumentu Evince w Nautilusie.

%package backend-djvu
Summary:	View DJVu documents with Evince
Group:		X11/Applications
Requires(post,preun):	GConf2
Requires:	%{name} = %{version}-%{release}
Requires:	djvulibre >= 3.5.17

%description backend-djvu
View DJVu documents with Evince.

%package backend-dvi
Summary:	View DVI documents with Evince
Group:		X11/Applications
Requires(post,preun):	GConf2
Requires:	%{name} = %{version}-%{release}

%description backend-dvi
View DVI documents with Evince.

%package backend-pdf
Summary:	View PDF documents with Evince
Group:		X11/Applications
Requires(post,preun):	GConf2
Requires:	%{name} = %{version}-%{release}
Requires:	poppler-glib >= 0.12.0

%description backend-pdf
View PDF documents with Evince.

%package backend-ps
Summary:	View Postscript documents with Evince
Group:		X11/Applications
Requires(post,preun):	GConf2
Requires:	%{name} = %{version}-%{release}

%description backend-ps
View Postscript documents with Evince.

%prep
%setup -q
sed -i s#^en@shaw## po/LINGUAS
rm po/en@shaw.po

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_apidocs:--enable-gtk-doc} \
	--disable-static \
	--disable-schemas-install \
	--disable-silent-rules \
	--enable-comics \
	--enable-djvu \
	--enable-dvi \
	--enable-impress \
	--enable-t1lib \
	--enable-nautilus \
	--enable-pdf \
	--enable-pixbuf \
	--enable-tiff \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{backendsdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0/*.la

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%gconf_schema_install evince.schemas
%gconf_schema_install evince-thumbnailer-comics.schemas
%gconf_schema_install evince-thumbnailer.schemas
%update_desktop_database_post
%scrollkeeper_update_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall evince.schemas
%gconf_schema_uninstall evince-thumbnailer-comics.schemas
%gconf_schema_uninstall evince-thumbnailer.schemas

%postun
/sbin/ldconfig
%update_desktop_database_postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post backend-djvu
%gconf_schema_install evince-thumbnailer-djvu.schemas

%preun backend-djvu
%gconf_schema_uninstall evince-thumbnailer-djvu.schemas

%post backend-dvi
%gconf_schema_install evince-thumbnailer-dvi.schemas

%preun backend-dvi
%gconf_schema_uninstall evince-thumbnailer-dvi.schemas

%post backend-ps
%gconf_schema_install evince-thumbnailer-ps.schemas

%preun backend-ps
%gconf_schema_uninstall evince-thumbnailer-ps.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/evince
%attr(755,root,root) %{_bindir}/evince-previewer
%attr(755,root,root) %{_bindir}/evince-thumbnailer
%attr(755,root,root) %{_libdir}/evince-convert-metadata
%attr(755,root,root) %{_libdir}/evinced
%attr(755,root,root) %{_libdir}/libevdocument.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libevdocument.so.2
%attr(755,root,root) %{_libdir}/libevview.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libevview.so.2
%dir %{_libdir}/evince
%dir %{_libdir}/evince/2
%dir %{backendsdir}
%attr(755,root,root) %{backendsdir}/libcomicsdocument.so
%{backendsdir}/comicsdocument.evince-backend
%attr(755,root,root) %{backendsdir}/libimpressdocument.so
%{backendsdir}/impressdocument.evince-backend
%attr(755,root,root) %{backendsdir}/libpixbufdocument.so
%{backendsdir}/pixbufdocument.evince-backend
%attr(755,root,root) %{backendsdir}/libtiffdocument.so
%{backendsdir}/tiffdocument.evince-backend
%{_sysconfdir}/gconf/schemas/evince.schemas
%{_sysconfdir}/gconf/schemas/evince-thumbnailer-comics.schemas
%{_sysconfdir}/gconf/schemas/evince-thumbnailer.schemas
%{_datadir}/dbus-1/services/org.gnome.evince.Daemon.service
%{_datadir}/%{name}
%{_mandir}/man1/evince.1*
%{_desktopdir}/evince.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg

%files backend-djvu
%defattr(644,root,root,755)
%attr(755,root,root) %{backendsdir}/libdjvudocument.so
%{backendsdir}/djvudocument.evince-backend
%{_sysconfdir}/gconf/schemas/evince-thumbnailer-djvu.schemas

%files backend-dvi
%defattr(644,root,root,755)
%attr(755,root,root) %{backendsdir}/libdvidocument.so
%{backendsdir}/dvidocument.evince-backend
%{_sysconfdir}/gconf/schemas/evince-thumbnailer-dvi.schemas

%files backend-ps
%defattr(644,root,root,755)
%attr(755,root,root) %{backendsdir}/libpsdocument.so
%{backendsdir}/psdocument.evince-backend
%{_sysconfdir}/gconf/schemas/evince-thumbnailer-ps.schemas

%files backend-pdf
%defattr(644,root,root,755)
%attr(755,root,root) %{backendsdir}/libpdfdocument.so
%{backendsdir}/pdfdocument.evince-backend

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libevdocument.so
%attr(755,root,root) %{_libdir}/libevview.so
%{_libdir}/libevdocument.la
%{_libdir}/libevview.la
%{_includedir}/evince
%{_pkgconfigdir}/evince-document-*.pc
%{_pkgconfigdir}/evince-view-*.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/evince
%{_gtkdocdir}/libevdocument-*
%{_gtkdocdir}/libevview-*
%endif

%files -n nautilus-extension-evince
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-2.0/libevince-properties-page.so
