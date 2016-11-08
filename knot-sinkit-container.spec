%global _systemddir /lib/systemd/system
%global debug_package %{nil}

Name:           knot-sinkit-container
Version:        0.0.1
Release:        2%{?dist}
Summary:        Knot DNS Resolver with Sinkit module Docker container.

License:        LGPLv3
URL:            https://github.com/Karm/knot-sinkit
Source:         https://github.com/Karm/knot-sinkit/archive/0.0.1.zip

%{?systemd_requires}
BuildRequires:    systemd-units
Requires(post):   systemd-units
Requires(preun):  systemd-units
Requires(postun): systemd-units
Requires:         docker-engine = 1.10.3

%description
Knot DNS Resolver with Sinkit module and Sinkit control daemon.

%prep
%setup -q -n knot-sinkit-%{version}

%build
#Silence is golden. We just use the systemd unit.

%install
ls -lah systemd/%{name}.service
pwd
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_systemddir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_unitdir}
%{__install} -m 0644 systemd/%{name}.service ${RPM_BUILD_ROOT}%{_unitdir}/%{name}.service

%files
%{_unitdir}/%{name}.service
%doc README.md
%license LICENSE

%post
%systemd_post knot-sinkit-container.service

%preun
%systemd_preun knot-sinkit-container.service

%postun
%systemd_postun_with_restart knot-sinkit-container.service

%changelog
* Mon Aug 8 2016 Michal Karm Babacek <karm@email.cz> 0.1.0-1
- Initial RPM release
