%global srcname toolz

Name:           python-%{srcname}
Version:        1.2.0
Release:        1
Summary:        A functional standard library for Python
Group:          Development/Python
License:        BSD
URL:            https://github.com/pytoolz/%{srcname}/
Source0:        https://files.pythonhosted.org/packages/source/t/toolz/toolz-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)

%description
A set of utility functions for iterators, functions, and dictionaries.

%prep
%autosetup -p1 -n toolz-%{version}
# The sdist is not a git checkout, so pin the version instead of
# asking setuptools-git-versioning to read a tag.
sed -i \
	-e '/setuptools-git-versioning/d' \
	-e 's/dynamic = \["version"\]/version = "%{version}"/' \
	pyproject.toml

%build
%py_build

%install
%py_install


%files
%{python_sitelib}/toolz/
%{python_sitelib}/toolz-%{version}.dist-info/
%{python_sitelib}/tlz/
