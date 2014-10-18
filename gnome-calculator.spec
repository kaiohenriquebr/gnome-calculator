%define url_ver %(echo %{version} | cut -d. -f1,2)

Name:		gnome-calculator
Version:	3.14.0
Release:	%mkrel 2
Summary:	GNOME Desktop calculator
Group:		Graphical desktop/GNOME
License:	GPLv2+
URL:		https://wiki.gnome.org/Calculator
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtksourceview-3.0)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
Provides:	gcalctool = %{version}
Obsoletes:	gcalctool <= 6.6.2

%description
Calculator is an application that solves mathematical equations and is
suitable as a default application in a Desktop environment.

What Calculator is:
- A tool for calculating mathematical equations.
- Uses standard mathematical notation where possible.
- Easy enough to use for simple maths.
- Powerful enough for mid-level mathematics.
- Fast to load and responsive to input.
- Appropriately sized to fit into standard screen resolutions.
- Fully accessible.
- Well documented.
- Integrated into the GNOME Desktop.

What Calculator is not:
- It does not emulate any existing calculator interfaces, hardware or software.
- It is not a power-tool for professional mathematicians.
- It is not a programming language.

%prep
%setup -q
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome --with-help --all-name

%files -f %{name}.lang
%doc COPYING NEWS
%{_bindir}/gcalccmd
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.calculator.gschema.xml
%{_datadir}/dbus-1/services/org.gnome.Calculator.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/%{name}-search-provider.ini
%{_datadir}/appdata/%{name}.appdata.xml
%doc %{_mandir}/man1/%{name}.1.*
%doc %{_mandir}/man1/gcalccmd.1*
/usr/libexec/%{name}-search-provider


%changelog
* Wed Oct 15 2014 umeabot <umeabot> 3.14.0-2.mga5
+ Revision: 751160
- Second Mageia 5 Mass Rebuild

* Mon Sep 22 2014 ovitters <ovitters> 3.14.0-1.mga5
+ Revision: 719200
- new version 3.14.0
- new version 3.13.92

  + umeabot <umeabot>
    - Mageia 5 Mass Rebuild

* Tue Aug 19 2014 ovitters <ovitters> 3.13.90-1.mga5
+ Revision: 665373
- new version 3.13.90

* Wed Jul 23 2014 ovitters <ovitters> 3.13.3-1.mga5
+ Revision: 655750
- new version 3.13.3
- dropped merged patch 1

* Thu May 29 2014 ovitters <ovitters> 3.13.2-1.mga5
+ Revision: 627412
- add patch to fix km desktop file
- new version 3.13.2

* Wed May 28 2014 ovitters <ovitters> 3.12.2-1.mga5
+ Revision: 627384
- new version 3.12.2

* Wed Apr 09 2014 ovitters <ovitters> 3.12.1-1.mga5
+ Revision: 613122
- new version 3.12.1

* Mon Mar 24 2014 ovitters <ovitters> 3.12.0-1.mga5
+ Revision: 608006
- new version 3.12.0

* Mon Mar 17 2014 ovitters <ovitters> 3.11.92-1.mga5
+ Revision: 604419
- new version 3.11.92

* Wed Mar 05 2014 ovitters <ovitters> 3.11.91-1.mga5
+ Revision: 600125
- new version 3.11.91

* Tue Feb 18 2014 ovitters <ovitters> 3.11.90-1.mga5
+ Revision: 594135
- new version 3.11.90

* Wed Feb 05 2014 dams <dams> 3.11.5-1.mga5
+ Revision: 583032
- new version 3.11.5

* Mon Nov 11 2013 ovitters <ovitters> 3.10.2-1.mga4
+ Revision: 550450
- new version 3.10.2

* Sun Nov 10 2013 tmb <tmb> 3.10.1-3.mga4
+ Revision: 550405
- dont conflict on virtual provide gcalctool

* Sat Nov 09 2013 ovitters <ovitters> 3.10.1-2.mga4
+ Revision: 550157
- fix url

* Wed Oct 23 2013 dams <dams> 3.10.1-1.mga4
+ Revision: 546528
- add back a patch for bad po file (nl)
- remove useless patch (merged upstream - translation)

  + ovitters <ovitters>
    - add patch to fix nl keyword translation in desktop file
    - new version 3.10.1

* Sun Oct 20 2013 umeabot <umeabot> 3.10.0-2.mga4
+ Revision: 536819
- Mageia 4 Mass Rebuild

* Tue Sep 24 2013 ovitters <ovitters> 3.10.0-1.mga4
+ Revision: 485711
- new version 3.10.0

* Tue Sep 17 2013 fwang <fwang> 3.9.92-1.mga4
+ Revision: 480779
- update file list

  + ovitters <ovitters>
    - new version 3.9.92

* Mon Aug 26 2013 ovitters <ovitters> 3.9.90-1.mga4
+ Revision: 471869
- new version 3.9.90

* Thu Jul 25 2013 dams <dams> 3.9.4-1.mga4
+ Revision: 458049
- new version 3.9.4

* Thu May 30 2013 dams <dams> 3.8.2-1.mga4
+ Revision: 432967
- imported package gnome-calculator

