CREATE TABLE IF NOT EXISTS Forums (
  forum_id        INTEGER NOT NULL  ,
  name            TEXT    ,
  creator         TEXT    ,
  PRIMARY KEY (forum_id)  ,
  FOREIGN KEY (creator) REFERENCES Users(username)
);

CREATE TABLE IF NOT EXISTS Threads (
  forum_id        INTEGER ,
  thread_id       INTEGER ,
  title           TEXT    ,
  thread_text     TEXT    ,
  creator         TEXT    ,
  thread_time     TEXT    ,
  PRIMARY KEY (thread_id) ,
  FOREIGN KEY (creator) REFERENCES Users(username)  ,
  FOREIGN KEY (forum_id) REFERENCES Forums(forum_id)
);

CREATE TABLE IF NOT EXISTS Posts (
  forum_id        INTEGER ,
  thread_id       INTEGER ,
  post_num        INTEGER ,
  author          TEXT    ,
  text_post       TEXT    ,
  post_time       TEXT    ,
  PRIMARY KEY (post_num)  ,
  FOREIGN KEY (author) REFERENCES Users(username)     ,
  FOREIGN KEY (forum_id) REFERENCES Forums(forum_id)  ,
  FOREIGN KEY (thread_id) REFERENCES Threads(thread_id)
);

CREATE TABLE IF NOT EXISTS Users (
  username        TEXT    ,
  password        TEXT    ,
  PRIMARY KEY (username)
);

CREATE UNIQUE INDEX Forums_List ON Forums (name);
CREATE INDEX Threads_List ON Threads (title);
CREATE INDEX Posts_List ON Posts (text_post);
CREATE UNIQUE INDEX Usernames ON Users (username);

INSERT INTO Users (username, password)
VALUES
  ('Alexander Truong', '12345'),
  ('Brian Truong', '23456'),
  ('Vivian Tran', '34567'),
  ('MrQuestions', '123'),
  ('DunceyMcDunce', '123'),
  ('FranticPerson', '123'),
  ('MrCSSPro', '123'),
  ('ImTheSmartest', '123'),
  ('MissAwesome', '123'),
  ('PHPHater', '123'),
  ('MrAnswers', '123'),
  ('AnotherDuncey', '123'),
  ('NonfranticLady', '123'),
  ('NonProCSSGuy', '123'),
  ('NotTheSmartest', '123');

INSERT INTO Forums (forum_id, name, creator)
VALUES
  (1, 'HTML', 'Alexander Truong'),
  (2, 'CSS', 'Brian Truong'),
  (3, 'PHP', 'Vivian Tran');

INSERT INTO Threads (forum_id, thread_id, title, thread_text, creator, thread_time)
VALUES
  (1, 1, 'How does one make an HTML file?', 'Do we just use a text file or what?','MrQuestions', '9-15-2018 at 10:32:08'),
  (1, 2, 'What IDE do you use?', 'Just curious on what everyone uses', 'DunceyMcDunce', '9-15-2018 at 11:00:09'),
  (1, 3, 'someone please help', 'i dont know how to make a link', 'FranticPerson', '9-15-2018 at 11:07:27'),
  (2, 4, 'What does CSS stand for?', 'Learning HTML and wanted to know what CSS stood for', 'MrCSSPro', '9-14-2018 at 09:58:46'),
  (2, 5, 'why use a .css file?', 'can''t you just style in your HTML file?', 'ImTheSmartest', '9-14-2018 at 15:17:19'),
  (3, 6, 'Is PHP better than SQL?', 'Never learned SQL and thinking about switching, but would like more info', 'MissAwesome', '9-16-2018 at 19:31:51'),
  (3, 7, 'php sux', 'PHPHater', 'it is so terrible', '9-17-2018 at 01:05:08');

INSERT INTO Posts (forum_id, thread_id, post_num, author, text_post, post_time)
VALUES
  (1, 1, 1, 'MrAnswers', 'For linux, just run the command ''touch filename.html''', '9-15-2018 at 10:33:10'),
  (1, 1, 2, 'MrQuestions', 'k thnx', '9-15-2018 at 15:13:29'),
  (1, 2, 3, 'AnotherDuncey', 'just use a text editor lol', '9-15-2018 at 13:29:20'),
  (1, 2, 4, 'DunceyMcDunce', 'like notepad++?', '9-15-2018 at 14:20:40'),
  (1, 2, 5, 'AnotherDuncey', 'yes', '9-15-2018 at 15:01:58'),
  (1, 3, 6, 'NonfranticLady', 'Did you check the HTML documentation?', '9-15-2018 at 11:08:13'),
  (1, 3, 7, 'FranticPerson', 'nevermind i ifugred it out lol', '9-15-2018 at 13:29:20'),
  (2, 1, 8, 'NonProCSSGuy', 'Cascading Style Sheets. Are you sure you''re a pro?', '9-14-2018 at 10:03:45'),
  (2, 1, 9, 'MrCSSPro', '... maybe', '9-15-2018 at 20:18:19'),
  (2, 2, 10, 'NotTheSmartest', 'It provides an easier way to style your HTML than in HTML itself', '9-14-2018 at 16:06:14'),
  (2, 2, 11, 'ImTheSmartest', 'I see. Thanks!', '9-14-2018 at 16:12:28'),
  (3, 1, 12, 'PHPHater', 'of course sql is so much better', '9-16-2018 at 21:13:24'),
  (3, 1, 13, 'MissAwesome', 'I think your name shows you''re biased', '9-16-2018 at 02:51:01'),
  (3, 2, 14, 'DunceyMcDunce', 'that''s not very constructive', '9-17-2018 at 07:30:17'),
  (3, 2, 15, 'PHPHater', 'neither are you LUL', '9-17-2018 at 08:03:41');
