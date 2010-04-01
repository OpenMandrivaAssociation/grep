%define _bindir /bin

Summary:	The GNU versions of grep pattern matching utilities
Name:		grep
Version:	2.6.2
Release:	%mkrel 1
License:	GPLv3
Group:		Text tools
URL:		http://www.gnu.org/software/grep/grep.html
Source0:	ftp://ftp.gnu.org/pub/gnu/grep/%{name}-%{version}.tar.xz
Source1:	%{SOURCE0}.sig
#Patch8:		grep-2.5.1a-mbcset.diff
# patches from debian
Patch100:	2-man_rgrep.patch
Patch101:	55-bigfile.patch
Patch103:	61-dfa.c-case_fold-charclass.patch
Patch104:	63-dfa.c-case_fold-range.patch
Patch105:	64-egf-speedup.patch
Patch106:	65-dfa-optional.patch
Patch107:	66-match_icase.patch
Patch108:	67-w.patch
Patch110:	70-man_apostrophe.patch
# git patches
# (none)
# Mandriva patches
# (eugeni) skip multibyte check for nowas it is failing with grep 2.6.1 on buildsystem
Patch301:	grep-2.6.1-skip_multibyte_check.patch
BuildRequires:	gettext
BuildRequires:	pcre-devel
BuildRequires:	texinfo
BuildRequires:	bison
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
Requires(post):	info-install
Requires(preun):	info-install

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

#%patch8 -p0 -b .mbcset

%patch100 -p0
#%patch101 -p0
%patch103 -p1
# eugeni: seems to be fixed upstream, but let's leave them for a couple of released to make sure
#%patch104 -p0
#%patch105 -p0
#%patch106 -p0
#%patch107 -p0
#%patch108 -p0
%patch110 -p0
# we might need it on our build system
#%patch301 -p1 -b .skip

%build
%configure2_5x \
    --without-included-regex \
    --without-included-getopt \
    --without-included-gettext \
    --enable-perl-regexp \
    --exec-prefix=/

%make

%check
make check

%install
rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%post doc
%_install_info %{name}.info

%preun doc
%_remove_install_info %{name}.info

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/*/*

%files doc
%defattr(-,root,root)
%doc AUTHORS THANKS TODO NEWS README ChangeLog
%{_infodir}/*.info*
