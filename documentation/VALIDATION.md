# Table of Contents

- [HTML Validation](#html-validation)
- [CSS Validation](#css-validation)
- [JS Validation](#js-validation)
- [Python Validation](#python-validation)

## HTML Validation

- Homepage

    ![Homepage](testing/w3c-testing-markup/home.png)

- Category page

    - Rooms
    ![Category - Rooms](testing/w3c-testing-markup/category_rooms.png)

    - Jobs
    ![Category - Jobs](testing/w3c-testing-markup/category_jobs.png)

    - Visas
    ![Category - Visas](testing/w3c-testing-markup/category_visas.png)

    - Market
    ![Category - Market](testing/w3c-testing-markup/category_market.png)

    - Random
    ![Category - Random](testing/w3c-testing-markup/category_random.png)

- Post detail page

    ![Post detail page](testing/w3c-testing-markup/post_read.png)

- Post create page

    ![Post create page](testing/w3c-testing-markup/post_create.png)

- Profile page

    - Activity - Posts
    ![Activity - Posts](testing/w3c-testing-markup/profile_activity_posts.png)

    - Activity - Comments
    ![Activity - Comments](testing/w3c-testing-markup/profile_activity_comments.png)

    - Activity - About
    ![Activity - About](testing/w3c-testing-markup/profile_activity_about.png)

    - Edit profile
    ![Edit profile](testing/w3c-testing-markup/profile_edit.png)

    - Password change
    ![Password change](testing/w3c-testing-markup/profile_pwchange.png)

- Sign up page

    ![Sign up page](testing/w3c-testing-markup/signup.png)

- Sign in page

    ![Sign in page](testing/w3c-testing-markup/signin.png)

- Sign out page

    ![Sign out page](testing/w3c-testing-markup/signout.png)

- Password reset page

    Previously there was an error as I added class attributes not knowing that Django-allauth already set it.
    ![Password reset page error](testing/w3c-testing-markup/pwreset-error.png)

    It has been resolved.
    ![Password reset page fix](testing/w3c-testing-markup/pwreset-fix.png)

[Back To **Table of Contents**](#table-of-contents)

<br>

## CSS Validation

![CSS Validation](testing/w3c-testing-css/validity.png)

When passing through the validation for the first time, the validator found 17 errors with `Parse Error`. This was with Bootstrap version 5.2 so I replaced it with a downgrade version(5.1).

![Errors](testing/w3c-testing-css/error.png)

All 262 warnings are from the Bootstrap code and the messages are either `Due to their dynamic nature, CSS variables are currently not statically checked`, `-ooo is a vendor extension` or `Same color for background-color and border-color`. These do not affect the site functionality and even support cross-browser compatibility.

![Warnings](testing/w3c-testing-css/warning.png)

[Back To **Table of Contents**](#table-of-contents)

<br>

## JS Validation

![JSHint](testing/jshint.png)

[Back To **Table of Contents**](#table-of-contents)

<br>

## Python Validation

The project settings script(`krie/settings.py`) contains 5 issues related to the line length. After reading through some conversations on the _Slack_ channel, I decided not to modify the code as they are part of Django's configuration.

![Python Validation](testing/pycodestyle.png)

[Back To **Table of Contents**](#table-of-contents)