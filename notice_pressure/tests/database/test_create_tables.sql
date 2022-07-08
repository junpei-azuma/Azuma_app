DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS passwords;

CREATE TABLE users (
    id VARCHAR(30) PRIMARY KEY unique,
    email VARCHAR(100) NOT NULL unique,
    is_active BOOLEAN NOT NULL DEFAULT FALSE,
    is_deleted BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE passwords (
   user_id VARCHAR(30) , INDEX password_index(user_id), FOREIGN KEY fk_userid(user_id) REFERENCES users(id) ON DELETE CASCADE,
   value VARCHAR(200) NOT NULL unique
);