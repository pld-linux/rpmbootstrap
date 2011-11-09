%include	/usr/lib/rpm/macros.perl
Summary:	Tool similar to debootstrap for RPM based distributions
Name:		rpmbootstrap
Version:	0.11.3
Release:	1
License:	GPL
Group:		Applications/Archiving
URL:		http://trac.project-builder.org/
Source0:	ftp://ftp.project-builder.org/src/%{name}-%{version}.tar.gz
# Source0-md5:	be748b98ae4004092f068b5da6a2daa4
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

rm $RPM_BUILD_ROOT%{perl_vendorarch}/auto/%{name}/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING INSTALL NEWS README
%attr(755,root,root) %{_bindir}/rpmbootstrap
%{_mandir}/man1/rpmbootstrap.1*
