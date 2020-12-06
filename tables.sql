USE sql_intro;

-- CREATE TABLE Type(
--     id TINYINT AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(20)
-- );

-- CREATE TABLE Trainer(
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(20),
--     city VARCHAR(20)
-- );

-- CREATE TABLE Pokimon(
--     id INT NOT NULL PRIMARY KEY,
--     name VARCHAR(20),
--     type TINYINT,
--     height INT,
--     weight INT,
--     FOREIGN KEY(type) REFERENCES Type(id)
-- );

CREATE TABLE OwnedBy(
    pokimon_id INT,
    trainer_id INT,
    satiety_level INT,
    FOREIGN KEY(pokimon_id) REFERENCES Pokimon(id),
    FOREIGN KEY(trainer_id) REFERENCES Trainer(id)
);