Name:		texlive-komacv
Version:	57721
Release:	2
Summary:	Typesetting a beautiful CV with various style options
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/komacv
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/komacv.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/komacv.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/komacv.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class simplifies the creation of beautiful CV. The user may
choose between different styles, and may adjust settings to
tune the output.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/komacv
%{_texmfdistdir}/tex/latex/komacv
%doc %{_texmfdistdir}/doc/latex/komacv

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
