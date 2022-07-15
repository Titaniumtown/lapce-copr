Name:           lapce
Version:        0.1.3
Release:        1
Summary:        Lightning-fast and Powerful Code Editor written in Rust
License:        Apache-2.0
URL:            https://github.com/lapce/lapce
Source0:        https://github.com/lapce/lapce/archive/refs/tags/v0.1.3.tar.gz
BuildRequires:  cargo perl-FindBin cairo-devel cairo-gobject-devel atk-devel gdk-pixbuf2-devel pango-devel gtk3-devel

%description
Lapce is written in pure Rust, with the UI in Druid. It uses Xi-Editor's Rope
Science for text editing, and the Wgpu Graphics API for rendering.

%prep
%autosetup

%build
cargo build --profile release-lto

%install
install -Dm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE*
%doc *.md
%{_bindir}/%{name}

%changelog
* Fri Jul 15 2022 Simon Gardling <titaniumtown@gmail.com> - 0.1.3
- first created
