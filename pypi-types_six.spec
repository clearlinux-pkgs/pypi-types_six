#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-types_six
Version  : 1.16.18
Release  : 14
URL      : https://files.pythonhosted.org/packages/cb/42/5572b4f4b215f93e023aada6d40f9950a5ee5f4b2d4e67214efd0efcf390/types-six-1.16.18.tar.gz
Source0  : https://files.pythonhosted.org/packages/cb/42/5572b4f4b215f93e023aada6d40f9950a5ee5f4b2d4e67214efd0efcf390/types-six-1.16.18.tar.gz
Summary  : Typing stubs for six
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-types_six-python = %{version}-%{release}
Requires: pypi-types_six-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
No detailed description available

%package python
Summary: python components for the pypi-types_six package.
Group: Default
Requires: pypi-types_six-python3 = %{version}-%{release}

%description python
python components for the pypi-types_six package.


%package python3
Summary: python3 components for the pypi-types_six package.
Group: Default
Requires: python3-core
Provides: pypi(types_six)

%description python3
python3 components for the pypi-types_six package.


%prep
%setup -q -n types-six-1.16.18
cd %{_builddir}/types-six-1.16.18
pushd ..
cp -a types-six-1.16.18 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657660283
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
