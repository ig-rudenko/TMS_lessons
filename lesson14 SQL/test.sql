-- Создаем базу данных.
create database if not exists test;

-- Начинаем работать с конкретной базой.
use test;

-- Посмотреть какие есть таблицы.
show tables;

create table users (
	id int unsigned primary key auto_increment,  -- Уникальный идентификатор
	username varchar(64) not null,  -- длина 64 символа (обязательно для заполнения)
    password varchar(64) not null,
    phone varchar(20) null
);

-- Вернуть все записи из таблицы users
select * from users;

-- Вставка данных
insert users(username, password) values('igor', 'password');
insert users(username, password) values('igor', 'password');

-- Удалим пользователя с идентификатором 2
delete from users where id = 2;

-- Обновляем поле username (чтобы оно было уникальным)
alter table users add unique (username);

-- Таблица для заметок пользователя
create table posts (
	id int unsigned primary key auto_increment,
    user_id int unsigned not null,  -- Для уникального ключа пользователя
    title varchar(200) default 'Заголовок не указан' not null,  -- Со значением по умолчанию
    created datetime not null,
    content text not null,

    -- Связываем таблицу пользователей (поле id) с полем user_id в текущей таблице.
    -- Создаем "внешний ключ".
    foreign key (user_id) references users (id)
);

-- Добавляем запись и указываем в ней идентификатор пользователя, который её создал.
insert posts(title, created, content, user_id) values('T1', '2018-05-25 19:21:34', 'test', 1);
-- Заголовок будет по умолчанию.
insert posts(created, content, user_id) values('2023-05-25 19:21:34', 'test', 1);

-- Смотрим все записи
select * from posts;

-- Смотрим только заголовки всех записей
select title from posts;

-- Смотрим только заголовки всех записей для пользователя под id = 1 и длина заголовка больше 5.
select title from posts where user_id = 1 or length(title) > 5;

select title, created from posts where year(created) >= 2023;

-- Удалим таблицы
drop table posts;
drop table users;

-- Валидаторы
create table users (
	id int primary key auto_increment,
    username varchar(64) unique not null,  -- Уникальный
	first_name varchar(50) not null,
    last_name varchar(50),
	age tinyint unsigned not null,  -- целые числа от 0 до 255
    passwd varchar(50) not null,
    email varchar(50) unique not null,  -- Уникальный
    phone varchar(20) not null unique,  -- Уникальный

    constraint name_check check (username != ''),  -- username НЕ должен быть пустой строкой.
    constraint age_check check (age > 0 and age < 150),
    constraint email_check check (email regexp '^[0-9a-zA-Z-\._]+@[0-9a-zA-Z-\._]+'),
    constraint passwd_check check (length(passwd) >= 8),
    -- Регулярное выражение для проверки номера.
    constraint phone_check check (phone regexp '^[0-9]+$')  -- Должен состоять только из цифр.
);

insert users(username, first_name, age, passwd, email, phone)
		value('user', '', 1, "12345678", "user@mail", "000000000");

select * from users;
