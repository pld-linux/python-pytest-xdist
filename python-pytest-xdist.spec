#
# Conditional build:
%bcond_without	python2		# CPython 2.x module
%bcond_with	python3		# CPython 3.x module (built from python3-pytest-xdist.spec)
%bcond_with	tests		# tests [sensitive to pytest warnings or other output changes, ptys needed]

Summary:	py.test distributed testing plugin
Summary(pl.UTF-8):	Wtyczka py.test do testów rozproszonych
Name:		python-pytest-xdist
# keep 1.x here for python2 support
Version:	1.34.0
Release:	6
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-xdist/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-xdist/pytest-xdist-%{version}.tar.gz
# Source0-md5:	23bcf5f0c6f1f84edced37d04b721281
URL:		https://github.com/pytest-dev/pytest-xdist
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
%if %{with tests}
BuildRequires:	python-execnet >= 1.1
BuildRequires:	python-filelock
BuildRequires:	python-py >= 1.4.22
BuildRequires:	python-pytest >= 4.4.0
BuildRequires:	python-pytest-forked
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-execnet >= 1.1
BuildRequires:	python3-filelock
BuildRequires:	python3-py >= 1.4.22
BuildRequires:	python3-pytest >= 4.4.0
BuildRequires:	python3-pytest-forked
BuildRequires:	python3-six
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The pytest-xdist plugin extends py.test with some unique test
execution modes, like parallelization.

%description -l pl.UTF-8
Wtyczka pytest-xdist rozszerza py.test o kilka unikatowych
trybów wykonywania testów, jak choćby zrównoleglenie.

%package -n python3-pytest-xdist
Summary:	py.test distributed testing plugin
Summary(pl.UTF-8):	Wtyczka py.test do testów rozproszonych
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-pytest-xdist
The pytest-xdist plugin extends py.test with some unique test
execution modes, like parallelization.

%description -n python3-pytest-xdist -l pl.UTF-8
Wtyczka pytest-xdist rozszerza py.test o kilka unikatowych
trybów wykonywania testów, jak choćby zrównoleglenie.

%prep
%setup -q -n pytest-xdist-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=xdist.plugin,xdist.looponfail \
PYTHONPATH=$(pwd) \
%{__python} -m pytest testing
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=xdist.plugin,xdist.looponfail \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest testing
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst ISSUES.txt LICENSE OVERVIEW.md README.rst example/boxed.txt
%{py_sitescriptdir}/xdist
%{py_sitescriptdir}/pytest_xdist-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-xdist
%defattr(644,root,root,755)
%doc CHANGELOG.rst ISSUES.txt LICENSE OVERVIEW.md README.rst example/boxed.txt
%{py3_sitescriptdir}/xdist
%{py3_sitescriptdir}/pytest_xdist-%{version}-py*.egg-info
%endif
