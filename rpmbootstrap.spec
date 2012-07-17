%include	/usr/lib/rpm/macros.perl
Summary:	Tool similar to debootstrap for RPM based distributions
Name:		rpmbootstrap
Version:	0.12.1
Release:	1
License:	GPL
Group:		Applications/Archiving
Source0:	ftp://ftp.project-builder.org/src/rpmbootstrap-0.12.1.tar.gz
# Source0-md5:	21123d36a0b55012ed45e181c8b2e796
URL:		http://trac.project-builder.org/
BuildRequires:	perl >= 5.8.4
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-libwww
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rpmbootstrap is a tool similar to debootstrap for RPM based
distributions. It helps building a chrooted environment for the
related distribution

%prep
%setup -q

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/%{name}/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING INSTALL NEWS README
%attr(755,root,root) %{_bindir}/rpmbootstrap
%{_mandir}/man1/rpmbootstrap.1*
