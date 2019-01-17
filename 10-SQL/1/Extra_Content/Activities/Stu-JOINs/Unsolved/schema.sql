DROP DATABASE IF EXISTS programming_db;
CREATE DATABASE programming_db;

USE programming_db;

CREATE TABLE programming_languages(
  id INTEGER(11) AUTO_INCREMENT NOT NULL,
  language VARCHAR(20),
  rating INTEGER(11),
  mastered BOOLEAN DEFAULT false,
  PRIMARY KEY (id)
);

CREATE TABLE programming_libraries (
	id INTEGER(11) AUTO_INCREMENT NOT NULL,
  name VARCHAR(20),
  languageID INTEGER(11),
  PRIMARY KEY (id)
);

INSERT INTO programming_languages (language, rating)
VALUES ("Python", 100);

INSERT INTO programming_languages (language)
VALUES ("JavaScript");

INSERT INTO programming_languages (language, rating)
VALUES ("Java", 0);

INSERT INTO programming_libraries (name, languageID)
VALUES ("Matplotlib", 1), ("Pandas", 1), ("D3.js", 2), ("Leaflet", 2);

INSERT INTO programming_libraries (name)
VALUES ("libavcodec");

SELECT * FROM programming_libraries;
SELECT * FROM programming_languages;

-- write an INNER JOIN query on programming_languages & programming_libraries


-- write a LEFT JOIN query on programming_languages & programming_libraries


-- write a RIGHT JOIN query on programming_languages & programming_libraries
