%global debug_package %{nil}

Name:           bandwidth
Version:        1.9.4
Release:        1
Summary:        Memory and network benchmark program
License:        GPL-2.0
Group:          System/Benchmark
URL:            https://zsmith.co/bandwidth.php
Source:         https://zsmith.co/archives/%{name}-%{version}.tar.gz

BuildRequires:  nasm

%description
bandwidth is an artificial benchmark primarily for measuring memory bandwidth
on x86 and x86_64 based computers, useful for identifying weaknesses in a
computer's memory subsystem, in the bus architecture, in the cache architecture
and in the processor itself.

%prep
%setup -q

%build
# currently fails with No rule to make target 'routines-arm-32bit.asm', needed by 'bandwidth-arm32'
%ifarch %{arm}
%make_build bandwidth-arm32
%endif

%ifarch %{ix86}
%make_build bandwidth32 CFLAGS="%{optflags}"
mv bandwidth32 %{name}
%endif

%ifarch %{x86_64}
%make_build bandwidth64 CFLAGS="%{optflags}"
mv bandwidth64 %{name}
%endif

%install
install -Dsm 755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%license GPL.txt
%doc README.txt
%{_bindir}/%{name}

