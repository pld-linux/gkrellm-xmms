Summary:	XMMS plugin for gkrellm
Summary(es):	XMMS plugin for gkrellm
Summary(pl):	Plugin gkrellm do XMMS
Summary(pt_BR):	Plugin gkrellm para o XMMS
Name:		gkrellm-xmms
Version:	0.5.5
Release:	2
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://gkrellm.luon.net/files/gkrellmms-%{version}.tar.gz
URL:		http://gkrellm.luon.net/gkrellmms.phtml
BuildRequires:	gkrellm-devel
BuildRequires:	imlib-devel
BuildRequires:	xmms-devel
Requires:	gkrellm >= 1.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
A GKrellM plugin which allows you to control XMMS from within GKrellM.

%description -l es
A GKrellM plugin which allows you to control XMMS from within GKrellM.

%description -l pl
Plugin GKrellM pozwalaj±cy na sterowanie XMMS.

%description -l pt_BR
Um plugin GKrellM para controlar o XMMS a partir do GKrellM.

%prep
%setup -q -n gkrellmms

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gkrellm

install gkrellmms.so $RPM_BUILD_ROOT%{_libdir}/gkrellm

gzip -9nf README Changelog FAQ Themes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/gkrellm/gkrellmms.so
