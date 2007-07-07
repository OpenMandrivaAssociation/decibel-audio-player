%define	name	decibel-audio-player
%define	version 0.04
%define realver %version
%define rel	1
%define	release	%mkrel %rel

Name:		%{name}
Summary:	A clean and user-friendly audio player
Version:	%{version} 
Release:	%{release} 
Source0:	%{name}-%{realver}.tar.bz2
URL:		http://www.exaile.org/
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
BuildRequires:	pygtk2.0-devel python-devel
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
%setup -q -n %{name}-%{realver}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_menudir}

# Mandrivaify the desktop file
perl -pi -e "s#Categories=#Categories=X-MandrivaLinux-Multimedia-Sound;Sound;GNOME;#" ./res/decibel-audio-player.desktop

cat << EOF > ./start.sh
#!/bin/bash
# Decibel Audio Player launch script
# This script will autodetect language and copy the holiday file the first time
# plan is run. This script is licensed under the GNU General Public License
# and comes with ABSOLUTELY NO WARRANTY

exec python -OO %_datadir/%name/src/decibel-audio-player.py "\$@"
EOF

%makeinstall

%py_compile $RPM_BUILD_ROOT/usr/share/%name

# Find the localization
%find_lang %{name}

# Useless dir
rm -rf $RPM_BUILD_ROOT/usr/share/pixmaps

%post
%update_desktop_database
%update_menus

%postun
%clean_desktop_database
%update_menus

%clean 
rm -rf $RPM_BUILD_ROOT 

%files -f %name.lang
%defattr(-,root,root)
%doc ./doc/ChangeLog
%_bindir/%name
%_datadir/%name/
%_datadir/applications/*
%{_mandir}/*/*
#%_datadir/pixmaps/*
#%_menudir/%name
