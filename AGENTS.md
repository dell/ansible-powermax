# AGENTS.md - Dell Ansible Collection for PowerMax

## Project Overview

This is the Ansible Galaxy collection for Dell PowerMax enterprise storage arrays. It provides Ansible modules and roles for automating provisioning and management of PowerMax arrays.

- **Language:** Python
- **Collection namespace:** `dellemc.powermax`
- **Collection version:** 4.0.2
- **SDK:** `PyU4V` v10.2.x
- **License:** GNU General Public License v3.0

## Architecture

The collection follows the standard Ansible Galaxy collection layout. Each module is a self-contained Python file under `plugins/modules/` that communicates with the PowerMax Unisphere REST API through the `PyU4V` SDK.

### Authentication

Modules authenticate to a PowerMax Unisphere server using `unispherehost`, `universion`, `username`, `password`, `serial_no`, and optional `verifycert` parameters.

### SDK Strategy

Uses `PyU4V` — a Dell-published Python SDK for the PowerMax Unisphere API, installed via `pip`. Version pinned in `requirements.txt` to `>= 10.2.0.3, == 10.2.0.*`. Also requires `urllib3` and `packaging`.

### Module and Role Count

The collection includes approximately 30 modules and 1 role covering PowerMax entities such as storage groups, port groups, hosts, host groups, masking views, volumes, SRPs, SRDF replication, and snapshots.

## Directory Structure

```
galaxy.yml                        Collection metadata (namespace, name, version)
plugins/
  modules/                        Ansible modules (one .py file per resource)
  module_utils/
    storage/                      Shared utility classes and SDK wrappers
  doc_fragments/                  Shared documentation fragments
meta/                             Collection metadata (runtime.yml)
roles/                            Ansible roles
tests/
  unit/
    plugins/                      Unit tests (pytest)
playbooks/                        Example playbooks
docs/                             Module documentation
changelogs/                       Release changelog fragments
requirements.txt                  Python dependencies (PyU4V, urllib3, packaging)
requirements.yml                  Ansible collection dependencies
```

## Build Commands

| Command | Description |
|---------|-------------|
| `ansible-galaxy collection build` | Build the collection tarball |
| `ansible-galaxy collection install <tarball>` | Install the collection locally |
| `pytest tests/unit/` | Run unit tests |

## Testing

### Unit Tests

- Test files follow `test_*.py` convention in `tests/unit/plugins/`.
- Framework: `pytest` with `unittest.mock` for mocking SDK calls.
- No hardware required.

### Running Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run unit tests
pytest tests/unit/ -v
```

## Code Style and Conventions

### Module Pattern

Each module follows the standard Ansible module pattern:
1. `DOCUMENTATION`, `EXAMPLES`, and `RETURN` docstrings at the top.
2. An `AnsibleModule` argument spec defining parameters.
3. A main class that wraps SDK calls and handles idempotency.
4. `module.exit_json()` for success, `module.fail_json()` for errors.

### Shared Utilities

- `plugins/module_utils/storage/` contains shared base classes and SDK initialization code.
- `plugins/doc_fragments/` contains reusable documentation for common parameters.

### File Header

All source files must include the Dell copyright and GPL v3.0 license header.

## Common Development Tasks

### Adding a New Module

1. Create `plugins/modules/<resource>.py` following the Ansible module pattern.
2. Add unit tests in `tests/unit/plugins/`.
3. Add example playbooks in `playbooks/`.
4. Update `changelogs/` with a changelog fragment.

### Updating the SDK

Update `requirements.txt` with the new `PyU4V` version pin.

## CI/CD

GitHub Actions workflows in `.github/workflows/`. Code coverage tracked via `codecov.yml`.

## Code Ownership

All files are owned by the maintainers defined in `.github/CODEOWNERS`.
