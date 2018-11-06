%define _bindir /bin

# (tpg) optimize it a bit
%global optflags %{optflags} -O3 --rtlib=compiler-rt

Summary:	The GNU versions of grep pattern matching utilities
Name:		grep
Version:	3.1
Release:	3
License:	GPLv3
Group:		Text tools
Url:		http://www.gnu.org/software/grep/grep.html
Source0:	ftp://ftp.gnu.org/pub/gnu/grep/%{name}-%{version}.tar.xz
# (tpg) fix build with LLVM/clang
Patch0:		grep-3.1-check-for-__builtin_mul_overflow_p.patch
Patch1:		grep-3.1-glibc-2.28-fix.patch
BuildRequires:	bison
BuildRequires:	gettext
BuildRequires:	texinfo
BuildRequires:	pkgconfig(libpcre)
Provides:	/bin/grep

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
%autosetup -p1

%build
# Always use pkg-config to get lib info for pcre.
export ac_cv_search_pcre_compile="$(pkg-config --libs --static libpcre)"
%configure \
	--without-included-regex \
	--enable-perl-regexp \
	--exec-prefix=/ \
	--enable-threads=posix

%make_build CFLAGS="%{optflags}"

%ifnarch %{ix86}
%check
make check || cat tests/test-suite.log && exit 1
%endif

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/*
%{_mandir}/*/*

%files doc
%doc AUTHORS THANKS TODO NEWS README
%{_infodir}/*.info*
