Name:		texlive-fontsize
Version:	60161
Release:	2
Summary:	A small package to set arbitrary sizes for the main font of the document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fontsize
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontsize.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontsize.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontsize.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows you to set arbitrary sizes for the main font
of the document, through the fontsize=<size> option.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/fontsize
%{_texmfdistdir}/tex/latex/fontsize
%doc %{_texmfdistdir}/doc/latex/fontsize

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
