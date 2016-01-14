%{?scl:%scl_package perl-Carp}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Carp
Version:        1.32
Release:        3.sc1%{?dist}
Summary:        Alternative warn and die for modules
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Carp/
Source0:        http://www.cpan.org/authors/id/Z/ZE/ZEFRAM/Carp-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(warnings)
BuildRequires:  %{?scl_prefix}perl(strict)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Exporter)
# Tests:
BuildRequires:  %{?scl_prefix}perl(B)
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(IPC::Open3)
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(parent)
BuildRequires:  %{?scl_prefix}perl(Test::More)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

# Do not export private DB module stub
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^%{?scl_prefix}perl\\(DB\\)

%if ( 0%{?rhel} && 0%{?rhel} < 7 )
%filter_from_provides /perl(DB)/d
%filter_setup
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
%setup -q -n Carp-%{version}

%build
%{?scl:scl enable %{scl} "}
perl Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{?scl:"}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Feb 13 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.32-3
- Update conditions to work for non-RHEL systems
- Resolves: rhbz#1064855

* Mon Dec 02 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.32-2
- Update filters
- Resolves: rhbz#1036795

* Tue Nov 12 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.32-1
- 1.32 bump

* Mon May 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.26-101
- Update BRs

* Mon Feb  4 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.26-100
- Stack package - initial release
