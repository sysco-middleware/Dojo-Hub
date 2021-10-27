## Check for an existing SSH key

- Let's check if we already have some keys:

`ls -al ~/.ssh`{{copy}}

- In case we get a "no such file or directory" error message we would need to 
create the .ssh directory (`mkdir $HOME/.ssh`), but in this example it is already there, 
so let's skip to the next task:

## Generate a new set of keys

- Let's generate some keys specifically for this purpose (GitHub SSH integration):

`ssh-keygen -t rsa -b 4096 -C your@email.com`{{copy}}

- Be careful to replace your actual email (the one you use for GitHub) into the command
- When you're prompted for a file in which to save the key use: `/root/.ssh/id_rsa_git`{{copy}}
- For simplicity, it is better to not use a passphrase (just click enter twice in a row when prompted)

## Add your SSH key to ssh-agent

- Make sure that the agent is running:

`eval "$(ssh-agent -s)"`{{copy}}

- Add the private key to the agent:

`ssh-add ~/.ssh/id_rsa_git`{{copy}}

## Copy your public SSH key to the clipboard

- print the contents of your public key to the console with: 

`cat ~/.ssh/id_rsa_git.pub`{{copy}}

- then highlight and copy the output.

## Add your public SSH key to GitHub

- Follow these instructions from step 2 (web browser):

https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

## Test Authentication

`ssh -T git@github.com`{{copy}}

- If you've followed all of these steps correctly, you should see this message:

`Hi your_user_name! You've successfully authenticated, but GitHub does not provide shell access.`

- Now you can also try cloning a repo with SSH, for example:

`git@github.com:sysco-middleware/osb-integration-logger-sp.git`{{copy}}