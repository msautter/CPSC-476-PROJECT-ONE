ATTACH DATABASE 'tables.db' AS 'tables';
ATTACH DATABASE 'post_0.db' AS 'posts1';
ATTACH DATABASE 'post_1.db' AS 'posts2';
ATTACH DATABASE 'post_2.db' AS 'posts3';

CREATE TABLE IF NOT EXISTS tables.Forums (
  forum_id        INTEGER NOT NULL,
  forum_title     TEXT,
  creator         TEXT,
  PRIMARY KEY (forum_id),
  FOREIGN KEY (creator) REFERENCES Users(username)
);

CREATE TABLE IF NOT EXISTS tables.Threads (
  forum_id        INTEGER,
  thread_id       INTEGER NOT NULL,
  thread_key      TEXT,
  thread_title    TEXT,
  thread_text     TEXT,
  creator         TEXT,
  thread_time     TEXT,
  PRIMARY KEY (thread_key, thread_id),
  FOREIGN KEY (creator) REFERENCES Users(username)  ,
  FOREIGN KEY (forum_id) REFERENCES Forums(forum_id)
);

CREATE TABLE IF NOT EXISTS tables.Users (
  username        TEXT,
  password        TEXT,
  PRIMARY KEY (username)
);

CREATE TABLE IF NOT EXISTS posts1.Posts (
  post_key        TEXT,
  author          TEXT,
  post_text       TEXT,
  post_time       TEXT    
);

CREATE TABLE IF NOT EXISTS posts2.Posts (
  post_key        TEXT,
  author          TEXT,
  post_text       TEXT,
  post_time       TEXT    
);

CREATE TABLE IF NOT EXISTS posts3.Posts (
  post_key        TEXT,
  author          TEXT,
  post_text       TEXT,
  post_time       TEXT    
);

INSERT INTO tables.Users (username, password)
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

INSERT INTO tables.Forums (forum_id, forum_title, creator)
VALUES
  (1, 'Python', 'marek.sautter'),
  (2, 'Java', 'jesus.christ'),
  (3, 'C++', 'ray.comfort');

INSERT INTO tables.Threads (forum_id, thread_id, thread_key, thread_title, thread_text, creator, thread_time)
VALUES
  (1, 1, '577043eb-2883-4dc1-9731-a7d71755e1c4', 'Python is the future of programming!', 'I love Python so much I just wanted to make my own thread about it!','martin.luther', '2018-09-13 10:31:10.682060'),
  (1, 2, '8bebbeed-1d2c-4a0d-a1d7-3a8618c87418', 'How do you avoid creating spaghetti-code?', 'Everytime I start something in Python it just ends up being a huge mess. What are the best practices for OOP principles in Python?', 'billy.graham', '2018-09-13 11:31:10.682060'),
  (2, 3, '1e8039c3-057e-4470-af25-24fa47bdfd10', 'Is Java Dying?', 'My friend made fun of me for coding in Java the other day. He said I was coding in a dead language, is that true?', 'kirk.cameron', '2018-09-13 12:31:10.682060'),
  (2, 4, '9bfadfda-89f8-4851-9960-b5f7f58131c3', 'Tips For Java?', 'I just wanna learn some tips for Java', 'rick.warren', '2018-09-13 13:31:10.682060'),
  (3, 5, '7d26c609-667c-42fc-8926-83c97b50a6a9', 'Why do schools still teach C++ first', 'C++ isnt the most difficult language but it certainly isnt the easiest. Why do most colleges teach such a difficult language to begin with?', 'joseph.smith', '2018-09-13 14:31:10.682060'),
  (3, 6, '43b127fe-36e2-473e-b1cc-57fa85391438', 'Game Development with C++?', 'Do people still use C++ for gamedev?','marry.eddy', '2018-09-13 15:31:10.682060');

INSERT INTO posts1.Posts (post_key, author, post_text, post_time)
VALUES
  ('1e8039c3-057e-4470-af25-24fa47bdfd10', 'td.jakes', 'Yup, it is dead', '2018-09-23 05:32:17.075185'),
  ('1e8039c3-057e-4470-af25-24fa47bdfd10', 'marek.sautter', 'No it isnt!', '2018-09-24 06:32:17.075185'),
  ('43b127fe-36e2-473e-b1cc-57fa85391438', 'martin.luther', 'I made minecraft on C++', '2018-09-23 11:32:17.075185'),
  ('43b127fe-36e2-473e-b1cc-57fa85391438', 'marek.sautter', 'I did not know MLK made minecraft?', '2018-09-24 12:32:17.075185');

INSERT INTO posts2.Posts (post_key, author, post_text, post_time)
VALUES
  ('577043eb-2883-4dc1-9731-a7d71755e1c4', 'mary.magdalene', 'Python Smython, Its all about x86 Assembly!', '2018-09-23 01:32:17.075185'),
  ('577043eb-2883-4dc1-9731-a7d71755e1c4', 'mary.magdalene', 'Im gonna make the next Facebook all on Assembly!', '2018-09-23 01:33:17.075185'),
  ('577043eb-2883-4dc1-9731-a7d71755e1c4', 'marek.sautter', 'Ha! Good luck with that', '2018-09-24 02:32:17.075185'),
  ('9bfadfda-89f8-4851-9960-b5f7f58131c3', 'nick.vujicic', '1. Stop 2. Drop 3. Roll', '2018-09-23 07:32:17.075185'),
  ('9bfadfda-89f8-4851-9960-b5f7f58131c3', 'rick.warren', 'Wow! Thank you', '2018-09-24 08:32:17.075185');

INSERT INTO posts3.Posts (post_key, author, post_text, post_time)
VALUES
  ('8bebbeed-1d2c-4a0d-a1d7-3a8618c87418', 'franklin.graham', 'Stop eating spaghetti while coding!', '2018-09-23 03:32:17.075185'), 
  ('8bebbeed-1d2c-4a0d-a1d7-3a8618c87418', 'marek.sautter', 'Watch my python tutorials!', '2018-09-24 04:32:17.075185'),
  ('7d26c609-667c-42fc-8926-83c97b50a6a9', 'joel.olsteen', 'We make them learn the hard stuff first so they drop out!', '2018-09-23 09:32:17.075185'),
  ('7d26c609-667c-42fc-8926-83c97b50a6a9', 'marek.sautter', 'As bad as it is, this is true', '2018-09-24 10:32:17.075185');
