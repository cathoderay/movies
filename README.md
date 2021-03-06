# movies
Django app to show movies

## quick start

In order to get started, run:
```shell
 $ curl -s https://raw.githubusercontent.com/cathoderay/movies/master/run.sh | bash
```
This script assumes you have *git*, *virtualenv* and *pip* installed. I suggest you to read it before running. If you trust me, you can run it anyway, =)

If everything runs smoothly, you should be able to see something like this:
![Screenshot](https://github.com/cathoderay/movies/blob/master/screenshots/home.jpg)

## database
This projects contains a db.sqlite database, so you can deal with the resulting app right away. The dataset was collected via webscrapping. The script used is contained in the **fixtures** directory.

## admin
In order to manage the movies, you can go to **/admin**:

Default username: admin

Default password: 1234

## todo
   * In order to scale, this code should migrate from python to js. Using angularjs + pagination (fetching data as needed) would improve its performance a lot; Unfortunately, I didn't have time to make it work yet;
   * Add prod settings;
   * Write tests!
