
# 0x0F. Python - Object-relational mapping

Python - Object Relational Mapping (ORM).

## Tasks

- ***[0-select_states.py](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/0-select_states.py)***

    A script that lists all `states` from the database `hbtn_0e_0_usa` using `MySQLdb`.
    - The script takes 3 arguments: `mysql username`, `mysql password` and `database name`

- ***[1-filter_states.py](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/1-filter_states.py)***

    A script that lists all `states` with a name starting with `N` from the
    database `hbtn_0e_0_usa` using `MySQLdb`.
    - The script takes 3 arguments: `mysql username`, `mysql password` and `database name`

- ***[2-my_filter_states.py](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/2-my_filter_states.py)***

    A script that takes in an argument and displays all values in the `states`
    table of `hbtn_0e_0_usa` where `name` matches the argument using `MySQLdb`.
    - The script takes 4 arguments: `mysql username`, `mysql password`,
    `database name` and `state name searched`.

- ***[3-my_safe_filter_states.py](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/3-my_safe_filter_states.py)***

    A script that takes in arguments and displays all values in the `states`
    table of `hbtn_0e_0_usa` where `name` matches the argument. This script is safe
    from MySQL injections!
    - The script takes 4 arguments: `mysql username`, `mysql password`, `database
    name` and `state name searched`

- ***[4-cities_by_state.py](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/4-cities_by_state.py)***

    A script that lists all `cities` from the `database hbtn_0e_4_usa` using MySQLdb.
    - The script takes 3 arguments: `mysql username`, `mysql password` and `database name`

- ***[5-filter_cities.py](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/5-filter_cities.py)***

    A script that takes in the name of a state as an argument and lists
    all `cities` of that state, using the `database hbtn_0e_4_usa`.
    - The script takes 4 arguments: `mysql username`, `mysql password`,
    `database name` and `state name`.

- ***[model_state.py](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/model_state.py)***

    A python file that contains the class definition of a State
    (a class that map to `state` table in a database).

- ***[7-model_state_fetch_all.py](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/7-model_state_fetch_all.py)***

    A script that lists all `State` objects from the database `hbtn_0e_6_usa`
    using `SQLAlchemy`.
    - The script takes 3 arguments: `mysql username`, `mysql password` and `database name`

- ***[8-model_state_fetch_first.py](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/8-model_state_fetch_first.py)***

    A script that prints the first `State` object from the `database hbtn_0e_6_usa`
    using `SQLAlchemy`.
    - The script takes 3 arguments: `mysql username`, `mysql password` and `database name`

    *Example*
    ```
    guillaume@ubuntu:~/0x0F$ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
    1: California
    guillaume@ubuntu:~/0x0F$ 
    ```

- ***[9-model_state_filter_a.py](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/9-model_state_filter_a.py)***

    A script that lists all State objects that contain the letter `a`
    from the database `hbtn_0e_6_usa` using `SQLAlchemy`.
    - The script takes 3 arguments: `mysql username`, `mysql password` and `database name`

    *Example*
    ```
    guillaume@ubuntu:~/0x0F$ ./9-model_state_filter_a.py root root hbtn_0e_6_usa
    1: California
    2: Arizona
    3: Texas
    5: Nevada
    guillaume@ubuntu:~/0x0F$ 
    ```

- ***[10-model_state_my_get.py](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/10-model_state_my_get.py)***

    A script that prints the `State` object with the `name` passed as argument
    from the database `hbtn_0e_6_usa` using `SQLAlchemy`
    - The script takes 4 arguments: `mysql username`, `mysql password`,
    `database name` and `state name to search`

    *Example*
    ```
    guillaume@ubuntu:~/0x0F$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
    3
    guillaume@ubuntu:~/0x0F$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Illinois
    Not found
    guillaume@ubuntu:~/0x0F$ 
    ```

- ***[11-model_state_insert.py](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/11-model_state_insert.py)***

    A script that adds the `State` object “Louisiana” to the `database hbtn_0e_6_usa`
    using `SQLAlchemy`.
    - The script takes 3 arguments: `mysql username`, `mysql password` and `database name`

    *Example*
    ```
    guillaume@ubuntu:~/0x0F$ ./11-model_state_insert.py root root hbtn_0e_6_usa 
    6
    ```

- ***[12-model_state_update_id_2.py](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/12-model_state_update_id_2.py)***

    A script that changes the name of a `State` object from the `database hbtn_0e_6_usa`
    using `SQLAlchemy`.
    - This script takes 3 arguments: `mysql username`, `mysql password` and
    `database name`

- ***[13-model_state_delete_a.py](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/13-model_state_delete_a.py)***

    A script that deletes all `State` objects with a name containing the letter
    `a` from the database `hbtn_0e_6_usa` usign `SQLAlchemy`.
    - The script takes 3 arguments: `mysql username`, `mysql password` and `database name`

- ***[model_city.py](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/model_city.py)***

    A Python file that contains the class definition of a `City`
    (a class that map to `city` table in a database).

- ***[14-model_city_fetch_by_state.py](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/14-model_city_fetch_by_state.py)***

    A script that prints all `City` objects from the database `hbtn_0e_14_usa`
    using `SQLAlchemy`.
    - The script takes 3 arguments: `mysql username`, `mysql password` and `database name`

- ***[relationship_city.py](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/relationship_city.py)***

    A Python file that contains the class definition of a `City`
    (a class that map to `city` table in a database) and extablishes a
    relationship to `State` class

- ***[relationship_state.py](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/relationship_state.py)***

    A Python file that contains the class definition of a `State`
    (a class that map to `state` table in a database) and extablishes a
    relationship to `City` class.

- ***[100-relationship_states_cities.py](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/100-relationship_states_cities.py)***

    A script that creates the `State` “California” with the `City` “San Francisco”
    from the database `hbtn_0e_100_usa`.
    - The script takes 3 arguments: `mysql username`, `mysql password` and `database name`

- ***[101-relationship_states_cities_list.py](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/101-relationship_states_cities_list.py)***

    A script that lists all `State` objects, and corresponding `City` objects,
    contained in the database `hbtn_0e_101_usa` using `SQLAlchemy`.
    - The script takes 3 arguments: mysql username, mysql password and database name

- ***[102-relationship_cities_states_list.py](https://github.com/10thcode/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/102-relationship_cities_states_list.py)***

    A script that lists all `City` objects from the database `hbtn_0e_101_usa`.
    - The script takes 3 arguments: `mysql username`, `mysql password` and `database name`
