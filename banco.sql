CREATE TABLE user (
	id_user integer PRIMARY KEY AUTOINCREMENT,
	user_name varchar,
	login varchar,
	password varchar,
	phone varchar
);

CREATE TABLE audio (
	id_audio integer PRIMARY KEY AUTOINCREMENT,
	arq_name varchar,
	id_user varchar,
	creation_date date
);

CREATE TABLE text_audio (
	id_text integer PRIMARY KEY AUTOINCREMENT,
	text text,
	id_audio integer
);

CREATE TABLE payment (
	id_payment integer PRIMARY KEY AUTOINCREMENT,
	value float,
	id_user integer,
	id_audio integer
);

CREATE TABLE audio_preset (
	id_preset integer PRIMARY KEY AUTOINCREMENT,
	id_text integer,
	config text
);






