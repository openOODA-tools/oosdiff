Name:           oosdiff
Version:        0.1.0
Release:        1%{?dist}
Summary:        Side-by-side visual diff tool rendering interactive split terminals with sync scroll.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oosdiff
Source0:        oosdiff-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oosdiff is a sovereign, capability-bounded SIDE-BY-SIDE written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oosdiff
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oosdiff-uninstall

%files
/usr/bin/oosdiff
/usr/bin/oosdiff-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
