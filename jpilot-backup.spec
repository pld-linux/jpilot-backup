Summary:	A backup-plugin for jpilot
Summary(pl):	Wtyczka obs³uguj±ca backup dla jpilota
Name:		jpilot-backup
Version:	0.50
Release:	0.1
License:	GPL
Group:		Applications/Communications
Source0:	http://jasonday.home.att.net/code/backup/%{name}-%{version}.tar.gz
# Source0-md5:	c17b679d3a0c1bb1a9dc74f3c88be58c
URL:		http://jasonday.home.att.net/code/backup/
BuildRequires:	gtk+2-devel
BuildRequires:	pilot-link-devel
Requires:	jpilot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_jpluginsdir	/usr/lib/jpilot/plugins

%description
jpilot-Backup is a plugin for jpilot

%description -l pl

%prep
%setup -q

%build
# dont call any auto scripts - it's completly broken
%configure --enable-gtk2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog INSTALL README TODO
%{_jpluginsdir}/*
