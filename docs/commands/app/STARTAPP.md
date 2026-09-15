# STARTAPP

Starts an app by name.

| | |
|---|---|
| Syntax | `STARTAPP("AppName")` |
| Group | app |
| Runs on the PC | no |

## Examples

| Call | Result | Known from |
|---|---|---|
| `STARTAPP("Function")` | *no value* | HP help |

## Behaviour

There is nothing to record: it leaves your program and opens an app, so a
batch that ran it would abandon the batch (HP help). That is why it is not in
any of the measured runs here, and it is the reason this entry has no result
rather than an unmeasured one.

The name is the app's, as it appears under `[Apps]` (HP help), which for an
app of your own is the folder name of its `.hpappdir`
([apps.hpappdir-contents](../../topics/apps.md#apps.hpappdir-contents)).

What an app's own program can rely on once it is open -- its hooks, and why
they do not fire in an app built with no base view -- is measured (G2) in
[apps.blank-app-hooks](../../topics/apps.md#apps.blank-app-hooks).

The interpreter does not implement it, so `hpprime run` cannot check a program
that uses it (unverified).

## Related

[STARTVIEW](STARTVIEW.md) ·
[apps.hooks](../../topics/apps.md#apps.hooks) ·
[apps.blank-app-hooks](../../topics/apps.md#apps.blank-app-hooks)
