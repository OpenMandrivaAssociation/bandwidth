%global debug_package %{nil}

Name:           bandwidth
Version:        1.15.1
Release:        1
Summary:        Memory and network benchmark program
License:        GPL-2.0
Group:          System/Benchmark
URL:            http://zs3.me/bandwidth
Source:         https://zs3.me/bandwidth-%{version}.tar.bz2

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:  nasm

%description
bandwidth is an artificial benchmark primarily for measuring memory bandwidth
on x86 and x86_64 based computers, useful for identifying weaknesses in a
computer's memory subsystem, in the bus architecture, in the cache architecture
and in the processor itself.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
install -Dsm 755 %{name}* %{buildroot}/%{_bindir}/%{name}

%files
%license GPL.txt
%doc README.txt
%{_bindir}/%{name}

