Summary:	XMMS plugin for gkrellm
Summary(pl.UTF-8):	Plugin gkrellm do XMMS
Summary(pt_BR.UTF-8):	Plugin gkrellm para o XMMS
Name:		gkrellm-xmms
Version:	2.1.22
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://gkrellm.luon.net/files/gkrellmms-%{version}.tar.gz
# Source0-md5:	2739eaf7047d7c8d203111a3c2e7eb17
URL:		http://gkrellm.luon.net/gkrellmms.phtml
BuildRequires:	gkrellm-devel >= 2.0
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
BuildRequires:	xmms-devel
Requires:	gkrellm >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GKrellM plugin which allows you to control XMMS from within GKrellM.

%description -l pl.UTF-8
Plugin GKrellM pozwalający na sterowanie XMMS.

%description -l pt_BR.UTF-8
Um plugin GKrellM para controlar o XMMS a partir do GKrellM.

%prep
%setup -q -n gkrellmms

%build
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D gkrellmms.so $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins/gkrellmms.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog FAQ README Themes
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/gkrellmms.so
