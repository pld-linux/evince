#
# TODO: fix t1lib build time misdetection (very low prio)
#
# Conditional build:
%bcond_without	dbus	# enable DBUS support
#
Summary:	Document viewer for multiple document formats
Summary(pl.UTF-8):   Przeglądarka dokumentów w wielu formatach
Name:		evince
Version:	0.7.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/gnome/sources/evince/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	1288d21b183127af36dd58158caa59b5
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-gs8.patch
URL:		http://www.gnome.org/projects/evince/
BuildRequires:	GConf2-devel >= 2.16.0
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_dbus:BuildRequires:	dbus-glib-devel >= 0.71}
BuildRequires:	djvulibre-devel >= 3.5.17
BuildRequires:	ghostscript
BuildRequires:	gnome-doc-utils >= 0.8.0
BuildRequires:	gnome-icon-theme >= 2.17.1
BuildRequires:	gnome-vfs2-devel >= 2.16.1
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	intltool >= 0.35.0
BuildRequires:	kpathsea-devel
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.16.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libxslt-progs >= 1.1.17
BuildRequires:	nautilus-devel >= 2.16.1
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.5.4
BuildRequires:	python-libxml2
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,preun):	GConf2
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2 >= 2:2.10.6
Requires(post,postun):	scrollkeeper
Requires:	cairo >= 1.2.4
Requires:	djvulibre >= 3.5.17
Requires:	gtk+2 >= 2:2.10.6
Requires:	libgnomeui >= 2.16.1
Requires:	poppler-glib >= 0.5.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package -n nautilus-extension-evince
Summary:	Evince extension for Nautilus
Summary(pl.UTF-8):   Rozszerzenie Evince dla Nautilusa
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus >= 2.16.1

%description -n nautilus-extension-evince
Shows Evince document properties in Nautilus.

%description -n nautilus-extension-evince -l pl.UTF-8
Pokazuje właściwości dokumentu Evince w Nautilusie.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gnome_doc_prepare}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--disable-schemas-install \
	--enable-comics \
	%{?with_dbus:--enable-dbus} \
	--enable-djvu \
	--enable-dvi \
	--enable-impress \
	--enable-nautilus \
	--enable-pixbuf \
	--enable-tiff \
	--with-print=gtk
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-1.0/*.la

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install evince.schemas
%gconf_schema_install evince-thumbnailer-comics.schemas
%gconf_schema_install evince-thumbnailer-djvu.schemas
%gconf_schema_install evince-thumbnailer-dvi.schemas
%gconf_schema_install evince-thumbnailer.schemas
%update_desktop_database_post
%scrollkeeper_update_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall evince.schemas
%gconf_schema_uninstall evince-thumbnailer-comics.schemas
%gconf_schema_uninstall evince-thumbnailer-djvu.schemas
%gconf_schema_uninstall evince-thumbnailer-dvi.schemas
%gconf_schema_uninstall evince-thumbnailer.schemas

%postun
%update_desktop_database_postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/evince.schemas
%{_sysconfdir}/gconf/schemas/evince-thumbnailer-comics.schemas
%{_sysconfdir}/gconf/schemas/evince-thumbnailer-djvu.schemas
%{_sysconfdir}/gconf/schemas/evince-thumbnailer-dvi.schemas
%{_sysconfdir}/gconf/schemas/evince-thumbnailer.schemas
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/*/*/*/*
%{_omf_dest_dir}/evince

%files -n nautilus-extension-evince
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/*.so*
