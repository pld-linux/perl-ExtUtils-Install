#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	ExtUtils
%define		pnam	Install
Summary:	ExtUtils::AutoInstall - automatic install of dependencies via CPAN
Summary(pl.UTF-8):	ExtUtils::AutoInstall - automatyczna instalacja zależności z CPAN
Name:		perl-ExtUtils-Install
Version:	1.46
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3bea2cfd64653e576d732aa16bbeb169
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Install perl modules into the source tree. Used by ExtUtils::MakeMaker and
Module::Build.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"ExtUtils::Install")' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
