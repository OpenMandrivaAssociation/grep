%define	name	grep
%define version 2.5.3
%define _bindir /bin
%define release %mkrel 1

Summary:	The GNU versions of grep pattern matching utilities
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Text tools
Source0:	ftp://ftp.gnu.org/pub/gnu/grep/%{name}-%{version}.tar.bz2

Patch8:		grep-2.5.1a-mbcset.diff
# fix tests:
# - GREP_COLOR conflicts with test foad1.sh
# - in yesno.sh "-m 5 -C 1" test expects the context not to be printed after 5 matches,
#   it seems quite valid to display the context even in that case. (same for -m 2 -C 1)
Patch11:	grep-2.5.3-fix-tests.patch

# patches from debian
Patch100:	2-man_rgrep.patch
Patch101:	55-bigfile.patch
Patch102:	60-dfa.c-case_fold.patch
Patch103:	61-dfa.c-case_fold-charclass.patch
Patch104:	63-dfa.c-case_fold-range.patch
Patch105:	64-egf-speedup.patch
Patch106:	65-dfa-optional.patch
Patch107:	66-match_icase.patch
Patch108:	67-w.patch
Patch109:	68-no-grep.texi.patch

URL:		http://www.gnu.org/software/grep/grep.html
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gettext texinfo

%description
The GNU versions of commonly used grep utilities.  Grep searches one or
more input files for lines which contain a match to a specified pattern
and then prints the matching lines.  GNU's grep utilities include grep,
egrep and fgrep.

You should install grep on your system, because it is a very useful utility
for searching through text files, for system administration tasks, etc.

%package	doc
Summary:	Grep documentation in info format
Group:		Books/Computer books
Requires(post):	info-install
Requires(preun):	info-install

%description	doc
The GNU versions of commonly used grep utilities.  Grep searches one or
more input files for lines which contain a match to a specified pattern
and then prints the matching lines.  GNU's grep utilities include grep,
egrep and fgrep.  

You should install grep on your system, because it is a very useful utility
for searching through text files, for system administration tasks, etc.

Install this package if you want info documentation on grep.

%prep
%setup -q

%patch8 -p0 -b .mbcset
%patch11 -p1

%patch100 -p0
%patch101 -p0
%patch102 -p0
%patch103 -p0
%patch104 -p0
%patch105 -p0
%patch106 -p0
%patch107 -p0
%patch108 -p0
%patch109 -p0

%build
rm -f m4/header.m4 m4/init.m4 m4/install.m4 m4/largefile.m4 m4/missing.m4 m4/sanity.m4
./autogen.sh
#test -f po/Makevars || mv po/Makevars.template po/Makevars
%configure2_5x \
	--exec-prefix=/ \
	--disable-perl-regexp

%make

%check
make check

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%find_lang %{name}

%post doc
%_install_info %{name}.info

%preun doc
%_remove_install_info %{name}.info

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS THANKS TODO NEWS README ChangeLog
%{_bindir}/*
%{_mandir}/*/*

%files doc
%defattr(-,root,root)
%doc COPYING
%{_infodir}/*.info*


