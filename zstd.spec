#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : zstd
Version  : 1.4.4
Release  : 57
URL      : https://github.com/facebook/zstd/releases/download/v1.4.4/zstd-1.4.4.tar.gz
Source0  : https://github.com/facebook/zstd/releases/download/v1.4.4/zstd-1.4.4.tar.gz
Summary  : Fast lossless compression algorithm library and tools
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: zstd-bin = %{version}-%{release}
Requires: zstd-lib = %{version}-%{release}
Requires: zstd-license = %{version}-%{release}
Requires: zstd-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-meson
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : lz4-dev
BuildRequires : lz4-dev32
BuildRequires : util-linux
BuildRequires : xz-dev
BuildRequires : xz-dev32
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
Patch1: multi-thread-default.patch

%description
Zstandard, or zstd as short version, is a fast lossless compression algorithm,
targeting real-time compression scenarios at zlib-level and better compression
ratios. It's backed by a very fast entropy stage, provided by Huff0 and FSE
library. The project is provided as an open-source dual BSD and GPLv2 licensed
C library, and a command line utility producing and decoding .zst, .gz, .xz and
.lz4 files.

%package bin
Summary: bin components for the zstd package.
Group: Binaries
Requires: zstd-license = %{version}-%{release}

%description bin
bin components for the zstd package.


%package dev
Summary: dev components for the zstd package.
Group: Development
Requires: zstd-lib = %{version}-%{release}
Requires: zstd-bin = %{version}-%{release}
Provides: zstd-devel = %{version}-%{release}
Requires: zstd = %{version}-%{release}

%description dev
dev components for the zstd package.


%package dev32
Summary: dev32 components for the zstd package.
Group: Default
Requires: zstd-lib32 = %{version}-%{release}
Requires: zstd-bin = %{version}-%{release}
Requires: zstd-dev = %{version}-%{release}

%description dev32
dev32 components for the zstd package.


%package lib
Summary: lib components for the zstd package.
Group: Libraries
Requires: zstd-license = %{version}-%{release}

%description lib
lib components for the zstd package.


%package lib32
Summary: lib32 components for the zstd package.
Group: Default
Requires: zstd-license = %{version}-%{release}

%description lib32
lib32 components for the zstd package.


%package license
Summary: license components for the zstd package.
Group: Default

%description license
license components for the zstd package.


%package man
Summary: man components for the zstd package.
Group: Default

%description man
man components for the zstd package.


%package staticdev
Summary: staticdev components for the zstd package.
Group: Default
Requires: zstd-dev = %{version}-%{release}

%description staticdev
staticdev components for the zstd package.


%package staticdev32
Summary: staticdev32 components for the zstd package.
Group: Default
Requires: zstd-dev = %{version}-%{release}

%description staticdev32
staticdev32 components for the zstd package.


%prep
%setup -q -n zstd-1.4.4
cd %{_builddir}/zstd-1.4.4
%patch1 -p1
pushd ..
cp -a zstd-1.4.4 build32
popd
pushd ..
cp -a zstd-1.4.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1580439887
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CFLAGS_GENERATE="$CFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FCFLAGS_GENERATE="$FCFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FFLAGS_GENERATE="$FFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CXXFLAGS_GENERATE="$CXXFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export LDFLAGS_GENERATE="$LDFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CFLAGS_USE="$CFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FCFLAGS_USE="$FCFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FFLAGS_USE="$FFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export CXXFLAGS_USE="$CXXFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export LDFLAGS_USE="$LDFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
pushd build/meson
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddefault_library=both  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=haswell" CXXFLAGS="$CXXFLAGS -m64 -march=haswell " LDFLAGS="$LDFLAGS -m64 -march=haswell" meson --libdir=lib64/haswell --prefix=/usr --buildtype=plain -Ddefault_library=both  builddiravx2
ninja -v -C builddiravx2
popd
pushd ../build32/build/meson
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
meson --libdir=lib32 --prefix=/usr --buildtype=plain -Ddefault_library=both  builddir
ninja -v -C builddir
popd

%install
mkdir -p %{buildroot}/usr/share/package-licenses/zstd
cp %{_builddir}/zstd-1.4.4/COPYING %{buildroot}/usr/share/package-licenses/zstd/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8
cp %{_builddir}/zstd-1.4.4/LICENSE %{buildroot}/usr/share/package-licenses/zstd/c4130945ca3d1f8ea4a3e8af36d3c18b2232116c
cp %{_builddir}/zstd-1.4.4/contrib/linux-kernel/COPYING %{buildroot}/usr/share/package-licenses/zstd/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8
pushd ../build32/build/meson
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd build/meson
DESTDIR=%{buildroot} ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/haswell/pkgconfig/libzstd.pc

%files bin
%defattr(-,root,root,-)
/usr/bin/unzstd
/usr/bin/zstd
/usr/bin/zstd-frugal
/usr/bin/zstdcat
/usr/bin/zstdgrep
/usr/bin/zstdless
/usr/bin/zstdmt

%files dev
%defattr(-,root,root,-)
/usr/include/zbuff.h
/usr/include/zdict.h
/usr/include/zstd.h
/usr/include/zstd_errors.h
/usr/lib64/haswell/libzstd.so
/usr/lib64/libzstd.so
/usr/lib64/pkgconfig/libzstd.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libzstd.so
/usr/lib32/pkgconfig/32libzstd.pc
/usr/lib32/pkgconfig/libzstd.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libzstd.so.1
/usr/lib64/haswell/libzstd.so.1.4.4
/usr/lib64/libzstd.so.1
/usr/lib64/libzstd.so.1.4.4

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libzstd.so.1
/usr/lib32/libzstd.so.1.4.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zstd/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8
/usr/share/package-licenses/zstd/c4130945ca3d1f8ea4a3e8af36d3c18b2232116c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/unzstd.1
/usr/share/man/man1/zstd.1
/usr/share/man/man1/zstdcat.1
/usr/share/man/man1/zstdgrep.1
/usr/share/man/man1/zstdless.1
/usr/share/man/man1/zstdmt.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/haswell/libzstd.a
/usr/lib64/libzstd.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libzstd.a
