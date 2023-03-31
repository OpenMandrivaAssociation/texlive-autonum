Name:		texlive-autonum
Version:	36084
Release:	2
Summary:	Automatic equation references
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/autonum
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autonum.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autonum.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autonum.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package arranges that equation numbers are applied only to
those equations that are referenced. This operation is similar
to the showonlyrefs option of the package mathtools.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/autonum/autonum.sty
%doc %{_texmfdistdir}/doc/latex/autonum/README
%doc %{_texmfdistdir}/doc/latex/autonum/autonum.pdf
%doc %{_texmfdistdir}/doc/latex/autonum/test-autonum.pdf
%doc %{_texmfdistdir}/doc/latex/autonum/test-autonum.tex
%doc %{_texmfdistdir}/doc/latex/autonum/test-freeze.tex
#- source
%doc %{_texmfdistdir}/source/latex/autonum/autonum.dtx
%doc %{_texmfdistdir}/source/latex/autonum/autonum.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
