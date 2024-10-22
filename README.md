# uv workspace example: cable

This project contains a workspace with four packages: cable, cable-experiments, cable-cli, and cable-core. cable is the main project that users install. It has extras `cable[cli]` and `cable[experiments]` that pull in cable-experiments and cable-cli respectively. `cable-core` implements shared utils.

Since cable is the main project, it lives in the workspace root (not all workspaces have a root, but for many project a clear root that (indirectly) depends on everything else is very convenient), while all other packages live in `packages`.

```
        ---> cable-cli -----------|
cable --|                         |--> cable-core
        ---> cable-experiments ---|
```

or with `uv tree`:

```
cable v0.1.0
├── cable-cli v0.1.0 (extra: cli)
│   └── cable-core v0.1.0
└── cable-experiments v0.1.0 (extra: experiments)
    └── cable-core v0.1.0
```

When the user installs cable, they can decide if they want from a minimal installation (`cable`) to all features (`cable[cli,experiments]`).

The project offers an optional CLI. The script entrypoint lives in cable-cli, because there's a current limitation that scripts can't depend on extras, so cable-cli installs a `cable <name>` script; It's still installed through `cable[cli]`.

You can create this workspace structure roughly with:

```shell
uv init --lib cable
cd cable/
mkdir packages
cd packages/
uv init --lib cable-core
uv init --lib cable-cli
uv init --lib cable-experiments
cd cable-cli/
uv add ../cable-core
cd ../cable-experiments/
uv add ../cable-core
cd ../..
uv add --optional cli packages/cable-cli/
uv add --optional experiments packages/cable-experiments/
uv sync --all-extras
```
