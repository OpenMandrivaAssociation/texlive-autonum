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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package arranges that equation numbers are applied only to those
equations that are referenced. This operation is similar to the
showonlyrefs option of the package mathtools.

