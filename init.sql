CREATE TABLE IF NOT EXISTS Forums (
  forum_id        INTEGER NOT NULL,
  forum_title     TEXT,
  creator         TEXT,
  PRIMARY KEY (forum_id),
  FOREIGN KEY (creator) REFERENCES Users(username)
);

CREATE TABLE IF NOT EXISTS Threads (
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

CREATE TABLE IF NOT EXISTS Posts (
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

CREATE TABLE IF NOT EXISTS Users (
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
  (1, 1, 'Python is the future of programming!', 'I love Python so much I just wanted to make my own thread about it!','martin.luther', '9-14-2018 at 11:37:45'),
  (1, 2, 'How do you avoid creating spaghetti-code?', 'Everytime I start something in Python it just ends up being a huge mess. What are the best practices for OOP principles in Python?', 'billy.graham', '9-14-2018 at 11:49:10'),
  (2, 3, 'Is Java Dying?', 'My friend made fun of me for coding in Java the other day. He said I was coding in a dead language, is that true?', 'kirk.cameron', '9-14-2018 at 06:34:29'),
  (2, 4, 'Tips For Java?', 'I just wanna learn some tips for Java', 'rick.warren', '9-12-2018 at 05:13:12'),
  (3, 5, 'Why do schools still teach C++ first', 'C++ isnt the most difficult language but it certainly isnt the easiest. Why do most colleges teach such a difficult language to begin with?', 'joseph.smith', '9-11-2018 at 11:11:11'),
  (3, 6, 'Game Development with C++?', 'Do people still use C++ for gamedev?','marry.eddy', '9-10-2018 at 03:54:09');

INSERT INTO Posts (forum_id, thread_id, post_id, author, post_text, post_time)
VALUES
  (1, 1, 1, 'mary.magdalene', 'Python Smython, Its all about x86 Assembly!', '9-20-2018 at 11:23:54'),
  (1, 1, 2, 'marek.sautter', 'Ha! Good luck with that', '9-20-2018 at 19:23:05'),
  (1, 2, 3, 'franklin.graham', 'Stop eating spaghetti while coding!', '9-20-2018 at 06:45:24'),
  (1, 2, 4, 'marek.sautter', 'Watch my python tutorials!', '9-20-2018 at 17:45:22'),
  (2, 3, 5, 'td.jakes', 'Yup, it is dead', '9-19-2018 at 01:06:15'),
  (2, 3, 6, 'marek.sautter', 'No it isnt!', '9-19-2018 at 03:05:45'),
  (2, 4, 7, 'nick.vujicic', '1. Stop 2. Drop 3. Roll', '9-20-2018 at 13:27:19'),
  (2, 4, 8, 'rick.warren', 'Wow! Thank you', '9-20-2018 at 19:04:34'),
  (3, 5, 9, 'joel.olsteen', 'We make them learn the hard stuff first so they drop out!', '9-14-2018 at 19:28:01'),
  (3, 5, 10, 'marek.sautter', 'As bad as it is, this is true', '9-14-2018 at 22:22:22'),
  (3, 6, 11, 'martin.luther', 'I made minecraft on C++', '9-12-2018 at 03:30:29'),
  (3, 6, 12, 'marek.sautter', 'I did not know MLK made minecraft?', '9-12-2018 at 23:23:23');
