%define release %mkrel 6

%define nameorig xcircuit
%define version 3.4.30

Summary: Electronic circuit schematic drawing program
Name: %{nameorig}-tcl
Version: %{version}
Release: %{release}
License: GPLv2+
Group: Sciences/Other
URL: http://opencircuitdesign.com/xcircuit
Source0: 	http://opencircuitdesign.com/xcircuit/archive/%{nameorig}-%{version}.tgz
Source1:	%{nameorig}.16.png
Source2:	%{nameorig}.32.png
Source3:	%{nameorig}.48.png
Patch0:		xcircuit-fix-linkage.patch
Patch1:		xcircuit-3.4.30-fix-format-errors.patch
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: tcl >= 8.4.11 tk >= 8.4.11
BuildRequires: tcl-devel >= 8.4.11 tk-devel >= 8.4.11
BuildRequires: libxpm-devel
BuildRequires: X11-devel
Obsoletes: %{nameorig} %{nameorig}-python
Provides: %{nameorig} %{nameorig}-python
Requires: tcl >= 8.4.11
Requires: tk >= 8.4.11

%description
Xcircuit is a general-purpose drawing program and also a specific-purpose
CAD program for circuit schematic drawing and schematic capture.  Output
is PostScript.  TCL scripting is available.

%prep
%setup -q -n %{nameorig}-%{version}
%patch0 -p0
%patch1 -p1

%build
autoreconf
%configure2_5x --with-tcl --with-tcllibs=%{_libdir} --with-tklibs=%{_libdir}
%make tcl

%install
rm -rf %buildroot
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=XCircuit
Comment=%{summary}
Exec=%{_bindir}/xcircuit
Icon=%{name}
Terminal=false
Type=Application
Categories=Electronics
EOF

mkdir -p $RPM_BUILD_ROOT%{_miconsdir} $RPM_BUILD_ROOT%{_liconsdir} $RPM_BUILD_ROOT%{_iconsdir}
cp %{SOURCE1}  $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
cp %{SOURCE2}  $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
cp %{SOURCE3}  $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

chmod 644 $RPM_BUILD_ROOT/%{_prefix}/lib/xcircuit-3.4/console.tcl

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

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
%{_datadir}/applications/*.desktop
