# revision 31448
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-publist
# catalog-date 2013-08-16 15:58:19 +0200
# catalog-license lppl1.3
# catalog-version 0.8
Name:		texlive-biblatex-publist
Version:	0.8
Release:	4
Summary:	BibLaTeX bibliography support for publication lists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-publist
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-publist.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-publist.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a BibLaTeX bibliography style file (*.bbx)
for publication lists. The style file draws on BibLaTeX's
authoryear style, but provides some extra features often
desired for publication lists, such as the omission of the
author's own name from author or editor data.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-publist/publist.bbx
%doc %{_texmfdistdir}/doc/latex/biblatex-publist/README
%doc %{_texmfdistdir}/doc/latex/biblatex-publist/biblatex-publist.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-publist/biblatex-publist.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
