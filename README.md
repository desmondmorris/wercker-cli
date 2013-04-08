[![Wercker status](https://app.wercker.com/status/e03bf0c77a793a7857a2b8abc9fac779/m)](https://app.wercker.com/project/bykey/e03bf0c77a793a7857a2b8abc9fac779)
# wercker-cli #

A cli tool for <http://wercker.com/> - Continuous deployment made easy.

Usage:

    $ wercker
    -----------------------
    welcome to wercker-cli
    -----------------------

    Usage:
        wercker create
        wercker status
        wercker deploy
        wercker builds
        wercker open targets
        wercker queue
        wercker apps
        wercker link
        wercker login
        wercker logout
        wercker targets add
        wercker targets list
        wercker targets details
        wercker validate
        wercker --version

## Commands
### create
Starts a wizard like setup, to get your application fully working on wercker. In detail it:
* adds a new application based on your current git repository
* checks for permissions on github or bitbucket
* triggers a build
* tries to find and add a heroku deploy target.

The newly created application information is stored in a .wercker file in the root of your repository. You don't need to add this file to your git repository, if a user has access to the project, a user can run `wercker link` to rebuild the .wercker file

### status
Shows the status of the latest build.

### deploy
Starts a simple wizard like setup for deploying your latest build to a deploy target.

### login
Retrieves a login token for wercker and stores it in the .netrc in the users' home folder.

### logout
Removes the login token from the .netrc file

### open targets
Opens a webpage showing a deploy target's details

### apps
Shows a list of all applications available to the user

### queue
Shows a list of all builds and deploys that are still scheduled.

### apps link
Retrieve application information for storing in the .wercker file.

### builds
Shows a list of the most recent builds

### targets add
Add a new deploy target to your application. Currently only supports heroku targets.

### targets list
Lists all deploy targets

### targets details
This is an alias for `wercker open targets`

### validate
Checks if your [wercker.json](http://devcenter.wercker.com/articles/werckerjson) is valid.
