#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tis
Version  : 1.30
Release  : 5
URL      : http://cran.r-project.org/src/contrib/tis_1.30.tar.gz
Source0  : http://cran.r-project.org/src/contrib/tis_1.30.tar.gz
Summary  : Time Indexes and Time Indexed Series
Group    : Development/Tools
License  : Public-Domain
Requires: R-tis-lib
BuildRequires : clr-R-helpers

%description
The ti (Time Index) and tis (Time Indexed Series) classes in the
package provide date arithmetic facilities and an alternative to the somewhat
inflexible ts class in the standard R stats package.

%package lib
Summary: lib components for the R-tis package.
Group: Libraries

%description lib
lib components for the R-tis package.


%prep
%setup -q -c -n tis

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -ffunction-sections -fno-semantic-interposition -freorder-functions "
export CXXFLAGS="$CXXFLAGS -O3 -flto -ffunction-sections -fno-semantic-interposition -freorder-functions "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library tis
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library tis


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tis/COPYRIGHTS
/usr/lib64/R/library/tis/DESCRIPTION
/usr/lib64/R/library/tis/INDEX
/usr/lib64/R/library/tis/Meta/Rd.rds
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
/usr/lib64/R/library/tis/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/tis/libs/tis.so
