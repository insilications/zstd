#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : zstd
Version  : 1.4.8
Release  : 66
URL      : file:///insilications/build/clearlinux/packages/zstd/zstd-1.4.8.tar.gz
Source0  : file:///insilications/build/clearlinux/packages/zstd/zstd-1.4.8.tar.gz
Summary  : Fast lossless compression algorithm library and tools
Group    : Development/Tools
License  : GPL-2.0+
Requires: zstd-bin = %{version}-%{release}
Requires: zstd-lib = %{version}-%{release}
Requires: zstd-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-meson
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : lz4-dev
BuildRequires : lz4-dev32
BuildRequires : lz4-staticdev
BuildRequires : pkgconfig(liblz4)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(zlib)
BuildRequires : xz-dev
BuildRequires : xz-dev32
BuildRequires : xz-staticdev
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
BuildRequires : zlib-staticdev

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

%description bin
bin components for the zstd package.


%package dev
Summary: dev components for the zstd package.
Group: Development
Requires: zstd-lib = %{version}-%{release}
Requires: zstd-bin = %{version}-%{release}
Provides: zstd-devel = %{version}-%{release}
Requires: zstd = %{version}-%{release}
Requires: zstd-dev = %{version}-%{release}
Requires: zstd-dev32 = %{version}-%{release}

%description dev
dev components for the zstd package.


%package dev32
Summary: dev32 components for the zstd package.
Group: Default
Requires: zstd-lib32 = %{version}-%{release}
Requires: zstd-bin = %{version}-%{release}
Requires: zstd-dev = %{version}-%{release}
Requires: zstd-dev32 = %{version}-%{release}

%description dev32
dev32 components for the zstd package.


%package lib
Summary: lib components for the zstd package.
Group: Libraries

%description lib
lib components for the zstd package.


%package lib32
Summary: lib32 components for the zstd package.
Group: Default

%description lib32
lib32 components for the zstd package.


%package man
Summary: man components for the zstd package.
Group: Default

%description man
man components for the zstd package.


%package staticdev
Summary: staticdev components for the zstd package.
Group: Default
Requires: zstd-dev = %{version}-%{release}
Requires: zstd-dev32 = %{version}-%{release}

%description staticdev
staticdev components for the zstd package.


%package staticdev32
Summary: staticdev32 components for the zstd package.
Group: Default
Requires: zstd-dev32 = %{version}-%{release}

%description staticdev32
staticdev32 components for the zstd package.


%prep
%setup -q -n zstd
cd %{_builddir}/zstd

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610598435
pushd build/cmake
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -fPIC $PGO_GEN"
export FCFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -fPIC $PGO_GEN"
export FFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -fPIC $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC $PGO_GEN"
export LDFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -fPIC -Wl,--whole-archive /usr/lib64/libz.a /usr/lib64/liblzma.a /usr/lib64/liblz4.a -pthread -ldl -lm -lmvec -Wl,--no-whole-archive $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden -flto-partition=none
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC $PGO_USE"
export FCFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC $PGO_USE"
export FFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC $PGO_USE"
export CXXFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC $PGO_USE"
export LDFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,--whole-archive /usr/lib64/libz.a /usr/lib64/liblzma.a /usr/lib64/liblz4.a -pthread -ldl -lm -lmvec -Wl,--no-whole-archive $PGO_USE"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
#
# export PATH="/usr/lib64/ccache/bin:$PATH"
# export CCACHE_NOHASHDIR=1
# export CCACHE_DIRECT=1
# export CCACHE_SLOPPINESS=pch_defines,locale,time_macros
# export CCACHE_DISABLE=1
export FUZZER_FLAGS="--no-big-tests"
export FUZZERTEST="-T30s"
export ZSTREAM_TESTTIME="-T30s"
export DECODECORPUS_TESTTIME="-T30s"
## altflags_pgo end
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
%cmake ..   -DZSTD_PROGRAMS_LINK_SHARED=OFF -DZSTD_BUILD_PROGRAMS=ON -DZSTD_BUILD_STATIC=ON -DZSTD_BUILD_SHARED=ON -DBUILD_TESTING=ON -DZSTD_BUILD_TESTS=ON -DZSTD_MULTITHREAD_SUPPORT=ON -DFUZZER_FLAGS="--no-big-tests" -DFUZZERTEST="-T30s" -DZSTREAM_TESTTIME="-T30s" -DDECODECORPUS_TESTTIME="-T30s" -DZSTD_ZLIB_SUPPORT=ON -DZSTD_LZMA_SUPPORT=ON -DZSTD_LZ4_SUPPORT=ON
make  PREFIX=%{_prefix} LIBDIR=%{_libdir} V=1 VERBOSE=1 LDFLAGS="${LDFLAGS} -Wl,--whole-archive /usr/lib64/libz.a /usr/lib64/liblzma.a /usr/lib64/liblz4.a -pthread -ldl -lm -lmvec -Wl,--no-whole-archive"

find ../../../ -name '*.c' -exec sh -c "cat {} | programs/zstd -v -9 | programs/zstd -v -d > /dev/null" \;
find ../../../ -name '*.c' -exec sh -c "cat {} | programs/zstd -v -1 | programs/zstd -v -d > /dev/null" \;
find ../../../ -name '*.c' -exec sh -c "cat {} | programs/zstd -v -19 | programs/zstd -v -d > /dev/null" \;
ctest -j1 -V --progress || :
find . -type f,l -not -name '*.gcno' -delete -print
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%cmake ..   -DZSTD_PROGRAMS_LINK_SHARED=OFF -DZSTD_BUILD_PROGRAMS=ON -DZSTD_BUILD_STATIC=ON -DZSTD_BUILD_SHARED=ON -DBUILD_TESTING=ON -DZSTD_BUILD_TESTS=ON -DZSTD_MULTITHREAD_SUPPORT=ON -DFUZZER_FLAGS="--no-big-tests" -DFUZZERTEST="-T30s" -DZSTREAM_TESTTIME="-T30s" -DDECODECORPUS_TESTTIME="-T30s" -DZSTD_ZLIB_SUPPORT=ON -DZSTD_LZMA_SUPPORT=ON -DZSTD_LZ4_SUPPORT=ON
make  PREFIX=%{_prefix} LIBDIR=%{_libdir} V=1 VERBOSE=1 LDFLAGS="${LDFLAGS} -Wl,--whole-archive /usr/lib64/libz.a /usr/lib64/liblzma.a /usr/lib64/liblz4.a -pthread -ldl -lm -lmvec -Wl,--no-whole-archive"
popd
mkdir -p clr-build32
pushd clr-build32
export CFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export CXXFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export LDFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
unset LD_LIBRARY_PATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%cmake -DLIB_INSTALL_DIR:PATH=/usr/lib32 -DCMAKE_INSTALL_LIBDIR=/usr/lib32 -DLIB_SUFFIX=32 ..   -DZSTD_PROGRAMS_LINK_SHARED=OFF -DZSTD_BUILD_PROGRAMS=OFF -DZSTD_BUILD_STATIC=ON -DZSTD_BUILD_SHARED=ON -DZSTD_BUILD_TESTS=OFF
make  PREFIX=%{_prefix} LIBDIR=%{_libdir} V=1 VERBOSE=1
unset PKG_CONFIG_PATH
popd
popd

%install
export SOURCE_DATE_EPOCH=1610598435
rm -rf %{buildroot}
pushd build/cmake
pushd clr-build32
%make_install32 PREFIX=%{_prefix} LIBDIR=%{_libdir}
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd clr-build
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
popd
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/unzstd
/usr/bin/zstd
/usr/bin/zstdcat
/usr/bin/zstdgrep
/usr/bin/zstdless
/usr/bin/zstdmt

%files dev
%defattr(-,root,root,-)
/usr/include/zdict.h
/usr/include/zstd.h
/usr/include/zstd_errors.h
/usr/lib64/cmake/zstd/zstdConfig.cmake
/usr/lib64/cmake/zstd/zstdConfigVersion.cmake
/usr/lib64/cmake/zstd/zstdTargets-relwithdebinfo.cmake
/usr/lib64/cmake/zstd/zstdTargets.cmake
/usr/lib64/libzstd.so
/usr/lib64/pkgconfig/libzstd.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/cmake/zstd/zstdConfig.cmake
/usr/lib32/cmake/zstd/zstdConfigVersion.cmake
/usr/lib32/cmake/zstd/zstdTargets-relwithdebinfo.cmake
/usr/lib32/cmake/zstd/zstdTargets.cmake
/usr/lib32/libzstd.so
/usr/lib32/pkgconfig/32libzstd.pc
/usr/lib32/pkgconfig/libzstd.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libzstd.so.1
/usr/lib64/libzstd.so.1.4.8

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libzstd.so.1
/usr/lib32/libzstd.so.1.4.8

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/unzstd.1
/usr/share/man/man1/zstd.1
/usr/share/man/man1/zstdcat.1
/usr/share/man/man1/zstdgrep.1
/usr/share/man/man1/zstdless.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libzstd.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libzstd.a
