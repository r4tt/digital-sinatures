create table user(
    id varchar(255) not null primary key,
    i varchar(255) not null,
    d varchar(255) not null
);

create table signature(
    id int primary key auto_increment,
    user_id varchar(255) not null,
    document varchar(255) not null,
    constraint user_ibfk_1
    foreign key (user_id) references user (id)
        on delete cascade,
    constraint uq_user_id_document
        unique (user_id, document)
)