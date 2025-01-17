%global forgeurl https://github.com/ToxicFrog/vstruct
%global tag v%{version}

%define lua_version %(lua -e 'print(_VERSION)' | cut -d ' ' -f 2)
%define lua_pkgdir %{_datadir}/lua/%{lua_version}

Name:      lua-vstruct
Version:   2.1.1
Release:   1
Summary:   Lua library to manipulate binary data
Group:     Development/Other
License:   MIT
URL:       %{forgeurl}

%forgemeta
Source:    %{forgesource}

BuildArch:     noarch
BuildRequires: lua-devel

%description
%{summary}.

%prep
%forgesetup

%build
# Nothing to do here

%install
install -dD %{buildroot}%{lua_pkgdir}/vstruct

install -p -m 644 api.lua %{buildroot}%{lua_pkgdir}/vstruct/
install -p -m 644 ast.lua %{buildroot}%{lua_pkgdir}/vstruct/
install -p -m 644 compat1x.lua %{buildroot}%{lua_pkgdir}/vstruct/
install -p -m 644 cursor.lua %{buildroot}%{lua_pkgdir}/vstruct/
install -p -m 644 frexp.lua %{buildroot}%{lua_pkgdir}/vstruct/
install -p -m 644 init.lua %{buildroot}%{lua_pkgdir}/vstruct/
install -p -m 644 io.lua %{buildroot}%{lua_pkgdir}/vstruct/
install -p -m 644 lexer.lua %{buildroot}%{lua_pkgdir}/vstruct/
cp -av ast/ %{buildroot}%{lua_pkgdir}/vstruct/
cp -av io/ %{buildroot}%{lua_pkgdir}/vstruct/

%check
# Fails due to package.path magic in the test file depends on
# the parent folder name
# lua test.lua

LUA_PATH="%{buildroot}%{lua_pkgdir}/?.lua;%{buildroot}%{lua_pkgdir}/?/init.lua" \
lua -e 'local vstruct = require "vstruct"
print(vstruct._VERSION)'

%files
%license COPYING
%doc README.md
%doc CHANGES
%{lua_pkgdir}/vstruct/
