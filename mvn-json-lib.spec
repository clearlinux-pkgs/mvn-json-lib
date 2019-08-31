#
# FIXME: autospec completely fails to build this package now (see previous commit)
# It might be related to a sources.jar being listed for Source0...
#
Name     : mvn-json-lib
Version  : 1
Release  : 5
URL      : https://downloads.sourceforge.net/project/json-lib/json-lib/json-lib-2.3/json-lib-2.3-jdk15-sources.jar
Source0  : https://downloads.sourceforge.net/project/json-lib/json-lib/json-lib-2.3/json-lib-2.3-jdk15-sources.jar
Source1  : https://repo.gradle.org/gradle/libs-releases/net/sf/json-lib/json-lib/2.3/json-lib-2.3-jdk15.jar
Source2  : https://repo.gradle.org/gradle/libs-releases/net/sf/json-lib/json-lib/2.3/json-lib-2.3.pom
Source3  : https://repo.gradle.org/gradle/libs-releases/net/sf/json-lib/json-lib/2.4/json-lib-2.4-jdk15.jar
Source4  : https://repo.gradle.org/gradle/libs-releases/net/sf/json-lib/json-lib/2.4/json-lib-2.4.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0

%description
No detailed description available

%package data
Summary: data components for the mvn-json-lib package.
Group: Data

%description data
data components for the mvn-json-lib package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/sf/json-lib/json-lib/2.3
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/net/sf/json-lib/json-lib/2.3/json-lib-2.3-jdk15.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/sf/json-lib/json-lib/2.3
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/net/sf/json-lib/json-lib/2.3/json-lib-2.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/sf/json-lib/json-lib/2.4
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/net/sf/json-lib/json-lib/2.4/json-lib-2.4-jdk15.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/net/sf/json-lib/json-lib/2.4
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/net/sf/json-lib/json-lib/2.4/json-lib-2.4.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/net/sf/json-lib/json-lib/2.3/json-lib-2.3-jdk15.jar
/usr/share/java/.m2/repository/net/sf/json-lib/json-lib/2.3/json-lib-2.3.pom
/usr/share/java/.m2/repository/net/sf/json-lib/json-lib/2.4/json-lib-2.4-jdk15.jar
/usr/share/java/.m2/repository/net/sf/json-lib/json-lib/2.4/json-lib-2.4.pom
