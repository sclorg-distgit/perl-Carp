%{?scl:%scl_package perl-Carp}

%global cpan_version 1.38

Name:           %{?scl_prefix}perl-Carp
# Keep 2-digit precision
#Version:        %%(echo '%%{cpan_version}' | sed 's/\(\...\)\(.\)/\1.\2/')
Version:        1.40
Release:        366%{?dist}
Summary:        Alternative warn and die for modules
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Carp/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/Carp-%{cpan_version}.tar.gz
# Unbundled from perl 5.24.0
Patch0:         Carp-1.38-Upgrade-to-1.40.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(warnings)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  sed
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Exporter)
# Tests:
BuildRequires:  %{?scl_prefix}perl(B)
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
# IPC::Open3  >= 1.0103 in reality, but the provides is 2-digit number only
BuildRequires:  %{?scl_prefix}perl(IPC::Open3)
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.47
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))

# Do not export private DB module stub
%if 0%{?rhel} < 7
# RPM 4.8 style
%{?filter_setup:
%filter_from_provides /^%{?scl_prefix}perl(DB)/d
%?perl_default_filter
}
%else
# RPM 4.9 style
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^%{?scl_prefix}perl\\(DB\\)
%endif

%description
The Carp routines are useful in your own modules because they act like
die() or warn(), but with a message which is more likely to be useful to a
user of your module. In the case of cluck, confess, and longmess that
context is a summary of every call in the call-stack. For a shorter message
you can use carp or croak which report the error as being from where your
module was called. There is no guarantee that that is where the error was,
but it is a good educated guess.

%prep
%setup -q -n Carp-%{cpan_version}
%patch0 -p1

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jul 11 2016 Petr Pisar <ppisar@redhat.com> - 1.40-366
- SCL

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.40-365
- Increase release to favour standalone package

* Wed May 11 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.40-1
- 1.40 bump in order to dual-live with perl 5.24

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Petr Pisar <ppisar@redhat.com> - 1.38-1
- 1.38 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36-346
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.36-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.36-2
- Perl 5.22 rebuild

* Fri Mar 20 2015 Petr Pisar <ppisar@redhat.com> - 1.36-1
- 1.36 bump

* Mon Mar 16 2015 Petr Pisar <ppisar@redhat.com> - 1.35-1
- 1.35 bump

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.33.01-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.33.01-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.33.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 04 2014 Petr Pisar <ppisar@redhat.com> - 1.33.01-1
- 1.3301 bump

* Wed Mar 26 2014 Petr Pisar <ppisar@redhat.com> - 1.33-1
- 1.33 bump

* Tue Sep 10 2013 Petr Pisar <ppisar@redhat.com> - 1.32-1
- 1.32 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26-245
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1.26-244
- Link minimal build-root packages against libperl.so explicitly

* Tue Apr 30 2013 Petr Pisar <ppisar@redhat.com> - 1.26-243
- Increase release number to supersede perl sub-package (bug #957931)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26-241
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 13 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1.26-240
- Bump release to override sub-package from perl.spec

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 1.26-2
- Perl 5.16 rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 1.26-1
- 1.26 bump

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 1.25-2
- Perl 5.16 rebuild

* Thu Mar 15 2012 Petr Pisar <ppisar@redhat.com> - 1.25-1
- 1.25 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep 07 2011 Petr Pisar <ppisar@redhat.com> 1.22-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot and defattr code from spec
- Do not export private module DB
