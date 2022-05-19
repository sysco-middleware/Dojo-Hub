- tags: #tmux #linux #cheetsheet
- ## remap prefix from 'C-b' to 'C-a'
  collapsed:: true
  
  unbind C-b \
  set-option -g prefix C-a \
  bind-key C-a send-prefix
- ## split panes using | and -
  collapsed:: true
  
  unbind '"'
  unbind %
  bind | split-window -h
  bind - split-window -v
- ## reload config file
  collapsed:: true
  
   (change file location to your the tmux.conf you want to use)
  bind r source-file ~/.tmux.conf
- ## switch panes using Alt-arrow without prefix
  collapsed:: true
  
  bind -n M-Left select-pane -L
  bind -n M-Right select-pane -R
  bind -n M-Up select-pane -U
  bind -n M-Down select-pane -D
- ## Enable mouse control
  collapsed:: true
  
  set -g mouse on
- ## sync panes
  collapsed:: true
  
  unbind s
  bind s setw synchronize-panes