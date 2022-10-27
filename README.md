# KRIE

_KRIE_ is a website for Korean people living in Ireland to share information about visas, accomodation, work and so on. All the users can view the posts and comments without registration and the registered users can write posts and comments.

![Multi device website mockup](documentation/responsive.png)

__Note__: The site is for educational purposes only and written in English.

<br>

# Table of Contents

[User Experience (UX)](#user-experience-ux)
- [Project Manifesto](#project-manifesto)
- [Website Name](#website-name)
- [Website Goal](#website-goal)
- [Target Audience](#target-audience)
- [User Stories](#user-stories)
- [Design](#design)
- [Wireframes](#wireframes)

[Database Model](#database-model)
- [Database](#database)
- [Entity Relationship Diagram](#entity-relationship-diagram)
- [Models](#models)

[Agile methodology](#agile-methodology)
- [MoSCoW method and story points](#moscow-method-and-story-points)
- [Iterations](#iterations)

[Technologies Used](#technologies-used)
- [Languages](#languages)
- [Framework](#framework)
- [Programs](#programs)

<br>

# User Experience (UX)

## Project Manifesto

There are very few platforms that are used by Koreans in Ireland. A _Facebook_ page, _Daum_ cafe and _Kakaotalk_ group chat are all that are available. The first two are managed by language school agencies and have become inactive and the latter is the most active platform but there are some limitations, such as anyone who wants to join needs to be invited by one of the members as it is a private group, and a new member will have a difficult time trying to find information that was posted before they joined the chat. This project is intended to overcome all of these flaws with the current platforms.

## Website Name

_KRIE_ comes from the country code top-level domains for South Korea and Ireland: .kr and .ie.

## Website Goal

To provide a platform where a user can easily find information and interact with others.

## Target Audience

- Korean people who are planning to live or currently living in Ireland.
- Other nationality people who are interested in interacting with Korean people in Ireland.

## User Stories

- As a first-time visitor,
    - [#1](https://github.com/sejungkwak/krie/issues/1) I want to know what this site is about immediately so that I can decide whether I will explore further.
    - [#2](https://github.com/sejungkwak/krie/issues/2) I want to navigate pages so that I can understand what types of information I could find here.

<br>

- As an unregistered user,
    - [#3](https://github.com/sejungkwak/krie/issues/3) I want to view a list of posts' titles so that I can choose which one to read.
    - [#4](https://github.com/sejungkwak/krie/issues/4) I want to order the posts by their number of likes so that I can see which is the most popular.
    - [#5](https://github.com/sejungkwak/krie/issues/5) I want to view comments on an individual post so that I can read the conversation.
    - [#6](https://github.com/sejungkwak/krie/issues/6) I want to search information with keywords so that I can easily find information that is useful and relevant to me.
    - [#7](https://github.com/sejungkwak/krie/issues/7) I want to sign up so that I can write posts, comment and give a like to other users' posts.
    - [#8](https://github.com/sejungkwak/krie/issues/8) I want to sign up with my _Google_ or _Facebook_ account so that I can easily sign in.

<br>

- As a registered user,
    - [#9](https://github.com/sejungkwak/krie/issues/9) I want to create a post to ask about others' recent experiences with the immigration office so that I can prepare for my upcoming appointment.
    - [#10](https://github.com/sejungkwak/krie/issues/10) I want to create a draft post so that I can continue it at a later date.
    - [#11](https://github.com/sejungkwak/krie/issues/11) I want to leave comments on a post so that I can be involved in the conversation.
    - [#12](https://github.com/sejungkwak/krie/issues/12) I want to leave secret comments with any sensitive information directly visible to the original poster so that I can comfortably share it.
    - [#13](https://github.com/sejungkwak/krie/issues/13) I want to send direct messages to other users so that I can interact with them privately.
    - [#14](https://github.com/sejungkwak/krie/issues/14) I want to give a like to a post so that I can highlight useful content for other users.
    - [#15](https://github.com/sejungkwak/krie/issues/15) I want to remove a like from a post so that I can ensure that I only give it to the content I feel is useful.
    - [#16](https://github.com/sejungkwak/krie/issues/16) I want to edit my post so that I can correct any mistakes or update other users with new information.
    - [#17](https://github.com/sejungkwak/krie/issues/17) I want to delete my post if no one answers my question so that I can maintain a clean profile.
    - [#18](https://github.com/sejungkwak/krie/issues/18) I want to see another user's posts and comments by clicking the username so that I can decide if the user is trustworthy.
    - [#19](https://github.com/sejungkwak/krie/issues/19) I want to see what posts I marked with a like so that I can easily find the post again.
    - [#20](https://github.com/sejungkwak/krie/issues/20) I want to get notified when there is a new comment on my posts so that I can follow up.
    - [#21](https://github.com/sejungkwak/krie/issues/21) I want to sign in and sign out of my account with my credentials so that I can keep my account secure.
    - [#22](https://github.com/sejungkwak/krie/issues/22) I want to update my password so that I can keep my account secure.
    - [#23](https://github.com/sejungkwak/krie/issues/23) I want to reset my password so that I can access my account even if I forget it.
    - [#35](https://github.com/sejungkwak/krie/issues/35) I want to update my profile so that I can keep my information up to date.
    - [#36](https://github.com/sejungkwak/krie/issues/36) I want to get feedback so that I can ensure that I have interacted with the website correctly.

<br>

- As a superuser,
    - [#24](https://github.com/sejungkwak/krie/issues/24) I want to pin important posts so that users can easily view them.
    - [#25](https://github.com/sejungkwak/krie/issues/25) I want to create a category when needed so that I can manage the site effectively.
    - [#26](https://github.com/sejungkwak/krie/issues/26) I want to delete content when inappropriate so that I can maintain the site and ensure that only useful or relevant content remains.
    - [#27](https://github.com/sejungkwak/krie/issues/27) I want to ban scammers'/spammers' accounts so that I can ensure only trusted users can access the site.

<br>

## Design

- Colour Scheme

    The colour scheme has been created based on the Korean and Irish flags. The chosen colours were selected using [_Canva_](https://www.canva.com/).

    <details>
    <summary>View the colour scheme</summary>

    ![Colour Scheme](documentation/colour-scheme.png)

    </details>

<br>

- Typography

    [Gothic A1](https://fonts.google.com/specimen/Gothic+A1) is the main font used throughout the whole website with Sans Serif as the fallback font in case the font isn't imported into the browser correctly.

    I have chosen the font with the criteria below in mind:

    - It supports Korean characters.
    - It gives a neutral emotional response to the reader.
    - It has a readable body typeface.
    - It has a variety of weights and styles.

- Logo

    ![Logo](documentation/logo.png)

- Favicon

    ![Favicon](documentation/favicon.ico)

<br>

## Wireframes

<details>
    <summary>Homepage</summary>
    <img src="documentation/wireframes/home.png">
</details>

<details>
    <summary>Sign in</summary>
    <img src="documentation/wireframes/signin.png">
</details>

<details>
    <summary>Sign up</summary>
    <img src="documentation/wireframes/signup.png">
</details>

<details>
    <summary>Profile</summary>
    <img src="documentation/wireframes/profile_posts.png">
    <img src="documentation/wireframes/profile_comments.png">
    <img src="documentation/wireframes/profile_about.png">
    <img src="documentation/wireframes/profile_update.png">
    <img src="documentation/wireframes/profile_pwchange.png">
</details>

<details>
    <summary>Post list and CRUD</summary>
    <img src="documentation/wireframes/post_list.png">
    <img src="documentation/wireframes/post_create.png">
    <img src="documentation/wireframes/post_read.png">
    <img src="documentation/wireframes/post_update.png">
    <img src="documentation/wireframes/post_delete.png">
</details>

<details>
    <summary>Search result</summary>
    <img src="documentation/wireframes/search.png">
</details>

[Back To **Table of Contents**](#table-of-contents)

<br>

# Database Model

## Database

[_Heroku_ PostgreSQL](https://devcenter.heroku.com/categories/heroku-postgres) was used for the main database from the earliest stage of development.

## Entity Relationship Diagram

![ER Diagram](documentation/data-model.png)

## Models

- User/Profile table

    Profile model inherits the Django-allauth's user model containing the username, email address and password. I expanded it with the location and bio which are optional. The Django signals were used to create a profile for the newly registered user.

    | Field Name | Type | Arguments |
    | :--------: | :--: | :-------: |
    | id | BigAutoField | primary_key=True |
    | user | OneToOneField(User) | null=True, on_delete=models.CASCADE |
    | location | CharField | max_length=20, blank=True, null=True |
    | bio | CharField | max_length=200, blank=True, null=True |

    - Methods

        ```
        def __str__(self):
            return self.user.username
        ```

- Category table

    The slug field was added for the URL paths as it gives users more information than an id.

    | Field Name | Type | Arguments |
    | :--------: | :--: | :-------: |
    | slug | SlugField | max_length=15, unique=True |
    | name | CharField | max_length=15, unique=True |

    - Metadata

        ```
        class Meta:
            verbose_name_plural = 'Categories'
        ```

    - Methods

        ```
        def __str__(self):
            return self.name
        ```

- Post table

    | Field Name | Type | Arguments |
    | :--------: | :--: | :-------: |
    | id | BigAutoField | primary_key=True |
    | author | ForeignKey(User) | on_delete=models.CASCADE, related_name='posts' |
    | category | ForeignKey(Category) | on_delete=models.CASCADE, related_name='posts' |
    | title | CharField | max_length=200, unique=True |
    | body | TextField | verbose_name='Text' |
    | created_on | DateTimeField | auto_now_add=True |
    | updated_on | DateTimeField | auto_now=True |
    | likes | ManyToManyField(User) | related_name='post_likes', blank=True |

    - Metadata

        ```
        class Meta:
            ordering = ['-created_on']
        ```

    - Methods

        ```
        def __str__(self):
            return self.title

        def number_of_likes(self):
            return self.likes.count()

        def number_of_comments(self):
            return self.comments.count()
        ```

- Comment table

    | Field Name | Type | Arguments |
    | :--------: | :--: | :-------: |
    | original_post | ForeignKey(Post) | on_delete=models.CASCADE, related_name='comments' |
    | author | ForeignKey(User) | on_delete=models.CASCADE, related_name='comments' |
    | body | TextField | max_length=255 |
    | created_on | DateTimeField | auto_now_add=True |
    | updated_on | DateTimeField | auto_now=True |

    - Metadata

        ```
        class Meta:
            ordering = ['-created_on']
        ```

    - Methods

        ```
        def __str__(self):
            return self.body
        ```

[Back To **Table of Contents**](#table-of-contents)

<br>

# Agile methodology

## MoSCoW method and story points

_Github_ Projects kanban board and Issues were used to practise agile methodology. After creating the user stories, I prioritised each story using MoSCoW method, excluded ‘won’t have’ stories and set the points using modified Fibonacci sequence(1, 2, 3, 5, 8, 13, 20) based on complexity, amount of work and repetition.
The details are as following:

### Theme: Website appearance
- Epic: Intuitive website

    | Issue # | User Story | Prioritisation | Points |
    | :-----------: | :---------: | :-----------: | :-----------: |
    | [#1](https://github.com/sejungkwak/krie/issues/1) | As a first-time visitor, I want to know what this site is about immediately so that I can decide whether I will explore further. | Must have | 2 |
    | [#2](https://github.com/sejungkwak/krie/issues/2) | As a first-time visitor, I want to navigate pages so that I can understand what types of information I could find here. | Must have | 1 |

### Theme: Authentication
- Epic: Sign up

    | Issue # | User Story | Prioritisation | Points |
    | :-----------: | :---------: | :-----------: | :-----------: |
    | [#7](https://github.com/sejungkwak/krie/issues/7) | As an unregistered user, I want to sign up so that I can write posts, comment and give a like to other users' posts. | Must have | 8 |

- Epic: Sign in and sign out

    | Issue # | User Story | Prioritisation | Points |
    | :-----------: | :---------: | :-----------: | :-----------: |
    | [#21](https://github.com/sejungkwak/krie/issues/21) | As a registered user, I want to sign in and sign out of my account with my credentials so that I can keep my account secure. | Must have | 3 |

- Epic: Reset password

    | Issue # | User Story | Prioritisation | Points |
    | :-----------: | :---------: | :-----------: | :-----------: |
    | [#22](https://github.com/sejungkwak/krie/issues/22) | As a registered user, I want to update my password so that I can keep my account secure. | Could have | 8 |
    | [#23](https://github.com/sejungkwak/krie/issues/23) | As a registered user, I want to reset my password so that I can access my account even if I forget it. | Should have | 13 |

### Theme: CRUD
- Epic: Post CRUD

    | Issue # | User Story | Prioritisation | Points |
    | :-----------: | :---------: | :-----------: | :-----------: |
    | [#3](https://github.com/sejungkwak/krie/issues/3) | As an unregistered user, I want to view a list of posts' titles so that I can choose which one to read. | Must have | 5 |
    | [#9](https://github.com/sejungkwak/krie/issues/9) | As a registered user, I want to create a post to ask about others' recent experiences with the immigration office so that I can prepare for my upcoming appointment. | Must have | 5 |
    | [#16](https://github.com/sejungkwak/krie/issues/16) | As a registered user, I want to edit my post so that I can correct any mistakes or update other users with new information. | Should have | 8 |
    | [#17](https://github.com/sejungkwak/krie/issues/17) | As a registered user, I want to delete my post if no one answers my question so that I can maintain a clean profile. | Should have | 5 |

- Epic: Comment CRUD

    | Issue # | User Story | Prioritisation | Points |
    | :-----------: | :---------: | :-----------: | :-----------: |
    | [#11](https://github.com/sejungkwak/krie/issues/11) | As a registered user, I want to leave comments on a post so that I can be involved in the conversation. | Must have | 5 |
    | [#5](https://github.com/sejungkwak/krie/issues/5) | As an unregistered user, I want to view comments on an individual post so that I can read the conversation. | Must have | 3 |

- Epic: Likes

    | Issue # | User Story | Prioritisation | Points |
    | :-----------: | :---------: | :-----------: | :-----------: |
    | [#14](https://github.com/sejungkwak/krie/issues/14) | As a registered user, I want to give a like to a post so that I can highlight useful content for other users. | Could have | 3 |
    | [#15](https://github.com/sejungkwak/krie/issues/15) | As a registered user, I want to remove a like from a post so that I can ensure that I only give it to the content I feel is useful. | Could have | 3 |

- Epic: Search

    | Issue # | User Story | Prioritisation | Points |
    | :-----------: | :---------: | :-----------: | :-----------: |
    |[#6](https://github.com/sejungkwak/krie/issues/6) | As an unregistered user, I want to search information with keywords so that I can easily find information that is useful and relevant to me. | Could have | 20 |

- Epic: Profile

    | Issue # | User Story | Prioritisation | Points |
    | :-----------: | :---------: | :-----------: | :-----------: |
    | [#18](https://github.com/sejungkwak/krie/issues/18) | As a registered user, I want to see another user's posts and comments by clicking the username so that I can decide if the user is trustworthy. | Could have | 13 |

### Theme: Superuser

- Epic: Maintain the site 

    | Issue # | User Story | Prioritisation | Points |
    | :-----------: | :---------: | :-----------: | :-----------: |
    | [#26](https://github.com/sejungkwak/krie/issues/26) | As a superuser, I want to delete content when inappropriate so that I can maintain the site and ensure that only useful or relevant content remains. | Should have | 1 |
    | [#27](https://github.com/sejungkwak/krie/issues/27) | As a superuser, I want to ban scammers'/spammers' accounts so that I can ensure only trusted users can access the site. | Should have | 2 |

## Iterations

The project was carried out over 5 iterations between the 11th of October and the 25th of October and each iteration lasted 3 days due to the tight schedule. The velocity is 23.6 points.

- Iteration 1 (Closed points 11 / Planned points 24)

    ![Iteration 1](documentation/agile/agile_iter1.png)

- Iteration 2 (Closed points 24 / Planned points 24)

    ![Iteration 2](documentation/agile/agile_iter2.png)

- Iteration 3 (Closed points 34 / Planned points 34)

    ![Iteration 3](documentation/agile/agile_iter3.png)

- Iteration 4 (Closed points 23 / Planned points 25)

    ![Iteration 4](documentation/agile/agile_iter4.png)

- Iteration 5 (Closed points 26 / Planned points 26)

    ![Iteration 5](documentation/agile/agile_iter5.png)

The details can be found [here](https://github.com/sejungkwak/krie/milestones?direction=desc&sort=title&state=closed).

[Back To **Table of Contents**](#table-of-contents)

<br>

# Technologies Used

## Languages

- [Python](https://www.python.org/) was used as the main scripting language.
    - The list of third-party packages can be found [here: requirements.txt](requirements.txt).
- [HTML](https://en.wikipedia.org/wiki/HTML) was used to present and structure content.
- [CSS](https://en.wikipedia.org/wiki/CSS) was used to style content.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used to automatically close the alerts.

## Framework

- [Django](https://www.djangoproject.com/) was used as the main Python framework.
- [Bootstrap](https://getbootstrap.com/) was heavily used for styling.

## Programs

- [Adobe Express](https://www.adobe.com/express/feature/image/resize) was used to resize the landing page photos.
- [Balsamiq](https://balsamiq.com/) was used to create the wireframes.
- [Canva](https://www.canva.com/en_gb/) was used to design the logo, favicon and hero section images.
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) was used to view the site's styling, debug during development and check runtime performance.
- [Cloudinary](https://cloudinary.com/) was used to store static files.
- [Diagrams.net](https://app.diagrams.net/) was used to create the ERD.
- [Eightshapes](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23DB2A37%0D%0A%230C51AB%0D%0A%23000%0D%0A%2356AA35%0D%0A%23FFF%0D%0A%23F57B23&es-color-form__tile-size=compact&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18) was used to check the colour combination for accessibility purposes.
- [Favicon.io](https://favicon.io/) was used to create the favicon.
- [Font Awesome](https://fontawesome.com/) was used for the icons.
- [Git](https://git-scm.com/) was used for version control.
- [GitHub](https://github.com/) was used to store and deploy the project's code.
- [Gitpod](https://www.gitpod.io/) was used to develop and test my code.
- [Google Fonts](https://fonts.google.com/) was used to import Gothic A1 into the style.css file.
- [Grammarly](https://www.grammarly.com/) was used to check for errors in the README.
- [Heroku](https://heroku.com/) was used to deploy the project.
- [Pixlr](https://pixlr.com/) was used to change the hero section image colours.
- [Privacy Policy Generator](https://www.privacypolicygenerator.info/) was used to create the site's privacy policy.
- [Techsini](https://techsini.com/multi-mockup/index.php) was used to create the image showing a responsive design for the README.
- [Terms and Conditions Generator](https://www.termsandconditionsgenerator.com/) was used to create the site's terms and conditions.
- [Visual Studio Code](https://code.visualstudio.com/) was used to edit my code and create SVG paths from SVG image files.

[Back To **Table of Contents**](#table-of-contents)

<br>