-- persiana_paludo (banco de dados e usuario) Master12131415

--
-- PostgreSQL database dump
--

SET client_encoding = 'UTF8';
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'Standard public schema';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: website_log; Type: TABLE; Schema: public; Owner: persiana; Tablespace: 
--

CREATE TABLE website_log (
    id serial NOT NULL,
    usuario integer,
    operacao character varying(50) NOT NULL,
    endereco_ip character varying(50),
    log text NOT NULL,
    data timestamp without time zone NOT NULL,
    menu character varying(150)
);


ALTER TABLE public.website_log OWNER TO persiana;

--
-- Name: website_pagina; Type: TABLE; Schema: public; Owner: persiana; Tablespace: 
--

CREATE TABLE website_pagina (
    id serial NOT NULL,
    titulo character varying(250) NOT NULL,
    slug character varying(255) NOT NULL,
    data_criacao timestamp without time zone NOT NULL,
    ultima_alteracao timestamp without time zone NOT NULL,
    usuario_alteracao integer NOT NULL,
    conteudo text NOT NULL,
    descricao_completa character varying(255),
    palavras_chaves character varying(255),
    locked character varying(1) DEFAULT 'N'::character varying NOT NULL,
    status character varying(1) DEFAULT 'A'::character varying NOT NULL,
    moderate_id integer
);


ALTER TABLE public.website_pagina OWNER TO persiana;

--
-- Name: website_produto; Type: TABLE; Schema: public; Owner: persiana; Tablespace: 
--

CREATE TABLE website_produto (
    id serial NOT NULL,
    titulo character varying(250) NOT NULL,
    slug character varying(255) NOT NULL,
    data_criacao timestamp without time zone NOT NULL,
    ultima_alteracao timestamp without time zone NOT NULL,
    usuario_alteracao integer NOT NULL,
    caracteristicas text NOT NULL,
    palavras_chaves character varying(255),
    url_galeria character varying(255) NOT NULL,
    locked character varying(1) DEFAULT 'N'::character varying NOT NULL,
    status character varying(1) DEFAULT 'A'::character varying NOT NULL,
    moderate_id integer
);


ALTER TABLE public.website_produto OWNER TO persiana;

--
-- Name: website_usuario; Type: TABLE; Schema: public; Owner: persiana; Tablespace: 
--

CREATE TABLE website_usuario (
    id serial NOT NULL,
    "login" character varying(255) NOT NULL,
    senha character varying(8) NOT NULL,
    nivel_acesso integer NOT NULL
);


ALTER TABLE public.website_usuario OWNER TO persiana;

--
-- Name: website_log_pk; Type: CONSTRAINT; Schema: public; Owner: persiana; Tablespace: 
--

ALTER TABLE ONLY website_log
    ADD CONSTRAINT website_log_pk PRIMARY KEY (id);


--
-- Name: website_pagina_pk; Type: CONSTRAINT; Schema: public; Owner: persiana; Tablespace: 
--

ALTER TABLE ONLY website_pagina
    ADD CONSTRAINT website_pagina_pk PRIMARY KEY (id);


--
-- Name: website_pagina_titulo_uk; Type: CONSTRAINT; Schema: public; Owner: persiana; Tablespace: 
--

ALTER TABLE ONLY website_pagina
    ADD CONSTRAINT website_pagina_titulo_uk UNIQUE (titulo);


--
-- Name: website_produto_pk; Type: CONSTRAINT; Schema: public; Owner: persiana; Tablespace: 
--

ALTER TABLE ONLY website_produto
    ADD CONSTRAINT website_produto_pk PRIMARY KEY (id);


--
-- Name: website_produto_titulo_uk; Type: CONSTRAINT; Schema: public; Owner: persiana; Tablespace: 
--

ALTER TABLE ONLY website_produto
    ADD CONSTRAINT website_produto_titulo_uk UNIQUE (titulo);


--
-- Name: website_usuario_login_uk; Type: CONSTRAINT; Schema: public; Owner: persiana; Tablespace: 
--

ALTER TABLE ONLY website_usuario
    ADD CONSTRAINT website_usuario_login_uk UNIQUE ("login");


--
-- Name: website_usuario_pk; Type: CONSTRAINT; Schema: public; Owner: persiana; Tablespace: 
--

ALTER TABLE ONLY website_usuario
    ADD CONSTRAINT website_usuario_pk PRIMARY KEY (id);


--
-- Name: website_pagina_usuario_fk; Type: FK CONSTRAINT; Schema: public; Owner: persiana
--

ALTER TABLE ONLY website_pagina
    ADD CONSTRAINT website_pagina_usuario_fk FOREIGN KEY (usuario_alteracao) REFERENCES website_usuario(id);


--
-- Name: website_produto_usuario_fk; Type: FK CONSTRAINT; Schema: public; Owner: persiana
--

ALTER TABLE ONLY website_produto
    ADD CONSTRAINT website_produto_usuario_fk FOREIGN KEY (usuario_alteracao) REFERENCES website_usuario(id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;

CREATE TABLE website_promocao
(
  id serial NOT NULL,
  titulo character varying(250) NOT NULL,
  slug character varying(255) NOT NULL,
  data_criacao timestamp without time zone NOT NULL,
  ultima_alteracao timestamp without time zone NOT NULL,
  usuario_alteracao integer NOT NULL,
  conteudo text NOT NULL,
  ativo character varying(1) NOT NULL,
  locked character varying(1) NOT NULL DEFAULT 'N'::character varying,
  status character varying(1) NOT NULL DEFAULT 'A'::character varying,
  moderate_id integer,
  CONSTRAINT website_promocao_pk PRIMARY KEY (id),
  CONSTRAINT website_promocao_usuario_fk FOREIGN KEY (usuario_alteracao)
      REFERENCES website_usuario (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT website_promocao_titulo_uk UNIQUE (titulo)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE website_promocao OWNER TO persiana_paludo;
