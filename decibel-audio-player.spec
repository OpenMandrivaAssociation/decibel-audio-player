Name:		decibel-audio-player
Summary:	A clean and user-friendly audio player
Version:	1.08
Release:	1
Source0:	http://decibel.silent-blade.org/uploads/Main/%{name}-%{version}.tar.gz
URL:		https://decibel.silent-blade.org/
Group:		Sound
License:	GPLv2+
Requires:	pygtk2.0 
Requires: gstreamer1.0-python
Requires: pygtk2.0-libglade
Requires:	gstreamer1.0-plugins-good
Requires: gstreamer1.0-plugins-base
Requires:	gstreamer1.0-plugins-ugly
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
%doc ./doc/ChangeLog
%_bindir/*
%_datadir/%name/
%_datadir/applications/*
%_iconsdir/*
%{_mandir}/*/*
