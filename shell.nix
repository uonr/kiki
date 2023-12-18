{ pkgs ? import <nixpkgs> { } }:
with pkgs;
mkShell {
  buildInputs = [ ffmpeg yt-dlp ];
  shellHook = ''
    # ...
  '';
}
