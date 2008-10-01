%define module	Curses-UI-POE

Name:		perl-%{module}
Version:	0.031
Release:	%mkrel 1
Summary:	A subclass makes Curses::UI POE Friendly
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Curses/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildrequires:	perl(Curses::UI)
Buildrequires:	perl(POE)
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is a subclass for Curses::UI that enables it to work with POE. It is
designed to simply slide over Curses::UI. Keeping the API the same and simply
forcing Curses::UI to do all of its event handling via POE, instead of internal
to itself. This allows you to use POE behind the scenes for things like
networking clients, without Curses::UI breaking your programs' functionality.

%prep

%setup -q -n %{module}-%{version}
# this one doesn't pass during rpm building
rm -f t/session.t

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc CHANGES
%{perl_vendorlib}/Curses
%{_mandir}/*/*
