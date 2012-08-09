# revision 27224
# category Package
# catalog-ctan /macros/latex/contrib/autonum
# catalog-date 2012-07-08 14:35:29 +0200
# catalog-license lppl1.3
# catalog-version 0.2
Name:		texlive-autonum
Version:	0.2
Release:	1
Summary:	Automatic equation references
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/autonum
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autonum.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autonum.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/autonum.source.tar.xz
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
#- source
%doc %{_texmfdistdir}/source/latex/autonum/autonum.dtx
%doc %{_texmfdistdir}/source/latex/autonum/autonum.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
