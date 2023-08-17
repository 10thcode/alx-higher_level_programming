-- lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.name, states.name
FROM states AS states
INNER JOIN cities AS cities
ON states.id = cities.state_id;
