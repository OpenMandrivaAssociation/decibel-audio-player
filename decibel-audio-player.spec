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
License:	GPLv2+
Requires:	pygtk2.0 gstreamer0.10-python pygtk2.0-libglade
Requires:	gstreamer0.10-plugins-good gstreamer0.10-plugins-base 
Requires:	gstreamer0.10-plugins-ugly
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

make install DESTDIR=%{buildroot} prefix=%{_prefix}

# Move icons to correct dir
mkdir -p %buildroot/%{_iconsdir}
mv %buildroot/%{_datadir}/pixmaps/* %buildroot/%{_iconsdir}/

%find_lang %name


%files -f %name.lang
%defattr(-,root,root)
%doc ./doc/ChangeLog
%_bindir/*
%_datadir/%name/
%_datadir/applications/*
%_iconsdir/*
%{_mandir}/*/*
