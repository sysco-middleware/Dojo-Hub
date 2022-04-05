- tags: #linux #Ansible
  title:: Ansible
- ### Using password protected privatekey with Ansible
  collapsed:: true
  
  Update the ansible.cfg
  ```
  [defaults]
  host_key_checking = False
  
  [ssh_connection]
  ssh_args = -o ForwardAgent=yes -o ControlMaster=auto -o ControlPersist=60s
  ```
  
  Add the private key to the ssh-agent
  ```
  $ ssh-agent bash
  ssh-add ~/.ssh/<private_key>
  
  ```
  
  Running  playbook with password protected privatekey
  ```
  ansible-playbook fmw_install.yml -b -vv --private-key /home/dhayanand/dojo_dhayanand -u dhayanand.sahadevan
  ```