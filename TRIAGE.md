

> Replace every `TODO`. One section per defect, nine in total.
> For each one: what you saw, why it happened, what you changed, and how you
> proved it is fixed. Paste real output — not a description of output.

## 1. `scripts/ingest.sh` is not executable

**Symptom:** `ls -l scripts/ingest.sh` showed `-rw-r--r--`, and running `./scripts/ingest.sh` returned `Permission denied`.

**Cause:** The executable permission bit was missing from `scripts/ingest.sh`.

**Fix:** Ran `chmod +x scripts/ingest.sh` to add execute permission, then ran `git update-index --chmod=+x scripts/ingest.sh` so Git records the file as executable.

**Proof:** `ls -l scripts/ingest.sh` now shows `-rwxr-xr-x`. Running `./scripts/ingest.sh` no longer gives `Permission denied`; it reaches the script and reports `line 10: $1: unbound variable`.

**Why `git update-index --chmod=+x` was also needed:** `chmod +x` changes the permission on the local filesystem, while `git update-index --chmod=+x` tells Git to record the executable mode (`100755`) in the repository. This ensures the executable permission is preserved when the repository is cloned or checked out elsewhere.ø

## 2. Unquoted `$1` in `scripts/ingest.sh`
**Symptom:** TODO
**Cause:** TODO
**Fix:** TODO
**Proof:** TODO

## 3. Dockerfile copies source before installing dependencies
**Symptom:** TODO
**Cause:** TODO
**Fix:** TODO
**Proof (build output, before and after):** TODO

## 4. No `.dockerignore`
**Symptom:** TODO
**Cause:** TODO
**Fix:** TODO
**Proof (context size, before and after):** TODO

## 5. API key committed to the repository
**Symptom:** TODO
**Cause:** TODO
**Fix:** TODO
**Is the key gone now that you deleted the line?** TODO
**What would you have to do in real life?** TODO

## 6. `requests` call with no timeout
**Symptom:** TODO
**Cause:** TODO
**Fix:** TODO
**Why a hang is worse than an error:** TODO

## 7. Missing index on `orders.customer_id`
**Symptom:** TODO
**Plan before:** TODO
**Plan after:** TODO
**Timings, three runs each:** TODO
**Why the planner changed its mind:** TODO

## 8. SSH open to `0.0.0.0/0`
**Symptom:** TODO
**Why nothing warned you:** TODO
**Fix:** TODO
**What an attacker does with this:** TODO

## 9. `count` instead of `for_each`
**Plan with `count`, after removing `staging`:** TODO
**Plan with `for_each`, same edit:** TODO
**Why this is the most dangerous defect in the list:** TODO
