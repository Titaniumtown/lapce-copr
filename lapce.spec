Name:           lapce
Version:        0.1.3
Release:        3
Summary:        Lightning-fast and Powerful Code Editor written in Rust
License:        Apache-2.0
URL:            https://github.com/lapce/lapce
Source0:        https://github.com/lapce/lapce/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cargo perl-FindBin cairo-devel cairo-gobject-devel atk-devel gdk-pixbuf2-devel pango-devel gtk3-devel perl-lib perl-File-Compare mold clang

%description
Lapce is written in pure Rust with a UI in Druid (which is also written in Rust).
It is designed with Rope Science from the Xi-Editor which makes for lightning-fast computation, and leverages OpenGL for rendering.

%prep
%autosetup

%build
RUSTFLAGS="-C linker=clang -C link-arg=-fuse-ld=mold" cargo build --profile release-lto

%install
install -Dm755 target/release-lto/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm755 target/release-lto/%{name}-proxy %{buildroot}%{_bindir}/%{name}-proxy
install -Dm755 extra/linux/dev.lapce.lapce.desktop %{buildroot}/usr/share/applications/dev.lapce.lapce.desktop
install -Dm766 extra/linux/dev.lapce.lapce.metainfo.xml %{buildroot}/usr/share/metainfo/dev.lapce.lapce.metainfo.xml
install -Dm766 extra/images/logo.png %{buildroot}/usr/share/pixmaps/dev.lapce.lapce.png

%files
%license LICENSE*
%doc *.md
%{_bindir}/%{name}
%{_bindir}/%{name}-proxy
/usr/share/applications/dev.lapce.lapce.desktop
/usr/share/metainfo/dev.lapce.lapce.metainfo.xml
/usr/share/pixmaps/dev.lapce.lapce.png

%changelog
* Fri Jul 15 2022 Simon Gardling <titaniumtown@gmail.com> - 0.1.3
- first created
