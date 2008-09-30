#
# Conditional build:
%bcond_without	dbus		# disable DBUS support
%bcond_without	apidocs		# disable gtk-doc
#
Summary:	Document viewer for multiple document formats
Summary(pl.UTF-8):	Przeglądarka dokumentów w wielu formatach
Name:		evince
Version:	2.24.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evince/2.24/%{name}-%{version}.tar.bz2
# Source0-md5:	7d0f9850b0f33267d3977532f027ac95
URL:		http://www.gnome.org/projects/evince/
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
%{?with_dbus:BuildRequires:	dbus-glib-devel >= 0.74}
BuildRequires:	djvulibre-devel >= 3.5.17
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.18.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gnome-keyring-devel >= 2.24.0
BuildRequires:	gnome-icon-theme >= 2.24.0
BuildRequires:	gtk+2-devel >= 2:2.14.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.9}
BuildRequires:	intltool >= 0.40.0
BuildRequires:	kpathsea-devel
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libspectre-devel >= 0.2.0
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	nautilus-devel >= 2.24.0
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.8.0
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
BuildRequires:	t1lib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	djvulibre >= 3.5.17
Requires:	gtk+2 >= 2:2.14.0
Requires:	poppler-glib >= 0.8.0
Conflicts:	evince-gtk
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		backendsdir	%{_libdir}/evince/backends

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
Requires:	gtk+2-devel >= 2:2.14.0

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
Requires:	nautilus >= 2.24.0

%description -n nautilus-extension-evince
Shows Evince document properties in Nautilus.

%description -n nautilus-extension-evince -l pl.UTF-8
Pokazuje właściwości dokumentu Evince w Nautilusie.

%prep
%setup -q

%build
%{__gnome_doc_prepare}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_apidocs:--enable-gtk-doc} \
	--disable-static \
	--disable-schemas-install \
	--enable-comics \
	--enable-djvu \
	--enable-dvi \
	--enable-impress \
	--enable-t1lib \
	--enable-nautilus \
	--enable-pdf \
	--enable-pixbuf \
	--enable-tiff \
	--with-print=gtk \
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
%gconf_schema_install evince-thumbnailer-djvu.schemas
%gconf_schema_install evince-thumbnailer-dvi.schemas
%gconf_schema_install evince-thumbnailer.schemas
%gconf_schema_install evince-thumbnailer-ps.schemas
%update_desktop_database_post
%scrollkeeper_update_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall evince.schemas
%gconf_schema_uninstall evince-thumbnailer-comics.schemas
%gconf_schema_uninstall evince-thumbnailer-djvu.schemas
%gconf_schema_uninstall evince-thumbnailer-dvi.schemas
%gconf_schema_uninstall evince-thumbnailer.schemas
%gconf_schema_uninstall evince-thumbnailer-ps.schemas

%postun
/sbin/ldconfig
%update_desktop_database_postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/evince
%attr(755,root,root) %{_bindir}/evince-thumbnailer
%attr(755,root,root) %{_libdir}/libevbackend.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libevbackend.so.0
%dir %{_libdir}/evince
%dir %{backendsdir}
%attr(755,root,root) %{backendsdir}/libcomicsdocument.so
%{backendsdir}/comicsdocument.evince-backend
%attr(755,root,root) %{backendsdir}/libdjvudocument.so
%{backendsdir}/djvudocument.evince-backend
%attr(755,root,root) %{backendsdir}/libdvidocument.so*
%{backendsdir}/dvidocument.evince-backend
%attr(755,root,root) %{backendsdir}/libimpressdocument.so
%{backendsdir}/impressdocument.evince-backend
%attr(755,root,root) %{backendsdir}/libpdfdocument.so
%{backendsdir}/pdfdocument.evince-backend
%attr(755,root,root) %{backendsdir}/libpixbufdocument.so
%{backendsdir}/pixbufdocument.evince-backend
%attr(755,root,root) %{backendsdir}/libpsdocument.so
%{backendsdir}/psdocument.evince-backend
%attr(755,root,root) %{backendsdir}/libtiffdocument.so
%{backendsdir}/tiffdocument.evince-backend
%{_sysconfdir}/gconf/schemas/evince.schemas
%{_sysconfdir}/gconf/schemas/evince-thumbnailer-comics.schemas
%{_sysconfdir}/gconf/schemas/evince-thumbnailer-djvu.schemas
%{_sysconfdir}/gconf/schemas/evince-thumbnailer-dvi.schemas
%{_sysconfdir}/gconf/schemas/evince-thumbnailer-ps.schemas
%{_sysconfdir}/gconf/schemas/evince-thumbnailer.schemas
%{_datadir}/%{name}
%{_mandir}/man1/evince.1*
%{_desktopdir}/evince.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libevbackend.so
%{_libdir}/libevbackend.la
%{_includedir}/evince-2.20

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/evince
%endif

%files -n nautilus-extension-evince
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-2.0/libevince-properties-page.so
