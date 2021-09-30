Name:           npm
License:        MIT License
Version:        1.0.106
Release:        4
Summary:        A package manager for Node.js
Group:          Development/Libraries
URL:            http://npmjs.org/
BuildRoot:      %(mktemp -d %{_tmppath}/%{name}-%{version}-XXXXXX)
Source:         http://registry.npmjs.org/npm/-/npm-%{version}.tgz
BuildRequires:  nodejs
Requires:       nodejs
BuildArch:      noarch

%description
NPM is a package manager for Node.js.
You can use it to install and publish your node programs.
It manages dependencies and does other cool stuff.

%prep
%setup -q -n package

%install
rm -rf %{buildroot}
npm_config_prefix=%{buildroot}%{_prefix} node cli.js install -g
echo "prefix = /usr/local
globalconfig = /etc/npm/npmrc
globalignorefile = /etc/npm/npmignore" > %{buildroot}%{_prefix}/lib/node_modules/npm/npmrc
mkdir -p %{buildroot}/etc/npm
mkdir -p %{buildroot}/etc/bash_completion.d
ln -s %{_prefix}/lib/node_modules/npm/lib/utils/completion.sh %{buildroot}/etc/bash_completion.d/npm.sh

set +x
echo "Move man's"
find %{buildroot}%{_mandir} -type l | while read man; do
    cp $man $man.xxx~
    mv $man.xxx~ $man
done
set -x

%files
%defattr(-,root,root,-)
%dir /etc/npm
/etc/bash_completion.d/*
%{_prefix}/lib/node_modules/npm
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
#%exclude %{_prefix}/lib/node_modules/npm/deps
#%exclude %{_prefix}/lib/node_modules/npm/doc
#%exclude %{_prefix}/lib/node_modules/npm/html
#%exclude %{_prefix}/lib/node_modules/npm/man
#%exclude %{_prefix}/lib/node_modules/npm/test