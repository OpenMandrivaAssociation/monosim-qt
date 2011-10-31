Summary:   Qt user interface to manage sim card contacts
Name:      monosim-qt
Version:   2.0.0.0
Release:   %mkrel 2
License:   GPLv2
#ExcludeArch: ppc64
Group:     Office
Source:    http://monosim.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
URL:       http://monosim.googlecode.com/
BuildArch: noarch
# don't generate debug file because is empty
# % define debug_package %{nil}

BuildRequires: mono
BuildRequires: log4net-devel
BuildRequires: comex-base-devel >= 0.1.8.5
BuildRequires: qyoto
BuildRequires: qyoto-devel
BuildRequires: pinentry-qt4
BuildRequires: pkgconfig

Requires: mono
Requires: log4net
Requires: comex-base >= 0.1.8.5
Requires: qyoto
Requires: qyoto-devel


%description
Is Qt user interface of a simple application that can be used 
to manage sim card contacts using PC/SC standard readers or 
smartmouse phoenix serial reader.


%prep
%setup -q

%build
%configure2_5x --libdir=%_prefix/lib 
%make

%install
rm -fr %{buildroot}
%makeinstall_std


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc copying.gpl monosim-qt/readme
%{_bindir}/%{name}
%_prefix/lib/%{name}/
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop



