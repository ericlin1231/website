{
  description = "My Website Flake";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
      ...
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        devShells.default = pkgs.mkShell {
          name = "my-website-ts-py-shell";
          packages = with pkgs; [
            deno
            uv
            python313
          ];
          shellHook = ''
						export UV_VENV_PATH=./backend/.venv
						if [ ! -d "$UV_VENV_PATH" ]; then
							uv venv "$UV_VENV_PATH"
							uv pip install -r backend/pyproject.toml
						fi
						source "$UV_VENV_PATH/bin/activate"
					'';
        };
      }
    );
}
