Name:           sdlmame-data-roms
Version:        0120
Release:        3%{?dist}
Summary:        ROMs used for the SDLMAME package

Group:          Amusements/Games
License:        Public Domain
URL:            http://mamedev.org
Source0:        http://mamedev.org/roms/robby/robby.zip
Source1:        %{name}-README.ROMs
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

Requires:       sdlmame

%description
%{summary}.

%prep
%setup -qcT

unzip -qa %{SOURCE0} readme.txt -d .
mv readme.txt README.robby


%build
# Nothing to build


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/mame/roms
install -pm 644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_datadir}/mame/roms
install -pm 644 %{SOURCE1} ./README.ROMs


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.robby README.ROMs
%{_datadir}/mame


%changelog
* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0120-3
- rebuild for new F11 features

* Wed Jul 30 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0120-2
- rebuild for buildsys cflags issue

* Sun Oct 28 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0120-1
- First attempt at breaking down the package into smaller pieces
- Removed everything except robby due to copyright issues

