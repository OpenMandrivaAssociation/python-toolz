%global srcname toolz

Name:           python-%{srcname}
Version:        0.12.0
Release:        1
Summary:        A functional standard library for Python
Group:          Development/Python
License:        BSD
URL:            https://github.com/pytoolz/%{srcname}/
Source0:        https://files.pythonhosted.org/packages/source/t/toolz/toolz-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
#BuildRequires:  python3dist(pytest)

%description
A set of utility functions for iterators, functions, and dictionaries.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%py_build

%install
%py_install


%files
%{python_sitelib}/toolz/
%{python_sitelib}/toolz-%{version}-py*.*.egg-info/
%{python_sitelib}/tlz/
