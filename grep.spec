%define	name	grep
%define version 2.5.1a
%define _bindir /bin
%define release %mkrel 2

Summary:	The GNU versions of grep pattern matching utilities
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Text tools
Source0:	ftp://ftp.gnu.org/pub/gnu/grep/%{name}-%{version}.tar.bz2
Patch1:		grep-2.5.1-i18n-0.1.patch
Patch2:		grep-2.5.1-oi.patch
Patch3:		grep-2.5.1-manpage.patch
Patch4:		grep-2.5.1-color.patch
Patch5:		grep-2.5.1-icolor.patch
Patch6:		grep-P.patch
Patch7:		grep-2.5.1a-wordmatch.patch
Patch8:		grep-2.5.1a-mbcset.diff
Patch9:		grep-2.5.1a-skip-devices.patch
Patch10:	grep-2.5.1-nb.patch
URL:		http://www.gnu.org/software/grep/grep.html
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gettext pcre-devel texinfo

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
%patch1 -p1 -b .i18n
%patch2 -p1 -b .oi
%patch3 -p1 -b .manpage
%patch4 -p1 -b .color
%patch5 -p1 -b .icolor
%patch6 -p1 -b .P
%patch7 -p0 -b .wordmatch
%patch8 -p0 -b .mbcset
%patch9 -p0 -b .skip_devs
%patch10 -p0 -b .nb
rename no nb po/no.*

%build
rm -f m4/header.m4 m4/init.m4 m4/install.m4 m4/largefile.m4 m4/missing.m4 m4/sanity.m4
./autogen.sh
#test -f po/Makevars || mv po/Makevars.template po/Makevars
%configure2_5x \
	--exec-prefix=/ \
	--without-included-regex

%make

# (gb) why does spencer bre test #16 fails?
# (gw) Spencer test #55 has a syntax error: echo '-'| grep -E -e '(*)b'
# (fpons) removed make check as glibc is bogus currently.
#make -k check || echo "make check failed"
# (abel) however, if --with-included-regex is used, all test suite
#        passed flawlessly
#(peroyvind) reenabled test as it now works:)
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


