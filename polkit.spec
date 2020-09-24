#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x8CEB3030FFDCE258 (jrybar@redhat.com)
#
Name     : polkit
Version  : 0.117
Release  : 21
URL      : https://www.freedesktop.org/software/polkit/releases/polkit-0.117.tar.gz
Source0  : https://www.freedesktop.org/software/polkit/releases/polkit-0.117.tar.gz
Source1  : https://www.freedesktop.org/software/polkit/releases/polkit-0.117.tar.gz.sign
Summary  : PolicyKit Authorization API
Group    : Development/Tools
License  : Apache-2.0 LGPL-2.0
Requires: polkit-bin = %{version}-%{release}
Requires: polkit-data = %{version}-%{release}
Requires: polkit-lib = %{version}-%{release}
Requires: polkit-license = %{version}-%{release}
Requires: polkit-locales = %{version}-%{release}
Requires: polkit-services = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : docbook-xml
BuildRequires : expat-dev
BuildRequires : gettext
BuildRequires : gettext-bin
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : libxslt-bin
BuildRequires : m4
BuildRequires : perl(XML::Parser)
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(mozjs-68)
Patch1: 0001-data-Use-stateless-system-directories-for-d-bus-PAM-.patch
Patch2: 0002-pkexec-Support-a-stateless-configuration.patch
Patch3: 0003-Don-t-complain-about-etc-polkit-2-rules.d-missing.patch
Patch4: more-gc.patch

%description
OVERVIEW
========
polkit is a toolkit for defining and handling authorizations.  It is
used for allowing unprivileged processes to speak to privileged
processes.

%package bin
Summary: bin components for the polkit package.
Group: Binaries
Requires: polkit-data = %{version}-%{release}
Requires: polkit-license = %{version}-%{release}
Requires: polkit-services = %{version}-%{release}

%description bin
bin components for the polkit package.


%package data
Summary: data components for the polkit package.
Group: Data

%description data
data components for the polkit package.


%package dev
Summary: dev components for the polkit package.
Group: Development
Requires: polkit-lib = %{version}-%{release}
Requires: polkit-bin = %{version}-%{release}
Requires: polkit-data = %{version}-%{release}
Provides: polkit-devel = %{version}-%{release}
Requires: polkit = %{version}-%{release}

%description dev
dev components for the polkit package.


%package lib
Summary: lib components for the polkit package.
Group: Libraries
Requires: polkit-data = %{version}-%{release}
Requires: polkit-license = %{version}-%{release}

%description lib
lib components for the polkit package.


%package license
Summary: license components for the polkit package.
Group: Default

%description license
license components for the polkit package.


%package locales
Summary: locales components for the polkit package.
Group: Default

%description locales
locales components for the polkit package.


%package services
Summary: services components for the polkit package.
Group: Systemd services

%description services
services components for the polkit package.


%prep
%setup -q -n polkit-0.117
cd %{_builddir}/polkit-0.117
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1598917480
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
%reconfigure --disable-static --disable-gtk-doc-html --disable-man-pages --enable-libsystemd-login --with-os-type=ClearLinux
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1598917480
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/polkit
cp %{_builddir}/polkit-0.117/COPYING %{buildroot}/usr/share/package-licenses/polkit/d83b6378d06fdf228b1afc0bf97e09b44bbb2e7b
cp %{_builddir}/polkit-0.117/docs/polkit/html/license.html %{buildroot}/usr/share/package-licenses/polkit/ad3ea1bdee758f528b9d0baa4f92e548d64180d9
cp %{_builddir}/polkit-0.117/test/mocklibc/COPYING %{buildroot}/usr/share/package-licenses/polkit/2b8b815229aa8a61e483fb4ba0588b8b6c491890
%make_install
%find_lang polkit-1

%files
%defattr(-,root,root,-)
/usr/lib/polkit-1/polkit-agent-helper-1
/usr/lib/polkit-1/polkitd

%files bin
%defattr(-,root,root,-)
/usr/bin/pk-example-frobnicate
/usr/bin/pkaction
/usr/bin/pkcheck
/usr/bin/pkexec
/usr/bin/pkttyagent

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Polkit-1.0.typelib
/usr/lib64/girepository-1.0/PolkitAgent-1.0.typelib
/usr/share/dbus-1/system-services/org.freedesktop.PolicyKit1.service
/usr/share/dbus-1/system.d/org.freedesktop.PolicyKit1.conf
/usr/share/gettext/its/polkit.its
/usr/share/gettext/its/polkit.loc
/usr/share/gir-1.0/*.gir
/usr/share/pam.d/polkit-1
/usr/share/polkit-1/actions/org.freedesktop.policykit.examples.pkexec.policy
/usr/share/polkit-1/actions/org.freedesktop.policykit.policy
/usr/share/polkit-1/rules.d/50-default.rules

%files dev
%defattr(-,root,root,-)
/usr/include/polkit-1/polkit/polkit.h
/usr/include/polkit-1/polkit/polkitactiondescription.h
/usr/include/polkit-1/polkit/polkitauthority.h
/usr/include/polkit-1/polkit/polkitauthorityfeatures.h
/usr/include/polkit-1/polkit/polkitauthorizationresult.h
/usr/include/polkit-1/polkit/polkitcheckauthorizationflags.h
/usr/include/polkit-1/polkit/polkitdetails.h
/usr/include/polkit-1/polkit/polkitenumtypes.h
/usr/include/polkit-1/polkit/polkiterror.h
/usr/include/polkit-1/polkit/polkitidentity.h
/usr/include/polkit-1/polkit/polkitimplicitauthorization.h
/usr/include/polkit-1/polkit/polkitpermission.h
/usr/include/polkit-1/polkit/polkitprivate.h
/usr/include/polkit-1/polkit/polkitsubject.h
/usr/include/polkit-1/polkit/polkitsystembusname.h
/usr/include/polkit-1/polkit/polkittemporaryauthorization.h
/usr/include/polkit-1/polkit/polkittypes.h
/usr/include/polkit-1/polkit/polkitunixgroup.h
/usr/include/polkit-1/polkit/polkitunixnetgroup.h
/usr/include/polkit-1/polkit/polkitunixprocess.h
/usr/include/polkit-1/polkit/polkitunixsession.h
/usr/include/polkit-1/polkit/polkitunixuser.h
/usr/include/polkit-1/polkitagent/polkitagent.h
/usr/include/polkit-1/polkitagent/polkitagentenumtypes.h
/usr/include/polkit-1/polkitagent/polkitagentlistener.h
/usr/include/polkit-1/polkitagent/polkitagentsession.h
/usr/include/polkit-1/polkitagent/polkitagenttextlistener.h
/usr/include/polkit-1/polkitagent/polkitagenttypes.h
/usr/lib64/libpolkit-agent-1.so
/usr/lib64/libpolkit-gobject-1.so
/usr/lib64/pkgconfig/polkit-agent-1.pc
/usr/lib64/pkgconfig/polkit-gobject-1.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpolkit-agent-1.so.0
/usr/lib64/libpolkit-agent-1.so.0.0.0
/usr/lib64/libpolkit-gobject-1.so.0
/usr/lib64/libpolkit-gobject-1.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/polkit/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/polkit/ad3ea1bdee758f528b9d0baa4f92e548d64180d9
/usr/share/package-licenses/polkit/d83b6378d06fdf228b1afc0bf97e09b44bbb2e7b

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/polkit.service

%files locales -f polkit-1.lang
%defattr(-,root,root,-)

