# Release-tools

## Assumptions

- Currently released version can be obtained from the latest git tag.
- Git is in $PATH.
- Tags are created on a "main" branch.
- Releases are prepared on a "work" branch.

## Commands

### rlt-version

- Print released version with `rlt-version --released`.
- Print next version with `rlt-version --next`.
- Set next version with `rlt-version --set-next <version>`.

### rlt-changelog

Prints a summary of the changes between the released version and HEAD.

### rlt-updateworkbranch

Makes sure work branch is up to date.

### rlt-tag

Creates tag for the next version.

## releasetools.conf

```
[git]
main_branch=master
tag_prefix=
work_branch=dev

[version]
file=CMakeLists.txt
pattern="^    VERSION (.*)$")

[changelog]
git_log_options=--pretty=format:'- \%s (\%an)'
```
