CREATE TABLE Languages(
id INTEGER PRIMARY KEY,
language VARCHAR(40),
answer VARCHAR(40),
answered INTEGER,
guide TEXT);

INSERT INTO Languages
VALUES(1,"Python","google",0,"A folder named Python was created. Go there and fight with program.py!");

INSERT INTO Languages
Values(2,"Go","200 OK",0,"A folder named Go was created. Go there and try to make Google Go run.");

INSERT INTO Languages
Values(3,"Java","object oriented programming",0,"A folder named Java was created. Can you handle the class?");

INSERT INTO Languages
VALUES(4,"Haskell","Lambda",0,"Something pure has landed. Go to Haskell folder and see it!");

ALTER TABLE Languages
ADD COLUMN rating INTEGER;

UPDATE Languages
SET rating = 5
WHERE language = '%%';

UPDATE Languages
SET answered = 1
WHERE language == "Python" OR language == "Go";

SELECT language
FROM Languages
WHERE answer=="200 OK" OR answer == "Lambda";
