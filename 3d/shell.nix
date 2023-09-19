{ pkgs ? import <nixpkgs> {} }:
let
    my-python-packages = ps: with ps; [
        pandas
        numpy
        matplotlib
    ];
in pkgs.mkShell {
    packages = [
        (pkgs.python3.withPackages my-python-packages)
    ];
}
