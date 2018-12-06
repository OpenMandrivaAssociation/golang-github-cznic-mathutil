# https://github.com/cznic/mathutil
%global goipath github.com/cznic/mathutil
%global commit  ca4c9f2c136954238c3158b92de72078c7672ecc

%gometa

Name:           golang-github-cznic-mathutil
Version:        0
Release:        0.15%{?dist}
Summary:        Supplemental utilities for Go's rand and math packages
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

# BuildRequires: golang(github.com/remyoudompheng/bigfft)

%description
%{summary}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup

# Don't include "mersenne" sub-package, it pulls in arch-specific dependencies.
rm -r ./mersenne


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc CONTRIBUTORS AUTHORS README


%changelog
* Thu Nov 15 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.15.20180504gitca4c9f2
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.14.20180504gitca4c9f2
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.13.20180504gitca4c9f2
- Update to use spec 3.0.

* Thu Jul 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.12.gitca4c9f2
- Bump to commit ca4c9f2.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitc90ba19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitc90ba19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.9.gitc90ba19
- Bump to commit c90ba19.

* Wed Oct 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.8.git09cde8d
- Bump to commit 09cde8d.

* Tue Oct 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.7.git53c7078
- Bump to commit 53c7078.

* Tue Sep 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.6.git91af0ce
- Bump to commit 91af0ce.

* Sat Aug 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.5.git1447ad2
- Fix for new-style RPM macro expansion.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git1447ad2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git1447ad2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.2.git1447ad2
- Add missing BRs/Requires, guarded by "ifarch".

* Sat Mar 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.1.git1447ad2
- First package for Fedora

