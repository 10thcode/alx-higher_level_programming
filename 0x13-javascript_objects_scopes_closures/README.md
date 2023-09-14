
# 0x13. JavaScript - Objects, Scopes and Closures

JavaScript - Objects, scopes, closures and working with files.

## Tasks

- ***[0-rectangle.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/0-rectangle.js)***

    A script that creates an empty class Rectangle that defines a rectangle.

- ***[1-rectangle.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/1-rectangle.js)***

    A script that creates a class Rectangle that defines a rectangle.
    - The constructor takes 2 arguments `w` and `h`.

- ***[2-rectangle.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/2-rectangle.js)***

    A script that creates a class Rectangle that defines a rectangle.
    - The constructor must take 2 arguments `w` and `h`
    - If `w` or `h` is equal to 0 or not a positive integer, creates an empty object

- ***[3-rectangle.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/3-rectangle.js)***

    A script that creates a class Rectangle that defines a rectangle.
    - The constructor takes 2 arguments: `w` and `h`.
    - If `w` or `h` is equal to 0 or not a positive integer, create an empty object.
    - Creates an instance method called print() that prints the rectangle
    using the character X

- ***[4-rectangle.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/4-rectangle.js)***

    A script that creates a class Rectangle that defines a rectangle.
    - The constructor takes 2 arguments: `w` and `h`.
    - If `w` or `h` is equal to 0 or not a positive integer, create an empty object.
    - Creates an instance method called print() that prints the rectangle
    using the character X
    - Create an instance method called rotate() that exchanges
    the width and the height of the rectangle 
    - Create an instance method called double() that multiples
    the width and the height of the rectangle by 2

- ***[5-square.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/5-square.js)***

    A sctipt that creates a class Square that defines a square and inherits from Rectangle.
    - The constructor take 1 argument: size

- ***[6-square.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/6-square.js)***

    A script that creates a class Square that defines a square and inherits from Square.
    - Create an instance method called charPrint(c) that prints the
    rectangle using the character c

- ***[7-occurrences.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/7-occurrences.js)***

    A function that returns the number of occurrences in a list
    
    *Example*
    ```
    #!/usr/bin/node
    const nbOccurences = require('./7-occurrences').nbOccurences;

    console.log(nbOccurences([1, 2, 3, 4, 5, 6], 3));
    console.log(nbOccurences([3, 2, 3, 4, 5, 3, 3], 3));
    console.log(nbOccurences(["S", 12, "c", "S", "School", 8], "S"));
    ```

    *Output*
    ```
    1
    4
    2
    ```

- ***[8-esrever.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/8-esrever.js)***

    A function that returns the reversed version of a list.

    *Example*
    ```
    #!/usr/bin/node
    const esrever = require('./8-esrever').esrever;

    console.log(esrever([1, 2, 3, 4, 5]));
    console.log(esrever(["School", 89, { id: 12 }, "String"]));
    ```

    *Output*
    ```
    [ 5, 4, 3, 2, 1 ]
    [ 'String', { id: 12 }, 89, 'School' ]
    ```

- ***[9-logme.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/9-logme.js)***

    A function that prints the number of arguments already printed
    and the new argument value.

    *Example*
    ```
    #!/usr/bin/node
    const logMe = require('./9-logme').logMe;

    logMe("Hello");
    logMe("Best");
    logMe("School");
    ```

    *Output*
    ```
    0: Hello
    1: Best
    2: School
    ```

- ***[10-converter.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/10-converter.js)***

    A function that converts a number from base 10 to another base passed as argument

    *Example*
    ```
    #!/usr/bin/node
    const converter = require('./10-converter').converter;

    let myConverter = converter(10);

    console.log(myConverter(2));
    console.log(myConverter(12));
    console.log(myConverter(89));


    myConverter = converter(16);

    console.log(myConverter(2));
    console.log(myConverter(12));
    console.log(myConverter(89));
    ```

    *Output*
    ```
    2
    12
    89
    2
    c
    59
    ```

- ***[100-map.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/100-map.js)***

    A script that imports an array and computes a new array.

    *Example*
    ```
    #!/usr/bin/node
    exports.list = [1, 2, 3, 4, 5];
    ```

    *Output*
    ```
    [ 1, 2, 3, 4, 5 ]
    [ 0, 2, 6, 12, 20 ]
    ```

- ***[101-sorted.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/101-sorted.js)***

    A script that imports a dictionary of occurrences by user id and
    computes a dictionary of user ids by occurrence.

    *Example*
    ```
    #!/usr/bin/node
    exports.dict = {
      89: 1,
      90: 2,
      91: 1,
      92: 3,
      93: 1,
      94: 2
    };
    ```

    *Output*
    ```
    { '1': [ '89', '91', '93' ], '2': [ '90', '94' ], '3': [ '92' ] }
    ```

- ***[102-concat.js](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/102-concat.js)***

    A script that concats 2 files.

    *Example*
    ```
    guillaume@ubuntu:~/0x13$ cat fileA
    C is fun!
    guillaume@ubuntu:~/0x13$ cat fileB
    Python is Cool!!!
    guillaume@ubuntu:~/0x13$ ./102-concat.js fileA fileB fileC
    guillaume@ubuntu:~/0x13$ cat fileC
    C is fun!
    Python is Cool!!!
    guillaume@ubuntu:~/0x13$ 
    ```
