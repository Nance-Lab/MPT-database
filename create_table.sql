CREATE TABLE TRACKMATEDATA (
    ExpId INTEGER,
    Slide INTEGER,
    video INTEGER,
    Track_ID INTEGER,
    Frame INTEGER,
    X REAL,
    Y REAL,
    PRIMARY KEY (ExpId, Slide, video, Track_ID, Frame)
);

CREATE TABLE EXPNAMES (
    ExpId INTEGER,
    ExpName VARCHAR(20) -- 20 characters
);

-- Table for each experiment
-- CREATE TABLE TRACKMATEDATA_<EXPNAME> (
--     Slide INTEGER,
--     video INTEGER,
--     Track_ID INTEGER,
--     Frame INTEGER,
--     X REAL,
--     Y REAL,
--     PRIMARY KEY (ExpId, Slide, video, Track_ID, Frame)
-- );
