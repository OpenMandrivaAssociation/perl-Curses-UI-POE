%define upstream_name       Curses-UI-POE
%define upstream_version    0.035

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2
Epoch:      1
Summary:	A subclass makes Curses::UI POE Friendly
License:	GPL
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Curse/%{upstream_name}-%{upstream_version}.tar.gz
Buildrequires:	perl(Curses::UI)
Buildrequires:	perl(POE)
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is a subclass for Curses::UI that enables it to work with POE. It is
designed to simply slide over Curses::UI. Keeping the API the same and simply
forcing Curses::UI to do all of its event handling via POE, instead of internal
to itself. This allows you to use POE behind the scenes for things like
networking clients, without Curses::UI breaking your programs' functionality.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

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
