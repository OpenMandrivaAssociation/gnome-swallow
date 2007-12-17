%define name 	gnome-swallow
%define version 1.2
%define release %mkrel 2

Summary: 	Embeds small programs into the GNOME panel
Name: 		%name
Version: 	%version
Release: 	%release
License: 	GPL
URL:		http://www-unix.oit.umass.edu/~tetron/technology/swallow/
Group: 		Graphical desktop/GNOME
Source: 	%{name}-%{version}.tar.bz2
BuildRequires: 	gnome-panel-devel

%description
An applet for GNOME2 that allows any small application to be embedded into
the panel.  In this case embedded means physically shrunk into the panel, not
just an icon or an applet.

%prep
%setup -q

%build
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


