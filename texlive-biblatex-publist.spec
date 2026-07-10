%global tl_name biblatex-publist
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.16
Release:	%{tl_revision}.1
Summary:	BibLaTeX bibliography support for publication lists
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-publist
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-publist.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-publist.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a BibLaTeX bibliography style file (*.bbx) for
publication lists. The style file draws on BibLaTeX's authoryear style,
but provides some extra features often desired for publication lists,
such as the omission of the author's own name from author or editor
data. At least version 3.4 of biblatex is required.

