job :
    - title
    - location
    - job type
    - published at
    - vacancy
    - salary
    - category
    - experience
    - gender
    -


    - apply job
    - post job


blog:

    - title
    - descriptions
    - category
    - tags
    - content
    - auther
    -

    - search
    - comment
    - recent posts
    -

  contact
  home
  users




relations:

    - one to many    [ user - posts ]    - ForeignKey
    - many to many   [ user - groups ]   - many to many
    - one to one     [ user - profile ]  - one to one
