%define modname Kivy

Name:           python-kivy
Version:        1.6.0
Release:        1
URL:            http://kivy.org/
Summary:        Hardware-accelerated multitouch application library
License:        LGPLv3
Group:          Development/Python
Source:         http://pypi.python.org/packages/source/K/%{modname}/%{modname}-%{version}.tar.gz
BuildRequires:  pkgconfig(gl)
BuildRequires:  python-cython
BuildRequires:  python-sphinx
BuildRequires:  python-devel
Requires:       mtdev
Requires:       python-imaging
Requires:       pygame

%description
Kivy is an open source software library for rapid development of applications
that make use of innovative user interfaces, such as multi-touch apps.

%package doc
Summary:        Hardware-accelerated multitouch application library - Documentation
Group:          Development/Python
Requires:       %{name} = %{version}

%description doc
Kivy is an open source software library for rapid development of applications
that make use of innovative user interfaces, such as multi-touch apps.

This package contains the developer documentation and examples

%prep
%setup -q -n %{modname}-%{version}
sed -i "s|data_file_prefix = 'share/kivy-'|data_file_prefix = '%{_docdir}/%{name}/'|" setup.py
sed -i "s|#!/usr/bin/python||" kivy/lib/osc/OSC.py # Fix non-executable script
rm examples/demo/pictures/images/.empty # Remove empty file
rm -r examples/audio # Remove content with non-commercial only license (bnc#749340)

%build
CFLAGS="%{optflags} -fno-strict-aliasing" python setup.py build
cd doc && make html && rm -r build/html/.buildinfo # Build HTML documentation

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%doc AUTHORS COPYING doc/README doc/build/html
%{python_sitearch}/*
%exclude %{_datadir}/doc/%{name}

%files doc
%{_datadir}/doc/%{name}
%exclude %{_datadir}/doc/%{name}/AUTHORS
%exclude %{_datadir}/doc/%{name}/COPYING
%exclude %{_datadir}/doc/%{name}/README


