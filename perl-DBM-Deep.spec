%define upstream_name    DBM-Deep
%define upstream_version 1.0021

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A pure perl multi-level hash/array DBM that supports transactions
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DBM/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Fcntl)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Temp)
BuildRequires: perl(IO::Scalar)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Warn)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


