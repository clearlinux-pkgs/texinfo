#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDDBC579DAB37FBA9 (GavinSmith0123@gmail.com)
#
Name     : texinfo
Version  : 6.6
Release  : 24
URL      : http://mirrors.kernel.org/gnu/texinfo/texinfo-6.6.tar.xz
Source0  : http://mirrors.kernel.org/gnu/texinfo/texinfo-6.6.tar.xz
Source99 : http://mirrors.kernel.org/gnu/texinfo/texinfo-6.6.tar.xz.sig
Summary  : East Asian Width properties
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+ LGPL-2.1 MIT
Requires: texinfo-bin = %{version}-%{release}
Requires: texinfo-data = %{version}-%{release}
Requires: texinfo-lib = %{version}-%{release}
Requires: texinfo-license = %{version}-%{release}
Requires: texinfo-locales = %{version}-%{release}
Requires: texinfo-man = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : glibc-locale
BuildRequires : ncurses-dev
BuildRequires : nodejs
BuildRequires : procps-ng

%description
This file describes each of the numbered install-info tests.
0001: The 99% case. Installing an Info file.  Take a single entry from the
Info file and put it into a pre-existing section in the DIR file.
0002: Installing an Info file.  Take two entries from the Info file and put
it into a pre-existing section in the DIR file.
0003: Installing an Info file.  Take two entries from the Info file and put
it into a pre-existing section in the DIR file.  The entries are
described in two different `START-INFO-DIR-ENTRY' declarations.
0004: Installing an Info file.  Take two entries from the Info file and put
it into two pre-existing sections in the DIR file.  The entries are
described in two different `INFO-DIR-SECTION' and `START-INFO-DIR-ENTRY'
declarations.
0005: Installing an Info file.  Take two entries from the Info file and put
it into one pre-existing section and one non-existing section in the
DIR file.  The entries are described in two different `INFO-DIR-SECTION'
and `START-INFO-DIR-ENTRY' declarations.
0006: The 99% case, try 2.  Installing an Info file.  Take a single entry
from the Info file and put it into a pre-existing section in the DIR
file, but this time the name is not capitalized.
0007: The 99% case, try 3.  Installing an Info file.  Take a single entry
from the Info file and put it into a pre-existing section in the DIR
file, but this time the entry is not the final entry in the section.
0008: The 99% case, try 4.  Installing an Info file.  Take a single entry
from the Info file and put it into a pre-existing section in the DIR
file, but this time the entry's description spans more than one line.
0009: The 99% case, try 5.  Installing an Info file.  Take a single entry
from the Info file and put it into a pre-existing section in the DIR
file, but this time the entry's description does not start on the
33rd column and requires indentation.
0010: The 99% case, try 6.  Installing an Info file.  Take a single entry
from the Info file and put it into a pre-existing section in the DIR
file, but this time the entry's one line description requires
multi-line indentation.
0011: Installing an Info file.  Take a single entry from the Info file and
put it into a pre-existing section in the DIR file, but this time do
not indent the description.
0012: Installing an Info file.  Take a single entry from the Info file and
put it into a pre-existing section in the DIR file, but this time the
entry already exists and will be replaced.
0013: Installing an Info file.  Take a single entry from the Info file and
put it into a pre-existing section in the DIR file, but this time the
entry already exists and the --keep-old option is used to override the
replacement.
0014: Installing an Info file.  Take a single entry from the Info file and
put it into a pre-existing section in the DIR file, but this time the
entry already exists with a multi-line description and will be
replaced with a single-line description.
0015: Installing an Info file.  Take a single entry from the Info file and
put it into a pre-existing section in the DIR file, but this time the
entry already exists with a single-line description and will be
replaced with a multi-line description.
0016: Installing an Info file.  The Info file does not contain section or
entry hints, and neither a section nor an entry is specified on the
command-line.  Installation does not occur, but is not an error.
0017: Installing an initial Info file into a minimal DIR file.
0018: Installing an initial Info file into an empty (0 byte) DIR file.
Installation does not occur, and is an error.
0019: Installing an initial Info file into an empty (2 byte) DIR file.
Installation does not occur, and is an error.
0020: Installing an Info file.  The Info file does not contain section or
entry hints, and a section is not specified on the command-line, but
a --description is.
0021: Installing an Info file.  The Info file does not contain section or
entry hints, and a pre-existing --section is stated on the command-line
along with a --description.
0022: Installing an Info file.  The Info file does not contain section or
entry hints, and a --name is specified on the command-line.  The NAME
starts with *, so the whole name (up to the period) is replaced.
0023: Installing an Info file.  The Info file does not contain section or
entry hints, and a --name is specified on the command-line.  The NAME
does not start with a *, so just the name (up to the colon) is replaced.
0024: Installing an Info file.  The Info file contains section and entry
hints, but we override the section with a non-existing one from the
command-line.
0025: Installing an Info file.  The Info file contains section and entry
hints, but we override the section with an existing one from the
command-line.
0026: Installing an Info file.  The Info file contains section and entry
hints, but we override the entry with an --entry on the command-line.
0027: Installing an Info file.  The Info file contains section and entry
hints, but we override the entry with an --entry on the command-line,
and we also override the section with a --section on the command-line.
0028: Installing an Info file.  The Info file contains section and entry
hints, but we override the name portion of the entry with a --name
on the command-line.  The NAME starts with a `*' so it replaces the
entire name, up to the period.
0029: Installing an Info file.  The Info file contains section and entry
hints, but we override the name portion of the entry with a --name
on the command-line.  The NAME does not start with a `*' so it
replaces the name, up to the colon and presumes the basename.
0030: Installing an Info file.  The Info file contains section and entry
hints, but we override the description portion of the entry with a
--description on the command-line.
0031: Installing an Info file.  The Info file contains section and entry
hints, but we override the description and the name with
--description and --name options on the command-line.  The NAME starts
with a `*' so it replaces the entire name, up to the period.
0032: Installing an Info file.  The Info file contains section and entry
hints, but we try to override the section with a regular expression
that does not match any existing sections in the DIR file.  The
overriding cannot take place, and the entry is installed in the section
specified in the Info file.
0033: Installing an Info file.  The Info file contains an entry hint, but no
section hint.  We try to specify the section with a --regex option on
the command-line, but the regular expression does not match any
existing sections in the DIR file.
0034: Installing an Info file.  The Info file contains an entry hint, but
no section hint, and we try to specify the section with a regular
expression that does not match any existing sections in the DIR file.
We also specify a --section on the command-line to ensure that the
entry will be installed in a section that we explicitly name.
0035: Installing an Info file.  The Info file contains section and entry
hints, but we try to specify the section with a regular expression
that does not match any existing sections in the DIR file.  We also
specify a --section on the command-line to ensure that the entry will
be installed in a section that we explicitly name.
0036: Installing an Info file.  The Info file contains entry and section
hints, but try to specify the section with a --regex option on
the command-line, and the regular expression matches an existing
section in the DIR file.
0037: Installing an Info file.  The Info file contains section and entry
hints, but we try to specify the section with a regular expression
that does not match any existing sections in the DIR file.  We also
specify a --section on the command-line to ensure that the entry will
be installed in a section that we explicitly name.  We use the
alternative Debian --section REGEX TITLE syntax instead of the normal
GNU syntax.
0038: Installing an Info file.  The Info file does not contain section or
entry hints, and we specify that two entries go into two sections on
the command-line.  One section already exists, and the other doesn't.
0039: Installing an Info file.  The Info file contains section and entry
hints, but we override the entry with an --entry option on the
command-line.  The entry has a multi-line description and is not
indented.
0040: Installing an Info file.  The Info file contains section and entry
hints, but we override the entry with --name and --description options
on the command-line.  The entry is not indented.
0041: Installing an Info file.  The Info file contains section and entry
hints, and we're installing the entry into a gzipped DIR file.
0042: Installing an Info file.  The Info file contains section and entry
hints for two entries in two sections.  Both of the sections do not
already exist in the DIR file.  The sections will be added prior to
all other sections due to the alphabetic ordering of section names.
0043: Installing an Info file.  The Info file contains section and entry
hints, and we're going to install the new section admist many other
sections.  E.g. instead of always at the very bottom or at the very
top.
0044: The 99% case.  Removing an Info file.  The Info file is responsible
for a single entry in the DIR file.
0045: Removing an Info file.  The Info file is responsible for many entries
in the DIR file.
0046: Removing an Info file.  We no longer have the Info file, so we
specify --remove-exactly to remove it instead.
0047: Removing an Info file.  The Info file is responsible for the final
entry in the DIR file.  The section also gets removed.
0048: Removing an Info file.  The Info file is responsible for the final
entry in the DIR file, but we want to keep the section heading, so
we specify --keep-old.
0049: Removing an Info file.  The Info file is not responsible for any
entries in the DIR file.  A warning is issued, but it isn't an error.
0050: Removing an Info file.  The Info file is responsible for a single
entry in the gzipped DIR file.
0051: Allow periods in menu item name, e.g., config.status.
0052: Allow periods in node name also, e.g., "config.status Invocation".
0053: Check newline handling in input dir entries.

%package bin
Summary: bin components for the texinfo package.
Group: Binaries
Requires: texinfo-data = %{version}-%{release}
Requires: texinfo-license = %{version}-%{release}
Requires: texinfo-man = %{version}-%{release}

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
Requires: texinfo-man = %{version}-%{release}

%description doc
doc components for the texinfo package.


%package lib
Summary: lib components for the texinfo package.
Group: Libraries
Requires: texinfo-data = %{version}-%{release}
Requires: texinfo-license = %{version}-%{release}

%description lib
lib components for the texinfo package.


%package license
Summary: license components for the texinfo package.
Group: Default

%description license
license components for the texinfo package.


%package locales
Summary: locales components for the texinfo package.
Group: Default

%description locales
locales components for the texinfo package.


%package man
Summary: man components for the texinfo package.
Group: Default

%description man
man components for the texinfo package.


%prep
%setup -q -n texinfo-6.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1550422124
%configure --disable-static --without-readline
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1550422124
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/texinfo
cp COPYING %{buildroot}/usr/share/package-licenses/texinfo/COPYING
cp tp/maintain/lib/libintl-perl/COPYING.LESSER %{buildroot}/usr/share/package-licenses/texinfo/tp_maintain_lib_libintl-perl_COPYING.LESSER
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
/usr/share/texinfo/Texinfo/MiscXS.pm
/usr/share/texinfo/Texinfo/ModulePath.pm
/usr/share/texinfo/Texinfo/Parser.pm
/usr/share/texinfo/Texinfo/ParserNonXS.pm
/usr/share/texinfo/Texinfo/Report.pm
/usr/share/texinfo/Texinfo/Structuring.pm
/usr/share/texinfo/Texinfo/Transformations.pm
/usr/share/texinfo/Texinfo/XS/parsetexi/Parsetexi.pm
/usr/share/texinfo/Texinfo/XSLoader.pm
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
%defattr(0644,root,root,0755)
%doc /usr/share/info/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/texinfo/MiscXS.so
/usr/lib64/texinfo/Parsetexi.so
/usr/lib64/texinfo/XSParagraph.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/texinfo/COPYING
/usr/share/package-licenses/texinfo/tp_maintain_lib_libintl-perl_COPYING.LESSER

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/info.1
/usr/share/man/man1/install-info.1
/usr/share/man/man1/makeinfo.1
/usr/share/man/man1/pdftexi2dvi.1
/usr/share/man/man1/pod2texi.1
/usr/share/man/man1/texi2any.1
/usr/share/man/man1/texi2dvi.1
/usr/share/man/man1/texi2pdf.1
/usr/share/man/man1/texindex.1
/usr/share/man/man5/info.5
/usr/share/man/man5/texinfo.5

%files locales -f texinfo_document.lang -f texinfo.lang
%defattr(-,root,root,-)

