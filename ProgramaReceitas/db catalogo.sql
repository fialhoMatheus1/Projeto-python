create database Catalogo;
use Catalogo;

create table catalogo(
    codigo int primary key not null auto_increment,
    nome varchar(100) not null,
    igrediente varchar(300) not null,
    preparo varchar(3000) not null,
    link varchar(100) not null
) engine = InnoDB;