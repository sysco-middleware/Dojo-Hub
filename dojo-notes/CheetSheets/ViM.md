- Vim
  tags:: #vim, #linux, #cheatsheet
- Moving Around
  collapsed:: true
	- By Word
	  collapsed:: true
	  
	  `w / W` Forward Word
	  `b / B` Backword Word
	  `e / E` End of Word
	  #+BEGIN_TIP
	  lowercase counts puntuation as word & upper case ignores puntuations
	  #+END_TIP
	- By Page
	  collapsed:: true
	  
	  `ctrl+f / PgDn` shift down by screen
	  `ctrl+b / PgUp` shift up by screen
	  #+BEGIN_TIP
	  H, M & L - Highest , Middle & Lowest of page
	  #+END_TIP
	  `zz` positions current line at middle of screen
	  `zb` positions current line at bottom of screen
	  `zt` positions current line at top of screen
	- By line
	  
	  `gg` 1st line of doc
	  `G` last line of doc
	  `xG` xth line
	- By position
	  
	  `0` to position 1 on line
	  `^` to 1st non-blank character on line
	  `$` to end of line
	- By Paragraph
	  
	  `}` jump forward a para
	  `{` jump forward a para
	- :set scrolloff=5 (scroll offset)
- Copy / Paste
  collapsed:: true
  
  `yy`  complete line
  `y^`  cursor to 1st char
  `y$`  cursor to end of line
  `yG`  cursor to end of file
  `yw`  cursor to end of word
- Delete
  collapsed:: true
	- By line
	  
	  `dd` full file
	  `d^`  from starting of line to cursor
	  `d$`  cursor to end of line
	- By word
	  
	  `dw` from cursor to end of word
	  `db` word backword from cursor
	  
	  `d3b` 3 words backwards
	  `d3w` 3 words forward
	  
	  `cw` current word and insert
- Undo & Redo
  collapsed:: true
  
  `ESC & u` to undo
  `Esc & U` reverse change on current line
  `ctrl+r` reverse last undo
  
  #+BEGIN_TIP
  `g+ / g` step forward / backword with changes
  #+END_TIP
- Search
  collapsed:: true
  
  `/word` forward search
  `?word` reverse search
  
  `n / N` next occurrence & previous occurrence
	- More search patterns
	  `/the`
	  `/the\>`
	  `/\<the`
	  `/\<the>`
	- `highlight & *` search for string
- Search & Replace
  collapsed:: true
  
  `:s/the/THE` first instance of current line
  `:%s/the/THE/g` all instances per all line
  `:%s/the/THE/gc` all instances per all line with confirmation
  `:%s/the/THE/gci` all instances per all line with confirmation & case insensitive
  `:5,25 s/the/THE/g` all instances on line 5 to 25
	- `%` substitute all lines
	  `g` all occurrences
	  `c` confirm each operation
	  `i` case insensitive
- Visual Mode
  collapsed:: true
  
  `v`  by character
  `V`  by line
  `ctrl+v` by block
  
  #+BEGIN_TIP
  `o, O` move end point of highlight
  #+END_TIP
- Toggle
  collapsed:: true
  
  `~`  toggle case of single char
  `7~`  toggle 7 chars
  
  `gUw`  change case for word
  `gU3w`  change case for 3 words
  `gUU`  entire line to UPPER
  `guu`  entire line lower