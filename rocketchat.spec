%define name rocketchat
%define version 0.0.57.2
%define release 2
%define _binaries_in_noarch_packages_terminate_build   0
%define __os_install_post %{nil}

Summary: The ultimate Free Open Source Solution for team communications
Name: %{name}
Version: %{version}
Release: %{release}
License: GNU GPL version 2
URL: https://github.com/RocketChat/Rocket.Chat
Group: SMEserver/addon
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}
BuildArch: noarch
BuildRequires: e-smith-devtools
Requires:  e-smith-release >= 9.0
Requires:   nodejs >= 4.8.2
AutoReqProv: no

%description
The ultimate Free Open Source Solution for team communications.
https://github.com/RocketChat/Rocket.Chat

%prep

%setup -q

%install
rm -rf $RPM_BUILD_ROOT
cd root   ; find . -depth -print | cpio -dump --quiet $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc COPYING
/opt


%defattr(-,root,root)

%pre
# Let check if there is an existing directory and if so move it
if [[ -d /opt/Rocket.Chat ]]; then

  # Check a service exists and stop it prior to moving the directory
  if [[ -f /etc/rc.d/init.d/rocketchat ]]; then
    echo "Stopping RocketChat"
    service rocketchat stop
  fi
  # Now move the directory
  echo "Move old RocketChat directory"
  mv /opt/Rocket.Chat /opt/Rocket.Chat.$(date "+%Y.%m.%d-%H.%M")

fi


%preun

%post

# Now install the modules
cd /opt/Rocket.Chat/programs/server
echo "Installing npm modules for RocketChat - this may take a while"
npm install
npm install -g forever n
n 4.8.2
npm install -g npm@3.10.9

# Now restart the service if it exists
if [[ -f /etc/rc.d/init.d/rocketchat ]]; then
  echo "Starting RocketChat"
  service rocketchat start
  echo "You may have to wait for a minute for Rocket.Chat to restart"
else
  echo "No rocketchat service. You may need smeserver-rocketchat installed"
fi

echo "Installed node version:" `node -v`
echo "Installed npm version:" `npm -v`

%postun


%changelog
* Tue Jul 18 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.57.2-2
- Bump node version required

* Fri Jul 14 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.57.2-1
- Changes https://github.com/RocketChat/Rocket.Chat/releases/tag/0.57.2

* Thu Jul 06 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.57.1-1
- Changes https://github.com/RocketChat/Rocket.Chat/releases/tag/0.57.1

* Tue Jul 04 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.57.0-1
- Changes https://github.com/RocketChat/Rocket.Chat/releases/tag/0.57.0

* Thu Apr 20 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.56.0-1
- Changes https://github.com/RocketChat/Rocket.Chat/releases/tag/0.56.0

* Thu Apr 20 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.55.1-1
- Changes https://github.com/RocketChat/Rocket.Chat/releases/tag/0.55.1

* Wed Apr 19 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.55.0-1
- Changes https://github.com/RocketChat/Rocket.Chat/releases/tag/0.55.0

* Mon Mar 27 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.54.2-1
- Changes https://github.com/RocketChat/Rocket.Chat/releases/tag/0.54.2

* Fri Mar 24 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.54.1-1
- Changes https://github.com/RocketChat/Rocket.Chat/releases/tag/0.54.1

* Tue Feb 14 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.53.0-1
- Changes https://github.com/RocketChat/Rocket.Chat/releases/tag/0.53.0

* Tue Feb 14 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.52.0-1
- Changes https://github.com/RocketChat/Rocket.Chat/releases/tag/0.52.0

* Tue Feb 07 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.51.0-1
- update installed node version

* Thu Feb 02 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.50.1-2
- update installed node version

* Sun Jan 22 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.50.1-1
- Update to 0.50.1 (very rapidly updated from 50.0)

* Sun Jan 22 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.49.4-1
- Update to 0.49.4

* Tue Jan 17 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.49.3-1
- Update to 0.49.3

* Tue Jan 17 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.49.2-1
- Update to 0.49.2

* Mon Jan 16 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.49.1-1
- Update to 0.49.1

* Fri Jan 13 2017 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.49.0-1
- Update to 0.49.0

* Wed Dec 21 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.48.2-1
- Update to 0.48.2

* Tue Dec 13 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.48.1-1
- Update to 0.48.1

* Tue Dec 13 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.48.0-1
- Update to 0.48.0

* Mon Dec 12 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.47.1-1
- Update to 0.47.1

* Tue Dec 06 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.47.0-1
- Update to 0.47.0

* Tue Nov 01 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.45.0-1
- Update to 0.45.0

* Mon Oct 31 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.44.0-1
- Update to 0.44.0

* Tue Sep 06 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.39.0-1
- Update to 0.39.0

* Wed Aug 31 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.38.0-1
- Update to 0.38.0

* Wed Aug 24 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.37.1-1
- Update to 0.37.1

* Wed Aug 24 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.3.7-9
- Add check for the rocketchat service

* Wed Aug 24 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.3.7-8
- Add npm install -g forever

* Wed Aug 24 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.3.7-7
- Try again with symbolic links

* Tue Aug 23 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.3.7-6
- remove printenv test

* Tue Aug 23 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.3.7-5
- Remove %S from the move command
- Added ln -s `which npm` /usr/bin/npm to server to test %pre

* Tue Aug 23 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.3.7-4
- fix %pre if command

* Tue Aug 23 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.3.7-3
- add npm install to spec file

* Wed Aug 17 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.3.7-2
- add mail composer patch

* Wed Aug 17 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.0.3.7-1
- initial release
