Summary:	Document viewer for multiple document formats
Summary(pl):	Przegl±darka dokumentów w wielu formatach
Name:		evince
Version:	0.1.9
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/gnome/sources/evince/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	52a35ea0295ad5acace08ad840286d6a
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-gs8.patch
URL:		http://www.gnome.org/projects/evince/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ghostscript
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gtk+2-devel >= 2:2.6.2
BuildRequires:	intltool
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeprintui-devel
BuildRequires:	libgnomeui-devel >= 2.8.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	poppler-devel >= 0.1.2
Requires(post):	GConf2
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
	--enable-a4-paper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
%gconf_schema_install
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*.schemas
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
