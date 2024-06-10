## Normalisation Exercise

### The Scenario

The below table contains information about members of a movie tracking website. The website allows registered members to create a list of the movies they have seen.

Assumptions:

- The column `member` (email address) is unique to a single customer, but different customers could have the same name
- Members can specify just one single favourite genre
- The columns `movies` and `movie_years` contain lists of the movies a member has seen and the year that movie was released.

### The Goal

Normalise the data by working through each normal form one-by-one from 1NF to 3NF.

For each stage note what tables exist, and what attributes (columns) they contain. You do not need to show the actual data contained in the table, but may do so if it helps!

If there is no violation of the rules of a given normal form, there may be nothing to do at that step.

`member_movies` table

| member (KEY)      | fav_genre | username        | movies           | movie_years |
| ----------------- | --------- | --------------- | ---------------- | ----------- |
| tomk@example.com  | Horror    | tommy-k         | The Shining      | 1980        |
| johnd@example.com | Romance   | the-movie-guy   | Titanic          | 1997        |
| janed@example.com | Comedy    | i-love-minions  | Titanic, Minions | 1997, 2015  |
| maryw@example.com | Horror    | horror-fan-1990 | The Shining, IT  | 1980, 2017  |

### Exercise 1 - 1NF

| user_id | member (KEY)      | fav_genre | username        | movies      | movie_years |
| ------- | ----------------- | --------- | --------------- | ----------- | ----------- |
| U001    | tomk@example.com  | Horror    | tommy-k         | The Shining | 1980        |
| U002    | johnd@example.com | Romance   | the-movie-guy   | Titanic     | 1997        |
| U003    | janed@example.com | Comedy    | i-love-minions  | Titanic     | 1997        |
| U003    | janed@example.com | Comedy    | i-love-minions  | Minions     | 2015        |
| U004    | maryw@example.com | Horror    | horror-fan-1990 | The Shining | 1980        |
| U004    | maryw@example.com | Horror    | horror-fan-1990 | IT          | 2017        |


### Exercise 2 - 2NF


| user_id | member (KEY)      | fav_genre | username        |
| ------- | ----------------- | --------- | --------------- |
| U001    | tomk@example.com  | Horror    | tommy-k         |
| U002    | johnd@example.com | Romance   | the-movie-guy   |
| U003    | janed@example.com | Comedy    | i-love-minions  |
| U004    | maryw@example.com | Horror    | horror-fan-1990 |


| user_id | movie_id |
| ------- | -------- |
| U001    | M001     |
| U002    | M002     |
| U003    | M002     |
| U003    | M003     |
| U004    | M001     |
| U004    | M004     |

| movie_id | movies      | movie_year |
| -------- | ----------- | ---------- |
| M001     | The Shining | 1980       |
| M002     | Titanic     | 1997       |
| M003     | Minions     | 2015       |
| M004     | IT          | 2017       |
### Exercise 3 - 3NF


| user_id | member_email      | username        |
| ------- | ----------------- | --------------- |
| U001    | tomk@example.com  | tommy-k         |
| U002    | johnd@example.com | the-movie-guy   |
| U003    | janed@example.com | i-love-minions  |
| U004    | maryw@example.com | horror-fan-1990 |

| genre_id | genre   |
| -------- | ------- |
| G001     | Horror  |
| G002     | Romance |
| G003     | Comedy  |
| G004     | Horror  |

| user_id | favourite_genre_id |
| ------- | ------------------ |
| U001    | G001               |
| U002    | G002               |
| U003    | G003               |
| U004    | G004               |

| movie_id | movie       | movie_year |
| -------- | ----------- | ---------- |
| M001     | The Shining | 1980       |
| M002     | Titanic     | 1997       |
| M003     | Minions     | 2015       |
| M004     | IT          | 2017       |

| user_id | movies |
| ------- | ------ |
| U001    | M001   |
| U002    | M002   |
| U003    | M003   |
| U003    | M002   |
| U004    | M004   |
| U004    | M001   |


### Stretch Goal

Now create your normalised database design in SQL!

You can refer back to the 'prep' stage in databases-exercise.md for how to set up and access a locally run database. Use either the `docker-compose.postgres.yml` or `docker-compose.mysql.yml` file in the `handouts` folder, depending on which database engine you have been taught previously.

To run docker-compose with a custom .yml file, use the `-f` flag:
`docker-compose -f docker-compose.postgres.yml up -d`
