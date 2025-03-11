create table etage (
    id int not null primary key auto_increment,
    nom varchar(255),
    numero int,
    superficie int)
    ;


 create table salle(
    id int not null primary key auto_increment,
    nom varchar(255),
    id_etage int,
    capacite int,
    foreign key (id_etage) references etage(id)
    );