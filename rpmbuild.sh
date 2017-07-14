#!/bin/sh
cd ~
mkdir ~/rpmbuild
for i in BUILD BUILDROOT RPMS SOURCES SPECS SRPMS
do
 mkdir ~/rpmbuild/$i
done