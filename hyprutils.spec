Summary:	Hyprland utilities library used across the ecosystem
Name:		hyprutils
Version:	0.5.0
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/hyprwm/hyprutils/releases
Source0:	https://github.com/hyprwm/hyprutils/archive/v%{version}/%{name}-v%{version}.tar.gz
# Source0-md5:	3542ccccb38242f336362c5d43460468
Patch0:		flags.patch
URL:		https://hyprland.org/
BuildRequires:	cmake >= 3.19
BuildRequires:	libstdc++-devel >= 6:11
BuildRequires:	pixman-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hyprutils is a small C++ library for utilities used across the Hypr*
ecosystem.

%package devel
Summary:	Header files for hyprutils
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for hyprutils.

%prep
%setup -q
%patch -P0 -p1

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_libdir}/libhyprutils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhyprutils.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhyprutils.so
%{_includedir}/hyprutils
%{_pkgconfigdir}/hyprutils.pc
