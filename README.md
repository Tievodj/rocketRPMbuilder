# rocketRPMbuilder
RocketChat RPM builder

Just a bash script to grab the Rocket.Chat source and build a RPM from it for Koozali SME Server

You can modify the script to just build a standard rpm if you have a standard build setup

Usage:

Modify your spec file versions.

Run:
./rocketsetup.sh $rocketVersion $specVersion

e.g.

./rocketsetup.sh 0.57.2 3