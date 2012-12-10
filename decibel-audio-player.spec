%define	name	decibel-audio-player
%define	version 1.07
%define rel	1
%define	release	%mkrel %rel

Name:		%{name}
Summary:	A clean and user-friendly audio player
Version:	%{version} 
Release:	%{release} 
Source0:	http://decibel.silent-blade.org/uploads/Main/%{name}-%{version}.tar.gz
URL:		http://decibel.silent-blade.org/
Group:		Sound
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPLv2+
Requires:	pygtk2.0 gstreamer0.10-python pygtk2.0-libglade
Requires:	gstreamer0.10-plugins-good gstreamer0.10-plugins-base 
Requires:	gstreamer0.10-plugins-ugly python-pyxml
Requires:	mutagen
Requires:	python-notify
BuildArch:	noarch

%description
Decibel is a GTK+ audio player designed for GNU/Linux, which aims at
being very straightforward to use by means of a very clean and user
friendly interface. Decibel is especially targeted at Gnome and will
follow the Gnome HIG as closely as possible.

It does not include features that generally have had better support
in specialized software, e.g. tagging.

%prep
%setup -q -n %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=%{buildroot} prefix=%{_prefix}

# Move icons to correct dir
mkdir -p %buildroot/%{_iconsdir}
mv %buildroot/%{_datadir}/pixmaps/* %buildroot/%{_iconsdir}/

%find_lang %name

%if %mdkversion < 200900
%post
%update_desktop_database
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_desktop_database
%update_menus
%endif

%clean 
rm -rf $RPM_BUILD_ROOT 

%files -f %name.lang
%defattr(-,root,root)
%doc ./doc/ChangeLog
%_bindir/*
%_datadir/%name/
%_datadir/applications/*
%_iconsdir/*
%{_mandir}/*/*


%changelog
* Sun Mar 06 2011 Funda Wang <fwang@mandriva.org> 1.07-1mdv2011.0
+ Revision: 642252
- update to new version 1.07

* Thu Nov 18 2010 Funda Wang <fwang@mandriva.org> 1.06-1mdv2011.0
+ Revision: 598534
- update to new version 1.06

* Sat Jul 17 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.05-1mdv2011.0
+ Revision: 554545
- update to new version 1.05

* Tue Jan 12 2010 Funda Wang <fwang@mandriva.org> 1.03-1mdv2010.1
+ Revision: 490251
- new version 1.03

* Sun Nov 29 2009 Funda Wang <fwang@mandriva.org> 1.02-1mdv2010.1
+ Revision: 471357
- new version 1.02

* Thu Oct 01 2009 Funda Wang <fwang@mandriva.org> 1.01-1mdv2010.0
+ Revision: 451927
- New version 1.01

* Sun Nov 23 2008 Funda Wang <fwang@mandriva.org> 1.00-1mdv2009.1
+ Revision: 305983
- New version 1.00

* Thu Aug 21 2008 Funda Wang <fwang@mandriva.org> 0.11-1mdv2009.0
+ Revision: 274523
- New version 0.11
- drop patch merged upstream

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue May 13 2008 Funda Wang <fwang@mandriva.org> 0.10-1mdv2009.0
+ Revision: 206539
- update to new version 0.10

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Sun Jan 27 2008 Funda Wang <fwang@mandriva.org> 0.09-1mdv2008.1
+ Revision: 158779
- New version 0.09

* Mon Dec 31 2007 Funda Wang <fwang@mandriva.org> 0.08-1mdv2008.1
+ Revision: 139810
- New versioin 0.08

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 18 2007 Funda Wang <fwang@mandriva.org> 0.07-1mdv2008.1
+ Revision: 109895
- update to new version 0.07

* Sat Oct 20 2007 Funda Wang <fwang@mandriva.org> 0.06.3-1mdv2008.1
+ Revision: 100582
- add missing patch
- New version 0.06.3

* Fri Aug 10 2007 Funda Wang <fwang@mandriva.org> 0.05-1mdv2008.0
+ Revision: 61584
- New version 0.05

* Sat Jul 07 2007 Eskild Hustvedt <eskild@mandriva.org> 0.04-1mdv2008.0
+ Revision: 49411
- New version 0.04

* Mon Jun 11 2007 Eskild Hustvedt <eskild@mandriva.org> 0.03-1mdv2008.0
+ Revision: 38068
- Initial Mandriva Linux package
- Import decibel-audio-player

