DROP TABLE IF EXISTS Posts;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Threads;
DROP TABLE IF EXISTS Forums;

CREATE TABLE  Forums (
  forum_id        INTEGER NOT NULL,
  forum_title     TEXT,
  creator         TEXT,
  PRIMARY KEY (forum_id),
  FOREIGN KEY (creator) REFERENCES Users(username)
);

CREATE TABLE  Threads (
  forum_id        INTEGER,
  thread_id       INTEGER,
  thread_title    TEXT,
  thread_text     TEXT,
  creator         TEXT,
  thread_time     TEXT,
  PRIMARY KEY (thread_id),
  FOREIGN KEY (creator) REFERENCES Users(username),
  FOREIGN KEY (forum_id) REFERENCES Forums(forum_id)
);

CREATE TABLE  Posts (
  forum_id        INTEGER,
  thread_id       INTEGER,
  post_id        INTEGER,
  author          TEXT,
  post_text       TEXT,
  post_time       TEXT,
  PRIMARY KEY (post_id)  ,
  FOREIGN KEY (author) REFERENCES Users(username)     ,
  FOREIGN KEY (forum_id) REFERENCES Forums(forum_id)  ,
  FOREIGN KEY (thread_id) REFERENCES Threads(thread_id)
);

CREATE TABLE  Users (
  username        TEXT,
  password        TEXT,
  PRIMARY KEY (username)
);

CREATE UNIQUE INDEX Forums_List ON Forums (forum_title);
CREATE INDEX Threads_List ON Threads (thread_title);
CREATE INDEX Posts_List ON Posts (post_text);
CREATE UNIQUE INDEX Usernames ON Users (username);

INSERT INTO Users (username, password)
VALUES
("marek.sautter", "godIHopeIdoWellOnThisAssignment"),
("ray.comfort", "rayLovesJesus123"),
("martin.luther", "martinLovesJesus123"),
("billy.graham", "billyLovesJesus123"),
("kirk.cameron", "kirkLovesJesus123"),
("rick.warren", "rickLovesJesus123"),
("joseph.smith", "joeyLovesJesus123"),
("marry.eddy", "marryLovesJesus123"),
("mary.magdalene", "JesusLovesMags123"),
("franklin.graham", "frankieLovesJesus123"),
("td.jakes", "jakeyLovesJesus123"),
("nick.vujicic", "theNicksterLovesJesus123"),
("joel.olsteen", "jojoLovesJesus123"),
("jesus.christ", "iLoveMyself123");

INSERT INTO Forums (forum_id, forum_title, creator)
VALUES
  (1, 'Python', 'marek.sautter'),
  (2, 'Java', 'jesus.christ'),
  (3, 'C++', 'ray.comfort');

INSERT INTO Threads (forum_id, thread_id, thread_title, thread_text, creator, thread_time)
VALUES
  (1, 1, 'Python is the future of programming!', 'I love Python so much I just wanted to make my own thread about it!','martin.luther', '2018-09-13 10:31:10.682060'),
  (1, 2, 'How do you avoid creating spaghetti-code?', 'Everytime I start something in Python it just ends up being a huge mess. What are the best practices for OOP principles in Python?', 'billy.graham', '2018-09-13 11:31:10.682060'),
  (2, 3, 'Is Java Dying?', 'My friend made fun of me for coding in Java the other day. He said I was coding in a dead language, is that true?', 'kirk.cameron', '2018-09-13 12:31:10.682060'),
  (2, 4, 'Tips For Java?', 'I just wanna learn some tips for Java', 'rick.warren', '2018-09-13 13:31:10.682060'),
  (3, 5, 'Why do schools still teach C++ first', 'C++ isnt the most difficult language but it certainly isnt the easiest. Why do most colleges teach such a difficult language to begin with?', 'joseph.smith', '2018-09-13 14:31:10.682060'),
  (3, 6, 'Game Development with C++?', 'Do people still use C++ for gamedev?','marry.eddy', '2018-09-13 15:31:10.682060');

INSERT INTO Posts (forum_id, thread_id, post_id, author, post_text, post_time)
VALUES
  (1, 1, 1, 'mary.magdalene', 'Python Smython, Its all about x86 Assembly!', '2018-09-23 01:32:17.075185'),
  (1, 1, 2, 'mary.magdalene', 'Python Smython, Its all about x86 Assembly!', '2018-09-23 01:32:17.075185'),
  (1, 1, 3, 'marek.sautter', 'Ha! Good luck with that', '2018-09-24 02:32:17.075185'),
  (1, 2, 4, 'franklin.graham', 'Stop eating spaghetti while coding!', '2018-09-23 03:32:17.075185'),
  (1, 2, 5, 'marek.sautter', 'Watch my python tutorials!', '2018-09-24 04:32:17.075185'),
  (2, 3, 6, 'td.jakes', 'Yup, it is dead', '2018-09-23 05:32:17.075185'),
  (2, 3, 7, 'marek.sautter', 'No it isnt!', '2018-09-24 06:32:17.075185'),
  (2, 4, 8, 'nick.vujicic', '1. Stop 2. Drop 3. Roll', '2018-09-23 07:32:17.075185'),
  (2, 4, 9, 'rick.warren', 'Wow! Thank you', '2018-09-24 08:32:17.075185'),
  (3, 5, 10, 'joel.olsteen', 'We make them learn the hard stuff first so they drop out!', '2018-09-23 09:32:17.075185'),
  (3, 5, 11, 'marek.sautter', 'As bad as it is, this is true', '2018-09-24 10:32:17.075185'),
  (3, 6, 12, 'martin.luther', 'I made minecraft on C++', '2018-09-23 11:32:17.075185'),
  (3, 6, 13, 'marek.sautter', 'I did not know MLK made minecraft?', '2018-09-24 12:32:17.075185');
