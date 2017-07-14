# rocketRPMbuilder
RocketChat RPM builder

Just a bash script to grab the Rocket.Chat source and build a RPM from it for Koozali SME Server

You can modify the script to just build a standard rpm if you have a standard build setup

Usage:

Clone this git repo.

If you want to build standard RPMs make sure you have a build layout in place

Here's a little script to do it for you:

 #!/bin/sh
 cd ~
 mkdir ~/rpmbuild
 for i in BUILD BUILDROOT RPMS SOURCES SPECS SRPMS
 do
 mkdir ~/rpmbuild/$i
 done


Modify your spec file versions.

Run:
./rocketsetup.sh $rocketVersion $specVersion

e.g.

./rocketsetup.sh 0.57.2 3