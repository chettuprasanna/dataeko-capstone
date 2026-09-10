

> Replace every `TODO`. One section per defect, nine in total.
> For each one: what you saw, why it happened, what you changed, and how you
> proved it is fixed. Paste real output — not a description of output.

## 1. `scripts/ingest.sh` is not executable

**Symptom:** `ls -l scripts/ingest.sh` showed `-rw-r--r--`, and running `./scripts/ingest.sh` returned `Permission denied`.

**Cause:** The executable permission bit was missing from `scripts/ingest.sh`.

**Fix:** Ran `chmod +x scripts/ingest.sh` to add execute permission, then ran `git update-index --chmod=+x scripts/ingest.sh` so Git records the file as executable.

**Proof:** `ls -l scripts/ingest.sh` now shows `-rwxr-xr-x`. Running `./scripts/ingest.sh` no longer gives `Permission denied`; it reaches the script and reports `line 10: $1: unbound variable`.

**Why `git update-index --chmod=+x` was also needed:** `chmod +x` changes the permission on the local filesystem, while `git update-index --chmod=+x` tells Git to record the executable mode (`100755`) in the repository. This ensures the executable permission is preserved when the repository is cloned or checked out elsewhere.ø

## 2. `scripts/ingest.sh` fails when the CSV path contains spaces

**Symptom:** Running `bash scripts/ingest.sh "data/march orders.csv"` produced `binary operator expected`.

**Cause:** Line 10 used `$1` without quotes. The shell split `data/march orders.csv` into multiple words when evaluating the file test.

**Fix:** Changed `$1` to `"$1"` in the file existence check so the complete path is treated as one argument.

**Proof:** After the fix, `bash scripts/ingest.sh "data/march orders.csv"` completed successfully and staged the file as `data/staging/march orders.csv`.

## 3. Dockerfile reinstalls dependencies on every code change

**Symptom:** A source-code change caused Docker to reinstall the Python dependencies. In the defective Dockerfile, the source was copied before `pip install`, so changing `api/app.py` invalidated the dependency installation layer.

**Cause:** `COPY . .` was placed before `RUN pip install --no-cache-dir -r api/requirements.txt`. Docker therefore rebuilt the dependency layer whenever application source files changed.

**Fix:** Copied `api/requirements.txt` before installing dependencies, then copied the rest of the application source. This allows Docker to reuse the dependency layer when only source code changes.

**Proof:** With the defective Dockerfile, a source-code change caused `pip install` to run again and the build took **7.790s**. With the fixed Dockerfile, the source-code change produced `CACHED` for the `pip install` layer (`0.0s`), and the build completed in **4.231s**.

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
