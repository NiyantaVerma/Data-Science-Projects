// Loading movie names alongwith its properties
LOAD CSV WITH HEADERS FROM "http://localhost:11001/project-6fcd6f1e-8396-4c0d-b95d-eb2fee67d23c/movie.csv" AS row

// Tries to find a movie node with exactly all of these properties. If it doesn't exist, it //creates one
MERGE (m:movie{name : row.name, release_period : row.release_period, remake: row.remake, franchise: row.franchise, genre:row.genre, screens: toInteger(row.screens), revenue: toInteger(row.revenue), budget:toInteger(row.budget)});

// This is a schema constraint.It enforces that each movie node must have a unique name — no duplicates allowed.
CREATE CONSTRAINT movie_name FOR (m:movie) REQUIRE m.name IS UNIQUE;

////////////////////////

// Loading actor dataset creating relationships with the movies that they acted in
LOAD CSV WITH HEADERS FROM "http://localhost:11001/project-6fcd6f1e-8396-4c0d-b95d-eb2fee67d23c/actor_movie.csv" AS row
MERGE (a:actor {name:row.actor}) MERGE (m:movie {name:row.movie}) MERGE (a)-[r:ACTED_IN{new_actor:row.new_actor}]->(m);

// Loading director dataset creating relationships with the movies that they directed
LOAD CSV WITH HEADERS FROM "http://localhost:11001/project-6fcd6f1e-8396-4c0d-b95d-eb2fee67d23c/director_movie.csv" AS row
MERGE (d:director {name:row.director}) MERGE (m:movie {name:row.movie}) MERGE (d)-[r:DIRECTED{new_director:row.new_director}]->(m);

CREATE CONSTRAINT actor_name FOR (a:actor) REQUIRE a.name IS UNIQUE;
CREATE CONSTRAINT director_name FOR (d:director) REQUIRE d.name IS UNIQUE;

////////////////////////

MATCH (n:actor) RETURN n LIMIT 25

////////////////////////

MATCH (n:director) RETURN n LIMIT 25

////////////////////////

MATCH (n:movie) RETURN n LIMIT 25

///////////////////////

MATCH(n) RETURN (n)

//////////////////////

MATCH (n) RETURN n LIMIT 25

//////////////////////

MATCH (n:director) RETURN n LIMIT 25

/////////////////////

// Looking at the overall schema of the database
CALL db.schema.visualization()

////////////////////

// Genre Distribution
MATCH (m:movie)
WITH COUNT(m.name) AS total

MATCH (m:movie)
WITH m.genre AS genre_name, COUNT(DISTINCT(m.name)) AS genre_count, total

RETURN genre_name, genre_count, 100*genre_count/total AS genre_percentage
ORDER BY genre_count DESC

///////////////////

// Total revenue of Akshay Kumar movies
MATCH(a:actor{name:"Akshay Kumar"})-->(m:movie)
RETURN SUM(m.revenue);

///////////////////

MATCH(a:actor)-->(m:movie)
RETURN a.name, m.name, m.revenue, m.budget, 
m.revenue/m.budget AS rb_ratio
ORDER BY m.revenue DESC LIMIT 10;

///////////////////

// List of the biggest box-office bombs
MATCH (m:movie)
RETURN m.name, m.revenue, m.budget, m.revenue-m.budget AS profit
ORDER BY profit DESC LIMIT 10

/////////////////////

// Actor with most thriller and horror movies
MATCH (a:actor)-->(m:movie{genre:"thriller"})
RETURN a.name,COUNT(DISTINCT(m.name)) AS genre_count
ORDER BY genre_count DESC LIMIT 10

///////////////////

// how often some actor-director duo worked together
MATCH (a:actor)-->(m:movie)<--(d:director)
RETURN a.name AS actor, d.name AS director,
COUNT(DISTINCT(m.name)) AS num_collab
ORDER BY num_collab DESC LIMIT 10