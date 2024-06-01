%global debug_package %{nil}

Name:           bandwidth
Version:        1.14.10
Release:        1
Summary:        Memory and network benchmark program
License:        GPL-2.0
Group:          System/Benchmark
URL:            https://zsmith.co/bandwidth.php
Source:         https://zsmith.co/archives/%{name}-%{version}.tar.bz2

BuildRequires:  nasm

%description
bandwidth is an artificial benchmark primarily for measuring memory bandwidth
on x86 and x86_64 based computers, useful for identifying weaknesses in a
computer's memory subsystem, in the bus architecture, in the cache architecture
and in the processor itself.

%prep
%setup -q

%build
%configure
%make_build

%install
install -Dsm 755 %{name}* %{buildroot}/%{_bindir}/%{name}

%files
%license GPL.txt
%doc README.txt
%{_bindir}/%{name}

