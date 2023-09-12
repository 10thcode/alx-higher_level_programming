
# 0x12. JavaScript - Warm up

JavaScript - Variables, data types, operators, functions, objects and arrays.

## Tasks

- ***[0-javascript_is_amazing.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/0-javascript_is_amazing.js)***

    A script that prints “JavaScript is amazing”.

    *Example*
    ```
    guillaume@ubuntu:~/0x12$ ./0-javascript_is_amazing.js 
    JavaScript is amazing
    guillaume@ubuntu:~/0x12$ 
    guillaume@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js 
    guillaume@ubuntu:~/0x12$ 
    ```

- ***[1-multi_languages.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/1-multi_languages.js)***

    A script that prints 3 lines:
    - The first line: “C is fun”
    - The second line: “Python is cool”
    - The third line: “JavaScript is amazing”

    *Example*
    ```
    guillaume@ubuntu:~/0x12$ ./1-multi_languages.js 
    C is fun
    Python is cool
    JavaScript is amazing
    guillaume@ubuntu:~/0x12$ 
    ```

- ***[2-arguments.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/2-arguments.js)***

    A script that prints a message depending of the number of arguments passed

    *Example*
    ```
    guillaume@ubuntu:~/0x12$ ./2-arguments.js 
    No argument
    guillaume@ubuntu:~/0x12$ ./2-arguments.js Best
    Argument found
    guillaume@ubuntu:~/0x12$ ./2-arguments.js Best School
    Arguments found
    guillaume@ubuntu:~/0x12$ 
    ```

- ***[3-value_argument.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/3-value_argument.js)***

    A script that prints the first argument passed to it.

    *Example*
    ```
    guillaume@ubuntu:~/0x12$ ./3-value_argument.js 
    No argument
    guillaume@ubuntu:~/0x12$ ./3-value_argument.js School
    School
    guillaume@ubuntu:~/0x12$
    ```

- ***[4-concat.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/4-concat.js)***

    A script that prints two arguments passed to it, in the following format: “ is ”

    *Example*
    ```
    guillaume@ubuntu:~/0x12$ ./4-concat.js c cool
    c is cool
    guillaume@ubuntu:~/0x12$ ./4-concat.js c 
    c is undefined
    guillaume@ubuntu:~/0x12$ ./4-concat.js
    undefined is undefined
    guillaume@ubuntu:~/0x12$ 
    ```

- ***[5-to_integer.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/5-to_integer.js)***

    A script that prints My number: <first argument converted in integer>
    if the first argument can be converted to an integer. If the argument
    can’t be converted to an integer, it prints “Not a number”

    *Example*
    ```
    guillaume@ubuntu:~/0x12$ ./5-to_integer.js 
    Not a number
    guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89
    My number: 89
    guillaume@ubuntu:~/0x12$ ./5-to_integer.js "89"
    My number: 89
    guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89.89
    My number: 89
    guillaume@ubuntu:~/0x12$ ./5-to_integer.js School
    Not a number
    guillaume@ubuntu:~/0x12$ 
    ```

- ***[6-multi_languages_loop.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/6-multi_languages_loop.js)***

    A script that prints 3 lines using an array of string and a loop.

    *Example*
    ```
    guillaume@ubuntu:~/0x12$ ./6-multi_languages_loop.js 
    C is fun
    Python is cool
    JavaScript is amazing
    guillaume@ubuntu:~/0x12$ 
    ```

- ***[7-multi_c.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/7-multi_c.js)***

    A script that prints `x` times “C is fun”.

    *Example*
    ```
    guillaume@ubuntu:~/0x12$ ./7-multi_c.js 2
    C is fun
    C is fun
    guillaume@ubuntu:~/0x12$ ./7-multi_c.js 
    Missing number of occurrences
    guillaume@ubuntu:~/0x12$ 
    ```

- ***[8-square.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/8-square.js)***

    A script that prints a square.

    *Example*
    ```
    guillaume@ubuntu:~/0x12$ ./8-square.js 2
    XX
    XX
    guillaume@ubuntu:~/0x12$
    ```

- ***[9-add.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/9-add.js)***

    A script that prints the addition of 2 integers.

    *Example*
    ```
    guillaume@ubuntu:~/0x12$ ./9-add.js 13 89
    102
    guillaume@ubuntu:~/0x12$ 
    ```

- ***[10-factorial.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/10-factorial.js)***

    A script that computes and prints a factorial.

    *Example*
    ```
    guillaume@ubuntu:~/0x12$ ./10-factorial.js 
    1
    guillaume@ubuntu:~/0x12$ ./10-factorial.js 3
    6
    guillaume@ubuntu:~/0x12$ ./10-factorial.js 89
    1.6507955160908452e+136
    guillaume@ubuntu:~/0x12$ ./10-factorial.js 333
    Infinity
    guillaume@ubuntu:~/0x12$ 
    ```

- ***[11-second_biggest.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/11-second_biggest.js)***

    A script that searches the second biggest integer in the list of arguments.

    *Example*
    ```
    guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 4 2 5 3 0 -3
    4
    guillaume@ubuntu:~/0x12$ 
    ```

- ***[12-object.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/12-object.js)***

    A script that prints an object.

    *Example*
    ```
    guillaume@ubuntu:~/0x12$ ./12-object.js
    { type: 'object', value: 12 }
    { type: 'object', value: 89 }
    guillaume@ubuntu:~/0x12$ 
    ```

- ***[13-add.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/13-add.js)***

    A function that returns the addition of 2 integers.

- ***[100-let_me_const.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/100-let_me_const.js)***

    A script that modifies the value of myVar to 333

- ***[101-call_me_moby.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/101-call_me_moby.js)***

    A function that executes `x` times a function.

- ***[102-add_me_maybe.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/102-add_me_maybe.js)***

    A function that increments and calls a function.

- ***[103-object_fct.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x12-javascript-warm_up/103-object_fct.js)***

    A script that prints an object containing a method.
