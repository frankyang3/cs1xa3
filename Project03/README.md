# CS 1XA3 Project03 - yangf51
## Usage
Install conda enivornment with
```
conda create -n djangoenv python=3.7 
conda activate djangoenv
```
Run locally with:
```
python manage.py runserver localhost:8000
```
* access on localhost:8000/e/yangf51

Run on mac1xa3.ca with:
```
python manage.py runserver localhost:10113 &
```
* access on mac1xa3.ca/e/yangf51

...
Log in with: test9, password: 1234

Other notable users (objective 11):
User: bshnob1
Pass: 1234
User: jshmoe
Pass: 1234
User: throw1
Pass: happyjay


...
## Objective 01
Description:
- login.djhtml is displayed immediately after loading in. It also defaults here whenever a user is logged out
- If the signup button is clicked, it redirects to signup.djhtml
- Upon pressing login, it creates a pop up modal, with 2 inputs, username and password
- Logging in makes a post request to e/yangf51/messages.djhtml
- In signup.djhtml, a user may input a username and password to create a new user on the site

Exceptions:
- If the /e/yangf51/login.djhtml is called without arguments is redirects
to login.djhtml

## Objective 02 and 03
Description:
- clicking the profile button in the top right corner redirects to account.djhtml
- There are 2 forms on this page, one to change password, one to change about me
- Simply follow the instructions given to change your account info or password
- The information will be displayed on the left column

Exceptions:
- Note that all fields must be filled in a form to submit
- Password changes have requirements of minimum length and characters, unlike signup

## Objective 04 and 05 and 06
Description:
- Clicking on the person icon in the top navbar redirects to people.djhtml, showing potential friends
- Initially shows one person, pressing more will reveal 2 more, takes first non-friends in the user database
- The list will not contain any of your friends
- A session variable keeps track of how many people are shown, logging out will reset this number
- You can send a friend request to any person
- You can accept incoming friend requests on the right column, this is done through people.js sending an ajax POST request
- If the person accepts your friend request, you become friends, and his nae will appear on the right column in messages

Exceptions:
- Note that if someone accepts your friend request, you will have to refresh the page to update it, but if you accept a friend request it will automatically update for you

## Objective 07 and 08 and 09 and 10
Description:
- This shows messages.djhtml, the page shown when first logged in
- When you send a message, messages.js sends an ajax POST, which saves the message and username in the messages database
- The page shows all messages saved within the database, initally shows 1. Pressing more will show 2 more messages
- Pressing like will log the username as a liker for the message, making sure the user cannot like multiple times
- Upon pressing like, the page reloads due to messages.js, and the like is shown

Exceptions:
- Note that when another user likes a message, it will not be shown unti the page is refreshed
