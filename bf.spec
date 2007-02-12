Summary:	Brainfuck interpreter
Summary(pl.UTF-8):   Interpreter języka Brainfuck
Name:		bf
Version:	20041219
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://noxa.de/~sbeyer/debian/dists/unstable/main/source/%{name}_%{version}.tar.gz
# Source0-md5:	9930164483e23b7ef50892fe96e63211
URL:		http://noxa.de/~sbeyer/programming/projects/?dir=tools#bf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bf is a simple, fast interpreter for the esoteric programming language
Brainfuck.

%description -l pl.UTF-8
bf jest prostym, szybkim interpreterem ezoterycznego języka
programowania Brainfuck.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install bf.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc examples/
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/bf.1*
