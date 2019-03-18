#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-polynom
Version  : 1.3.9
Release  : 7
URL      : https://cran.r-project.org/src/contrib/polynom_1.3-9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/polynom_1.3-9.tar.gz
Summary  : A Collection of Functions to Implement a Class for Univariate
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R

%description
'polynom' is an R collection of functions to implement a class for
univariate polynomial manipulations.  It is based on the corresponding S
package by Bill Venables <Bill.Venables@adelaide.edu.au>, and was
adapted to R by Kurt Hornik <Kurt.Hornik@R-project.org> and Martin
Maechler <maechler@stat.math.ethz.ch>.

%prep
%setup -q -c -n polynom

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552935666

%install
export SOURCE_DATE_EPOCH=1552935666
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library polynom
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library polynom
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library polynom
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  polynom || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/polynom/CITATION
/usr/lib64/R/library/polynom/DESCRIPTION
/usr/lib64/R/library/polynom/INDEX
/usr/lib64/R/library/polynom/Meta/Rd.rds
/usr/lib64/R/library/polynom/Meta/features.rds
/usr/lib64/R/library/polynom/Meta/hsearch.rds
/usr/lib64/R/library/polynom/Meta/links.rds
/usr/lib64/R/library/polynom/Meta/nsInfo.rds
/usr/lib64/R/library/polynom/Meta/package.rds
/usr/lib64/R/library/polynom/NAMESPACE
/usr/lib64/R/library/polynom/R/polynom
/usr/lib64/R/library/polynom/R/polynom.rdb
/usr/lib64/R/library/polynom/R/polynom.rdx
/usr/lib64/R/library/polynom/help/AnIndex
/usr/lib64/R/library/polynom/help/aliases.rds
/usr/lib64/R/library/polynom/help/paths.rds
/usr/lib64/R/library/polynom/help/polynom.rdb
/usr/lib64/R/library/polynom/help/polynom.rdx
/usr/lib64/R/library/polynom/html/00Index.html
/usr/lib64/R/library/polynom/html/R.css
