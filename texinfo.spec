#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : texinfo
Version  : 6.3
Release  : 17
URL      : http://mirrors.kernel.org/gnu/texinfo/texinfo-6.3.tar.xz
Source0  : http://mirrors.kernel.org/gnu/texinfo/texinfo-6.3.tar.xz
Summary  : East Asian Width properties
Group    : Development/Tools
License  : GFDL-1.3 GPL-3.0 GPL-3.0+ LGPL-2.1 MIT
Requires: texinfo-bin
Requires: texinfo-doc
Requires: texinfo-locales
Requires: texinfo-data
BuildRequires : ncurses-dev
BuildRequires : procps-ng

%description
the preferred documentation format for GNU software.
2002, 2003, 2004, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016

%package bin
Summary: bin components for the texinfo package.
Group: Binaries
Requires: texinfo-data

%description bin
bin components for the texinfo package.


%package data
Summary: data components for the texinfo package.
Group: Data

%description data
data components for the texinfo package.


%package doc
Summary: doc components for the texinfo package.
Group: Documentation

%description doc
doc components for the texinfo package.


%package locales
Summary: locales components for the texinfo package.
Group: Default

%description locales
locales components for the texinfo package.


%prep
%setup -q -n texinfo-6.3

%build
export LANG=C
%configure --disable-static --without-readline
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang texinfo_document
%find_lang texinfo

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/info
/usr/bin/install-info
/usr/bin/makeinfo
/usr/bin/pdftexi2dvi
/usr/bin/pod2texi
/usr/bin/texi2any
/usr/bin/texi2dvi
/usr/bin/texi2pdf
/usr/bin/texindex

%files data
%defattr(-,root,root,-)
/usr/share/texinfo/DebugTexinfo/DebugCount.pm
/usr/share/texinfo/DebugTexinfo/DebugTree.pm
/usr/share/texinfo/Pod-Simple-Texinfo/Pod/Simple/Texinfo.pm
/usr/share/texinfo/Texinfo/Common.pm
/usr/share/texinfo/Texinfo/Convert/Converter.pm
/usr/share/texinfo/Texinfo/Convert/DocBook.pm
/usr/share/texinfo/Texinfo/Convert/HTML.pm
/usr/share/texinfo/Texinfo/Convert/IXIN.pm
/usr/share/texinfo/Texinfo/Convert/IXINSXML.pm
/usr/share/texinfo/Texinfo/Convert/Info.pm
/usr/share/texinfo/Texinfo/Convert/Line.pm
/usr/share/texinfo/Texinfo/Convert/NodeNameNormalization.pm
/usr/share/texinfo/Texinfo/Convert/Paragraph.pm
/usr/share/texinfo/Texinfo/Convert/ParagraphNonXS.pm
/usr/share/texinfo/Texinfo/Convert/PlainTexinfo.pm
/usr/share/texinfo/Texinfo/Convert/Plaintext.pm
/usr/share/texinfo/Texinfo/Convert/Texinfo.pm
/usr/share/texinfo/Texinfo/Convert/TexinfoSXML.pm
/usr/share/texinfo/Texinfo/Convert/TexinfoXML.pm
/usr/share/texinfo/Texinfo/Convert/Text.pm
/usr/share/texinfo/Texinfo/Convert/TextContent.pm
/usr/share/texinfo/Texinfo/Convert/UnFilled.pm
/usr/share/texinfo/Texinfo/Convert/Unicode.pm
/usr/share/texinfo/Texinfo/Documentlanguages.pm
/usr/share/texinfo/Texinfo/Encoding.pm
/usr/share/texinfo/Texinfo/ModulePath.pm
/usr/share/texinfo/Texinfo/Parser.pm
/usr/share/texinfo/Texinfo/Report.pm
/usr/share/texinfo/Texinfo/Structuring.pm
/usr/share/texinfo/htmlxref.cnf
/usr/share/texinfo/init/book.pm
/usr/share/texinfo/init/chm.pm
/usr/share/texinfo/init/html32.pm
/usr/share/texinfo/init/latex2html.pm
/usr/share/texinfo/init/tex4ht.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x00.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x01.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x02.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x03.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x04.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x05.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x06.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x07.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x09.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x0a.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x0b.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x0c.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x0d.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x0e.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x0f.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x10.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x11.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x12.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x13.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x14.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x15.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x16.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x17.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x18.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x1e.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x1f.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x20.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x21.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x22.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x23.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x24.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x25.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x26.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x27.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x28.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x2e.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x2f.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x30.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x31.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x32.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x33.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x4d.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x4e.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x4f.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x50.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x51.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x52.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x53.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x54.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x55.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x56.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x57.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x58.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x59.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x5a.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x5b.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x5c.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x5d.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x5e.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x5f.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x60.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x61.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x62.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x63.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x64.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x65.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x66.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x67.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x68.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x69.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x6a.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x6b.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x6c.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x6d.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x6e.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x6f.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x70.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x71.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x72.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x73.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x74.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x75.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x76.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x77.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x78.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x79.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x7a.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x7b.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x7c.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x7d.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x7e.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x7f.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x80.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x81.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x82.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x83.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x84.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x85.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x86.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x87.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x88.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x89.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x8a.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x8b.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x8c.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x8d.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x8e.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x8f.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x90.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x91.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x92.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x93.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x94.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x95.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x96.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x97.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x98.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x99.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x9a.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x9b.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x9c.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x9d.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x9e.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/x9f.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xa0.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xa1.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xa2.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xa3.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xa4.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xac.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xad.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xae.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xaf.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xb0.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xb1.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xb2.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xb3.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xb4.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xb5.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xb6.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xb7.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xb8.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xb9.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xba.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xbb.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xbc.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xbd.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xbe.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xbf.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xc0.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xc1.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xc2.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xc3.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xc4.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xc5.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xc6.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xc7.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xc8.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xc9.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xca.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xcb.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xcc.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xcd.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xce.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xcf.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xd0.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xd1.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xd2.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xd3.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xd4.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xd5.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xd6.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xd7.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xf9.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xfa.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xfb.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xfc.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xfd.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xfe.pm
/usr/share/texinfo/lib/Text-Unidecode/lib/Text/Unidecode/xff.pm
/usr/share/texinfo/lib/Unicode-EastAsianWidth/lib/Unicode/EastAsianWidth.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/Messages.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/Recode.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/Recode/_Aliases.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/Recode/_Conversions.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/ASMO_449.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/ATARI_ST.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/ATARI_ST_EURO.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/CP10007.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/CP1250.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/CP1251.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/CP1252.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/CP1253.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/CP1254.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/CP1256.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/CP1257.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/CSN_369103.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/CWI.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/DEC_MCS.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/EBCDIC_AT_DE.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/EBCDIC_AT_DE_A.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/EBCDIC_CA_FR.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/EBCDIC_DK_NO.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/EBCDIC_DK_NO_A.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/EBCDIC_ES.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/EBCDIC_ES_A.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/EBCDIC_ES_S.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/EBCDIC_FI_SE.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/EBCDIC_FI_SE_A.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/EBCDIC_FR.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/EBCDIC_IS_FRISS.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/EBCDIC_IT.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/EBCDIC_PT.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/EBCDIC_UK.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/EBCDIC_US.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/ECMA_CYRILLIC.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/GEORGIAN_ACADEMY.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/GEORGIAN_PS.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/GOST_19768_74.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/GREEK7.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/GREEK7_OLD.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/GREEK_CCITT.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/HP_ROMAN8.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM037.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM038.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM1004.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM1026.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM1047.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM256.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM273.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM274.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM275.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM277.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM278.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM280.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM281.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM284.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM285.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM290.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM297.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM420.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM423.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM424.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM437.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM500.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM850.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM851.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM852.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM855.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM857.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM860.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM861.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM862.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM863.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM864.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM865.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM866.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM868.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM869.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM870.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM871.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM874.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM875.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM880.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM891.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM903.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM904.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM905.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IBM918.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/IEC_P27_1.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/INIS.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/INIS_8.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/INIS_CYRILLIC.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/ISO_10367_BOX.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/ISO_2033_1983.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/ISO_5427.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/ISO_5427_EXT.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/ISO_5428.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/ISO_8859_1.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/ISO_8859_10.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/ISO_8859_11.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/ISO_8859_13.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/ISO_8859_14.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/ISO_8859_15.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/ISO_8859_16.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/ISO_8859_2.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/ISO_8859_3.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/ISO_8859_4.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/ISO_8859_5.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/ISO_8859_6.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/ISO_8859_7.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/ISO_8859_8.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/ISO_8859_9.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/KOI8_R.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/KOI8_RU.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/KOI8_T.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/KOI8_U.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/KOI_8.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/LATIN_GREEK.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/LATIN_GREEK_1.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/MACARABIC.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/MACCROATIAN.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/MACCYRILLIC.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/MACGREEK.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/MACHEBREW.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/MACICELAND.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/MACINTOSH.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/MACROMANIA.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/MACTHAI.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/MACTURKISH.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/MACUKRAINE.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/MAC_IS.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/MAC_SAMI.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/MAC_UK.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/NATS_DANO.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/NATS_SEFI.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/NEXTSTEP.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/SAMI_WS2.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/TIS_620.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/US_ASCII.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/UTF_8.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/VISCII.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/RecodeData/_Encode.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/TextDomain.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/Util.pm
/usr/share/texinfo/lib/libintl-perl/lib/Locale/gettext_pp.pm
/usr/share/texinfo/texindex.awk
/usr/share/texinfo/texinfo.dtd

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*

%files locales -f texinfo_document.lang -f texinfo.lang 
%defattr(-,root,root,-)

