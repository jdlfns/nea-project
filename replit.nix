{pkgs}: {
  deps = [
    pkgs.openjdk16-bootstrap
    pkgs.rustc
    pkgs.pkg-config
    pkgs.openssl
    pkgs.libxcrypt
    pkgs.libiconv
    pkgs.cargo
  ];
}
