Name: gkrellm-xmms
Version: 0.5.4
Release: 1cl
Summary: XMMS plugin for gkrellm
Summary(pt_BR): Plugin gkrellm para o XMMS
Summary(es): XMMS plugin for gkrellm
License: GPL
Group: X11
Group(pt_BR): X11
Group(es): X11
Source:	http://gkrellm.luon.net/files/gkrellmms-%{version}.tar.gz
Requires: gkrellm >= 1.0.2, xmms
BuildRequires: gkrellm-devel, gtk+-devel, imlib-devel, xmms-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
A GKrellM plugin which allows you to control XMMS from within GKrellM.

%description -l pt_BR
Um plugin GKrellM para controlar o XMMS a partir do GKrellM.

%description -l es
A GKrellM plugin which allows you to control XMMS from within GKrellM.

%prep
%setup -q -n gkrellmms

%build
CFLAGS="%{optflags}" make

%install
rm -rf %{buildroot}
install -D -m644 gkrellmms.so %{buildroot}%{_libdir}/gkrellm/plugins/gkrellmms.so

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changelog FAQ IMPORTANT Themes
%{_libdir}/gkrellm/plugins/gkrellmms.so

%changelog
* Thu Nov 30 2000 Claudio Matsuoka <claudio@conectiva.com>
- package created
