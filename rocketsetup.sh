#!/bin/sh
if [ "$1" == "" ]; then
    echo "Usage: `basename $0` [You need to add a version number e.g 0.38.0]"
    echo "Optional add the spec version e.g. 0.38.0 2"
        exit 0
fi

if [ -z $2 ]; then
    VER="1";
else
    VER="$2";
fi

cd ~/git/rocketRPMbuilder

mkdir -p rocketchat-0.$1/root/opt

echo "wget the source"
# Download tar.gz if we haven't already got a copy
wget https://rocket.chat/releases/$1/download -O rocket.chat-0.$1.tgz


# wget https://github.com/RocketChat/Rocket.Chat/archive/$1.tar.gz -O rocket.chat-0.$1.tgz

echo "Extract source"
# Extract
tar -xzf rocket.chat-0.$1.tgz -C rocketchat-0.$1/root/opt/

echo "Move the bundle"
# Move the bundle
mv rocketchat-0.$1/root/opt/bundle rocketchat-0.$1/root/opt/Rocket.Chat

echo "Copy the copyright notice"
# Copy the copyright notice
cp COPYING ./rocketchat-0.$1

echo "Remove the original downloaded tgz file"
# Remove the original downloaded tgz file
rm -f ./rocket.chat-0.$1.tgz

echo "Now tar the directory"
# Now tar the directory
tar -czf rocketchat-0.$1.tar.gz rocketchat-0.$1

echo "Now remove the old directory"
# Remove the old directory
rm -rf ./rocketchat-0.$1

echo " Copy spec, patch and tgz to build area"
# Copy the spec and source to the build area
\cp -rf *.tar.gz ~/rpmbuild/SOURCES;\cp -rf *.patch ~/rpmbuild/SOURCES;\cp -rf *.spec ~/rpmbuild/SPECS

echo "Remove the new tgz file"
# Remove the new tar.gz file - copy is in sources
rm -f ./rocketchat-0.$1.tar.gz

echo "Up a directory and"
# Now go up a directory
cd ..

echo "Build the rpm"

#And build the srpm
# This builds normally
# rpmbuild -ba /home/john/rpmbuild/SPECS/rocketchat.spec

# This mock builds
rpmbuild -bs /home/john/rpmbuild/SPECS/rocketchat.spec
mock -r /etc/mock/smeserver-9-x86_64-base.cfg rebuild /home/john/rpmbuild/SRPMS/rocketchat-0.$1-$VER.src.rpm
