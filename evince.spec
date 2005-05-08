Summary:	Document viewer for multiple document formats
Summary(pl):	Przegl±darka dokumentów w wielu formatach
Name:		evince
Version:	0.3.0
Release:	2
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/gnome/sources/evince/0.3/%{name}-%{version}.tar.bz2
# Source0-md5:	33e760db0295b393864b969f3b62a52a
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-gs8.patch
URL:		http://www.gnome.org/projects/evince/
BuildRequires:	GConf2-devel >= 2.10.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	djvulibre-devel
BuildRequires:	ghostscript
BuildRequires:	gnome-vfs2-devel >= 2.10.0-2
BuildRequires:	gtk+2-devel >= 2:2.6.4
BuildRequires:	intltool
BuildRequires:	kpathsea-devel
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeprintui-devel >= 2.10.0
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.3.1
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Evince is a document viewer for multiple document formats like pdf,
postscript, and many others. The goal of evince is to replace the
multiple document viewers that exist on the GNOME Desktop, like ggv,
gpdf, and xpdf with a single simple application.

%description -l pl
Evince jest przegl±dark± dokumentów w wielu formatach takich jak pdf,
postscript i wielu innych. W zamierzeniach program ma zast±piæ
przegl±darki dokumentów dla ¶rodowiska GNOME, takie jak ggv, gpdf i
xpdf jedn± prost± aplikacj±.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install \
	--enable-a4-paper \
	--enable-djvu \
	--enable-dvi

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install evince-thumbnailer.schemas
%gconf_schema_install evince.schemas
%update_desktop_database_post
%scrollkeeper_update_post

%preun
%gconf_schema_uninstall evince-thumbnailer.schemas
%gconf_schema_uninstall evince.schemas

%postun
%update_desktop_database_postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*.schemas
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_omf_dest_dir}/evince
