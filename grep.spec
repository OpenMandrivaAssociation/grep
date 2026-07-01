%define snapshot 24da-modified

Summary:	The GNU versions of grep pattern matching utilities
Name:		grep
Version:	3.12.35
Release:	2
License:	GPLv3
Group:		Text tools
Url:		https://www.gnu.org/software/grep/grep.html
%if 0%{?snapshot:1}
# To generate the snapshot tarball:
# git clone --recursive https://git.savannah.gnu.org/git/grep.git
# cd grep
# ./bootstrap
# ./configure
# make dist
Source0:	grep-%{version}-%{snapshot}.tar.xz
%else
Source0:	https://ftp.gnu.org/pub/gnu/grep/%{name}-%{version}.tar.xz
%endif
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	bison
BuildRequires:	gettext
BuildRequires:	texinfo
BuildRequires:	pkgconfig(libpcre2-8)
Provides:	/bin/grep

%patchlist
# Performance and rg replacement
0001-Fix-build-with-clang.patch
0002-perf-add-perf.c-perf.h-performance-helpers.patch
0003-grep-use-perf-helpers-for-I-O-binary-scan-and-mmap.patch
0004-grep-SIMD-memmem-fast-path-for-single-pattern-F.patch
0005-perf-aarch64-NEON-memmem-in-perf.c.patch
0006-perf-LoongArch-LSX-and-RISC-V-Vector-memmem-in-perf..patch
0007-rg-add-ripgrep-compatible-recursive-grep-C-23.patch
0008-fix-SIGBUS-in-perf_try_mmap-on-page-aligned-files.patch

%description
The GNU versions of commonly used grep utilities.  Grep searches one or
more input files for lines which contain a match to a specified pattern
and then prints the matching lines.  GNU's grep utilities include grep,
egrep and fgrep.

You should install grep on your system, because it is a very useful utility
for searching through text files, for system administration tasks, etc.

%package -n rg
Summary:	grep-based C++ implementation of ripgrep
Group:		Text tools
Obsoletes:	rust-ripgrep < 14.1.1-3

%description -n rg
grep-based C++ implementation of ripgrep

ripgrep started out trying to be a better and faster grep - but with current
optimizations, grep outperforms ripgrep by large margins.

With rg, it comes full circle: A grep-based better reimplementation of a tool
that started out trying to be a better reimplementation of grep.

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
%autosetup -p1 %{?snapshot:-n %{name}-%{version}-%{snapshot}}

%build
# Always use pkg-config to get lib info for pcre.
export ac_cv_search_pcre_compile="$(pkg-config --libs --static libpcre2-8)"
%configure \
	--without-included-regex \
	--enable-perl-regexp \
	--enable-threads=posix

%make_build CFLAGS="%{optflags}"

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/{e,f,}grep
%doc %{_mandir}/*/*

%files -n rg
%{_bindir}/rg

%files doc
%doc AUTHORS THANKS TODO NEWS README
%{_infodir}/*.info*
