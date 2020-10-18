CREATE TABLE parks (
	id smallserial NOT NULL,
	code varchar(32767) NULL,
	name varchar(32767) NULL,
	state varchar NULL,
	acres int4 NULL,
	lat numeric NULL,
	lon numeric NULL
);


CREATE TABLE public.species (
	species_id varchar(32767) NULL,
	name varchar(32767) NULL,
	category varchar(32767) NULL,
	order varchar(32767) NULL,
	family varchar(32767) NULL,
	sciname varchar(32767) NULL,
	comname varchar(32767) NULL,
	record_status varchar(32767) NULL,
	occurence varchar(32767) NULL,
	native varchar(32767) NULL,
	abundance varchar(32767) NULL,
	seasonality varchar(32767) NULL,
	conserve_status varchar(32767) NULL,
	id serial NOT NULL,
	CONSTRAINT species_pkey PRIMARY KEY (id)
);

ALTER TABLE species 
RENAME COLUMN id to species_id;


ALTER TABLE species 
ADD COLUMN id serial primary key;

CREATE TABLE merge AS SELECT 
            p.code, 
            p.name, 
            p.state, 
            p.acres, 
            p.lat, 
            p.lon, 
            s.species_id, 
            s.category, 
            s.order, 
            s.family, 
            s.sciname, 
            s.comname, 
            s.native, 
            s.abundance, 
            s.conserve_status 
FROM parks as p 
RIGHT JOIN species AS s 
ON (p.name =s.name);

ALTER TABLE merge 
ADD COLUMN id serial primary key