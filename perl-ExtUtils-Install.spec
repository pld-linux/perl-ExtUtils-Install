#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%define		pdir	ExtUtils
%define		pnam	Install
Summary:	ExtUtils::AutoInstall - automatic install of dependencies via CPAN
Summary(pl.UTF-8):	ExtUtils::AutoInstall - automatyczna instalacja zależności z CPAN
Name:		perl-ExtUtils-Install
Version:	2.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ae6af2689daa6f8c2d01d04a28ab0ef0
Patch0:		%{name}-write-permissions.patch
URL:		http://search.cpan.org/dist/ExtUtils-Install/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Install Perl modules into the source tree. Used by ExtUtils::MakeMaker
and Module::Build.

%description -l pl.UTF-8
Ten moduł instaluje moduły Perla w drzewie źródłowym. Jest
wykorzystywany przez moduły ExtUtils::MakeMaker i Module::Build.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
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
%{perl_vendorlib}/ExtUtils/Install.pm
%{perl_vendorlib}/ExtUtils/Installed.pm
%{perl_vendorlib}/ExtUtils/Packlist.pm
%{_mandir}/man3/ExtUtils::Install.3pm*
%{_mandir}/man3/ExtUtils::Installed.3pm*
%{_mandir}/man3/ExtUtils::Packlist.3pm*
