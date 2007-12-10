%define release %mkrel 1

%define nameorig xcircuit
%define version 3.4.26

Summary: Electronic circuit schematic drawing program
Name: %{nameorig}-tcl
Version: %{version}
Release: %{release}
License: GPL
Group: Sciences/Other
Source0: 	%{nameorig}-%{version}.tar.bz2
Source1:	%{nameorig}.16.png
Source2:	%{nameorig}.32.png
Source3:	%{nameorig}.48.png
URL: http://opencircuitdesign.com/xcircuit
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: tcl >= 8.4.11 tk >= 8.4.11
BuildRequires: tcl-devel >= 8.4.11 tk-devel >= 8.4.11
BuildRequires: libxpm-devel
BuildRequires: X11-devel
Obsoletes: %{nameorig} %{nameorig}-python
Provides: %{nameorig} %{nameorig}-python

%description
Xcircuit is a general-purpose drawing program and also a specific-purpose
CAD program for circuit schematic drawing and schematic capture.  Output
is PostScript.  TCL scripting is available.

%prep
%setup -q -n %{nameorig}-%{version}

%build
%configure --with-tcl --with-tcllibs=%{_libdir} --with-tklibs=%{_libdir}
%make tcl

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Mandrake Menu entry
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat <<EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): \
needs="x11" \
section="More Applications/Sciences/Electricity" \
title="XCircuit" \
longtitle="Electronic circuit schematic drawing program" \
command="/usr/bin/xcircuit" needs="X11" \
icon="%{name}.png"\
xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=XCircuit
Comment=%{summary}
Exec=%{_bindir}/xcircuit
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Sciences-Electricity;Science;Electronics;
EOF

mkdir -p $RPM_BUILD_ROOT%{_miconsdir} $RPM_BUILD_ROOT%{_liconsdir} $RPM_BUILD_ROOT%{_iconsdir}
cp %{SOURCE1}  $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
cp %{SOURCE2}  $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
cp %{SOURCE3}  $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

chmod 644 $RPM_BUILD_ROOT/%{_prefix}/lib/xcircuit-3.4/console.tcl

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -Rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYRIGHT README README.notes README.ISOLatin2 lib/pixmaps/xcircuit.xpm
%{_bindir}/xcircuit
%{_prefix}/lib/xcircuit-3.4
%{_iconsdir}/%{name}.*
%{_miconsdir}/%{name}.*
%{_liconsdir}/%{name}.*
%{_menudir}/%{name}
%{_datadir}/applications/*.desktop

