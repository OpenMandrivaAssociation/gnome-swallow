%define name 	gnome-swallow
%define version 1.2
%define release %mkrel 7

Summary: 	Embeds small programs into the GNOME panel
Name: 		%name
Version: 	%version
Release: 	%release
License: 	GPL
URL:		https://www-unix.oit.umass.edu/~tetron/technology/swallow/
Group: 		Graphical desktop/GNOME
Source: 	%{name}-%{version}.tar.bz2
Patch0:		gnome-swallow-1.2-as-needed.patch
Patch1:		gnome-swallow-1.2-libgnomeui-flags.patch
Patch2:		gnome-swallow-1.2-qa-warning.patch
Buildroot: 	%_tmppath/%{name}-root
BuildRequires: 	gnome-panel-devel
BuildRequires:	gnomeui2-devel

%description
An applet for GNOME2 that allows any small application to be embedded into
the panel.  In this case embedded means physically shrunk into the panel, not
just an icon or an applet.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoreconf -f -i
%configure2_5x
%make

%install
%makeinstall
rm -fr %buildroot/%_docdir/*
%if %_lib != lib
mv %buildroot%_prefix/lib %buildroot%_libdir
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING README ChangeLog
%{_libdir}/bonobo/servers/GNOME_Swallow.server
%{_libdir}/gnome-panel/gnome_swallow


