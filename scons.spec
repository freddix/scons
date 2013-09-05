Summary:	An Open Source software construction tool
Name:		scons
Version:	2.3.0
Release:	1
License:	MIT, freely distributable
Group:		Development/Tools
Source0:	http://downloads.sourceforge.net/scons/%{name}-%{version}.tar.gz
# Source0-md5:	083ce5624d6adcbdaf2526623f456ca9
URL:		http://www.scons.org/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	sed
%pyrequires_eq	python-modules
Requires:	python
Requires:	python-devel-tools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SCons is an Open Source software construction tool - that is, a build
tool; an improved substitute for the classic Make utility; a better
way to build software. SCons is based on the design which won the
Software Carpentry build tool design competition in August 2000.

%prep
%setup -q
%{__sed} -i "s,'lib','share',g" script/{scons,sconsign}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install			\
	--install-data=%{_datadir}		\
	--install-lib=%{py_sitescriptdir}	\
	--install-scripts=%{_bindir}		\
	--no-version-script			\
	--optimize=2				\
	--root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#LICENSE.txt must be added (read LICENSE.txt file)
%doc CHANGES.txt LICENSE.txt README.txt RELEASE.txt
%attr(755,root,root) %{_bindir}/scons*
%{py_sitescriptdir}/SCons
%{_mandir}/man1/scons*.1*

