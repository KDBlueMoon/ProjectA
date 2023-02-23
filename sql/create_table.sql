create table user(
    id bigserial not null,
    code varchar,
    user varchar,
    password varchar,
    class_ids bigint,
    role int,
    CONSTRAINT pkey_user PRIMARY KEY (id)
);