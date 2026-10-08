# Running `job-search-agent` daily on Windows

Schedule `jobscout.py` to run every morning with Windows Task Scheduler.
This is the Windows equivalent of the macOS LaunchAgent and the Linux
systemd timer.

## 1. Check a manual run works first

Open Command Prompt in the repo folder:

```bat
cd C:\path\to\job-search-agent
python jobscout.py --dry-run
```

If `python` isn't found, try `py -3 jobscout.py --dry-run`. The python.org
installer always adds the `py` launcher, and only adds `python` to PATH
if you ticked that box.

Fix anything that fails here before you automate it. A scheduled task
that fails runs silently, which is much harder to debug.

## 2. Try the wrapper script

`windows\run-jobscout.bat` does one run from the repo folder, uses `py -3`
if it's there (otherwise `python`), and appends everything it prints to
`jobscout.log` in the state folder (`%USERPROFILE%\.local\state\jobscout`,
or `%JOBSCOUT_STATE_DIR%` if you set it). Arguments are passed through:

```bat
windows\run-jobscout.bat --dry-run
type %USERPROFILE%\.local\state\jobscout\jobscout.log
```

## 3. Create the task

1. Open **Task Scheduler** (search for it in the Start menu)
2. Click **Create Basic Task**
3. Name it `JobScout Daily` and click Next
4. Choose **Daily**, set it to 6:00 AM, click Next
5. Choose **Start a program**, click Next
6. Set:
   - **Program/script:** `C:\path\to\job-search-agent\windows\run-jobscout.bat`
   - **Start in:** `C:\path\to\job-search-agent`
7. Check **Open the Properties dialog** and click Finish
8. In Properties, under **Conditions**, uncheck "Start the task only if the computer is on AC power"
9. Under **Settings**, check "Run task as soon as possible after a scheduled start is missed"

If you'd rather not use the wrapper, set **Program/script** to the full path
of `python.exe` (run `where python` to find it) and **Add arguments** to
`C:\path\to\job-search-agent\jobscout.py`. Output then goes nowhere, so
the wrapper is easier to debug.

## 4. Environment variables

Task Scheduler runs with your user environment, so set any variables
once with `setx` (they apply to new processes, not the current window):

```bat
setx JOBSCOUT_LLM_ENDPOINT http://localhost:11434
setx JOBSCOUT_LLM_MODEL llama3.1:8b
```

That example is for Ollama, which serves the same `/v1/chat/completions`
API on port 11434. The default model name is an MLX model, and MLX only
runs on Apple silicon, so on Windows always set `JOBSCOUT_LLM_MODEL` to
whatever your server has loaded. To use Claude instead:

```bat
setx ANTHROPIC_API_KEY sk-ant-...
```

The local model server has to be running at 6 AM too, or every role is
saved with score 0. If you don't keep one running, the Anthropic API is
the simpler choice on Windows.

## 5. Test it

Right-click the task and choose **Run**, then check `jobscout.log` and
the newest file in `%USERPROFILE%\.local\state\jobscout\results\`.
