# Project Title: 0x14 JavaScript - Web scraping

## Overview

This project focuses on web scraping using JavaScript, with an emphasis on manipulating JSON data, using the request and fetch API, and reading/writing files using the fs module. The project is designed to enhance your understanding of JavaScript programming, JSON manipulation, and web scraping techniques.

## Project Information

- **Author:** Guillaume, CTO at Holberton School
- **Weight:** 1

## Learning Objectives

By the end of this project, you should be able to:

- Understand why JavaScript programming is powerful.
- Manipulate JSON data effectively.
- Use the request and fetch API for making HTTP requests.
- Read and write files using the fs module.

## Resources

Read or watch the following resources:

- [Working with JSON data](#)
- [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](#)
- [request module](#)
- Modern JS
- [Learning Objectives](#)

## Requirements

### General

- **Allowed Editors:** vi, vim, emacs
- **Interpretation:** Ubuntu 20.04 LTS using node (version 14.x)
- **File Endings:** All files should end with a new line
- **Shebang Line:** The first line of all files should be exactly `#!/usr/bin/node`
- **README.md:** A README.md file at the root of the project folder is mandatory
- **Code Style:** Code should be semistandard compliant with semicolons on top (Reference: AirBnB style)
- **File Execution:** All files must be executable
- **No var:** You are not allowed to use var
- **File Length:** The length of your files will be tested using `wc`

### More Info

- **Node 14 Installation:**
  ```
  $ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
  $ sudo apt-get install -y nodejs
  ```

- **Semi-standard Installation:**
  ```
  $ sudo npm install semistandard --global
  ```

- **Request Module Installation:**
  ```
  $ sudo npm install request --global
  $ export NODE_PATH=/usr/lib/node_modules
  ```

_Note: The request module has been deprecated since February 2020, but it's still widely used for practicing web-scraping in JavaScript._

## Tasks

### Task 0: Readme

Write a script that reads and prints the content of a file.

```bash
$ ./0-readme.js cisfun
C is super fun!

$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
  at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
```

### Task 1: Write me

Write a script that writes a string to a file.

```bash
$ ./1-writeme.js my_file.txt "Python is cool"
$ cat my_file.txt ; echo ""
Python is cool
```

### Task 2: Status code

Write a script that displays the status code of a GET request.

```bash
$ ./2-statuscode.js https://alx-intranet.hbtn.io/status
code: 200

$ ./2-statuscode.js https://alx-intranet.hbtn.io/doesnt_exist
code: 404
```

### Task 3: Star wars movie title

Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

```bash
$ ./3-starwars_title.js 1
A New Hope

$ ./3-starwars_title.js 5
Attack of the Clones
```

### Task 4: Star wars Wedge Antilles

Write a script that prints the number of movies where the character “Wedge Antilles” is present.

```bash
$ ./4-starwars_count.js https://swapi-api.alx-tools.com/api/films/
3
```

### Task 5: Loripsum

Write a script that gets the contents of a webpage and stores it in a file.

```bash
$ ./5-request_store.js http://loripsum.net/api loripsum
$ cat loripsum
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...</p>
```

### Task 6: How many completed?

Write a script that computes the number of tasks completed by user id.

```bash
$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{ '1': 11, '2': 8, '3': 7, '4': 6, '5': 12, '6': 6, '7': 9, '8': 11, '9': 8, '10': 12 }
```

### Task 7: Who was playing in this movie? (Advanced)

Write a script that prints all characters of a Star Wars movie.

```bash
$ ./100-starwars_characters.js 3
Darth Vader
R2-D2
Luke Skywalker
Han Solo
Leia Organa
Chewbacca
Palpatine
Obi-Wan Kenobi
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Boba Fett
Ackbar
Arvel Crynyd
Mon Mothma
Nien Nunb
Wicket Systri Warrick
Bib Fortuna
C-3PO
Lando Calrissian
```

### Task 8: Right order (Advanced)

Write a script that prints all characters of a Star Wars movie in the right order.

```bash
$ ./101-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```