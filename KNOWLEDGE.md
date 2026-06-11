# KNOWLEDGE.md — ansible-powermax

<!-- yaml-metadata-start -->
scope_paths: ["./"]
capture_git_sha: "9c9c2d8b957efd7794a246b972fcebc92cd0f636"
status: "current"
auto_update: false
preview_before_apply: true
scaffold_version: "1.0"
# session_state: { is_complete: true }
<!-- yaml-metadata-end -->

<!-- quick-reference-start -->
## Agent Quick Reference

| Section | Heading | Summary | never_again_count |
|---------|---------|---------|-------------------|
| Component Overview | `## Component Overview` | dellemc.powermax collection for PowerMax | — |
| Architectural Rationale | `## Architectural Rationale` | PyU4V SDK; Ansible collection pattern | — |
| Failure Modes & Gotchas | `## Failure Modes & Gotchas` | SDK coupling, idempotency, verify_ssl | 0 |
| Implicit Contracts | `## Implicit Contracts` | Connection params, ordering, action groups | — |
<!-- quick-reference-end -->

## Five Questions Quick Reference

### What does it do?
Ansible Galaxy collection `dellemc.powermax` (v4.0.2). Provides 17 modules and 1 roles for declarative, idempotent management of Dell PowerMax enterprise storage arrays. Uses `PyU4V` (>=10.2.0.3,==10.2.0.*) Python SDK.

### How do you modify it?
Create module file in `plugins/modules/`, add example playbook in `playbooks/modules/`, add unit test in `tests/unit/plugins/modules/`, append module FQCN to `meta/runtime.yml` action group.

### What breaks?
SDK version mismatch is a blocking defect. Missing tombstone/redirect entry leaves deprecated module names unresolved. `verifycert: false` in production violates security constitution.

### What depends on it?
`PyU4V` >=10.2.0.3,==10.2.0.*, Ansible >= 2.15.0. Ordering: dependent resources must exist before referencing them.

### What's undocumented?
No shared base — modules call `utils.get_powermax_connection()` directly. Uses `logging.basicConfig` with `CustomRotatingFileHandler`. Writes `ansible_powermax.log` by default (5 MB rotate, 5 backups).

---

## Component Overview

Ansible Galaxy collection `dellemc.powermax` (v4.0.2) for Dell PowerMax enterprise storage arrays. 17 modules and 1 roles covering volumes, storage groups, port groups, host groups, hosts, masking views, snapshots, SRDF pairs, RDF groups, and more.

---

## Architectural Rationale

Standard Ansible Galaxy collection layout. Each module is a self-contained Python file under `plugins/modules/` that communicates with the PowerMax REST API through the `PyU4V` SDK.

**SDK strategy:** Static import. Version pinned at `>=10.2.0.3,==10.2.0.*` in `requirements.txt`.


### Evolution

Early collections used a flat module structure with duplicated auth
and API logic in each module. The shared base class was introduced
after initial module growth to centralize authentication, argument
parsing, and API client initialization. Major refactors include:

- Base class introduction (centralized SDK initialization)
- Module naming standardization
- SDK / REST client improvements
- Improved error handling consistency

---

## Failure Modes & Gotchas

### 1. SDK version coupling

Each collection release is tested against exactly one SDK version (or tight range for PyU4V). A mismatch between collection and SDK version is a blocking defect. Never update `requirements.txt` SDK versions without verifying against the corresponding collection release notes.

### 2. Idempotency assumptions

Modules are designed to be idempotent but some parameters may be accepted by the module yet ignored by the underlying API. Always verify with a second run.

### 3. Verify SSL setting

`verifycert: false` is used in example playbooks but is a lab-only setting. Production requires `true`. Modules must not default to skipping verification.

### 4. Acceptance test cleanup

If tests fail mid-run, resources may be left on the array. Clean up manually before re-running.

### No Base Class

Unlike PowerScale, PowerStore, and PowerFlex, this collection does **not** have a `libraries/` or `shared_library/` directory. Module classes call `utils.get_powermax_connection()` directly in their `__init__`. There is no `PowerMaxBase` to subclass.

### SDK Version Range Pin

PyU4V uses a range-pinned version (`>=10.2.0.3,==10.2.0.*`) rather than single-version pin. Both floor and ceiling are defined.

### TODO Markers

`plugins/modules/volume.py` contains TODO comments about PyU4V implementation gaps. These represent known incomplete areas.


### 5. Idempotency drift

Occasional idempotency failures where a module reports `changed=false`
but state actually changed on the array. Caused by incomplete state
comparison logic — some parameters accepted by the module are ignored
by the underlying API. Always verify with a second run.

### 6. SDK import failures

Dependency or version mismatches between the collection and its SDK
cause import failures at module load time. Manifests as
`ModuleNotFoundError` or `ImportError` with no actionable message
unless `-vvv` is used.

### 7. Check mode inaccuracies

Not all modules fully simulate changes correctly in check mode.
Some modules report `changed=true` in check mode but would actually
make no change, or vice versa. Treat check mode as advisory, not
authoritative.

### Never Again

#### NA-001: SDK version mismatch causing silent failures
- **Impact:** Modules loaded but returned incorrect data due to
  SDK API changes between versions.
- **Constraint:** SDK version must be pinned exactly in
  `requirements.txt`. Never update without full test pass.
- **Applies to:** All Dell Ansible collections.

#### NA-002: Idempotency regression on update operations
- **Impact:** Repeated playbook runs made unintended changes to
  array resources due to incomplete state comparison.
- **Constraint:** Every module must compare full current state
  before applying changes.
- **Applies to:** All Dell Ansible collections.

#### NA-003: Orphaned resources from test failures
- **Impact:** Test resources left on array after test failure,
  consuming capacity.
- **Constraint:** Manual cleanup required after failed test runs.
- **Applies to:** All Dell Ansible collections.
### Evolution

Failure modes evolved with the base class introduction. Error
handling was standardized across modules during the naming
convention refactor. SDK import failures became less common after
the `HAS_*` flag pattern was adopted consistently.

---

## Performance Characteristics

**Sequential execution:** Ansible executes modules sequentially per
host within a play. Large inventories with many tasks experience
linear performance degradation. No built-in batching or pipelining
at the module level.

**API rate limiting:** PowerMax arrays enforce implicit
throttling under heavy parallel execution (high Ansible fork count).
Reduce `forks` or add `throttle` to tasks hitting the same array.

**Bulk operations:** Module execution is slower for bulk operations
due to per-task API calls with no batching support. Async operations
(where supported) can mitigate but add complexity.

**No connection reuse:** Each module invocation creates a new SDK
client and HTTP session. No connection pooling across tasks.

### Evolution

Performance improved after the base class centralized SDK
initialization, reducing per-module overhead. Connection reuse
remains an open area for improvement.

---

## Implicit Contracts

**Connection parameters required:** All modules require `unispherehost`, `user`, `password`, `verifycert` — these are not optional.

**Resource ordering:** Dependent resources must exist before being referenced (e.g., filesystem before snapshot, volume group before volumes, policies before assignment).

**Runtime registration:** Deprecated module names must have tombstone or redirect entries in `meta/runtime.yml`.

### Evolution

Connection parameter patterns were established early and carried
forward. Resource ordering constraints are implicit — the API
returns errors but the collection does not enforce ordering.

---

## Threading & Synchronization

Ansible handles concurrency via forks at the play level. Individual
module executions are single-threaded. However, multiple forks
hitting the same PowerMax array simultaneously causes:

**API contention:** High fork counts cause throttling or transient
errors from the array API. Mitigate with `throttle: N` on tasks
targeting the same array.

**Connection pool exhaustion:** Possible when many forks execute
without HTTP session reuse. Each fork creates independent SDK
client connections.

**Race conditions on shared resources:** Concurrent modifications
to interdependent resources (e.g., volume + host mapping,
replication configurations) can produce inconsistent state.
Serialize dependent operations with `serial: 1` or task ordering.

### Evolution

Concurrency issues became more visible as collections grew and
users ran larger playbooks with higher fork counts against single
arrays.

---

## Build System & Configuration

| Command | Description |
|---------|-------------|
| `ansible-galaxy collection build` | Build collection tarball |
| `ansible-galaxy collection install <tarball>` | Install locally |
| `pytest tests/unit/` | Run unit tests |
| `ansible-playbook --syntax-check` | Validate playbook syntax |

---

## Operational Knowledge

**Logging:** Enable `-vvv` for detailed output including API
request/response payloads. Correlate Ansible output with array
logs for full troubleshooting.

**Common support scenarios:**
- Authentication failures — verify `unispherehost`, credentials,
  and `verifycert` settings
- Idempotency issues — run playbook twice, compare `changed`
  status
- Timeout / async completion problems — increase timeout
  parameters, check array load

**Test environment requirements:**
- Dedicated PowerMax array or simulator
- Stable API version matching SDK pin
- Isolated test datasets (avoid shared resources)

### Evolution

Debugging patterns improved with `-vvv` adoption as standard
practice. Common failure patterns documented after recurring
support cases.

---

## General Context

No additional context beyond what has been captured.

### Open Issues

No TODO/FIXME/HACK markers found in non-test source files.

---

## References

- [Ansible Galaxy — dellemc.powermax](https://galaxy.ansible.com/dellemc/powermax)
- [Ansible Collection Developer Guide](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections.html)

---

## Governance Spec Discrepancies

No discrepancies detected.
