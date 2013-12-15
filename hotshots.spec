######################################################
# SpecFile: hotshots.spec 
# Generato: http://www.mandrivausers.ro/
# MRB-Falticska Florin
######################################################
#define  distsuffix mrb
#define debug_package   %{nil}
# lang 
%define _files_listed_twice_terminate_build 0

Name:           hotshots
Version:        2.0.0
Release:        1
License:        GPLv2+
Summary:        Screen-shot and Annotation Tool
URL:            https://sourceforge.net/projects/hotshots/
Group:          Graphics
Source0:        http://sourceforge.net/projects/hotshots/files/%{version}/HotShots-%{version}-src.zip
BuildRequires:  imagemagick
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqxt-devel
BuildRequires:  qt4-devel
BuildRequires:  desktop-file-utils



%description
HotShots is an application for capturing screens and saving them in
a variety of image formats as well as adding annotations and graphical
data (arrows, lines, texts, ...).

%prep
%setup -qn HotShots-%{version}-src
sed -i 's/\r$//' *.txt

%build
cd build
%qmake_qt4 \
    QMAKE_CFLAGS+="%{optflags}" \
    QMAKE_CXXFLAGS+="%{optflags}" \
    QMAKE_STRIP="true" \
    INSTALL_PREFIX=%{_prefix} 
%make

%install
pushd build
make INSTALL_ROOT=%{buildroot} install
popd

# icons
rm -f %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -Dm 0644 res/%{name}.png \
    %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
for size in 96x96 64x64 48x48 32x32 22x22 16x16 ; do
    install -dm 0755 \
        %{buildroot}%{_datadir}/icons/hicolor/${size}/apps
    convert -strip -resize ${size} res/%{name}.png \
        %{buildroot}%{_datadir}/icons/hicolor/${size}/apps/%{name}.png
done
# menu entry
cd build
desktop-file-install %{name}.desktop \
  --dir=%{buildroot}%{_datadir}/applications \
  --remove-key=Version \
  --remove-key=Icon \
  --set-icon=%{name} \
  --remove-key=GenericName \
  --remove-category=Utility \
  --remove-category=Application \
  --add-category=Qt \
  --add-category=KDE \
  --add-category=Graphics 
cd -


%files
%doc *.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_mandir}/man?/*
%{_datadir}/%{name}
%{_datadir}/application/hotshots.desktop
%{_datadir}/mime/packages/hotshots.xml
%lang(cs) %{_datadir}/%{name}/locale/hotshots_cs.qm
%lang(de) %{_datadir}/%{name}/locale/hotshots_de.qm
%lang(el) %{_datadir}/%{name}/locale/hotshots_el.qm
%lang(es) %{_datadir}/%{name}/locale/hotshots_es.qm
%lang(eu) %{_datadir}/%{name}/locale/hotshots_eu.qm
%lang(fr) %{_datadir}/%{name}/locale/hotshots_fr.qm
%lang(gl) %{_datadir}/%{name}/locale/hotshots_gl.qm
%lang(it) %{_datadir}/%{name}/locale/hotshots_it.qm
%lang(ja) %{_datadir}/%{name}/locale/hotshots_ja.qm
%lang(lt) %{_datadir}/%{name}/locale/hotshots_lt.qm
%lang(pl) %{_datadir}/%{name}/locale/hotshots_pl.qm
%lang(ro) %{_datadir}/%{name}/locale/hotshots_ro.qm
%lang(ru) %{_datadir}/%{name}/locale/hotshots_ru.qm
%lang(si) %{_datadir}/%{name}/locale/hotshots_si.qm
%lang(sk) %{_datadir}/%{name}/locale/hotshots_sk.qm
%lang(sr) %{_datadir}/%{name}/locale/hotshots_sr.qm
%lang(tr) %{_datadir}/%{name}/locale/hotshots_tr.qm
%lang(uk) %{_datadir}/%{name}/locale/hotshots_uk.qm
%lang(vi) %{_datadir}/%{name}/locale/hotshots_vi.qm
%lang(zh) %{_datadir}/%{name}/locale/hotshots_zh.qm
