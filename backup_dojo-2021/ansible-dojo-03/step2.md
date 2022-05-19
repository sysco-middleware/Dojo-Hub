## Task

Implement an Ansible Playbook  which automatically installs and runs: Tomcat9 web server

### Considerations

1. Ubuntu's apt-get catalog must be updated as the first (separate) task of the playbook
2. When executing this step, an error might show up due to a broken link in the catalog; 
you don't need to fix this, but you will need to ignore the error and continue for your playbook
to run successfully (the catalog will be updated in spite of the error)
3. The playbook must make sure that the correct package is installed and the service up & running

## Acceptance Criteria

1. Your playbook executes properly within Katacoda and you're able to see the Tomcat9 landing page 
   in the upper frame
2. Your pull request has been reviewed and merged by a code owner