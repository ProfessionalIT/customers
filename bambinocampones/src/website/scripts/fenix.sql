--
-- PostgreSQL database dump
--

-- Dumped from database version 9.1.6
-- Dumped by pg_dump version 9.1.6
-- Started on 2012-11-13 08:57:24 BRST

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 2144 (class 1262 OID 28597)
-- Name: fenix_db; Type: DATABASE; Schema: -; Owner: -
--

CREATE DATABASE fenix_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';


\connect fenix_db

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 194 (class 3079 OID 11680)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2146 (class 0 OID 0)
-- Dependencies: 194
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 162 (class 1259 OID 26648)
-- Dependencies: 1996 1997 5
-- Name: aviso; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE aviso (
    id integer NOT NULL,
    titulo character varying(250) NOT NULL,
    slug character varying(255) NOT NULL,
    data_publicacao timestamp without time zone NOT NULL,
    data_expiracao timestamp without time zone NOT NULL,
    autor integer NOT NULL,
    texto text NOT NULL,
    ativo character varying(1),
    locked character varying(1) DEFAULT 'N'::character varying NOT NULL,
    status character varying(1) DEFAULT 'A'::character varying NOT NULL,
    moderate_id integer,
    draft character varying(1)
);


--
-- TOC entry 161 (class 1259 OID 26646)
-- Dependencies: 5 162
-- Name: aviso_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE aviso_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2147 (class 0 OID 0)
-- Dependencies: 161
-- Name: aviso_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE aviso_id_seq OWNED BY aviso.id;


--
-- TOC entry 2148 (class 0 OID 0)
-- Dependencies: 161
-- Name: aviso_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('aviso_id_seq', 1, true);


--
-- TOC entry 164 (class 1259 OID 26659)
-- Dependencies: 1999 2000 5
-- Name: banner; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE banner (
    id integer NOT NULL,
    titulo character varying(250) NOT NULL,
    slug character varying(255) NOT NULL,
    autor integer NOT NULL,
    tipo character varying(1) NOT NULL,
    foto_banner character varying(255) NOT NULL,
    link_banner character varying(255) NOT NULL,
    exibir_pagina_inicial character varying(1) NOT NULL,
    ativo character varying(1) NOT NULL,
    locked character varying(1) DEFAULT 'N'::character varying NOT NULL,
    status character varying(1) DEFAULT 'A'::character varying NOT NULL,
    moderate_id integer,
    count_clicks integer,
    custom_banner_code text,
    draft character varying(1)
);


--
-- TOC entry 163 (class 1259 OID 26657)
-- Dependencies: 164 5
-- Name: banner_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE banner_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2149 (class 0 OID 0)
-- Dependencies: 163
-- Name: banner_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE banner_id_seq OWNED BY banner.id;


--
-- TOC entry 2150 (class 0 OID 0)
-- Dependencies: 163
-- Name: banner_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('banner_id_seq', 5, true);


--
-- TOC entry 166 (class 1259 OID 26670)
-- Dependencies: 2002 2003 5
-- Name: documento; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE documento (
    id integer NOT NULL,
    titulo character varying(250) NOT NULL,
    slug character varying(255) NOT NULL,
    data_publicacao timestamp without time zone NOT NULL,
    autor integer NOT NULL,
    thumb_arquivo character varying(255) NOT NULL,
    link_arquivo character varying(255) NOT NULL,
    ativo character varying(1) NOT NULL,
    locked character varying(1) DEFAULT 'N'::character varying NOT NULL,
    status character varying(1) DEFAULT 'A'::character varying NOT NULL,
    moderate_id integer,
    tipo integer NOT NULL,
    draft character varying(1)
);


--
-- TOC entry 165 (class 1259 OID 26668)
-- Dependencies: 166 5
-- Name: documento_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE documento_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2151 (class 0 OID 0)
-- Dependencies: 165
-- Name: documento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE documento_id_seq OWNED BY documento.id;


--
-- TOC entry 2152 (class 0 OID 0)
-- Dependencies: 165
-- Name: documento_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('documento_id_seq', 1, true);


--
-- TOC entry 168 (class 1259 OID 26681)
-- Dependencies: 2005 2006 5
-- Name: enquete; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE enquete (
    id integer NOT NULL,
    pergunta character varying(250) NOT NULL,
    slug character varying(255) NOT NULL,
    resposta_01 character varying(255) NOT NULL,
    votos_resposta_01 integer NOT NULL,
    resposta_02 character varying(255) NOT NULL,
    votos_resposta_02 integer NOT NULL,
    resposta_03 character varying(255),
    votos_resposta_03 integer,
    ativo character varying(1),
    locked character varying(1) DEFAULT 'N'::character varying NOT NULL,
    status character varying(1) DEFAULT 'A'::character varying NOT NULL,
    moderate_id integer,
    autor integer NOT NULL,
    draft character varying(1)
);


--
-- TOC entry 167 (class 1259 OID 26679)
-- Dependencies: 168 5
-- Name: enquete_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE enquete_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2153 (class 0 OID 0)
-- Dependencies: 167
-- Name: enquete_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE enquete_id_seq OWNED BY enquete.id;


--
-- TOC entry 2154 (class 0 OID 0)
-- Dependencies: 167
-- Name: enquete_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('enquete_id_seq', 1, true);


--
-- TOC entry 170 (class 1259 OID 26692)
-- Dependencies: 2008 2009 2010 5
-- Name: galeria; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE galeria (
    id integer NOT NULL,
    titulo character varying(250) NOT NULL,
    slug character varying(255) NOT NULL,
    data_criacao timestamp without time zone NOT NULL,
    autor integer NOT NULL,
    tipo character varying(1) NOT NULL,
    midia character varying(1) NOT NULL,
    url_galeria character varying(255) NOT NULL,
    locked character varying(1) DEFAULT 'N'::character varying NOT NULL,
    status character varying(1) DEFAULT 'A'::character varying NOT NULL,
    moderate_id integer,
    permite_comentario character varying(1) DEFAULT 'N'::character varying NOT NULL,
    draft character varying(1)
);


--
-- TOC entry 169 (class 1259 OID 26690)
-- Dependencies: 170 5
-- Name: galeria_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE galeria_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2155 (class 0 OID 0)
-- Dependencies: 169
-- Name: galeria_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE galeria_id_seq OWNED BY galeria.id;


--
-- TOC entry 2156 (class 0 OID 0)
-- Dependencies: 169
-- Name: galeria_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('galeria_id_seq', 1, true);


--
-- TOC entry 172 (class 1259 OID 26704)
-- Dependencies: 5
-- Name: log; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE log (
    id integer NOT NULL,
    usuario integer,
    operacao character varying(50) NOT NULL,
    endereco_ip character varying(50),
    log text NOT NULL,
    data timestamp without time zone NOT NULL,
    menu character varying(150)
);


--
-- TOC entry 171 (class 1259 OID 26702)
-- Dependencies: 172 5
-- Name: log_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2157 (class 0 OID 0)
-- Dependencies: 171
-- Name: log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE log_id_seq OWNED BY log.id;


--
-- TOC entry 2158 (class 0 OID 0)
-- Dependencies: 171
-- Name: log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('log_id_seq', 75, true);


--
-- TOC entry 173 (class 1259 OID 26711)
-- Dependencies: 5
-- Name: menu_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE menu_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2159 (class 0 OID 0)
-- Dependencies: 173
-- Name: menu_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('menu_id_seq', 9, true);


--
-- TOC entry 174 (class 1259 OID 26713)
-- Dependencies: 2012 2013 2014 5
-- Name: menu; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE menu (
    id integer DEFAULT nextval('menu_id_seq'::regclass) NOT NULL,
    ordem integer NOT NULL,
    titulo character varying(250) NOT NULL,
    descricao character varying(255) NOT NULL,
    slug character varying(255) NOT NULL,
    data_criacao timestamp without time zone NOT NULL,
    ultima_alteracao timestamp without time zone NOT NULL,
    autor integer NOT NULL,
    pagina integer NOT NULL,
    endereco character varying(255) NOT NULL,
    menu_pai integer,
    nivel integer NOT NULL,
    key_words character varying(250) NOT NULL,
    locked character varying(1) DEFAULT 'N'::character varying NOT NULL,
    status character varying(1) DEFAULT 'A'::character varying NOT NULL,
    moderate_id integer,
    draft character varying(1)
);


--
-- TOC entry 176 (class 1259 OID 26724)
-- Dependencies: 5
-- Name: moderacao; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE moderacao (
    id integer NOT NULL,
    data_hora timestamp without time zone NOT NULL,
    autor integer NOT NULL,
    onde character varying(250) NOT NULL,
    operacao character varying(250) NOT NULL,
    moderador integer,
    data_hora_operacao timestamp without time zone,
    acao character varying(1),
    detalhamento text
);


--
-- TOC entry 175 (class 1259 OID 26722)
-- Dependencies: 5 176
-- Name: moderacao_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE moderacao_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2160 (class 0 OID 0)
-- Dependencies: 175
-- Name: moderacao_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE moderacao_id_seq OWNED BY moderacao.id;


--
-- TOC entry 2161 (class 0 OID 0)
-- Dependencies: 175
-- Name: moderacao_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('moderacao_id_seq', 1, true);


--
-- TOC entry 178 (class 1259 OID 26733)
-- Dependencies: 2017 2018 2019 5
-- Name: modulo; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE modulo (
    id integer NOT NULL,
    titulo character varying(250) NOT NULL,
    class_name character varying(250) NOT NULL,
    slug character varying(255) NOT NULL,
    ativo character varying(1),
    perfil_acesso character varying(5) DEFAULT 'A'::character varying NOT NULL,
    locked character varying(1) DEFAULT 'N'::character varying NOT NULL,
    status character varying(1) DEFAULT 'A'::character varying NOT NULL,
    moderate_id integer,
    draft character varying(1)
);


--
-- TOC entry 177 (class 1259 OID 26731)
-- Dependencies: 5 178
-- Name: modulo_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE modulo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2162 (class 0 OID 0)
-- Dependencies: 177
-- Name: modulo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE modulo_id_seq OWNED BY modulo.id;


--
-- TOC entry 2163 (class 0 OID 0)
-- Dependencies: 177
-- Name: modulo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('modulo_id_seq', 1, false);


--
-- TOC entry 180 (class 1259 OID 26745)
-- Dependencies: 2021 2022 2023 5
-- Name: pagina; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE pagina (
    id integer NOT NULL,
    titulo character varying(250) NOT NULL,
    slug character varying(255) NOT NULL,
    data_criacao timestamp without time zone NOT NULL,
    ultima_alteracao timestamp without time zone NOT NULL,
    autor integer NOT NULL,
    conteudo text NOT NULL,
    descricao_completa character varying(255),
    palavras_chaves character varying(255),
    locked character varying(1) DEFAULT 'N'::character varying NOT NULL,
    status character varying(1) DEFAULT 'A'::character varying NOT NULL,
    moderate_id integer,
    permite_comentario character varying(1) DEFAULT 'N'::character varying NOT NULL,
    draft character varying(1)
);


--
-- TOC entry 179 (class 1259 OID 26743)
-- Dependencies: 5 180
-- Name: pagina_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE pagina_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2164 (class 0 OID 0)
-- Dependencies: 179
-- Name: pagina_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE pagina_id_seq OWNED BY pagina.id;


--
-- TOC entry 2165 (class 0 OID 0)
-- Dependencies: 179
-- Name: pagina_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('pagina_id_seq', 251, true);


--
-- TOC entry 182 (class 1259 OID 26757)
-- Dependencies: 2025 2026 5
-- Name: parametro; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE parametro (
    id integer NOT NULL,
    titulo character varying(250) NOT NULL,
    valor character varying(250) NOT NULL,
    locked character varying(1) DEFAULT 'N'::character varying NOT NULL,
    status character varying(1) DEFAULT 'A'::character varying NOT NULL,
    moderate_id integer,
    autor integer NOT NULL
);


--
-- TOC entry 181 (class 1259 OID 26755)
-- Dependencies: 182 5
-- Name: parametro_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE parametro_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2166 (class 0 OID 0)
-- Dependencies: 181
-- Name: parametro_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE parametro_id_seq OWNED BY parametro.id;


--
-- TOC entry 2167 (class 0 OID 0)
-- Dependencies: 181
-- Name: parametro_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('parametro_id_seq', 1, true);


--
-- TOC entry 184 (class 1259 OID 26768)
-- Dependencies: 2028 2029 2030 5
-- Name: publicacao; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE publicacao (
    id integer NOT NULL,
    titulo character varying(250) NOT NULL,
    slug character varying(255) NOT NULL,
    data_hora timestamp without time zone NOT NULL,
    autor integer NOT NULL,
    data_publicacao timestamp without time zone NOT NULL,
    palavras_chaves character varying(255) NOT NULL,
    intro text NOT NULL,
    completa text NOT NULL,
    thumb_publicacao character varying(255) NOT NULL,
    slug_galeria character varying(255) NOT NULL,
    destaque character varying(1) NOT NULL,
    locked character varying(1) DEFAULT 'N'::character varying NOT NULL,
    status character varying(1) DEFAULT 'A'::character varying NOT NULL,
    moderate_id integer,
    permite_comentario character varying(1) DEFAULT 'N'::character varying NOT NULL,
    draft character varying(1)
);


--
-- TOC entry 183 (class 1259 OID 26766)
-- Dependencies: 5 184
-- Name: publicacao_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE publicacao_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2168 (class 0 OID 0)
-- Dependencies: 183
-- Name: publicacao_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE publicacao_id_seq OWNED BY publicacao.id;


--
-- TOC entry 2169 (class 0 OID 0)
-- Dependencies: 183
-- Name: publicacao_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('publicacao_id_seq', 1, true);


--
-- TOC entry 185 (class 1259 OID 26778)
-- Dependencies: 5
-- Name: publicacao_tipo_publicacao; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE publicacao_tipo_publicacao (
    publicacao integer NOT NULL,
    tipo_publicacao integer NOT NULL
);


--
-- TOC entry 186 (class 1259 OID 26781)
-- Dependencies: 5
-- Name: template_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE template_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2170 (class 0 OID 0)
-- Dependencies: 186
-- Name: template_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('template_id_seq', 1, true);


--
-- TOC entry 187 (class 1259 OID 26783)
-- Dependencies: 2031 2032 2033 5
-- Name: template; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE template (
    id integer DEFAULT nextval('template_id_seq'::regclass) NOT NULL,
    titulo character varying(250) NOT NULL,
    slug character varying(255) NOT NULL,
    data_publicacao timestamp without time zone NOT NULL,
    autor integer NOT NULL,
    path character varying(250) NOT NULL,
    ativo character varying(1),
    locked character varying(1) DEFAULT 'N'::character varying NOT NULL,
    status character varying(1) DEFAULT 'A'::character varying NOT NULL,
    moderate_id integer,
    draft character varying(1)
);


--
-- TOC entry 189 (class 1259 OID 26794)
-- Dependencies: 2035 2036 2037 5
-- Name: tipo_documento; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE tipo_documento (
    id integer NOT NULL,
    titulo character varying(250) NOT NULL,
    locked character varying(1) DEFAULT 'N'::character varying NOT NULL,
    status character varying(1) DEFAULT 'A'::character varying NOT NULL,
    moderate_id integer,
    autor integer DEFAULT 1 NOT NULL
);


--
-- TOC entry 188 (class 1259 OID 26792)
-- Dependencies: 189 5
-- Name: tipo_documento_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE tipo_documento_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2171 (class 0 OID 0)
-- Dependencies: 188
-- Name: tipo_documento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE tipo_documento_id_seq OWNED BY tipo_documento.id;


--
-- TOC entry 2172 (class 0 OID 0)
-- Dependencies: 188
-- Name: tipo_documento_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('tipo_documento_id_seq', 1, true);


--
-- TOC entry 191 (class 1259 OID 26803)
-- Dependencies: 2039 2040 2041 5
-- Name: tipo_publicacao; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE tipo_publicacao (
    id integer NOT NULL,
    titulo character varying(250) NOT NULL,
    locked character varying(1) DEFAULT 'N'::character varying NOT NULL,
    status character varying(1) DEFAULT 'A'::character varying NOT NULL,
    moderate_id integer,
    autor integer DEFAULT 1 NOT NULL
);


--
-- TOC entry 190 (class 1259 OID 26801)
-- Dependencies: 191 5
-- Name: tipo_publicacao_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE tipo_publicacao_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2173 (class 0 OID 0)
-- Dependencies: 190
-- Name: tipo_publicacao_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE tipo_publicacao_id_seq OWNED BY tipo_publicacao.id;


--
-- TOC entry 2174 (class 0 OID 0)
-- Dependencies: 190
-- Name: tipo_publicacao_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('tipo_publicacao_id_seq', 3, true);


--
-- TOC entry 193 (class 1259 OID 26812)
-- Dependencies: 5
-- Name: usuario; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE usuario (
    id integer NOT NULL,
    login character varying(255) NOT NULL,
    senha character varying(8) NOT NULL,
    nivel_acesso integer NOT NULL
);


--
-- TOC entry 192 (class 1259 OID 26810)
-- Dependencies: 193 5
-- Name: usuario_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE usuario_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2175 (class 0 OID 0)
-- Dependencies: 192
-- Name: usuario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE usuario_id_seq OWNED BY usuario.id;


--
-- TOC entry 2176 (class 0 OID 0)
-- Dependencies: 192
-- Name: usuario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('usuario_id_seq', 2, true);


--
-- TOC entry 1995 (class 2604 OID 26651)
-- Dependencies: 161 162 162
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY aviso ALTER COLUMN id SET DEFAULT nextval('aviso_id_seq'::regclass);


--
-- TOC entry 1998 (class 2604 OID 26662)
-- Dependencies: 163 164 164
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY banner ALTER COLUMN id SET DEFAULT nextval('banner_id_seq'::regclass);


--
-- TOC entry 2001 (class 2604 OID 26673)
-- Dependencies: 165 166 166
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY documento ALTER COLUMN id SET DEFAULT nextval('documento_id_seq'::regclass);


--
-- TOC entry 2004 (class 2604 OID 26684)
-- Dependencies: 167 168 168
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY enquete ALTER COLUMN id SET DEFAULT nextval('enquete_id_seq'::regclass);


--
-- TOC entry 2007 (class 2604 OID 26695)
-- Dependencies: 169 170 170
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY galeria ALTER COLUMN id SET DEFAULT nextval('galeria_id_seq'::regclass);


--
-- TOC entry 2011 (class 2604 OID 26707)
-- Dependencies: 171 172 172
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY log ALTER COLUMN id SET DEFAULT nextval('log_id_seq'::regclass);


--
-- TOC entry 2015 (class 2604 OID 26727)
-- Dependencies: 176 175 176
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY moderacao ALTER COLUMN id SET DEFAULT nextval('moderacao_id_seq'::regclass);


--
-- TOC entry 2016 (class 2604 OID 26736)
-- Dependencies: 177 178 178
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY modulo ALTER COLUMN id SET DEFAULT nextval('modulo_id_seq'::regclass);


--
-- TOC entry 2020 (class 2604 OID 26748)
-- Dependencies: 180 179 180
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY pagina ALTER COLUMN id SET DEFAULT nextval('pagina_id_seq'::regclass);


--
-- TOC entry 2024 (class 2604 OID 26760)
-- Dependencies: 181 182 182
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY parametro ALTER COLUMN id SET DEFAULT nextval('parametro_id_seq'::regclass);


--
-- TOC entry 2027 (class 2604 OID 26771)
-- Dependencies: 183 184 184
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY publicacao ALTER COLUMN id SET DEFAULT nextval('publicacao_id_seq'::regclass);


--
-- TOC entry 2034 (class 2604 OID 26797)
-- Dependencies: 189 188 189
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY tipo_documento ALTER COLUMN id SET DEFAULT nextval('tipo_documento_id_seq'::regclass);


--
-- TOC entry 2038 (class 2604 OID 26806)
-- Dependencies: 191 190 191
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY tipo_publicacao ALTER COLUMN id SET DEFAULT nextval('tipo_publicacao_id_seq'::regclass);


--
-- TOC entry 2042 (class 2604 OID 26815)
-- Dependencies: 192 193 193
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY usuario ALTER COLUMN id SET DEFAULT nextval('usuario_id_seq'::regclass);


--
-- TOC entry 2123 (class 0 OID 26648)
-- Dependencies: 162 2140
-- Data for Name: aviso; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO aviso VALUES (1, 'Teste', 'teste', '2012-05-02 15:25:34', '2012-05-02 15:25:35', 1, '<p><span style="font-family: Arial, Helvetica, sans; font-size: 11px; line-height: 14px; text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vel nulla eget leo rhoncus dignissim nec vel sapien. Nam fermentum augue nec justo dapibus tempor. In et magna enim, vel faucibus augue. Donec purus dolor, dignissim quis iaculis ut, sollicitudin eget sapien. Vivamus ultricies, purus ut blandit accumsan, felis eros mattis ligula, eget fermentum lacus nunc in turpis. Nullam urna odio, facilisis ac fringilla sed, mollis et velit. Etiam interdum, augue et varius rutrum, augue neque pulvinar urna, vitae malesuada justo magna eu sapien. Phasellus sodales accumsan nisl eu ultricies. Nullam quam neque, convallis vel elementum vitae, porttitor eu ligula. Nunc tincidunt aliquam lorem, ac pulvinar ipsum aliquam eu. Nullam id ullamcorper neque. In mollis consectetur commodo. Vivamus magna tellus, scelerisque et iaculis ut, facilisis ac elit.</span></p>', 'S', 'N', 'A', NULL, 'N');


--
-- TOC entry 2124 (class 0 OID 26659)
-- Dependencies: 164 2140
-- Data for Name: banner; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO banner VALUES (2, 'Banner Agenda Top do site', 'banner-agenda-top-do-site', 1, 'T', '/static/images/img1.jpg', '#', 'S', 'S', 'N', 'A', NULL, NULL, 'Agendas bonitas e legais', NULL);
INSERT INTO banner VALUES (4, 'Banner Convites', 'banner-convites', 1, 'T', '/static/images/img3.jpg', '#', 'S', 'S', 'N', 'A', NULL, NULL, 'Convites para casamentos e formaturas', NULL);
INSERT INTO banner VALUES (5, 'Banner Livros', 'banner-livros', 1, 'T', '/static/images/img4.jpg', '#', 'S', 'S', 'N', 'A', NULL, NULL, 'Livros de varios formatos e tipos.', NULL);
INSERT INTO banner VALUES (3, 'Banner Sacolas', 'banner-sacolas', 1, 'T', '/static/images/img2.jpg', '#', 'S', 'S', 'N', 'A', NULL, NULL, 'Sacolas coloridas e resistentes', NULL);


--
-- TOC entry 2125 (class 0 OID 26670)
-- Dependencies: 166 2140
-- Data for Name: documento; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO documento VALUES (1, 'Manual do Produto XYZ', 'manual-do-produto-xyz', '2012-05-02 15:32:17', 1, 'http://www.valeria_websiteurbo.com.br/static/docs/manual_xyz.png', 'http://www.valeria_websiteurbo.com.br/static/docs/manual_xyz.pdf', 'S', 'N', 'A', NULL, 1, 'N');


--
-- TOC entry 2126 (class 0 OID 26681)
-- Dependencies: 168 2140
-- Data for Name: enquete; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO enquete VALUES (1, 'Você gostou do novo site ?', 'voc-gostou-do-novo-site', 'Sim', 0, 'Não', 0, '', 0, 'S', 'S', 'A', NULL, 1, 'N');


--
-- TOC entry 2127 (class 0 OID 26692)
-- Dependencies: 170 2140
-- Data for Name: galeria; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO galeria VALUES (1, 'Fotos do Produto XYZ', 'fotos-do-produto-xyz', '2012-05-02 15:33:21', 1, 'S', 'F', 'https://picasaweb.google.com/106640973776692814000/Imagens_web?authuser=0&feat=directlink', 'N', 'A', NULL, 'N', 'N');


--
-- TOC entry 2128 (class 0 OID 26704)
-- Dependencies: 172 2140
-- Data for Name: log; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO log VALUES (1, 1, 'LOGIN', '189.114.71.202', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-05-02 15:16:22.399023', 'Home');
INSERT INTO log VALUES (2, 1, 'LOGOFF', '189.114.71.202', 'O usuario saiu do Modulo Administrativo', '2012-05-02 15:37:05.588423', 'Home');
INSERT INTO log VALUES (3, 1, 'LOGIN', '189.114.71.202', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-05-02 15:50:14.070735', 'Home');
INSERT INTO log VALUES (4, 1, 'LOGOFF', '189.114.71.202', 'O usuario saiu do Modulo Administrativo', '2012-05-02 15:50:38.800877', 'Home');
INSERT INTO log VALUES (5, 1, 'LOGIN', '189.27.190.95', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-05-03 08:00:39.936662', 'Home');
INSERT INTO log VALUES (6, 1, 'LOGIN', '200.143.70.37', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-05-24 14:08:33.362509', 'Home');
INSERT INTO log VALUES (7, 1, 'LOGIN', '200.143.70.37', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-05-29 09:46:04.105972', 'Home');
INSERT INTO log VALUES (8, 1, 'LOGIN', '189.27.204.108', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-06-16 15:02:39.486749', 'Home');
INSERT INTO log VALUES (9, 1, 'LOGOFF', '189.27.204.108', 'O usuario saiu do Modulo Administrativo', '2012-06-16 17:55:03.232318', 'Home');
INSERT INTO log VALUES (10, 1, 'LOGIN', '200.143.70.37', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-23 12:43:25.37511', 'Home');
INSERT INTO log VALUES (11, 1, 'LOGOFF', '200.143.70.37', 'O usuario saiu do Modulo Administrativo', '2012-08-23 13:06:57.752282', 'Home');
INSERT INTO log VALUES (12, 1, 'LOGIN', '177.18.161.254', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-26 17:49:36.525246', 'Home');
INSERT INTO log VALUES (13, 1, 'LOGOFF', '177.18.161.254', 'O usuario saiu do Modulo Administrativo', '2012-08-26 20:07:07.998506', 'Home');
INSERT INTO log VALUES (14, 1, 'LOGIN', '177.18.160.166', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-27 23:00:12.833609', 'Home');
INSERT INTO log VALUES (15, 1, 'LOGIN', '177.18.160.166', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-28 07:53:41.506738', 'Home');
INSERT INTO log VALUES (16, 1, 'LOGOFF', '177.18.160.166', 'O usuario saiu do Modulo Administrativo', '2012-08-28 07:54:27.721032', 'Home');
INSERT INTO log VALUES (17, 2, 'LOGIN', '177.18.160.166', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-28 07:54:50.210576', 'Home');
INSERT INTO log VALUES (18, 2, 'LOGIN', '177.18.160.166', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-28 08:04:06.310033', 'Home');
INSERT INTO log VALUES (19, 2, 'LOGOFF', '177.18.160.166', 'O usuario saiu do Modulo Administrativo', '2012-08-28 08:04:19.051704', 'Home');
INSERT INTO log VALUES (20, 1, 'LOGIN', '200.143.70.37', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-28 09:51:58.334136', 'Home');
INSERT INTO log VALUES (21, 1, 'LOGOFF', '200.143.70.37', 'O usuario saiu do Modulo Administrativo', '2012-08-28 10:37:33.238039', 'Home');
INSERT INTO log VALUES (22, 2, 'LOGIN', '187.36.41.195', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-28 14:21:50.115007', 'Home');
INSERT INTO log VALUES (23, 2, 'LOGOFF', '187.36.41.195', 'O usuario saiu do Modulo Administrativo', '2012-08-28 14:43:28.093798', 'Home');
INSERT INTO log VALUES (24, 2, 'LOGIN', '187.36.41.195', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-28 14:43:58.894305', 'Home');
INSERT INTO log VALUES (25, 2, 'LOGOFF', '187.36.41.195', 'O usuario saiu do Modulo Administrativo', '2012-08-28 15:05:07.916069', 'Home');
INSERT INTO log VALUES (26, 1, 'LOGIN', '200.143.70.37', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-28 15:07:54.042451', 'Home');
INSERT INTO log VALUES (27, 2, 'LOGIN', '177.18.135.19', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-28 16:36:47.072143', 'Home');
INSERT INTO log VALUES (28, 1, 'LOGIN', '177.18.135.19', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-28 21:43:10.092017', 'Home');
INSERT INTO log VALUES (29, 2, 'LOGIN', '177.18.135.19', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-28 22:38:11.349044', 'Home');
INSERT INTO log VALUES (30, 2, 'LOGIN', '177.18.135.19', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-29 09:12:17.659667', 'Home');
INSERT INTO log VALUES (31, 1, 'LOGIN', '200.143.70.37', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-29 09:21:16.993961', 'Home');
INSERT INTO log VALUES (32, 1, 'LOGOFF', '200.143.70.37', 'O usuario saiu do Modulo Administrativo', '2012-08-29 09:47:22.276764', 'Home');
INSERT INTO log VALUES (33, 2, 'LOGIN', '187.36.41.195', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-04 16:15:35.260908', 'Home');
INSERT INTO log VALUES (34, 2, 'LOGOFF', '187.36.41.195', 'O usuario saiu do Modulo Administrativo', '2012-09-04 16:22:08.108123', 'Home');
INSERT INTO log VALUES (35, 2, 'LOGIN', '187.36.41.195', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-06 14:31:36.677043', 'Home');
INSERT INTO log VALUES (36, 1, 'LOGIN', '189.114.75.66', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-10 10:32:03.510748', 'Home');
INSERT INTO log VALUES (37, 1, 'LOGIN', '189.114.85.84', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-15 19:16:49.295863', 'Home');
INSERT INTO log VALUES (38, 1, 'LOGIN', '189.114.85.84', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-15 19:25:20.996483', 'Home');
INSERT INTO log VALUES (39, 1, 'LOGIN', '189.114.85.84', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-15 19:56:52.439302', 'Home');
INSERT INTO log VALUES (40, 1, 'LOGIN', '189.114.85.84', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-15 20:08:48.372382', 'Home');
INSERT INTO log VALUES (41, 1, 'LOGIN', '189.114.85.84', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-15 20:39:51.664769', 'Home');
INSERT INTO log VALUES (42, 1, 'LOGIN', '189.114.85.84', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-15 21:20:32.679409', 'Home');
INSERT INTO log VALUES (43, 1, 'LOGOFF', '189.114.85.84', 'O usuario saiu do Modulo Administrativo', '2012-09-15 21:21:33.446499', 'Home');
INSERT INTO log VALUES (44, 1, 'LOGIN', '189.114.85.84', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-15 21:38:12.664911', 'Home');
INSERT INTO log VALUES (45, 1, 'LOGIN', '189.114.85.84', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-15 21:48:06.145589', 'Home');
INSERT INTO log VALUES (46, 1, 'LOGOFF', '189.114.85.84', 'O usuario saiu do Modulo Administrativo', '2012-09-15 21:48:56.461877', 'Home');
INSERT INTO log VALUES (47, 1, 'LOGIN', '189.114.85.84', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-16 22:20:03.738751', 'Home');
INSERT INTO log VALUES (48, 1, 'LOGIN', '189.114.75.66', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-17 09:23:50.756553', 'Home');
INSERT INTO log VALUES (49, 1, 'LOGIN', '187.115.98.237', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-17 21:10:21.867086', 'Home');
INSERT INTO log VALUES (50, 1, 'LOGIN', '177.18.128.199', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-19 22:29:46.459962', 'Home');
INSERT INTO log VALUES (51, 1, 'LOGIN', '189.114.75.66', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-21 14:35:20.310659', 'Home');
INSERT INTO log VALUES (52, 1, 'LOGOFF', '189.114.75.66', 'O usuario saiu do Modulo Administrativo', '2012-09-21 14:35:41.13039', 'Home');
INSERT INTO log VALUES (53, 2, 'LOGIN', '187.36.40.134', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-24 10:01:23.702948', 'Home');
INSERT INTO log VALUES (54, 1, 'LOGIN', '189.114.75.66', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-24 13:04:47.409087', 'Home');
INSERT INTO log VALUES (55, 1, 'LOGOFF', '189.114.75.66', 'O usuario saiu do Modulo Administrativo', '2012-09-24 13:05:05.292523', 'Home');
INSERT INTO log VALUES (56, 1, 'LOGIN', '200.175.127.107', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-24 21:35:55.943875', 'Home');
INSERT INTO log VALUES (57, 1, 'LOGOFF', '200.175.127.107', 'O usuario saiu do Modulo Administrativo', '2012-09-24 22:04:54.872763', 'Home');
INSERT INTO log VALUES (58, 2, 'LOGIN', '200.175.127.107', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-24 22:05:07.511387', 'Home');
INSERT INTO log VALUES (59, 2, 'LOGOFF', '200.175.127.107', 'O usuario saiu do Modulo Administrativo', '2012-09-24 22:17:28.025596', 'Home');
INSERT INTO log VALUES (60, 1, 'LOGIN', '189.114.75.66', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-25 10:36:52.119689', 'Home');
INSERT INTO log VALUES (61, 1, 'LOGIN', '200.175.127.196', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-25 21:09:23.802545', 'Home');
INSERT INTO log VALUES (62, 1, 'LOGIN', '200.175.127.196', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-25 21:24:54.386921', 'Home');
INSERT INTO log VALUES (63, 1, 'LOGOFF', '200.175.127.196', 'O usuario saiu do Modulo Administrativo', '2012-09-25 21:25:35.891413', 'Home');
INSERT INTO log VALUES (64, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-26 09:54:47.681456', 'Home');
INSERT INTO log VALUES (65, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-26 09:55:04.685393', 'Home');
INSERT INTO log VALUES (66, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-29 10:02:27.019443', 'Home');
INSERT INTO log VALUES (67, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-29 10:03:09.604932', 'Home');
INSERT INTO log VALUES (68, 2, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-10-20 17:23:36.137372', 'Home');
INSERT INTO log VALUES (69, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-10-20 17:23:53.09006', 'Home');
INSERT INTO log VALUES (70, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-11-05 20:33:12.925072', 'Home');
INSERT INTO log VALUES (71, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-11-05 20:33:19.45144', 'Home');
INSERT INTO log VALUES (72, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-11-06 21:06:28.745322', 'Home');
INSERT INTO log VALUES (73, 1, 'LOGOFF', '127.0.0.1', 'O usuario saiu do Modulo Administrativo', '2012-11-06 23:20:44.061933', 'Home');
INSERT INTO log VALUES (74, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-11-08 08:11:56.984165', 'Home');
INSERT INTO log VALUES (75, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-11-10 08:22:28.558223', 'Home');


--
-- TOC entry 2129 (class 0 OID 26713)
-- Dependencies: 174 2140
-- Data for Name: menu; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO menu VALUES (1, 0, 'MenuBar', 'Barra de Menus', 'menubar', '2012-09-17 21:18:39.89362', '2012-09-17 21:18:39.89362', 1, 155, '#', 1, 0, 'menu', 'N', 'A', NULL, NULL);


--
-- TOC entry 2130 (class 0 OID 26724)
-- Dependencies: 176 2140
-- Data for Name: moderacao; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO moderacao VALUES (1, '2012-05-02 15:23:32.588105', 1, '<a href=''javascript: void(0)'' onclick="popup(''http://www.valeria_websiteurbo.com.br/site.fcgi/admin/editar/Pagina/1?op=moderate_on'')">Pagina</a>', 'Inserir', NULL, NULL, NULL, 'Inseriu a Pagina Empresa');


--
-- TOC entry 2131 (class 0 OID 26733)
-- Dependencies: 178 2140
-- Data for Name: modulo; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO modulo VALUES (6, 'Enquetes', 'Enquete', 'enquetes', 'S', 'A', 'N', 'A', NULL, 'N');
INSERT INTO modulo VALUES (5, 'Avisos', 'Aviso', 'avisos', 'S', 'A', 'N', 'A', NULL, 'N');
INSERT INTO modulo VALUES (4, 'Páginas', 'Pagina', 'paginas', 'S', 'AO', 'N', 'A', NULL, 'N');
INSERT INTO modulo VALUES (3, 'Menus', 'Menu', 'menus', 'S', 'A', 'N', 'A', NULL, 'N');
INSERT INTO modulo VALUES (2, 'Templates', 'Template', 'templates', 'S', 'A', 'N', 'A', NULL, 'N');
INSERT INTO modulo VALUES (1, 'Usuários', 'Usuario', 'usuarios', 'S', 'A', 'N', 'A', NULL, 'N');
INSERT INTO modulo VALUES (8, 'Publicações', 'Publicacao', 'publicacoes', 'S', 'A', 'N', 'A', NULL, 'N');
INSERT INTO modulo VALUES (9, 'Documentos', 'Documento', 'documentos', 'S', 'A', 'N', 'A', NULL, 'N');
INSERT INTO modulo VALUES (10, 'Galerias', 'Galeria', 'galerias', 'S', 'A', 'N', 'A', NULL, 'N');
INSERT INTO modulo VALUES (11, 'Parâmetros', 'Parametro', 'parametros', 'S', 'A', 'N', 'A', NULL, 'N');
INSERT INTO modulo VALUES (12, 'Moderação', 'Moderacao', 'moderacao', 'S', 'AM', 'N', 'A', NULL, 'N');
INSERT INTO modulo VALUES (7, 'Banners', 'Banner', 'banners', 'S', 'AO', 'N', 'A', NULL, 'N');


--
-- TOC entry 2132 (class 0 OID 26745)
-- Dependencies: 180 2140
-- Data for Name: pagina; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO pagina VALUES (5, 'index', 'index', '2012-05-17 21:32:04.047939', '2012-09-29 10:03:50.571838', 1, '<div style="margin-bottom: 20px; text-align: center;">
<object style="width: 740px; height: 198px;" width="740" height="198" data="../../../static/images/banner.swf" type="application/x-shockwave-flash">
<param name="src" value="../../../static/images/banner.swf" />
</object>
</div>
<h1 style="text-align: center;">Principais Marcas</h1>
<p style="text-align: center;">&nbsp;<img src="../../../static/images/marcas/volkswagen_logo_thumb.jpg" alt="" /><img src="../../../static/images/marcas/gm_logo_thumb.jpg" alt="" />&nbsp; <img src="../../../static/images/marcas/ford_logo_thumb.jpg" alt="" />&nbsp;&nbsp;&nbsp;<img src="../../../static/images/marcas/agrale_thumb.jpg" alt="" />&nbsp; <img src="../../../static/images/marcas/volvo-logo_thumb.jpg" alt="" /><img src="../../../static/images/marcas/caterpillar-logo_thumb.jpg" alt="" /><img src="../../../static/images/marcas/cummins_logo_thumb.gif" alt="" /><img src="../../../static/images/marcas/Scania logo_thumb.jpg" alt="" /><img src="../../../static/images/marcas/Mercedes-Logo-12_thumb.jpg" alt="" /></p>
<h1 style="text-align: center;">Promo&ccedil;&otilde;es</h1>
<p style="text-align: center;"><span style="font-family: arial black,avant garde;"><span style="font-size: xx-large;"><strong><span style="color: #ff0000;">Remanufatura de Turbos a partir de R$405,00</span></strong></span></span></p>
<p>&nbsp;</p>
<p style="text-align: center;"><strong><span style="font-size: x-large;"><span style="color: #ff0000;">Turbo Novos<br /></span></span></strong></p>
<p style="text-align: center;"><span style="font-family: arial black,avant garde;"><strong><span style="font-size: x-large;">Aplica&ccedil;&atilde;o: OM904LA, 914C e 1215C</span></strong></span><strong><span style="font-size: large;">&nbsp;</span></strong></p>
<p style="text-align: center;"><img src="data:image/jpeg;base64,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anooAwbzwd4evz/pGkWre4Xb/KoF8CeGFtvsw0S0EQ9Fwf++s5rpaKXKh3Z5L43+EehPoN1c6TbXMN7Gm5FQvMG56bCST+Fec+EPhfqfiE3UN0ZtP8uNnt2kt3A8xWGNxbqDk+uPQ19QUUcq6Bc+Q9T8D+KvDt28N5odzJGnCzwoZY/qCo/wAPoK9P+EVtpWozlbvQ7uPUrVfNS4uN5iOCOmcANz09K9toosFxB0paKKYgooooAKKKKACiiigAooooAax564rzrW9QW/1SWRW/dp+7T6D/AOvmvR8UmK0pzUHexnUhzq1zzzw/fWtjqTT3Mu1PL2r8pb5iR6VFrV9Bf6tJcQyAxMFVCQR2/wAc16QVHek2rWntlzc1iPYvl5bnH6Lrlgukiw1A7AAV6HDLn1FTR6xomj2kiaZmWR+QPm5PbJbtXVbVo2Kahzi3t+JahJdfwOK8O6tZWTXk15cqskzbgdpwcZJIP4/pTtG1y3ttTvjcTBYJ5GkVuThs/wBR/Kuz2CjYKbqRd7rcSptWs9jjbXUNKtvE096LtBBJEcEKw+dmGR+fP41ZnuvDVxqQv5bzdMpUry2AV6cDmup2CjYKTqJu+v3/APAGoNK36HDan4ihn1a1nth+5tmLZbguT1wK0ru58O6wqS3FyEZB03FTj0PtXT7F9KNi+lHtFpZWsL2b1u9zi9b1y1ksxp2nsvlcBn5xgdgD1qczaDqmmxpJNDZyrhmwNjKcY6/jXW+WvpSeWn92j2iS0X4h7N3u2cxNf2s1pb6JYXBuXkVYnkBztQdTmumgiWGBIkGEQBVHsOKXYgPTFPqJSvsXGNtwoooqSgooooAKKKKACiiigAooooAKKKKACiiigDP1XQ9M1yKOPUrOO4WNt6bsjaenBH1qewsLXS7GKysoVht4htSNegFWaKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAP/9k=" alt="" /></p>
<p style="text-align: center;"><strong><span style="font-size: large;">Valor: R$1.360,00</span></strong></p>
<p style="text-align: center;"><strong><span style="font-size: large;">Em at&eacute; 3X sem entrada</span></strong></p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><strong><span style="font-size: x-large;">Aplica&ccedil;&atilde;o: OM352</span><span style="font-size: large;">&nbsp;</span></strong></p>
<p style="text-align: center;"><img src="data:image/jpeg;base64,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" alt="" /></p>
<p style="text-align: center;"><strong><span style="font-size: large;">Valor: R</span></strong><strong><span style="font-size: large;">$960,00</span></strong></p>
<p style="text-align: center;"><strong><span style="font-size: large;">Em at&eacute; 3X sem entrada</span></strong></p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><strong><span style="font-size: x-large;"><span style="color: #ff0000;">&nbsp;</span></span></strong></p>
<p style="text-align: center;">&nbsp;</p>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS.', 'Convites, impressos digitais, convites, cartões de visita, agenda, livros, sacolas, revistas, folders, panfletos, embalagens, calendários de mesa, caderno executivo, risque e rabisque, matériais de escritório, folhas A4, folhas A3', 'N', 'A', NULL, 'N', 'N');
INSERT INTO pagina VALUES (250, 'Folha A3', 'folha-a3', '2012-11-08 08:59:12.018294', '2012-11-08 08:59:12.018294', 1, '<h1>Folha A3</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'portifólio, produtos', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (13, 'Localização', 'localizacao', '2012-05-17 21:57:06.482103', '2012-11-08 09:53:51.295327', 1, '<h1><span>Localiza&ccedil;&atilde;o</span></h1>
<p><span class="endereco_field">Rua Augusto Severo, 652 - Bairro S&atilde;o Jo&atilde;o<br />Cep 90240-480 - Porto Alegre - RS</span> <br /> <small><a class="link_mapa" href="http://maps.google.com.br/maps?q=-30.001678,-51.188899&amp;num=1&amp;sll=-14.179186,-50.449219&amp;sspn=44.419463,47.900391&amp;ie=UTF8&amp;ll=-30.00169,-51.188908&amp;spn=0.004646,0.006931&amp;z=15&amp;source=embed" target="_blank">Exibir mapa ampliado</a></small></p>', 'Mapa de Localização', 'mapa, localização, endereço', 'N', 'A', NULL, 'N', 'N');
INSERT INTO pagina VALUES (2, 'Agradece', 'agradece', '2012-05-24 14:29:03.980429', '2012-08-28 15:02:32.761632', 2, '<h1><span>Obrigado pelo seu contato</span></h1>
<p>Obrigado pela mensagem !. Em breve estaremos entrando em contato.</p>', 'Agradecimento do contato', 'agradecimento', 'N', 'A', NULL, 'N', 'N');
INSERT INTO pagina VALUES (155, 'no-page', 'no-page', '2012-09-17 21:17:55.339057', '2012-09-17 21:17:55.339057', 1, '<p>no page.</p>', 'no-page', 'no page', 'N', 'A', NULL, 'N', 'N');
INSERT INTO pagina VALUES (12, 'Contato', 'contato', '2012-05-17 21:56:37.439523', '2012-11-05 22:11:40.492508', 1, '<h1>Contato</h1>
<form action="contato"> <fieldset> <label>Empresa/Nome</label> <input id="nome" type="text" /> <label>E-mail</label> <input id="email" type="text" /> <label>Fone</label> <input id="fone" type="text" /> <label>Mensagem</label> <textarea id="mensagem"></textarea> </fieldset> </form>', 'Formulário de Contato', 'contato, form', 'N', 'A', NULL, 'N', 'N');
INSERT INTO pagina VALUES (217, 'Portifólio', 'portifolio', '2012-11-05 21:47:20.085952', '2012-11-08 09:07:15.865751', 1, '<h1 class="portifolio">Portif&oacute;lio</h1>
<p class="portifolio">Conhe&ccedil;a o portif&oacute;lio da <strong><span style="color: #9d7098;">F&ecirc;nix Artes Gr&aacute;ficas</span></strong>:</p>
<div class="prod"><img src="../../../static/images/servicos/fotolito.png" alt="" width="173" height="110" />
<p><strong>Agenda</strong>&nbsp;</p>
<p>Matriz para impress&atilde;o de qualquer material gr&aacute;fico.</p>
<div class="prod-bottom"><a href="../../../agenda">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/img.jpg" alt="" />
<p><strong>Blocos</strong>&nbsp;</p>
<p>Lorem ipsum dolor sit amet, adipisicing elit.</p>
<div class="prod-bottom"><a href="../../../blocos">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/img.jpg" alt="" />
<p><strong>Cadernos Executivos</strong>&nbsp;</p>
<p>Lorem ipsum dolor sit amet, adipisicing elit.</p>
<div class="prod-bottom"><a href="../../../cadernos-executivos">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/img.jpg" alt="" />
<p><strong>Calend&aacute;rio de Mesa</strong>&nbsp;</p>
<p>Lorem ipsum dolor sit amet, adipisicing elit.</p>
<div class="prod-bottom"><a href="../../../calendario-de-mesa">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/img.jpg" alt="" />
<p><strong>Capa de CD</strong>&nbsp;</p>
<p>Lorem ipsum dolor sit amet, adipisicing elit.</p>
<div class="prod-bottom"><a href="../../../capa-de-cd">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/servicos/fotolito.png" alt="" width="173" height="110" />
<p><strong>Cart&atilde;o Postal</strong>&nbsp;</p>
<p>Matriz para impress&atilde;o de qualquer material gr&aacute;fico.</p>
<div class="prod-bottom"><a href="../../../cartao-postal">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/img.jpg" alt="" />
<p><strong>Cartela para Expositor</strong>&nbsp;</p>
<p>Lorem ipsum dolor sit amet, adipisicing elit.</p>
<div class="prod-bottom"><a href="../../../cartela-para-expositor">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/img.jpg" alt="" />
<p><strong>Cart&otilde;es de Visita</strong>&nbsp;</p>
<p>Lorem ipsum dolor sit amet, adipisicing elit.</p>
<div class="prod-bottom"><a href="../../../cartoes-de-visita">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/img.jpg" alt="" />
<p><strong>Cat&aacute;logos</strong>&nbsp;</p>
<p>Lorem ipsum dolor sit amet, adipisicing elit.</p>
<div class="prod-bottom"><a href="../../../catalagos">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/img.jpg" alt="" />
<p><strong>Convites</strong>&nbsp;</p>
<p>Lorem ipsum dolor sit amet, adipisicing elit.</p>
<div class="prod-bottom"><a href="../../../convites">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/servicos/fotolito.png" alt="" width="173" height="110" />
<p><strong>Embalagens</strong>&nbsp;</p>
<p>Matriz para impress&atilde;o de qualquer material gr&aacute;fico.</p>
<div class="prod-bottom"><a href="../../../embalagens">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/img.jpg" alt="" />
<p><strong>Envelopes</strong>&nbsp;</p>
<p>Lorem ipsum dolor sit amet, adipisicing elit.</p>
<div class="prod-bottom"><a href="../../../envelopes">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/img.jpg" alt="" />
<p><strong>Etiquetas/TAGs/R&oacute;tulos</strong>&nbsp;</p>
<p>Lorem ipsum dolor sit amet, adipisicing elit.</p>
<div class="prod-bottom"><a href="../../../etiquetas">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/img.jpg" alt="" />
<p><strong>Folders</strong>&nbsp;</p>
<p>Lorem ipsum dolor sit amet, adipisicing elit.</p>
<div class="prod-bottom"><a href="../../../folders">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/img.jpg" alt="" />
<p><strong>Folhas Timbradas</strong>&nbsp;</p>
<p>Lorem ipsum dolor sit amet, adipisicing elit.</p>
<div class="prod-bottom"><a href="../../../folhas-timbradas">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/servicos/fotolito.png" alt="" width="173" height="110" />
<p><strong>Im&atilde;s de Geladeira</strong>&nbsp;</p>
<p>Matriz para impress&atilde;o de qualquer material gr&aacute;fico.</p>
<div class="prod-bottom"><a href="../../../imas-de-geladeira">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/img.jpg" alt="" />
<p><strong>Livros</strong>&nbsp;</p>
<p>Lorem ipsum dolor sit amet, adipisicing elit.</p>
<div class="prod-bottom"><a href="../../../livros">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/img.jpg" alt="" />
<p><strong>Manuais</strong>&nbsp;</p>
<p>Lorem ipsum dolor sit amet, adipisicing elit.</p>
<div class="prod-bottom"><a href="../../../manuais">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/img.jpg" alt="" />
<p><strong>Notas Fiscais</strong>&nbsp;</p>
<p>Lorem ipsum dolor sit amet, adipisicing elit.</p>
<div class="prod-bottom"><a href="../../../notas-fiscais">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/img.jpg" alt="" />
<p><strong>Panfletos/Flyers</strong>&nbsp;</p>
<p>Lorem ipsum dolor sit amet, adipisicing elit.</p>
<div class="prod-bottom"><a href="../../../panfletos">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/servicos/fotolito.png" alt="" width="173" height="110" />
<p><strong>Pastas</strong>&nbsp;</p>
<p>Matriz para impress&atilde;o de qualquer material gr&aacute;fico.</p>
<div class="prod-bottom"><a href="../../../pastas">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/img.jpg" alt="" />
<p><strong>Receitu&aacute;rios</strong>&nbsp;</p>
<p>Lorem ipsum dolor sit amet, adipisicing elit.</p>
<div class="prod-bottom"><a href="../../../receituarios">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/img.jpg" alt="" />
<p><strong>Revistas</strong>&nbsp;</p>
<p>Lorem ipsum dolor sit amet, adipisicing elit.</p>
<div class="prod-bottom"><a href="../../../revistas">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/img.jpg" alt="" />
<p><strong>Risque e Rabisque</strong>&nbsp;</p>
<p>Lorem ipsum dolor sit amet, adipisicing elit.</p>
<div class="prod-bottom"><a href="../../../risque-e-rabisque">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/img.jpg" alt="" />
<p><strong>Sacolas</strong>&nbsp;</p>
<p>Lorem ipsum dolor sit amet, adipisicing elit.</p>
<div class="prod-bottom"><a href="../../../sacolas">Saiba mais</a></div>
</div>', 'Portifólio da Gráfica Fênix', 'portifólio, produtos', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (251, 'Material de Escritório', 'material-de-escritorio', '2012-11-08 09:19:37.466218', '2012-11-08 09:22:35.352899', 1, '<h1>Material de Escrit&oacute;rio</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'portifólio, produtos', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (6, 'empresa', 'empresa', '2012-05-17 21:36:18.197956', '2012-11-05 22:34:39.463834', 1, '<h1 class="empresa">A nossa empresa</h1>
<p class="empresa">Iniciamos nossas atividades no ano de 1987. Come&ccedil;amos com impress&atilde;o em SERIGRAFIA, que mantemos at&eacute; hoje para atender aos clientes.</p>
<p class="empresa">Hoje, contamos com  m&aacute;quinas de impress&atilde;o em OFF-SET, e investindo em novos equipamentos conseguido agilizar a entrega e qualidade de seus produtos e  servi&ccedil;os.</p>
<p class="empresa">Nossa empresa conta com uma equipe de profissionais gr&aacute;ficos que acompanham todos os processos, assessorando voc&ecirc;, desde a cria&ccedil;&atilde;o, desenvolvendo a sua id&eacute;ia, apresentando a pr&eacute;-impress&atilde;o, a impress&atilde;o e acabamento.</p>
<p class="empresa">O impresso que voc&ecirc; precisa, para a sua empresa n&oacute;s temos!</p>
<h2>Valores e Princ&iacute;pios</h2>
<p class="empresa">A F&ecirc;nix artes gr&aacute;ficas t&ecirc;m como valor principal a &eacute;tica:</p>
<ul class="empresa">
<li>Respeito com o cliente, fornecedores e colaboradores.</li>
<li>A simplicidade e a compet&ecirc;ncia na contrata&ccedil;&atilde;o de seus servi&ccedil;os.</li>
<li>A transpar&ecirc;ncia, responsabilidade e clareza nos contatos.</li>
<li>O aprendizado cont&iacute;nuo de cada colaborador.</li>
<li>Constante evolu&ccedil;&atilde;o e qualidade nos processos produtivos.</li>
<li>Responsabilidade e comprometimento em todos os trabalhos realizados.</li>
</ul>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'empresa, perfil, missão, filosofia', 'N', 'A', NULL, 'N', 'N');
INSERT INTO pagina VALUES (219, 'fotolito', 'fotolito', '2012-11-05 23:01:14.472007', '2012-11-05 23:47:02.62301', 1, '<h1>Fotolito</h1>
<p style="margin: 0px 0px 20px; padding: 0px; border: 0px; outline: 0px; font-family: Arial, Helvetica, sans-serif; vertical-align: baseline; color: #666666; line-height: 14px;"><span style="margin: 0px; padding: 0px; border: 0px; outline: 0px; font-style: inherit; font-family: inherit; vertical-align: baseline;"><strong><span style="margin: 0px; padding: 0px; border: 0px; outline: 0px; font-weight: inherit; font-style: inherit; font-family: inherit; vertical-align: baseline; color: #00ccff;"><span style="margin: 0px; padding: 0px; border: 0px; outline: 0px; font-weight: inherit; font-style: inherit; font-size: large; vertical-align: baseline;"><span style="color: #993366;">O que &eacute; Fotolito e para que serve?</span></span></span></strong></span></p>
<p style="margin: 0px 0px 20px; padding: 0px; border: 0px; outline: 0px; font-family: Arial, Helvetica, sans-serif; vertical-align: baseline; color: #666666; line-height: 14px;"><span style="margin: 0px; padding: 0px; border: 0px; outline: 0px; font-style: inherit; font-size: small; font-family: inherit; vertical-align: baseline;"><span style="margin: 0px; padding: 0px; border: 0px; outline: 0px; font-style: inherit; font-size: 13px; font-family: inherit; vertical-align: baseline;">Fotolito &eacute; um filme transparente que serve como matriz para impress&atilde;o de qualquer material gr&aacute;fico. Sua origem esta no processo de foto e grava&ccedil;&atilde;o. &Eacute; a m&iacute;dia intermedi&aacute;ria entre a finaliza&ccedil;&atilde;o (arte final) e o impresso, geralmente em offset. O Fotolito Digital, &eacute; um processo de transfer&ecirc;ncia das informa&ccedil;&otilde;es da arte final editada eletronicamente, com a utiliza&ccedil;&atilde;o de modernos recursos de computa&ccedil;&atilde;o gr&aacute;fica, para o suporte</span>&nbsp;do filme transparente. Esta transfer&ecirc;ncia de informa&ccedil;&otilde;es no modo digital tem a precis&atilde;o e a qualidade de ferramentas com a proje&ccedil;&atilde;o de lazer sobre um filme ultra-sens&iacute;vel. Esse processo &eacute; utilizado principalmente para a sele&ccedil;&atilde;o de cores em impress&otilde;es com policromia.</span></p>
<p style="margin: 0px 0px 20px; padding: 0px; border: 0px; outline: 0px; font-family: Arial, Helvetica, sans-serif; vertical-align: baseline; color: #666666; line-height: 14px;"><span style="margin: 0px; padding: 0px; border: 0px; outline: 0px; font-style: inherit; font-size: small; font-family: inherit; vertical-align: baseline;">Atualmente os processos mais modernos de impress&atilde;o offset substituem o fotolito pelo processo do CTP (Computer To Plate) eliminando a cria&ccedil;&atilde;o do fotolito e gravando a lazer a chapa de impress&atilde;o diretamente do computador.</span></p>
<p style="margin: 0px 0px 20px; padding: 0px; border: 0px; outline: 0px; font-family: Arial, Helvetica, sans-serif; vertical-align: baseline; color: #666666; line-height: 14px;"><span style="margin: 0px; padding: 0px; border: 0px; outline: 0px; font-style: inherit; font-size: small; font-family: inherit; vertical-align: baseline;">A F&ecirc;nix Artes Gr&aacute;ficas utiliza o que existe de mais moderno nos seus processos de grava&ccedil;&atilde;o de chapa. Com o CTP nossos impressos e embalagens ganham uma maior defini&ccedil;&atilde;o por cm&sup2; alem de proporcionar uma economia sobre o material produzido que &eacute; transferida diretamente ao cliente atrav&eacute;s de pre&ccedil;os mais competitivos.</span></p>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'fotolito', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (222, 'Impressão OffSet', 'impressao-offset', '2012-11-06 22:28:41.068017', '2012-11-06 22:30:38.941574', 1, '<h1>Impress&atilde;o OffSet</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'impressão offset', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (220, 'Gravação de Chapa', 'gravacao-de-chapa', '2012-11-06 22:21:54.313099', '2012-11-06 22:23:18.05099', 1, '<h1>Grava&ccedil;&atilde;o de Chapa</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'gravação de chapa', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (221, 'Impressão Digital', 'impressao-digital', '2012-11-06 22:26:16.884948', '2012-11-06 22:28:11.17713', 1, '<h1>Impress&atilde;o Digital</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'impressão digital', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (4, 'Serviços', 'servicos', '2012-08-28 10:03:39.581544', '2012-11-06 22:31:30.245698', 1, '<!--    div.conteudo { background-color: red !important; } -->
<h1 class="servicos">Servi&ccedil;os</h1>
<p class="servicos">Conhe&ccedil;a os servi&ccedil;os de gr&aacute;fica que realizamos na <strong><span style="color: #9d7098;">F&ecirc;nix Artes Gr&aacute;ficas</span></strong>:</p>
<div class="prod"><img src="../../../static/images/servicos/fotolito.png" alt="" width="173" height="110" />
<p><strong>Fotolito</strong>&nbsp;</p>
<p>Matriz para impress&atilde;o de qualquer material gr&aacute;fico.</p>
<div class="prod-bottom"><a href="../../../fotolito">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/img.jpg" alt="" />
<p><strong>Grava&ccedil;&atilde;o de chapa</strong>&nbsp;</p>
<p>Lorem ipsum dolor sit amet, adipisicing elit.</p>
<div class="prod-bottom"><a href="../../../gravacao-de-chapa">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/img.jpg" alt="" />
<p><strong>Impress&atilde;o &nbsp;digital</strong>&nbsp;</p>
<p>Lorem ipsum dolor sit amet, adipisicing elit.</p>
<div class="prod-bottom"><a href="../../../impressao-digital">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/img.jpg" alt="" />
<p><strong>Impress&atilde;o Offset</strong>&nbsp;</p>
<p>Lorem ipsum dolor sit amet, adipisicing elit.</p>
<div class="prod-bottom"><a href="../../../impressao-offset">Saiba mais</a></div>
</div>
<div class="prod"><img src="../../../static/images/img.jpg" alt="" />
<p><strong>Acabamento</strong>&nbsp;</p>
<p>Lorem ipsum dolor sit amet, adipisicing elit.</p>
<div class="prod-bottom"><a href="../../../acabamento">Saiba mais</a></div>
</div>', 'Serviços da Rede SOS Turbo', 'serviços', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (223, 'Acabamento', 'acabamento', '2012-11-06 22:31:02.352509', '2012-11-06 22:33:42.34273', 1, '<h1>Acabamento</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'acabamento', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (224, 'Agenda', 'agenda', '2012-11-06 22:34:12.21178', '2012-11-06 22:34:12.21178', 1, '<h1>Agenda</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'agenda', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (225, 'Blocos', 'blocos', '2012-11-06 22:36:04.354139', '2012-11-06 22:36:04.354139', 1, '<h1>Blocos</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'blocs', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (235, 'Envelopes', 'envelopes', '2012-11-08 08:34:03.420146', '2012-11-08 08:34:03.420146', 1, '<h1>Envelopes</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'portifólio, produtos', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (228, 'Capa de CD', 'capa-de-cd', '2012-11-08 08:12:47.527618', '2012-11-08 08:18:19.995616', 1, '<h1>Capa de CD</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'capa de cd', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (226, 'Cadernos Executivos', 'cadernos-executivos', '2012-11-06 22:38:57.605733', '2012-11-06 23:13:31.524985', 1, '<p><span>Voc&ecirc; est&aacute; em:</span> <a href="../../../portifolio">Portif&oacute;lio</a> -&gt; <a href="../../../cadernos-executivos">Cadernos Executivos</a></p>
<h1>Cadernos Executivos</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'cadernos executivos', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (236, 'Etiquetas', 'etiquetas', '2012-11-08 08:36:06.49905', '2012-11-08 08:36:06.49905', 1, '<h1>Etiquetas</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'portifólio, produtos', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (227, 'Calendário de Mesa', 'calendario-de-mesa', '2012-11-06 23:14:03.250031', '2012-11-06 23:16:15.957731', 1, '<h1>Calend&aacute;rio de Mesa</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'calendário de mesa', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (229, 'Cartão Postal', 'cartao-postal', '2012-11-08 08:18:53.428865', '2012-11-08 08:19:07.528816', 1, '<h1>Cart&atilde;o Postal</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'portifólio, produtos', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (230, 'Cartela para Expositor', 'cartela-para-expositor', '2012-11-08 08:24:33.808976', '2012-11-08 08:25:18.121014', 1, '<h1>Cartela para Expositor</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'portifólio, produtos', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (237, 'Folders', 'folders', '2012-11-08 08:36:59.598585', '2012-11-08 08:36:59.598585', 1, '<h1>Folders</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'portifólio, produtos', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (231, 'Cartões de Visita', 'cartoes-de-visita', '2012-11-08 08:27:38.434252', '2012-11-08 08:28:42.804071', 1, '<h1>Cart&otilde;es de Visita</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'portifólio, produtos', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (232, 'Catálogos', 'catalogos', '2012-11-08 08:29:23.851029', '2012-11-08 08:29:23.851029', 1, '<h1>Cat&aacute;logos</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'portifólio, produtos', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (233, 'Convites', 'convites', '2012-11-08 08:32:21.040406', '2012-11-08 08:32:21.040406', 1, '<h1>Convites</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'portifólio, produtos', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (234, 'Embalagens', 'embalagens', '2012-11-08 08:33:09.571944', '2012-11-08 08:33:09.571944', 1, '<h1>Embalagens</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'portifólio, produtos', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (238, 'Folhas Timbradas', 'folhas-timbradas', '2012-11-08 08:37:53.320783', '2012-11-08 08:37:53.320783', 1, '<h1>Folhas Timbradas</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'portifólio, produtos', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (239, 'Imãs de Geladeira', 'imas-de-geladeira', '2012-11-08 08:38:52.022699', '2012-11-08 08:39:24.552484', 1, '<h1>Im&atilde;s de Geladeira</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'portifólio, produtos', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (240, 'Livros', 'livros', '2012-11-08 08:41:04.813109', '2012-11-08 08:41:04.813109', 1, '<h1>Livros</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'portifólio, produtos', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (241, 'Manuais', 'manuais', '2012-11-08 08:42:52.392335', '2012-11-08 08:42:52.392335', 1, '<h1>Manuais</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'portifólio, produtos', 'N', 'A', NULL, 'S', 'S');
INSERT INTO pagina VALUES (242, 'Notas Fiscais', 'notas-fiscais', '2012-11-08 08:44:03.978082', '2012-11-08 08:44:03.978082', 1, '<h1>Notas Fiscais</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'portifólio, produtos', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (243, 'Panfletos', 'panfletos', '2012-11-08 08:46:08.039178', '2012-11-08 08:46:08.039178', 1, '<h1>Panfletos</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'portifólio, produtos', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (244, 'Pastas', 'pastas', '2012-11-08 08:46:58.428695', '2012-11-08 08:46:58.428695', 1, '<h1>Pastas</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'portifólio, produtos', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (245, 'Receituários', 'receituarios', '2012-11-08 08:47:44.678656', '2012-11-08 08:47:44.678656', 1, '<h1>Receitu&aacute;rios</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'portifólio, produtos', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (246, 'Revistas', 'revistas', '2012-11-08 08:48:44.757392', '2012-11-08 08:48:44.757392', 1, '<h1>Revistas</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'portifólio, produtos', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (247, 'Risque e Rabisque', 'risque-e-rabisque', '2012-11-08 08:49:33.478268', '2012-11-08 08:50:28.485695', 1, '<h1>Risque e Rabisque</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'portifólio, produtos', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (248, 'Sacolas', 'sacolas', '2012-11-08 08:51:39.236378', '2012-11-08 08:51:39.236378', 1, '<h1>Sacolas</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'portifólio, produtos', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (249, 'Folha A4', 'folha-a4', '2012-11-08 08:57:50.435587', '2012-11-08 08:57:50.435587', 1, '<h1>Folha A4</h1>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'portifólio, produtos', 'N', 'A', NULL, 'S', 'N');
INSERT INTO pagina VALUES (218, 'Orçamento', 'orcamento', '2012-11-05 22:43:30.946802', '2012-11-11 10:09:07.958401', 1, '<h1>Or&ccedil;amento</h1>
<p class="orcamento">Fa&ccedil;a sua solicita&ccedil;&atilde;o de or&ccedil;amento e entraremos em contato com voc&ecirc;:</p>
<form action="#" method="POST"> <fieldset class="orcamento"> <legend class="orcamento">Dados Gerais</legend> <label class="orcamento">Empresa/Nome:</label> <input id="nome" class="orcamento" size="70" type="text" /> <label class="orcamento">CNPJ/CPF:</label> <input id="cpf" class="orcamento" size="30" type="text" /> <br /> <label class="orcamento">Fone:</label> <input id="fone" class="orcamento" size="20" type="text" /> <br /> <label class="orcamento">E-mail:</label> <input id="e-mail" class="orcamento" size="70" type="text" /> </fieldset> <fieldset class="orcamento"> <legend class="orcamento">Dados Produto</legend> <label class="orcamento">Produto:</label> <select class="orcamento"> <option>[Selecione]</option> <option value="Agenda">Agenda</option> <option value="Blocos">Blocos</option> <option value="Cadernos Executivos">Cadernos Executivos</option> <option value="Calend&aacute;rio de Mesa">Calend&aacute;rio de Mesa</option> <option value="Capa de CD">Capa de CD</option> <option value="Cart&atilde;o Postal">Cart&atilde;o Postal</option> <option value="Cartela para Expositor">Cartela para Expositor</option> <option value="Cart&otilde;es de Visita">Cart&otilde;es de Visita</option> <option value="Cat&aacute;logos">Cat&aacute;logos</option> <option value="Convites">Convites</option> <option value="Embalagens">Embalagens</option> <option value="Envelopes">Envelopes</option> <option value="Etiquetas">Etiquetas/TAGs/R&oacute;tulos</option> <option value="Folders">Folders</option> <option value="Folhas Timbradas">Folhas Timbradas</option> <option value="Im&atilde;s de Geladeira">Im&atilde;s de Geladeira</option> <option value="Livros">Livros</option> <option value="Manuais">Manuais</option> <option value="Notas Fiscais">Notas Fiscais</option> <option value="Panfletos/Flyers">Panfletos/Flyers</option> <option value="Pastas">Pastas</option> <option value="Receitu&aacute;rios">Receitu&aacute;rios</option> <option value="Revistas">Revistas</option> <option value="Risque e Rabisque">Risque e Rabisque</option> <option value="Sacolas">Sacolas</option> <option value="Folhas A4">Folhas A4</option> <option value="Folhas A3">Folhas A3</option> <option value="Fotolito">Fotolito</option> <option value="Grava&ccedil;&atilde;o de Chapa">Grava&ccedil;&atilde;o de Chapa</option> <option value="Impress&atilde;o Digital">Impress&atilde;o Digital</option> <option value="Impress&atilde;o Offset">Impress&atilde;o Offset</option> <option value="Acabamento">Acabamento</option> <option>[Outro]</option> </select>&nbsp;&nbsp;<input id="outro_produto" class="orcamento" size="20" type="text" /> <br /> <label class="orcamento">Formato (em cm):</label>&nbsp; <span style="font-size: small;">Aberto</span>: <input id="formato_aberto" class="orcamento" size="15" type="text" />&nbsp; &nbsp;&nbsp;<span style="font-size: small;">Fechado</span>: <input id="formato_fechado" class="orcamento" size="15" type="text" /><label class="orcamento">Quantidade:</label> <input id="quantidade" class="orcamento" size="10" type="text" /> <label class="orcamento">Tipo de Papel:</label> <input id="tipo_papel" class="orcamento" size="15" type="text" /> <label class="orcamento">Cores:</label> <input id="cores" class="orcamento" size="20" type="text" /> <label class="orcamento">Gramatura:</label> <select class="orcamento"> <option>[Selecione]</option> <option>56</option> <option>63</option> <option>75</option> <option>90</option> <option>120</option> <option>150</option> <option>180</option> <option>230</option> <option>300</option> </select> </fieldset> <fieldset class="orcamento_destaque"> <legend class="orcamento">Revista/Livros/Cat&aacute;logos/Manuais</legend>
<h4>&nbsp; Dados da Capa</h4>
<label class="orcamento">Capa:</label> <input id="capa" class="orcamento" size="10" type="text" /> <label class="orcamento">Formato:</label> <input id="formato_capa" class="orcamento" size="10" type="text" /> <label class="orcamento">Papel:</label> <input id="papel_capa" class="orcamento" size="10" type="text" /> <label class="orcamento">Gramatura:</label> <select class="orcamento"> <option>[Selecione]</option> <option>56</option> <option>63</option> <option>75</option> <option>90</option> <option>120</option> <option>150</option> <option>180</option> <option>230</option> <option>300</option> </select> <label class="orcamento">Cores:</label> <input id="cores_capa" class="orcamento" size="10" type="text" /> <label class="orcamento">Orelha:</label> <input id="orelha_capa" class="orcamento" size="10" type="text" />
<h4>&nbsp; Dados do Miolo</h4>
<label class="orcamento">Miolo:</label> <input id="miolo" class="orcamento" size="10" type="text" /> <label class="orcamento">Formato:</label> <input id="formato_miolo" class="orcamento" size="10" type="text" /> <label class="orcamento">Papel:</label> <input id="papel_miolo" class="orcamento" size="10" type="text" /> <label class="orcamento">Gramatura:</label> <select class="orcamento"> <option>[Selecione]</option> <option>56</option> <option>63</option> <option>75</option> <option>90</option> <option>120</option> <option>150</option> <option>180</option> <option>230</option> <option>300</option> </select> <label class="orcamento">Cores:</label> <input id="cores_miolo" class="orcamento" size="10" type="text" /> <label class="orcamento">Qtde de P&aacute;ginas:</label> <input id="quantidade_pagina_miolo" class="orcamento" size="10" type="text" /> </fieldset> <fieldset class="orcamento"> <legend class="orcamento">Acabamento</legend> 
<table class="orcamento" border="0">
<tbody>
<tr>
<td><input class="orcamento" type="checkbox" /> Plastifica&ccedil;&atilde;o Fosca</td>
<td><input type="checkbox" /> Numera&ccedil;&atilde;o</td>
</tr>
<tr>
<td><input class="orcamento" type="checkbox" /> Plastifica&ccedil;&atilde;o Brilho</td>
<td><input type="checkbox" /> Colagem de Capas</td>
</tr>
<tr>
<td><input type="checkbox" /> Plastifica&ccedil;&atilde;o Bopp Fosca</td>
<td class="orcamento"><input type="checkbox" /> Dobras N&ordm; <input class="orcamento" size="5" type="text" /></td>
</tr>
<tr>
<td><input type="checkbox" /> Plastifica&ccedil;&atilde;o Bopp Brilho</td>
<td><input type="checkbox" /> Encaderna&ccedil;&atilde;o</td>
</tr>
<tr>
<td><input type="checkbox" /> Verniz UV Localizado</td>
<td><input type="checkbox" /> Wiro</td>
</tr>
<tr>
<td><input type="checkbox" /> Verniz Total</td>
<td><input type="checkbox" /> Aspiral</td>
</tr>
<tr>
<td>&nbsp;</td>
<td><input type="checkbox" /> Hot Melt</td>
</tr>
</tbody>
</table>
</fieldset> <fieldset class="orcamento_center"> <legend class="orcamento">Arte e Prova Digital</legend> <input type="checkbox" /> Com Arte &nbsp;&nbsp;<select class="orcamento"> <option>[Selecione]</option> <option>Word</option> <option>Corel Draw</option> <option>Ilustrator</option> <option>Indesign</option> <option>PDF</option> <option>Outros</option> </select>&nbsp;&nbsp;<input size="25" type="text" />&nbsp;&nbsp; <input type="checkbox" /> Sem Arte             <br /><br /> <input type="checkbox" /> Com Prova Digital &nbsp;&nbsp;<input type="checkbox" /> Sem Prova Digital </fieldset> <fieldset class="orcamento"> <legend class="orcamento">Prazos/Entrega/Pagamento</legend> <label class="orcamento">Prazo de Entrega:</label> <input id="prazo_de_entrega" class="orcamento" size="20" type="text" /> <label class="orcamento">Forma de Entrega:</label> <select class="orcamento"> <option>[Selecione]</option> <option>Retira no local</option> <option>&agrave; domic&iacute;lio</option> <option>Transportadora</option> <option>Motoboy</option> </select> <label class="orcamento">Forma de Pagto:</label> <select class="orcamento"> <option>[Selecione]</option> <option>&Agrave; Vista</option> <option>Dep&oacute;sito</option> <option>Boleto</option> <option>Cheque</option> </select> </fieldset> <fieldset class="orcamento_center"> <legend class="orcamento">Informa&ccedil;&otilde;es Complementares</legend> <textarea class="orcamento" cols="70" rows="10"></textarea> </fieldset>
<div style="margin: 0px auto; width: 100%; height: 50px; text-align: center;"><button class="orcamento">Limpar</button><button class="orcamento">Cancelar</button><button class="orcamento">Enviar</button></div>
</form>', 'Fênix Artes Gráficas - Convites, impressos e impressão digital em Canoas/RS', 'orçamento', 'N', 'A', NULL, 'S', 'N');


--
-- TOC entry 2133 (class 0 OID 26757)
-- Dependencies: 182 2140
-- Data for Name: parametro; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO parametro VALUES (1, 'REPORT TITLE', 'Rede SOS Turbo', 'N', 'A', NULL, 1);


--
-- TOC entry 2134 (class 0 OID 26768)
-- Dependencies: 184 2140
-- Data for Name: publicacao; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO publicacao VALUES (1, 'Novo Notícia', 'novo-noticia', '2012-05-02 15:30:44', 1, '2012-05-02 15:30:51', 'noticia, rede sos turbo', '<p>&nbsp;</p>
<p>&nbsp;</p>
<p><span style="font-family: Arial, Helvetica, sans; font-size: 11px; line-height: 14px; text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vel nulla eget leo rhoncus dignissim nec vel sapien. Nam fermentum augue nec justo dapibus tempor. In et magna enim, vel faucibus augue. Donec purus dolor, dignissim quis iaculis ut, sollicitudin eget sapien. Vivamus ultricies, purus ut blandit accumsan, felis eros mattis ligula, eget fermentum lacus nunc in turpis. Nullam urna odio, facilisis ac fringilla sed, mollis et velit. Etiam interdum, augue et varius rutrum, augue neque pulvinar urna, vitae malesuada justo magna eu sapien. Phasellus sodales accumsan nisl eu ultricies. Nullam quam neque, convallis vel elementum vitae, porttitor eu ligula. Nunc tincidunt aliquam lorem, ac pulvinar ipsum aliquam eu. Nullam id ullamcorper neque. In mollis consectetur commodo. Vivamus magna tellus, scelerisque et iaculis ut, facilisis ac elit.&nbsp;</span></p>', '<p><span style="font-family: Arial, Helvetica, sans; font-size: 11px; line-height: 14px; text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vel nulla eget leo rhoncus dignissim nec vel sapien. Nam fermentum augue nec justo dapibus tempor. In et magna enim, vel faucibus augue. Donec purus dolor, dignissim quis iaculis ut, sollicitudin eget sapien. Vivamus ultricies, purus ut blandit accumsan, felis eros mattis ligula, eget fermentum lacus nunc in turpis. Nullam urna odio, facilisis ac fringilla sed, mollis et velit. Etiam interdum, augue et varius rutrum, augue neque pulvinar urna, vitae malesuada justo magna eu sapien. Phasellus sodales accumsan nisl eu ultricies. Nullam quam neque, convallis vel elementum vitae, porttitor eu ligula. Nunc tincidunt aliquam lorem, ac pulvinar ipsum aliquam eu. Nullam id ullamcorper neque. In mollis consectetur commodo. Vivamus magna tellus, scelerisque et iaculis ut, facilisis ac elit.</span></p>', 'http://www.valeria_websiteurbo.com.br/static/images/icone.png', 'fotos-do-produto-xyz', 'S', 'N', 'A', NULL, 'N', 'N');


--
-- TOC entry 2135 (class 0 OID 26778)
-- Dependencies: 185 2140
-- Data for Name: publicacao_tipo_publicacao; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO publicacao_tipo_publicacao VALUES (1, 1);
INSERT INTO publicacao_tipo_publicacao VALUES (1, 2);
INSERT INTO publicacao_tipo_publicacao VALUES (1, 3);


--
-- TOC entry 2136 (class 0 OID 26783)
-- Dependencies: 187 2140
-- Data for Name: template; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO template VALUES (1, 'Default', 'default', '2012-09-17 21:07:49', 1, 'site', 'S', 'N', 'A', NULL, NULL);


--
-- TOC entry 2137 (class 0 OID 26794)
-- Dependencies: 189 2140
-- Data for Name: tipo_documento; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO tipo_documento VALUES (1, 'Manual do Produto', 'N', 'A', NULL, 1);


--
-- TOC entry 2138 (class 0 OID 26803)
-- Dependencies: 191 2140
-- Data for Name: tipo_publicacao; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO tipo_publicacao VALUES (1, 'Notícia', 'N', 'A', NULL, 1);
INSERT INTO tipo_publicacao VALUES (2, 'Eventos', 'N', 'A', NULL, 1);
INSERT INTO tipo_publicacao VALUES (3, 'Festa', 'N', 'A', NULL, 1);


--
-- TOC entry 2139 (class 0 OID 26812)
-- Dependencies: 193 2140
-- Data for Name: usuario; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO usuario VALUES (1, 'site@fenixgrafica.com.br', 'website', 1);
INSERT INTO usuario VALUES (2, 'admin@fenixgrafica.com.br', 'website', 2);


--
-- TOC entry 2044 (class 2606 OID 26821)
-- Dependencies: 162 162 2141
-- Name: aviso_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY aviso
    ADD CONSTRAINT aviso_pk PRIMARY KEY (id);


--
-- TOC entry 2046 (class 2606 OID 26823)
-- Dependencies: 162 162 2141
-- Name: aviso_titulo_uk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY aviso
    ADD CONSTRAINT aviso_titulo_uk UNIQUE (titulo);


--
-- TOC entry 2048 (class 2606 OID 26825)
-- Dependencies: 164 164 2141
-- Name: banner_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY banner
    ADD CONSTRAINT banner_pk PRIMARY KEY (id);


--
-- TOC entry 2050 (class 2606 OID 26827)
-- Dependencies: 164 164 2141
-- Name: banner_titulo_uk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY banner
    ADD CONSTRAINT banner_titulo_uk UNIQUE (titulo);


--
-- TOC entry 2052 (class 2606 OID 26829)
-- Dependencies: 166 166 2141
-- Name: documento_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY documento
    ADD CONSTRAINT documento_pk PRIMARY KEY (id);


--
-- TOC entry 2056 (class 2606 OID 26831)
-- Dependencies: 168 168 2141
-- Name: enquete_pergunta_uk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY enquete
    ADD CONSTRAINT enquete_pergunta_uk UNIQUE (pergunta);


--
-- TOC entry 2058 (class 2606 OID 26833)
-- Dependencies: 168 168 2141
-- Name: enquete_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY enquete
    ADD CONSTRAINT enquete_pk PRIMARY KEY (id);


--
-- TOC entry 2060 (class 2606 OID 26835)
-- Dependencies: 170 170 2141
-- Name: galeria_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY galeria
    ADD CONSTRAINT galeria_pk PRIMARY KEY (id);


--
-- TOC entry 2062 (class 2606 OID 26837)
-- Dependencies: 170 170 2141
-- Name: galeria_titulo_uk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY galeria
    ADD CONSTRAINT galeria_titulo_uk UNIQUE (titulo);


--
-- TOC entry 2064 (class 2606 OID 26839)
-- Dependencies: 172 172 2141
-- Name: log_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY log
    ADD CONSTRAINT log_pk PRIMARY KEY (id);


--
-- TOC entry 2066 (class 2606 OID 26841)
-- Dependencies: 174 174 2141
-- Name: menu_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY menu
    ADD CONSTRAINT menu_pk PRIMARY KEY (id);


--
-- TOC entry 2068 (class 2606 OID 26843)
-- Dependencies: 174 174 2141
-- Name: menu_slug_unique; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY menu
    ADD CONSTRAINT menu_slug_unique UNIQUE (slug);


--
-- TOC entry 2070 (class 2606 OID 26845)
-- Dependencies: 176 176 2141
-- Name: moderacao_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY moderacao
    ADD CONSTRAINT moderacao_pk PRIMARY KEY (id);


--
-- TOC entry 2072 (class 2606 OID 26847)
-- Dependencies: 178 178 2141
-- Name: modulo_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY modulo
    ADD CONSTRAINT modulo_pk PRIMARY KEY (id);


--
-- TOC entry 2074 (class 2606 OID 26849)
-- Dependencies: 178 178 2141
-- Name: modulo_titulo_uk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY modulo
    ADD CONSTRAINT modulo_titulo_uk UNIQUE (titulo);


--
-- TOC entry 2076 (class 2606 OID 26851)
-- Dependencies: 180 180 2141
-- Name: pagina_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY pagina
    ADD CONSTRAINT pagina_pk PRIMARY KEY (id);


--
-- TOC entry 2078 (class 2606 OID 26853)
-- Dependencies: 180 180 2141
-- Name: pagina_titulo_uk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY pagina
    ADD CONSTRAINT pagina_titulo_uk UNIQUE (titulo);


--
-- TOC entry 2080 (class 2606 OID 26855)
-- Dependencies: 182 182 2141
-- Name: parametro_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY parametro
    ADD CONSTRAINT parametro_pk PRIMARY KEY (id);


--
-- TOC entry 2082 (class 2606 OID 26857)
-- Dependencies: 182 182 2141
-- Name: parametro_titulo_uk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY parametro
    ADD CONSTRAINT parametro_titulo_uk UNIQUE (titulo);


--
-- TOC entry 2084 (class 2606 OID 26859)
-- Dependencies: 184 184 2141
-- Name: publicacao_id_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY publicacao
    ADD CONSTRAINT publicacao_id_pk PRIMARY KEY (id);


--
-- TOC entry 2088 (class 2606 OID 26861)
-- Dependencies: 185 185 185 2141
-- Name: publicacao_tipo_publicao_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY publicacao_tipo_publicacao
    ADD CONSTRAINT publicacao_tipo_publicao_pk PRIMARY KEY (publicacao, tipo_publicacao);


--
-- TOC entry 2054 (class 2606 OID 26863)
-- Dependencies: 166 166 2141
-- Name: publicacao_titulo_uk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY documento
    ADD CONSTRAINT publicacao_titulo_uk UNIQUE (titulo);


--
-- TOC entry 2086 (class 2606 OID 26865)
-- Dependencies: 184 184 2141
-- Name: publicacao_uk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY publicacao
    ADD CONSTRAINT publicacao_uk UNIQUE (titulo);


--
-- TOC entry 2090 (class 2606 OID 26867)
-- Dependencies: 187 187 2141
-- Name: template_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY template
    ADD CONSTRAINT template_pk PRIMARY KEY (id);


--
-- TOC entry 2092 (class 2606 OID 26869)
-- Dependencies: 187 187 2141
-- Name: template_titulo_uk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY template
    ADD CONSTRAINT template_titulo_uk UNIQUE (titulo);


--
-- TOC entry 2094 (class 2606 OID 26871)
-- Dependencies: 189 189 2141
-- Name: tipo_documento_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY tipo_documento
    ADD CONSTRAINT tipo_documento_pk PRIMARY KEY (id);


--
-- TOC entry 2096 (class 2606 OID 26873)
-- Dependencies: 189 189 2141
-- Name: tipo_documento_uk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY tipo_documento
    ADD CONSTRAINT tipo_documento_uk UNIQUE (titulo);


--
-- TOC entry 2098 (class 2606 OID 26875)
-- Dependencies: 191 191 2141
-- Name: tipo_publicacao_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY tipo_publicacao
    ADD CONSTRAINT tipo_publicacao_pk PRIMARY KEY (id);


--
-- TOC entry 2100 (class 2606 OID 26877)
-- Dependencies: 191 191 2141
-- Name: tipo_publicacao_uk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY tipo_publicacao
    ADD CONSTRAINT tipo_publicacao_uk UNIQUE (titulo);


--
-- TOC entry 2102 (class 2606 OID 26879)
-- Dependencies: 193 193 2141
-- Name: usuario_login_uk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY usuario
    ADD CONSTRAINT usuario_login_uk UNIQUE (login);


--
-- TOC entry 2104 (class 2606 OID 26881)
-- Dependencies: 193 193 2141
-- Name: usuario_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY usuario
    ADD CONSTRAINT usuario_pk PRIMARY KEY (id);


--
-- TOC entry 2105 (class 2606 OID 28598)
-- Dependencies: 162 176 2069 2141
-- Name: aviso_moderate_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY aviso
    ADD CONSTRAINT aviso_moderate_fk FOREIGN KEY (moderate_id) REFERENCES moderacao(id);


--
-- TOC entry 2106 (class 2606 OID 28603)
-- Dependencies: 176 2069 164 2141
-- Name: banner_moderate_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY banner
    ADD CONSTRAINT banner_moderate_fk FOREIGN KEY (moderate_id) REFERENCES moderacao(id);


--
-- TOC entry 2107 (class 2606 OID 28608)
-- Dependencies: 166 176 2069 2141
-- Name: documento_moderate_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY documento
    ADD CONSTRAINT documento_moderate_fk FOREIGN KEY (moderate_id) REFERENCES moderacao(id);


--
-- TOC entry 2108 (class 2606 OID 28613)
-- Dependencies: 166 2093 189 2141
-- Name: documento_tipo_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY documento
    ADD CONSTRAINT documento_tipo_fk FOREIGN KEY (tipo) REFERENCES tipo_documento(id);


--
-- TOC entry 2109 (class 2606 OID 28618)
-- Dependencies: 176 2069 168 2141
-- Name: enquete_moderate_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY enquete
    ADD CONSTRAINT enquete_moderate_fk FOREIGN KEY (moderate_id) REFERENCES moderacao(id);


--
-- TOC entry 2110 (class 2606 OID 28623)
-- Dependencies: 2069 176 170 2141
-- Name: galeria_moderate_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY galeria
    ADD CONSTRAINT galeria_moderate_fk FOREIGN KEY (moderate_id) REFERENCES moderacao(id);


--
-- TOC entry 2111 (class 2606 OID 28628)
-- Dependencies: 176 2069 174 2141
-- Name: menu_moderate_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY menu
    ADD CONSTRAINT menu_moderate_fk FOREIGN KEY (moderate_id) REFERENCES moderacao(id);


--
-- TOC entry 2112 (class 2606 OID 28633)
-- Dependencies: 174 2075 180 2141
-- Name: menu_pagina_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY menu
    ADD CONSTRAINT menu_pagina_fk FOREIGN KEY (pagina) REFERENCES pagina(id);


--
-- TOC entry 2113 (class 2606 OID 28638)
-- Dependencies: 193 174 2103 2141
-- Name: menu_usuario_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY menu
    ADD CONSTRAINT menu_usuario_fk FOREIGN KEY (autor) REFERENCES usuario(id);


--
-- TOC entry 2114 (class 2606 OID 28643)
-- Dependencies: 176 2069 178 2141
-- Name: modulo_moderate_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY modulo
    ADD CONSTRAINT modulo_moderate_fk FOREIGN KEY (moderate_id) REFERENCES moderacao(id);


--
-- TOC entry 2115 (class 2606 OID 28648)
-- Dependencies: 2069 180 176 2141
-- Name: pagina_moderate_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY pagina
    ADD CONSTRAINT pagina_moderate_fk FOREIGN KEY (moderate_id) REFERENCES moderacao(id);


--
-- TOC entry 2116 (class 2606 OID 28653)
-- Dependencies: 176 182 2069 2141
-- Name: parametro_moderate_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY parametro
    ADD CONSTRAINT parametro_moderate_fk FOREIGN KEY (moderate_id) REFERENCES moderacao(id);


--
-- TOC entry 2117 (class 2606 OID 28658)
-- Dependencies: 176 2069 184 2141
-- Name: publicacao_moderate_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY publicacao
    ADD CONSTRAINT publicacao_moderate_fk FOREIGN KEY (moderate_id) REFERENCES moderacao(id);


--
-- TOC entry 2118 (class 2606 OID 28663)
-- Dependencies: 185 184 2083 2141
-- Name: publicacao_tipo_publicacao_publicacao_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY publicacao_tipo_publicacao
    ADD CONSTRAINT publicacao_tipo_publicacao_publicacao_fk FOREIGN KEY (publicacao) REFERENCES publicacao(id);


--
-- TOC entry 2119 (class 2606 OID 28668)
-- Dependencies: 2097 185 191 2141
-- Name: publicacao_tipo_publicacao_tipo_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY publicacao_tipo_publicacao
    ADD CONSTRAINT publicacao_tipo_publicacao_tipo_fk FOREIGN KEY (tipo_publicacao) REFERENCES tipo_publicacao(id);


--
-- TOC entry 2120 (class 2606 OID 28673)
-- Dependencies: 2069 187 176 2141
-- Name: template_moderate_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY template
    ADD CONSTRAINT template_moderate_fk FOREIGN KEY (moderate_id) REFERENCES moderacao(id);


--
-- TOC entry 2121 (class 2606 OID 28678)
-- Dependencies: 176 189 2069 2141
-- Name: tipo_documento_moderate_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tipo_documento
    ADD CONSTRAINT tipo_documento_moderate_fk FOREIGN KEY (moderate_id) REFERENCES moderacao(id);


--
-- TOC entry 2122 (class 2606 OID 28683)
-- Dependencies: 176 191 2069 2141
-- Name: tipo_publicacao_moderate_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY tipo_publicacao
    ADD CONSTRAINT tipo_publicacao_moderate_fk FOREIGN KEY (moderate_id) REFERENCES moderacao(id);


-- Completed on 2012-11-13 08:57:24 BRST

--
-- PostgreSQL database dump complete
--

