CREATE TABLE parks (
	id smallserial NOT NULL,
	code varchar NULL,
	name varchar NULL,
	state varchar NULL,
	acres int4 NULL,
	lat numeric NULL,
	lon numeric NULL
);


CREATE TABLE species (
	species_id varchar NULL,
	name varchar NULL,
	category varchar NULL,
	order varchar NULL,
	family varchar NULL,
	sciname varchar NULL,
	comname varchar NULL,
	record_status varchar NULL,
	occurence varchar NULL,
	native varchar NULL,
	abundance varchar NULL,
	seasonality varchar NULL,
	conserve_status varchar NULL,
	id serial NOT NULL,
	CONSTRAINT species_pkey PRIMARY KEY (id)
);

ALTER TABLE species 
RENAME COLUMN id to species_id;


ALTER TABLE species 
ADD COLUMN id serial primary key;

CREATE TABLE merge AS 
SELECT 
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
ON (p.name = s.name);

ALTER TABLE merge 
ADD COLUMN id serial primary key