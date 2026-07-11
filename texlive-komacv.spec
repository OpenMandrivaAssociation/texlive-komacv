%global tl_name komacv
%global tl_revision 57721

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.2
Release:	%{tl_revision}.1
Summary:	Typesetting a beautiful CV with various style options
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/komacv
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/komacv.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/komacv.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/komacv.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class simplifies the creation of beautiful CV. The user may choose
between different styles, and may adjust settings to tune the output.

