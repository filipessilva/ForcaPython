create database bdti13n;

use bdti13n;

create table cadastro(
CPF bigint(11) not null primary key,
nome varchar(100) not null,
usuario varchar(100) not null,
senha varchar(100) not null,
email varchar(100) not null,
dataDeNascimento date not null

)Engine= InnoDB;

