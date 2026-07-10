%global tl_name autonum
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3.11
Release:	%{tl_revision}.1
Summary:	Automatic equation references
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/autonum
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/autonum.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/autonum.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/autonum.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package arranges that equation numbers are applied only to those
equations that are referenced. This operation is similar to the
showonlyrefs option of the package mathtools.

%prep
%setup -q -c -a1 -a2
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
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/autonum
%dir %{_datadir}/texmf-dist/source/latex/autonum
%dir %{_datadir}/texmf-dist/tex/latex/autonum
%doc %{_datadir}/texmf-dist/doc/latex/autonum/README
%doc %{_datadir}/texmf-dist/doc/latex/autonum/autonum.pdf
%doc %{_datadir}/texmf-dist/doc/latex/autonum/test-autonum.pdf
%doc %{_datadir}/texmf-dist/doc/latex/autonum/test-autonum.tex
%doc %{_datadir}/texmf-dist/doc/latex/autonum/test-freeze.tex
%doc %{_datadir}/texmf-dist/source/latex/autonum/autonum.dtx
%doc %{_datadir}/texmf-dist/source/latex/autonum/autonum.ins
%{_datadir}/texmf-dist/tex/latex/autonum/autonum.sty
