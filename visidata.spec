Summary:	A terminal interface for exploring and arranging tabular data
Name:		visidata
Version:	2.10.1
Release:	1
License:	GPL v3+
Group:		Applications
Source0:	https://github.com/saulpw/visidata/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	38acc0c580c9ccb32078d1b0485bbdb4
URL:		https://www.visidata.org/
BuildRequires:	python3
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
Suggests:	python3-lxml
Suggests:	python3-odfpy
Suggests:	python3-openpyxl
Suggests:	python3-tabulate
Suggests:	python3-xlrd
Suggests:	python3-xlwt
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VisiData is an interactive multitool for tabular data. It combines the
clarity of a spreadsheet, the efficiency of the terminal, and the
power of Python, into a lightweight utility which can handle millions
of rows with ease.

%prep
%setup -q

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vd
%attr(755,root,root) %{_bindir}/visidata
%{py3_sitescriptdir}/visidata
%{py3_sitescriptdir}/visidata-%{version}-py*.egg-info
%{_mandir}/man1/vd.1*
%{_mandir}/man1/visidata.1*
