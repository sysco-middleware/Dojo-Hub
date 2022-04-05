- tags: #tmux #linux #cheatsheet
- change file location to your the tmux.conf
  ```
  bind r source-file ~/.tmux.conf
  ```
- remap prefix from 'C-b' to 'C-a'
  ```
  unbind C-b \
  set-option -g prefix C-a \
  bind-key C-a send-prefix
  ```
- split panes using | and -
  ```
  unbind '"'
  unbind %
  bind | split-window -h
  bind - split-window -v
  ```
- sync panes
  ```
  unbind s
  bind s setw synchronize-panes
  ```
- switch panes using Alt-arrow without prefix
  ```
  bind -n M-Left select-pane -L
  bind -n M-Right select-pane -R
  bind -n M-Up select-pane -U
  bind -n M-Down select-pane -D
  ```
- Enable mouse control
  ```
  set -g mouse on
  ```
-