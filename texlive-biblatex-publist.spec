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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a BibLaTeX bibliography style file (*.bbx) for
publication lists. The style file draws on BibLaTeX's authoryear style,
but provides some extra features often desired for publication lists,
such as the omission of the author's own name from author or editor
data. At least version 3.4 of biblatex is required.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-publist
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-publist
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-publist/lbx
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-publist/README
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-publist/biblatex-publist.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-publist/biblatex-publist.tex
%{_datadir}/texmf-dist/tex/latex/biblatex-publist/lbx/UKenglish-publist.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-publist/lbx/USenglish-publist.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-publist/lbx/american-publist.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-publist/lbx/australian-publist.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-publist/lbx/austrian-publist.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-publist/lbx/british-publist.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-publist/lbx/canadian-publist.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-publist/lbx/english-publist.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-publist/lbx/french-publist.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-publist/lbx/german-publist.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-publist/lbx/greek-publist.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-publist/lbx/naustrian-publist.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-publist/lbx/newzealand-publist.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-publist/lbx/ngerman-publist.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-publist/lbx/nswissgerman-publist.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-publist/lbx/swissgerman-publist.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-publist/publist.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-publist/publist.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-publist/publist.dbx
