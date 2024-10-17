%define upstream_name       Curses-UI-POE
%define upstream_version    0.035

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5
Epoch:		1
Summary:	A subclass makes Curses::UI POE Friendly
License:	GPL
Group:		Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source:		http://www.cpan.org/modules/by-module/Curse/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Curses::UI)
BuildRequires:	perl(POE)
BuildArch:	noarch

%description
This is a subclass for Curses::UI that enables it to work with POE. It is
designed to simply slide over Curses::UI. Keeping the API the same and simply
forcing Curses::UI to do all of its event handling via POE, instead of internal
to itself. This allows you to use POE behind the scenes for things like
networking clients, without Curses::UI breaking your programs' functionality.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc CHANGES
%{perl_vendorlib}/Curses
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1:0.35.0-2mdv2011.0
+ Revision: 680874
- mass rebuild

* Thu Jul 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.35.0-1mdv2011.0
+ Revision: 396677
- new version
- use %%perl_version macro
- drop patch, useless now

* Wed Jan 21 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.031-1mdv2009.1
+ Revision: 332116
- bumping epoch, to force new version
- applying fix for rt #19681, not yet included upstream

  + Oden Eriksson <oeriksson@mandriva.com>
    - 0.031

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jun 14 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.02801-1mdv2008.0
+ Revision: 39291
- import error
- import perl-Curses-UI-POE


* Tue Feb 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.02801-1mdv2007.1
- initial mdv release
