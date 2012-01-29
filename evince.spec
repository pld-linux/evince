# TODO
# - evince.desktop provides mimetypes for all possible choices, yet some of
#   them are in subpackages (backend-foo). multiple .desktop files is possible
#   for same application?
#
# Conditional build:
%bcond_without	dbus		# disable DBUS support
%bcond_without	apidocs		# disable gtk-doc

Summary:	Document viewer for multiple document formats
Summary(pl.UTF-8):	Przeglądarka dokumentów w wielu formatach
Name:		evince
Version:	3.2.1
Release:	7
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evince/3.2/%{name}-%{version}.tar.xz
# Source0-md5:	8c01b6741709b8e32b800b71820648ac
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-linking.patch
URL:		http://www.gnome.org/projects/evince/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.10
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	djvulibre-devel >= 3.5.17
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gnome-icon-theme >= 3.2.0
BuildRequires:	gobject-introspection-devel >= 0.6.0
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk+3-devel >= 3.0.2
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.13}
BuildRequires:	intltool >= 0.40.0
BuildRequires:	kpathsea-devel
BuildRequires:	libgnome-keyring-devel >= 2.26.0
BuildRequires:	libgxps-devel >= 0.0.1
BuildRequires:	libspectre-devel >= 0.2.0
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	nautilus-devel >= 3.0.0
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.16.0
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	t1lib-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	dconf
Requires:	gnome-icon-theme >= 3.2.0
Requires:	gsettings-desktop-schemas
Requires:	gtk+3 >= 3.0.2
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Suggests:	evince-backend-djvu
Suggests:	evince-backend-dvi
Suggests:	evince-backend-pdf
Suggests:	evince-backend-ps
Suggests:	gtk+3-cups
Conflicts:	evince-gtk
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		backendsdir	%{_libdir}/evince/3/backends

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
Requires:	gtk+3-devel >= 3.0.2

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
Shows Evince document properties in Nautilus.

%description -n nautilus-extension-evince -l pl.UTF-8
Pokazuje właściwości dokumentu Evince w Nautilusie.

%package backend-djvu
Summary:	View DJVu documents with Evince
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	djvulibre >= 3.5.17

%description backend-djvu
View DJVu documents with Evince.

%package backend-dvi
Summary:	View DVI documents with Evince
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description backend-dvi
View DVI documents with Evince.

%package backend-pdf
Summary:	View PDF documents with Evince
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	poppler-glib >= 0.16.0

%description backend-pdf
View PDF documents with Evince.

%package backend-ps
Summary:	View Postscript documents with Evince
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description backend-ps
View Postscript documents with Evince.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
	--disable-silent-rules \
	--enable-comics \
	--enable-djvu \
	--enable-dvi \
	--enable-introspection \
	--enable-t1lib \
	--enable-nautilus \
	--enable-pdf \
	--enable-tiff \
	--with-smclient=xsmp \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{backendsdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-3.0/*.la

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_desktop_database_post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
/sbin/ldconfig
%update_desktop_database_postun
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/evince
%attr(755,root,root) %{_bindir}/evince-previewer
%attr(755,root,root) %{_bindir}/evince-thumbnailer
%attr(755,root,root) %{_libexecdir}/evinced
%attr(755,root,root) %{_libdir}/libevdocument3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libevdocument3.so.3
%attr(755,root,root) %{_libdir}/libevview3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libevview3.so.3
%dir %{_libdir}/evince
%dir %{_libdir}/evince/3
%dir %{backendsdir}
%attr(755,root,root) %{backendsdir}/libcomicsdocument.so
%{backendsdir}/comicsdocument.evince-backend
%attr(755,root,root) %{backendsdir}/libtiffdocument.so
%{backendsdir}/tiffdocument.evince-backend
%attr(755,root,root) %{backendsdir}/libxpsdocument.so
%{backendsdir}/xpsdocument.evince-backend
%{_datadir}/GConf/gsettings/evince.convert
%{_datadir}/dbus-1/services/org.gnome.evince.Daemon.service
%{_datadir}/glib-2.0/schemas/org.gnome.Evince.gschema.xml
%{_datadir}/%{name}
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/evince.thumbnailer
%{_mandir}/man1/evince.1*
%{_desktopdir}/evince.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_libdir}/girepository-1.0/*.typelib

%files backend-djvu
%defattr(644,root,root,755)
%attr(755,root,root) %{backendsdir}/libdjvudocument.so
%{backendsdir}/djvudocument.evince-backend

%files backend-dvi
%defattr(644,root,root,755)
%attr(755,root,root) %{backendsdir}/libdvidocument.so
%{backendsdir}/dvidocument.evince-backend

%files backend-ps
%defattr(644,root,root,755)
%attr(755,root,root) %{backendsdir}/libpsdocument.so
%{backendsdir}/psdocument.evince-backend

%files backend-pdf
%defattr(644,root,root,755)
%attr(755,root,root) %{backendsdir}/libpdfdocument.so
%{backendsdir}/pdfdocument.evince-backend

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libevdocument3.so
%attr(755,root,root) %{_libdir}/libevview3.so
%{_includedir}/evince
%{_pkgconfigdir}/evince-document-*.pc
%{_pkgconfigdir}/evince-view-*.pc
%{_datadir}/gir-1.0/*.gir

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/evince
%{_gtkdocdir}/libevdocument-*
%{_gtkdocdir}/libevview-*
%endif

%files -n nautilus-extension-evince
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libevince-properties-page.so
