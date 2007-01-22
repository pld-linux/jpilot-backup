Summary:	A backup-plugin for jpilot
Summary(pl):	Wtyczka obs³uguj±ca backup dla jpilota
Name:		jpilot-backup
Version:	0.53
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://jasonday.home.att.net/code/backup/%{name}-%{version}.tar.gz
# Source0-md5:	c8a3eefd3706d9614cb25f2bebf48ece
URL:		http://jasonday.home.att.net/code/backup/
BuildRequires:	gtk+2-devel >= 1:2.0.3
BuildRequires:	pilot-link-devel
BuildRequires:	gdbm-devel
BuildRequires:	pkgconfig
Requires:	jpilot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_jpluginsdir	/usr/lib/jpilot/plugins

%description
jpilot-Backup is a plugin for jpilot.

%description -l pl
jpilot-Backup to wtyczka dla jpilota.

%prep
%setup -q

%build
# dont call any auto scripts - it's completly broken
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{_jpluginsdir}/*
