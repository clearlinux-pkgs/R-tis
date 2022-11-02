#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tis
Version  : 1.39
Release  : 77
URL      : https://cran.r-project.org/src/contrib/tis_1.39.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tis_1.39.tar.gz
Summary  : Time Indexes and Time Indexed Series
Group    : Development/Tools
License  : Public-Domain
Requires: R-tis-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
series, which are compatible with FAME frequencies.

%package lib
Summary: lib components for the R-tis package.
Group: Libraries

%description lib
lib components for the R-tis package.


%prep
%setup -q -c -n tis
cd %{_builddir}/tis

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641139564

%install
export SOURCE_DATE_EPOCH=1641139564
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tis
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tis
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tis
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc tis || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tis/COPYRIGHTS
/usr/lib64/R/library/tis/DESCRIPTION
/usr/lib64/R/library/tis/INDEX
/usr/lib64/R/library/tis/Meta/Rd.rds
/usr/lib64/R/library/tis/Meta/features.rds
/usr/lib64/R/library/tis/Meta/hsearch.rds
/usr/lib64/R/library/tis/Meta/links.rds
/usr/lib64/R/library/tis/Meta/nsInfo.rds
/usr/lib64/R/library/tis/Meta/package.rds
/usr/lib64/R/library/tis/NAMESPACE
/usr/lib64/R/library/tis/NEWS
/usr/lib64/R/library/tis/R/tis
/usr/lib64/R/library/tis/R/tis.rdb
/usr/lib64/R/library/tis/R/tis.rdx
/usr/lib64/R/library/tis/help/AnIndex
/usr/lib64/R/library/tis/help/aliases.rds
/usr/lib64/R/library/tis/help/paths.rds
/usr/lib64/R/library/tis/help/tis.rdb
/usr/lib64/R/library/tis/help/tis.rdx
/usr/lib64/R/library/tis/html/00Index.html
/usr/lib64/R/library/tis/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/tis/libs/tis.so
/usr/lib64/R/library/tis/libs/tis.so.avx2
/usr/lib64/R/library/tis/libs/tis.so.avx512
