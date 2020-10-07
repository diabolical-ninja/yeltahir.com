---
title: "VS Code"
draft: false
toc: true
---

# Handy Tricks for VS Code

## Extensions

Useful extensions for everyday use.

[autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)

[Beautify](https://marketplace.visualstudio.com/items?itemName=HookyQR.beautify)

[Guides](https://marketplace.visualstudio.com/items?itemName=spywhere.guides)

[Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

[R](https://marketplace.visualstudio.com/items?itemName=Ikuyadeu.r)

[vscode-icons](https://marketplace.visualstudio.com/items?itemName=robertohuertasm.vscode-icons)

[Charcoal Oceanic Next](https://marketplace.visualstudio.com/items?itemName=joshpeng.theme-charcoal-oceanicnext)

[Jupyter Notebook Previewer](https://marketplace.visualstudio.com/items?itemName=jithurjacob.nbpreviewer)

[Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)

[PlantUML](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml)

[Liveshare](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare-pack)


## Shortcuts

Open via `Preferences -> Open Keyboard Shortcuts (JSON)`

### Python Cell Symbol

Keyboard binding to add `#%%` to the in focus script.

```json
{
    "key": "ctrl+shift+a",
    "command": "type",
    "args": {"text": "#%%"},
    "when": "editorTextFocus"
}
```


### Send Text to Terminal

Binding to send any selected text to the current terminal. Useful when coding in a language with poor interactive support (eg anything other than python)

```json
{
    "key": "ctrl+shift+enter",
    "command": "workbench.action.terminal.runSelectedText"
}
```


## Force Clean workspace

To force vscode to open a new, clean workspace when opening (unless specifically opening from a directory) update:
* Window: Restore Windows
    - "none"
