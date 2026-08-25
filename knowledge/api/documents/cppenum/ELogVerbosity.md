---
id: "api:cppenum:ELogVerbosity"
title: "ELogVerbosity"
source: "https://developer.gp.qq.com/api/cppenum/detail/ELogVerbosity.json"
category: "API Wiki/cppenum"
kind: "cppenum"
api_root: "https://developer.gp.qq.com/api/"
---

# ELogVerbosity

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Fatal` | `1` | Always prints s fatal error to console (and log file) and crashes (even if logging is disabled) |
| `Error` | `2` | Prints an error to console (and log file).    Commandlets and the editor collect and report errors. Error messages result in commandlet failure. |
| `Warning` | `3` | Prints a warning to console (and log file).   Commandlets and the editor collect and report warnings. Warnings can be treated as an error. |
| `Display` | `4` | Prints a message to console (and log file) |
| `Log` | `5` | Prints a message to a log file (does not print to console) |
| `Verbose` | `6` | Prints a verbose message to a log file (if Verbose logging is enabled for the given category,     usually used for detailed logging) |
| `VeryVerbose` | `7` | Prints a verbose message to a log file (if VeryVerbose logging is enabled,    usually used for detailed logging that would otherwise spam output) |
