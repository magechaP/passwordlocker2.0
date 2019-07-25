# Password-Locker
#### By **[Peter Magecha]** (https://github.com/magechaP)
## Description
This is a commandline application that enables a user to sign up and once logged in, they are able to save details of any other accounts they have and access these details when they need them
## Setup/Installation Requirements
* Ensure git is intalled in your computer
* Use 'git clone' command to Clone and then unzip the repository from github, https://github.com/magechaP/Passwordlocker2.0.git
* Navigate to the folder in which the cloned repository is saved using the terminal
* Run the command 'chmod +x run.py' to make the file executable
* Use the command './run.py' to run the application on the terminal
## BDD
|Behavior                                    |Input                                  |Output
|--------------------------------------------|---------------------------------------|----------------------------------------
|User enters their name                      | Apwao                                 | Gives user options to create account or exit
|User chooses to create account              | ca (create account)                   | Asks user for username and password
|User chooses to exit account                | ex (exit account)                     | Exits the application
| User enters password and username          | purity, 89765                         | Gives user credential options
|User chooses to have password auto-generated| yes                                   | Asks user for length of password
|User chooses to find credential             | fc (find credential), Account name    | Display all details of the credential
|User chooses to display credentials         | dc (display credentials), account name| Displays all saved credentials
|User chooses to delete credential           | delc (delete credential), account name| Deletes the credential
|User chooses to copy credentials            | cp (copy credential)                  | Copies specified detail to clip board
|User chooses to exit cedentials             | ex (exit)                             | Returns to create account page
## Known Bugs
* No known bugs
## Technologies Used
* Python
* Unittesting
* Git
* pyperclip
## Support and contact details
Incase of any issues, ideas, questions or concerns, contact contributor at magechapeter@gmail.com
In order to contribute to the code: Fork a copy of the repository, push changes to a branch called contributions. Issue a pull request to the contributor.
### License
Copyright (c) 2019 **Peter Magecha**
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
