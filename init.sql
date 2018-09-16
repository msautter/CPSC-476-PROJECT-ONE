CREATE TABLE forums (
	forum_id	INTEGER ,
	forum_name	TEXT NOT NULL,
	forum_creator	TEXT ,
	forum_time	TEXT ,
	FOREIGN KEY (forum_creator) REFERENCES users(users_name)
	
);

CREATE TABLE threads (
	forum_id	INTEGER ,
	thread_id INTEGER ,
	thread_title	TEXT ,
	thread_creator	TEXT ,
	thread_time	TEXT ,
	FOREIGN KEY (forum_id) REFERENCES forums(forum_id),
	FOREIGN KEY (thread_creator) REFERENCES users(users_name)
	
);

CREATE TABLE posts (
	forum_id	INTEGER ,
	thread_id INTEGER ,
	post_text	TEXT,
	post_creator	TEXT ,
	post_time TEXT ,
	FOREIGN KEY (forum_id) REFERENCES forums(forum_id),
	FOREIGN KEY (thread_id) REFERENCES threads(thread_id),
	FOREIGN KEY (post_creator) REFERENCES users(users_name)
	
);

CREATE TABLE users (
	users_name	TEXT ,
	users_pw	TEXT ,
	PRIMARY KEY (users_name)
);

INSERT INTO users (users_name, users_pw)
VALUES ("marek.sautter", "scienceTrumpsReligionEverySecond");
INSERT INTO users (users_name, users_pw)
VALUES ("ray.comfort", "rayLovesJesus123");
INSERT INTO users (users_name, users_pw)
VALUES ("martin.luther", "martinLovesJesus123");
INSERT INTO users (users_name, users_pw)
VALUES ("billy.graham", "billyLovesJesus123");
INSERT INTO users (users_name, users_pw)
VALUES ("kirk.cameron", "kirkLovesJesus123");
INSERT INTO users (users_name, users_pw)
VALUES ("rick.warren", "rickLovesJesus123");
INSERT INTO users (users_name, users_pw)
VALUES ("joseph.smith", "joeyLovesJesus123");
INSERT INTO users (users_name, users_pw)
VALUES ("marry.eddy", "marryLovesJesus123");
INSERT INTO users (users_name, users_pw)
VALUES ("mary.magdalene", "JesusLovesMags123");
INSERT INTO users (users_name, users_pw)
VALUES ("franklin.graham", "frankieLovesJesus123");
INSERT INTO users (users_name, users_pw)
VALUES ("td.jakes", "jakeyLovesJesus123");
INSERT INTO users (users_name, users_pw)
VALUES ("nick.vujicic", "theNicksterLovesJesus123");
INSERT INTO users (users_name, users_pw)
VALUES ("joel.olsteen", "jojoLovesJesus123");
INSERT INTO users (users_name, users_pw)
VALUES ("jesus.christ", "iLoveMyself123");



INSERT INTO forums (forum_id, forum_name, forum_creator, forum_time)
VALUES (1, "Python", "marek.sautter", "2018-09-14 14:53:25.700766");
INSERT INTO forums (forum_id, forum_name, forum_creator, forum_time)
VALUES (2, "Java", "jesus.christ", "2018-09-14 14:57:22.716169");
INSERT INTO forums (forum_id, forum_name, forum_creator, forum_time)
VALUES (3, "C++", "ray.comfort", "2018-09-14 14:58:28.605170");

INSERT INTO threads (forum_id, thread_id, thread_title, thread_creator, thread_time)
VALUES (1,1, "Python is the future of programming!","martin.luther", "2018-09-14 15:00:47.128324");
INSERT INTO posts (forum_id, thread_id, post_text, post_creator, post_time)
VALUES (1,1, "I love Python so much I just wanted to make my own thread about it!", "martin.luther", "2018-09-14 15:00:47.128324");
INSERT INTO posts (forum_id, thread_id, post_text, post_creator, post_time)
VALUES (1,1, "Python Smython, It's all about x86 Assembly!", "mary.magdalene", "2018-09-14 15:17:28.082059");
INSERT INTO posts (forum_id, thread_id, post_text, post_creator, post_time)
VALUES (1,1, "Ha, try coding the next facebook on assembly code", "marek.sautter", "2018-09-14 15:31:11.063779");


INSERT INTO threads (forum_id, thread_id, thread_title, thread_creator, thread_time)
VALUES (1,2, "How do you avoid creating 'spaghetti-code'?", "billy.graham", "2018-09-14 15:03:17.245418");
INSERT INTO posts (forum_id, thread_id, post_text, post_creator, post_time)
VALUES (1,2, "Everytime I start something in Python it just ends up being a huge mess. What are the best practices for OOP principles in Python?", "billy.graham", "2018-09-14 15:03:17.245418");
INSERT INTO posts (forum_id, thread_id, post_text, post_creator, post_time)
VALUES (1,2, "The best way to avoid spaghetti code is to not eat spaghetti while coding", "franklin.graham", "2018-09-14 15:39:13.590829");
INSERT INTO posts (forum_id, thread_id, post_text, post_creator, post_time)
VALUES (1,2, "No, @franklin.graham, you've got the wrong idea. I would say the best way to avoid it is to sketch your code down on a piece of paper before you start", "marek.sautter", "2018-09-14 15:41:00.676886");

INSERT INTO threads (forum_id, thread_id, thread_title, thread_creator, thread_time)
VALUES (2,1, "Is Java Dying?", "kirk.cameron", "2018-09-14 15:08:39.121413");
INSERT INTO posts (forum_id, thread_id, post_text, post_creator, post_time)
VALUES (2,1, "My friend made fun of me for coding in Java the other day. He said I was coding in a dead language, is that true?", "kirk.cameron", "2018-09-14 15:08:39.121413");
INSERT INTO posts (forum_id, thread_id, post_text, post_creator, post_time)
VALUES (2,1, "Yup it's dead, switch while you can", "td.jakes", "2018-09-14 15:17:19.593804");
INSERT INTO posts (forum_id, thread_id, post_text, post_creator, post_time)
VALUES (2,1, "Well now hold on @td.jakes, there are still companies that need Java developers. It's not dead yet!", "marek.sautter", "2018-09-14 15:17:19.593804");


INSERT INTO threads (forum_id, thread_id, thread_title, thread_creator, thread_time)
VALUES (2,2, "Top 3 Tips For Java", "rick.warren", "2018-09-14 15:10:43.361063");
INSERT INTO posts (forum_id, thread_id, post_text, post_creator, post_time)
VALUES (2,2, "Just started coding in Java, what are your best tips for a newbie?", "rick.warren", "2018-09-14 15:10:43.361063");
INSERT INTO posts (forum_id, thread_id, post_text, post_creator, post_time)
VALUES (2,2, "I use these tips for roasting the best cup of Java: https://food-hacks.wonderhowto.com/how-to/make-perfect-coffee-every-time-with-these-java-pro-tips-0160957/", "nick.vujicic", "2018-09-14 15:17:45.812445");
INSERT INTO posts (forum_id, thread_id, post_text, post_creator, post_time)
VALUES (2,2, "@nick.vujicic, I think he meant Java the programming language. Here's a good video to watch before you start coding in java: https://www.youtube.com/watch?v=dQw4w9WgXcQ", "marek.sautter", "2018-09-14 15:18:19.812445");


INSERT INTO threads (forum_id, thread_id, thread_title, thread_creator, thread_time)
VALUES (3,1, "Why do schools still teach C++ first", "joseph.smith", "2018-09-14 15:13:38.751101");
INSERT INTO posts (forum_id, thread_id, post_text, post_creator, post_time)
VALUES (3,1, "C++ isn't the most difficult language but it certainly isn't the easiest. Why do most colleges teach such a difficult language to begin with?", "joseph.smith", "2018-09-14 15:13:38.751101");
INSERT INTO posts (forum_id, thread_id, post_text, post_creator, post_time)
VALUES (3,1, "Schools teach C++ first that way the losers that don't know how to code will drop out! More money for those who stay!", "joel.olsteen", "2018-09-14 15:47:05.833942");
INSERT INTO posts (forum_id, thread_id, post_text, post_creator, post_time)
VALUES (3,1, "While I do believe a lot of college freshmen transfer from CPSC because it's difficult, that doesn't mean it should be that way. We need to make it easier for our classmates to do well with coding. We need to make coding fun and available to everyone! And screw you @joel.osteen, you already have enough money, you don't need more!", "marek.sautter", "2018-09-14 15:50:00.048241");



INSERT INTO threads (forum_id, thread_id, thread_title, thread_creator, thread_time)
VALUES (3,2, "Game Development with C++?", "marry.eddy", "2018-09-14 15:15:09.371090");
INSERT INTO posts (forum_id, thread_id, post_text, post_creator, post_time)
VALUES (3,2,"Is C++ still the industry standard for making video games? I'm getting back into the game development business and I have no idea what's relevant these days", "marry.eddy", "2018-09-14 15:15:09.371090");
INSERT INTO posts (forum_id, thread_id, post_text, post_creator, post_time)
VALUES (3,2,"The best games are developed using x86 Assembly.", "mary.magdalene", "2018-09-14 15:51:10.570510");
INSERT INTO posts (forum_id, thread_id, post_text, post_creator, post_time)
VALUES (3,2,"God dammnit @mary.magdalene, who the hell let you into this private forum, was it @jesus.christ? C++ is still being used @marry.eddy but I would look into the C#/Unity Combo that's starting to get popular", "marek.sautter", "2018-09-14 15:52:39.208019");

