#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Net
%define		pnam	NTP
%include	/usr/lib/rpm/macros.perl
Summary:	Net::NTP - Perl extension for decoding NTP server responses
Summary(pl.UTF-8):	Net::NTP - rozszerzenie Perla do obsługi odpowiedzi od serwerów NTP
Name:		perl-%{pdir}-%{pnam}
Version:	1.3
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ddd9b21daac0c4adad32ece4c738ae71
URL:		http://search.cpan.org/dist/Net-NTP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module exports a single method (get_ntp_response) and returns an
associative array based upon RFC1305 and RFC2030. The response from
the server is "humanized" to a point that further processing of th
information recieved from the server can be manipulated. For example:
timestamps are in epoch, so one could use the localtime function to
produce an even more "human" representation of the timestamp.

%description -l pl.UTF-8
Ten moduł udostępnia jedną metodę (get_ntp_response) zwracającą
tablicę asocjacyjną na podstawie RFC1305 i RFC2030. Odpowiedź od
serwera jest przedstawiona w postaci umożliwiającej dalszę obróbkę
otrzymanych danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Net/NTP.pm
%{_mandir}/man3/*
