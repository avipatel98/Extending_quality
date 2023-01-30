| Initial State | Event | Next State | 
|-|-|-|
| Sign Up Page | Sign Up | Logged In |
| Sign Up Page | Invalid Sign Up Details | Sign Up Page |
| Log In Page | Log In | Logged In |
| Log In Page | Invalid Log In Details | Log In Page |
| Logged In Page | Log Out | Log In Page |
| Log In Page | Sign Up Redirect | Sign Up Page |
| Sign Up Page | Log In | Log In Page |

Test cases for each event:

1. Correct Sign up
    - Sign up with valid password and email.
2. Invalid Sign up (Based on the logic of the error handling only one would need to be tested)
    - Sign up with invalid email and correct password.
    - Sign up with correct email and invalid password.
    - Sign up with both fields invalid.
    - Empty email field and or empty password field.
3. Correct Log in
    - Log in with existing email and correct password.
4. Invalid Log in (Based on the logic of the error handling only one would need to be tested)
    - Log in with incorrect email.
    - Log in with incorrect password.
    - Log in with both fields incorrect.
    - Empty email field and or empty password field.
5. Log out
    - Click log out and return to log in page
6. Log in to sign up and vice versa
    - Click to take you to the opposite page

Test case that covers all events:
Start: Log in page
Sign up redirect => Sign up page
Sign up => Logged in page
Log out => Log in page
Log in => Logged in page