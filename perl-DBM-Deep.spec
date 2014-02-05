%define upstream_name    DBM-Deep
%define upstream_version 2.0011

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	A pure perl multi-level hash/array DBM that supports transactions
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DBM/DBM-Deep-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(Pod::Usage)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
A unique flat-file database module, written in pure perl. True multi-level
hash/array support (unlike MLDBM, which is faked), hybrid OO / tie()
interface, cross-platform FTPable files, ACID transactions, and is quite
fast. Can handle millions of keys and unlimited levels without significant
slow-down. Written from the ground-up in pure perl -- this is NOT a wrapper
around a C-based DBM. Out-of-the-box compatibility with Unix, Mac OS X and
Windows.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 2.0.400-2mdv2011.0
+ Revision: 656901
- rebuild for updated spec-helper

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 2.0004

* Tue Aug 24 2010 Jérôme Quelin <jquelin@mandriva.org> 2.0.100-1mdv2011.0
+ Revision: 572700
- update to 2.0001

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 2.0.0-1mdv2011.0
+ Revision: 561554
- update to 2.0000

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 1.2.500-1mdv2011.0
+ Revision: 553081
- update to 1.0025

* Tue Apr 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.2.100-1mdv2010.1
+ Revision: 536963
- update to 1.0021

* Mon Feb 08 2010 Jérôme Quelin <jquelin@mandriva.org> 1.1.600-1mdv2010.1
+ Revision: 502096
- update to 1.0016

* Wed Jan 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1.1.500-1mdv2010.1
+ Revision: 497007
- update to 1.0015

* Tue Nov 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.1.400-1mdv2010.1
+ Revision: 466976
- import perl-DBM-Deep


* Tue Nov 17 2009 cpan2dist 1.0014-1mdv
- initial mdv release, generated with cpan2dist


