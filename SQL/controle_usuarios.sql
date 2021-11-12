-- Criar cargo DBA 
CREATE ROLE dba_yelp;
GRANT ALL PRIVILEGES ON DATABASE "yelp" TO dba_yelp;
GRANT ALL ON ALL TABLES IN SCHEMA public TO dba_yelp;

-- Criar usuário DBA
CREATE USER dba WITH PASSWORD '12345';
GRANT dba_yelp TO dba;

-- Criar cargo Programador
CREATE ROLE programador_yelp;
GRANT INSERT, SELECT, UPDATE ON TABLE public.avaliacao, public.comercio, 
public.localizacao, public.transacao, public.usuario TO programador_yelp;
GRANT USAGE ON SCHEMA public TO programador_yelp;

-- Criar usuários Programador
CREATE USER programador1 WITH PASSWORD '12345';
GRANT programador_yelp TO programador1;
CREATE USER programador2 WITH PASSWORD '12345';
GRANT programador_yelp TO programador2;

