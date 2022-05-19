- tags: #vim #linux #cheetsheet
# Moving Around
## By Word
id:: 618e39ac-d7f0-4247-8965-ce313e9577b5

`w / W` Forward Word
`b / B` Backword Word
`e / E` End of Word

#+BEGIN_TIP
lowercase counts puntuation as word & upper case ignores puntuations
#+END_TIP
## By Page

`ctrl+f / PgDn` shift down by screen
`ctrl+b / PgUp` shift up by screen

#+BEGIN_TIP
H, M & L - Highest , Middle & Lowest of page
#+END_TIP
## By line

`gg` 1st line of doc
`G` last line of doc
`xG` xth line

`0` to position 1 on line
`^` to 1st non-blank character on line
`$` to end of line

`zz` positions current line at middle of screen
`zb` positions current line at bottom of screen
`zt` positions current line at top of screen
## By Paragraph

`}` jump forward a para
`{` jump forward a para

:set scrolloff=5 (scroll offset)
# Visual Mode

`v`  by character
`V`  by line
`ctrl+v` by block

`o, O` move end point of highlight
# Delete
- ## By line
  
  `dd` full file
  `d^`  from starting of line to cursor
  `d$`  cursor to end of line
- ## By word
  
  `dw` from cursor to end of word
  `db` word backword from cursor
  
  `d3b` 3 words backwards
  `d3w` 3 words forward
  
  `cw` current word and insert
# Undo & Redo

`ESC & u` to undo
`Esc & U` reverse change on current line
`ctrl+r` reverse last undo

#+BEGIN_TIP
`g+ / g` step forward / backword with changes
#+END_TIP
# Copy / Paste

`yy`  complete line
`y^`  cursor to 1st char
`y$`  cursor to end of line
`yG`  cursor to end of file
`yw`  cursor to end of word
# Toggle 

`~`  toggle case of single char
`7~`  toggle 7 chars

`gUw`  change case for word
`gU3w`  change case for 3 words
`gUU`  entire line to UPPER
`guu`  entire line lower
# Search & Replce

`/word` forward search
`?word` reverse search

`n / N` next occurrence & previous occurrence 

`/the`
`/the\>`
`/\<the`
`/\<the>`

`highlight & *` search for string

`:s/the/THE` first instance of current line
`:%s/the/THE/g` all instances per all line
`:%s/the/THE/gc` all instances per all line with confirmation
`:%s/the/THE/gci` all instances per all line with confirmation & case insensitive
`:5,25 s/the/THE/g` all instances on line 5 to 25

`%` substitute all lines
`g` all occurences
`c` confirm each operation
`i` case insensitive