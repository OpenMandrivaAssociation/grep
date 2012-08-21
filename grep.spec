%define _bindir /bin

Summary:	The GNU versions of grep pattern matching utilities
Name:		grep
Version:	2.14
Release:	1
License:	GPLv3
Group:		Text tools
URL:		http://www.gnu.org/software/grep/grep.html
Source0:	ftp://ftp.gnu.org/pub/gnu/grep/%{name}-%{version}.tar.xz
Source1:	ftp://ftp.gnu.org/pub/gnu/grep/%{name}-%{version}.tar.xz.sig
BuildRequires:	gettext
BuildRequires:	pcre-devel
#BuildRequires:	texinfo
BuildRequires:	bison

%description
The GNU versions of commonly used grep utilities.  Grep searches one or
more input files for lines which contain a match to a specified pattern
and then prints the matching lines.  GNU's grep utilities include grep,
egrep and fgrep.

You should install grep on your system, because it is a very useful utility
for searching through text files, for system administration tasks, etc.

%package doc
Summary:	Grep documentation in info format
Group:		Books/Computer books

%description doc
The GNU versions of commonly used grep utilities.  Grep searches one or
more input files for lines which contain a match to a specified pattern
and then prints the matching lines.  GNU's grep utilities include grep,
egrep and fgrep.

You should install grep on your system, because it is a very useful utility
for searching through text files, for system administration tasks, etc.

Install this package if you want info documentation on grep.

%prep

%setup -q

%build
%configure2_5x \
    --without-included-regex \
    --enable-perl-regexp \
    --exec-prefix=/ \
    --disable-rpath \
    --enable-threads=posix

%make

%check
make check

%install
rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/*
%{_mandir}/*/*

%files doc
%doc AUTHORS THANKS TODO NEWS README ChangeLog
%{_infodir}/*.info*
