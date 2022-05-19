tags:: #git #github, #cheatsheet

- used to re-write the commit history and below are the options available
  
  `pick` : use the commit
  `reword` : use the commit, but edit the commit message
  `edit` : use the commit but stop for amending
  `squash` : use commit contents but meld it into previous commit with new commit message
  `fixup` : use commit contents but meld it into previous commit and discard the commit message
  `drop` : remove the commit
- Interactive rebase example
	- The plan
	  ![2021-11-15_12-16.png](../assets/2021-11-15_12-16_1636975216849_0.png)
	- change the commit message
	  
	  `git rebase -i HEAD~9` then update the action in 1st window and change the commit message in 2nd window
	  
	  ![2021-11-15_11-29.png](../assets/2021-11-15_11-29_1636972952959_0.png) 
	  ![2021-11-15_11-29_1.png](../assets/2021-11-15_11-29_1_1636972964354_0.png)
	  ![2021-11-15_11-30.png](../assets/2021-11-15_11-30_1636973234182_0.png)
	- perform `fixup` to save the commit content but discard the commit messages
	  
	  `git rebase -i HEAD~9`
	  
	  ![2021-11-15_11-33.png](../assets/2021-11-15_11-33_1636973215819_0.png)
	  ![2021-11-15_11-34.png](../assets/2021-11-15_11-34_1636973342424_0.png)
	- completely drop a commit and changes made in that commit
	  
	  `git rebase -i HEAD~6`
	  #+BEGIN_CAUTION
	  With every `fixup` the no of commits gets changed so make sure to use the correct reference to HAED
	  #+END_CAUTION
	  ![2021-11-15_11-38.png](../assets/2021-11-15_11-38_1636973563490_0.png) 
	  ![2021-11-15_11-38_1.png](../assets/2021-11-15_11-38_1_1636973587219_0.png)
	- `fixup` vs `squash`
	  
	  `squash` prompts for new commit message but `fixup` uses the commit message of the commit that we will merge into
	  
	  ![2021-11-15_12-04.png](../assets/2021-11-15_12-04_1636975393378_0.png) 
	  ![2021-11-15_12-05.png](../assets/2021-11-15_12-05_1636975406231_0.png)
	  ![2021-11-15_12-06.png](../assets/2021-11-15_12-06_1636975428973_0.png)