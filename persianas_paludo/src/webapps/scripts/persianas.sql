--
-- PostgreSQL database dump
--

-- Dumped from database version 9.1.6
-- Dumped by pg_dump version 9.1.6
-- Started on 2012-11-13 09:01:57 BRST

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 1957 (class 1262 OID 17114)
-- Name: persiana_paludo; Type: DATABASE; Schema: -; Owner: -
--

CREATE DATABASE persiana_paludo WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';


\connect persiana_paludo

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 171 (class 3079 OID 11680)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 1959 (class 0 OID 0)
-- Dependencies: 171
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 162 (class 1259 OID 17117)
-- Dependencies: 5
-- Name: website_log; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE website_log (
    id integer NOT NULL,
    usuario integer,
    operacao character varying(50) NOT NULL,
    endereco_ip character varying(50),
    log text NOT NULL,
    data timestamp without time zone NOT NULL,
    menu character varying(150)
);


--
-- TOC entry 161 (class 1259 OID 17115)
-- Dependencies: 162 5
-- Name: website_log_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE website_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 1960 (class 0 OID 0)
-- Dependencies: 161
-- Name: website_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE website_log_id_seq OWNED BY website_log.id;


--
-- TOC entry 1961 (class 0 OID 0)
-- Dependencies: 161
-- Name: website_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('website_log_id_seq', 10, true);


--
-- TOC entry 164 (class 1259 OID 17126)
-- Dependencies: 1918 1919 5
-- Name: website_pagina; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE website_pagina (
    id integer NOT NULL,
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


--
-- TOC entry 163 (class 1259 OID 17124)
-- Dependencies: 5 164
-- Name: website_pagina_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE website_pagina_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 1962 (class 0 OID 0)
-- Dependencies: 163
-- Name: website_pagina_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE website_pagina_id_seq OWNED BY website_pagina.id;


--
-- TOC entry 1963 (class 0 OID 0)
-- Dependencies: 163
-- Name: website_pagina_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('website_pagina_id_seq', 3, true);


--
-- TOC entry 166 (class 1259 OID 17137)
-- Dependencies: 1921 1922 5
-- Name: website_produto; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE website_produto (
    id integer NOT NULL,
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


--
-- TOC entry 165 (class 1259 OID 17135)
-- Dependencies: 5 166
-- Name: website_produto_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE website_produto_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 1964 (class 0 OID 0)
-- Dependencies: 165
-- Name: website_produto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE website_produto_id_seq OWNED BY website_produto.id;


--
-- TOC entry 1965 (class 0 OID 0)
-- Dependencies: 165
-- Name: website_produto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('website_produto_id_seq', 10, true);


--
-- TOC entry 170 (class 1259 OID 17178)
-- Dependencies: 1925 1926 5
-- Name: website_promocao; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE website_promocao (
    id integer NOT NULL,
    titulo character varying(250) NOT NULL,
    slug character varying(255) NOT NULL,
    data_criacao timestamp without time zone NOT NULL,
    ultima_alteracao timestamp without time zone NOT NULL,
    usuario_alteracao integer NOT NULL,
    conteudo text NOT NULL,
    ativo character varying(1) NOT NULL,
    locked character varying(1) DEFAULT 'N'::character varying NOT NULL,
    status character varying(1) DEFAULT 'A'::character varying NOT NULL,
    moderate_id integer
);


--
-- TOC entry 169 (class 1259 OID 17176)
-- Dependencies: 5 170
-- Name: website_promocao_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE website_promocao_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 1966 (class 0 OID 0)
-- Dependencies: 169
-- Name: website_promocao_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE website_promocao_id_seq OWNED BY website_promocao.id;


--
-- TOC entry 1967 (class 0 OID 0)
-- Dependencies: 169
-- Name: website_promocao_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('website_promocao_id_seq', 2, true);


--
-- TOC entry 168 (class 1259 OID 17148)
-- Dependencies: 5
-- Name: website_usuario; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE website_usuario (
    id integer NOT NULL,
    login character varying(255) NOT NULL,
    senha character varying(8) NOT NULL,
    nivel_acesso integer NOT NULL
);


--
-- TOC entry 167 (class 1259 OID 17146)
-- Dependencies: 168 5
-- Name: website_usuario_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE website_usuario_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 1968 (class 0 OID 0)
-- Dependencies: 167
-- Name: website_usuario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE website_usuario_id_seq OWNED BY website_usuario.id;


--
-- TOC entry 1969 (class 0 OID 0)
-- Dependencies: 167
-- Name: website_usuario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('website_usuario_id_seq', 1, true);


--
-- TOC entry 1916 (class 2604 OID 17120)
-- Dependencies: 162 161 162
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY website_log ALTER COLUMN id SET DEFAULT nextval('website_log_id_seq'::regclass);


--
-- TOC entry 1917 (class 2604 OID 17129)
-- Dependencies: 164 163 164
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY website_pagina ALTER COLUMN id SET DEFAULT nextval('website_pagina_id_seq'::regclass);


--
-- TOC entry 1920 (class 2604 OID 17140)
-- Dependencies: 166 165 166
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY website_produto ALTER COLUMN id SET DEFAULT nextval('website_produto_id_seq'::regclass);


--
-- TOC entry 1924 (class 2604 OID 17181)
-- Dependencies: 170 169 170
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY website_promocao ALTER COLUMN id SET DEFAULT nextval('website_promocao_id_seq'::regclass);


--
-- TOC entry 1923 (class 2604 OID 17151)
-- Dependencies: 167 168 168
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY website_usuario ALTER COLUMN id SET DEFAULT nextval('website_usuario_id_seq'::regclass);


--
-- TOC entry 1948 (class 0 OID 17117)
-- Dependencies: 162 1953
-- Data for Name: website_log; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO website_log VALUES (1, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-03-20 15:30:50.576812', 'Home');
INSERT INTO website_log VALUES (2, 1, 'LOGOFF', '127.0.0.1', 'O usuario saiu do Modulo Administrativo', '2012-03-20 15:30:56.949116', 'Home');
INSERT INTO website_log VALUES (3, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-03-20 15:31:29.558943', 'Home');
INSERT INTO website_log VALUES (4, 1, 'LOGOFF', '127.0.0.1', 'O usuario saiu do Modulo Administrativo', '2012-03-20 15:33:21.939778', 'Home');
INSERT INTO website_log VALUES (5, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-03-20 15:54:16.777971', 'Home');
INSERT INTO website_log VALUES (6, 1, 'LOGOFF', '127.0.0.1', 'O usuario saiu do Modulo Administrativo', '2012-03-20 15:54:21.353498', 'Home');
INSERT INTO website_log VALUES (7, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-03-20 19:09:59.959656', 'Home');
INSERT INTO website_log VALUES (8, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-03-21 10:49:51.282118', 'Home');
INSERT INTO website_log VALUES (9, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-03-21 14:48:27.842569', 'Home');
INSERT INTO website_log VALUES (10, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-03-22 13:26:52.318985', 'Home');


--
-- TOC entry 1949 (class 0 OID 17126)
-- Dependencies: 164 1953
-- Data for Name: website_pagina; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO website_pagina VALUES (1, 'Empresa', 'empresa', '2012-03-20 19:11:12.645506', '2012-03-21 15:57:57.602791', 1, '<h1 id="empresa_title"><span>Empresa</span></h1>
<p><img title="Persianas Paludo" src="../../../static/images/empresa.jpg" alt="Imagem da Empresa" /></p>
<p>Com o objetivo de satisfazer os nossos clientes, prestamos servi&ccedil;os personalizados, adequando-se &agrave;s suas necessidades, com conforto, agilidade e qualidade, podendo contar com nosso suporte sempre que necessario.</p>
<p>Tem a miss&atilde;o de se tornar refer&ecirc;ncia no segmento.</p>
<p>Dispomos de prazos flex&iacute;veis e pre&ccedil;os competitivos em toda linha de persianas e cortinas.</p>
<p>Or&ccedil;amento Gratuito, ligue e agende uma visita.</p>', 'Página apresentando as Persianas Paludo.', 'empresa, perfil da empresa', 'N', 'A', 1);
INSERT INTO website_pagina VALUES (2, 'Manutenção', 'manutencao', '2012-03-20 19:12:06.9241', '2012-03-21 17:20:05.010437', 1, '<h1 id="manutencao_title"><span>Manutencao</span></h1>
<p><img style="margin-left: 135px;" title="Manuten&ccedil;&atilde;o de cortinas e persianas na Persianas Paludo" src="../../../static/images/manutencao.jpg" alt="Imagem de Manuten&ccedil;&atilde;o." /></p>
<p>Persianas Paludo, tamb&eacute;m especializada em manuten&ccedil;&atilde;o de persianas internas, externas e cortinas.</p>
<p>Or&ccedil;amento Gratuito !.</p>', 'Página apresentando o serviço de manutenção em persianas e cortinas.', 'manutenção, conserto, reparo', 'N', 'A', 1);
INSERT INTO website_pagina VALUES (3, 'Contato', 'contato', '2012-03-20 19:13:29.177317', '2012-03-21 17:09:15.14869', 1, '<h1 id="contato_title"><span>Contato</span></h1>
<p>Preencha o formul&aacute;rio abaixo e deixe seu recado, sua critica ou sua sugest&atilde;o, OU solicite o seu OR&Ccedil;AMENTO que com certeza entraremos em contato.</p>
<div id="painel_contato"><form id="contato_form" action="/contato" method="post"> <label for="nome_contato">Nome: <input id="nome_contato" name="nome_contato" size="40" type="text" /> </label><label for="email_contato">E-mail: <input id="email_contato" name="email_contato" size="40" type="text" /></label> <label for="telefone_contato">Telefone: <input id="telefone_contato" name="telefone_contato" size="40" type="text" /></label> <label for="mensagem_contato">Mensagem: <textarea id="mensagem_contato" title="Deixe sua mensagem." cols="35" rows="10" name="mensagem_contato"></textarea></label> <input onclick="return valida_contato();" type="submit" value="Enviar" /> </form></div>', 'Formulário de Contato', 'contato, formulário', 'N', 'A', 1);


--
-- TOC entry 1950 (class 0 OID 17137)
-- Dependencies: 166 1953
-- Data for Name: website_produto; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO website_produto VALUES (1, 'Horizontal em Aluminio', 'horizontal-em-aluminio', '2012-03-21 10:50:20.175731', '2012-03-21 10:50:20.175731', 1, '<p><span style="font-family: arial; text-align: justify; text-indent: 40px; font-size: medium;">Combinam com qualquer ambiente devido &agrave; sua praticidade e variedade de cores. Os acionamentos dispon&iacute;veis s&atilde;o: standard, monocomando e motorizado. Possuem tamb&eacute;m as op&ccedil;&otilde;es entre vidros, sem fura&ccedil;&atilde;o aparente e com cabo de a&ccedil;o. Proporcionam um perfeito controle de luminosidade. Dispon&iacute;veis em l&acirc;minas 16, 25 e 50mm, coordenadas no mesmo tom das cordas, cadar&ccedil;os e perfis.</span></p>', 'persianas, horizontal em aluminio', 'HorizontalEmAluminio', 'N', 'A', 1);
INSERT INTO website_produto VALUES (2, 'Horizontal em Madeira', 'horizontal-em-madeira', '2012-03-21 10:53:16.525547', '2012-03-21 10:53:16.525547', 1, '<p>Contempor&acirc;neas, renovam o ambiente atrav&eacute;s das suas diferentes texturas e combinam o r&uacute;stico com o moderno. S&atilde;o perfeitas para todos os tipos de decora&ccedil;&otilde;es. Com seus pr&aacute;ticos e diferentes acionamentos standard, monocomando, bast&atilde;o e motorizado, proporcionam mais leveza e encanto ao ambiente. Possuem tamb&eacute;m as op&ccedil;&otilde;es fita decorativa e cabo de a&ccedil;o. Dispon&iacute;veis em l&acirc;mina 50mm.</p>', 'persianas, horizontal em madeira', 'HorizontalEmMadeira', 'N', 'A', 1);
INSERT INTO website_produto VALUES (3, 'Vertical em Tecido', 'vertical-em-tecido', '2012-03-21 10:54:39.66766', '2012-03-21 10:54:39.66766', 1, '<p>Esse modelo atravessou o tempo atualizando-se nas suas mat&eacute;rias-primas. Inovou em texturas e cores. A persiana possibilita controle de luminosidade girando suas l&acirc;minas a 180&ordm;. Dispon&iacute;vel no acionamento standard (padr&atilde;o) e luxo com diversos opcionais que renovam o visual. Agora tamb&eacute;m na op&ccedil;&atilde;o motorizada.</p>', 'persianas, vertical em tecido', 'VerticalEmTecido', 'N', 'A', 1);
INSERT INTO website_produto VALUES (4, 'Vertical em PVC', 'vertical-em-pvc', '2012-03-21 10:58:50.994141', '2012-03-21 10:58:50.994141', 1, '<p>Pr&aacute;tica por ser de f&aacute;cil conserva&ccedil;&atilde;o e dur&aacute;vel, a persiana vertical PVC se adapta a qualquer ambiente, tanto residencial quanto comercial. Permite maior controle de luz e traz texturas e cores modernas, com acionamento standard, luxo e motorizado.</p>', 'persianas, vertical em PVC', 'VerticalEmPVC', 'N', 'A', 1);
INSERT INTO website_produto VALUES (5, 'Celular', 'celular', '2012-03-21 10:59:52.263825', '2012-03-21 10:59:52.263825', 1, '<p>Proporcionam ao ambiente eleg&acirc;ncia atrav&eacute;s de suas variadas nuances, como bloqueio dos raios UV de at&eacute; 100%, conforto t&eacute;rmico e ac&uacute;stico devido &agrave; sua composi&ccedil;&atilde;o em c&eacute;lulas (parecidas com uma colmeia de abelha). Seus acionamentos se adaptam a qualquer ambiente e arquitetura. Lan&ccedil;amento exclusivo com cole&ccedil;&otilde;es para maiores v&atilde;os com largura de at&eacute; 4,40m. Esse modelo possibilita 100% de escurecimento.</p>', 'cortina, celular', 'Celular', 'N', 'A', 1);
INSERT INTO website_produto VALUES (6, 'Painel', 'painel', '2012-03-21 11:00:41.936465', '2012-03-21 11:00:41.936465', 1, '<p>Esse produto &eacute; ideal para grandes v&atilde;os e divis&atilde;o de ambientes. Permite mais praticidade e modernidade atrav&eacute;s das texturas e cores. O produto est&aacute; dispon&iacute;vel em tecidos, tela solar (com fator de prote&ccedil;&atilde;o dos raios UV de at&eacute; 97%), blackouts e fibras naturais. Possui f&aacute;cil acionamento (manual ou standard), disposto de 2 at&eacute; 5 vias (tecidos).</p>', 'cortina, painel', 'Painel', 'N', 'A', 1);
INSERT INTO website_produto VALUES (7, 'Plissada', 'plissada', '2012-03-21 11:01:32.220148', '2012-03-21 11:01:32.220148', 1, '<p>A cortina plissada proporciona ao ambiente maior suavidade e delicadeza por meio dos tecidos especiais e texturas variadas. Possui diversas op&ccedil;&otilde;es de acionamentos, al&eacute;m de grande variedade de tecidos em 25 e 38mm.</p>', 'cortina, plissada', 'Plissada', 'N', 'A', 1);
INSERT INTO website_produto VALUES (8, 'Rollo', 'rollo', '2012-03-21 11:03:10.989659', '2012-03-21 11:03:10.989659', 1, '<p>O produto &eacute; atual e pr&aacute;tico. Possibilita privacidade sem perda da ilumina&ccedil;&atilde;o e transpar&ecirc;ncia, al&eacute;m de oferecer conforto t&eacute;rmico e bloqueio dos raios UV atrav&eacute;s de tecidos blackout, transl&uacute;cidos e telas solares (screen). Seus acionamentos diferenciados s&atilde;o standard, motorizado, com mola para pequenos v&atilde;os, duplo, com suporte intermedi&aacute;rio e de liga&ccedil;&atilde;o dupla. Para gerar 100% de escurecimento do ambiente, utilizam-se guias laterais e band&ocirc;s.</p>', 'cortina, rollo', 'CortinaRollo', 'N', 'A', 1);
INSERT INTO website_produto VALUES (9, 'Rollo Double Vision', 'rollo-double-vision', '2012-03-21 11:04:31.698919', '2012-03-21 11:04:31.698919', 1, '<p>A rollo double vision permite n&iacute;veis diferentes de luminosidade atrav&eacute;s do seu mecanismo revolucion&aacute;rio e do tecido especialmente desenvolvido. Destaca-se por suas faixas horizontais compostas de diferentes tramas e sobreposi&ccedil;&otilde;es. Dispon&iacute;vel em acionamento standard e motorizado. Confere mais aconchego e classe ao ambiente.</p>', 'cortina, rollo double vision', 'DoubleVision', 'N', 'A', 1);
INSERT INTO website_produto VALUES (10, 'Romana Clássica', 'romana-classica', '2012-03-21 11:05:44.856226', '2012-03-21 11:05:44.856226', 1, '<p>Com seu design moderno e clean, as romanas permitem a utiliza&ccedil;&atilde;o da mais variada gama de texturas e cores em tecidos, fibras naturais, telas solares e blackouts. &Eacute; poss&iacute;vel obter o alinhamento perfeito dos gomos por meio de montagem padr&atilde;o. Os acionamentos podem ser standard, monocomando, easy up e motorizado.</p>', 'cortina, romana clássica', 'Romana', 'N', 'A', 1);


--
-- TOC entry 1952 (class 0 OID 17178)
-- Dependencies: 170 1953
-- Data for Name: website_promocao; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO website_promocao VALUES (1, '50 % de Desconto', '50-de-desconto', '2012-03-22 13:27:27.587848', '2012-03-22 13:27:27.587848', 1, '<p>Todos os produtos com 50 % de desconto.</p>', 'S', 'N', 'A', 1);
INSERT INTO website_promocao VALUES (2, 'Teste de promoção', 'teste-de-promocao', '2012-03-22 13:27:58.179443', '2012-03-22 13:27:58.179443', 1, '<p>Essa &eacute; uma promo&ccedil;&atilde;o de teste.</p>', 'S', 'N', 'A', 1);


--
-- TOC entry 1951 (class 0 OID 17148)
-- Dependencies: 168 1953
-- Data for Name: website_usuario; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO website_usuario VALUES (1, 'leandro@professionalit.com.br', 'master', 1);


--
-- TOC entry 1928 (class 2606 OID 17153)
-- Dependencies: 162 162 1954
-- Name: website_log_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY website_log
    ADD CONSTRAINT website_log_pk PRIMARY KEY (id);


--
-- TOC entry 1930 (class 2606 OID 17155)
-- Dependencies: 164 164 1954
-- Name: website_pagina_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY website_pagina
    ADD CONSTRAINT website_pagina_pk PRIMARY KEY (id);


--
-- TOC entry 1932 (class 2606 OID 17157)
-- Dependencies: 164 164 1954
-- Name: website_pagina_titulo_uk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY website_pagina
    ADD CONSTRAINT website_pagina_titulo_uk UNIQUE (titulo);


--
-- TOC entry 1934 (class 2606 OID 17159)
-- Dependencies: 166 166 1954
-- Name: website_produto_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY website_produto
    ADD CONSTRAINT website_produto_pk PRIMARY KEY (id);


--
-- TOC entry 1936 (class 2606 OID 17161)
-- Dependencies: 166 166 1954
-- Name: website_produto_titulo_uk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY website_produto
    ADD CONSTRAINT website_produto_titulo_uk UNIQUE (titulo);


--
-- TOC entry 1942 (class 2606 OID 17188)
-- Dependencies: 170 170 1954
-- Name: website_promocao_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY website_promocao
    ADD CONSTRAINT website_promocao_pk PRIMARY KEY (id);


--
-- TOC entry 1944 (class 2606 OID 17190)
-- Dependencies: 170 170 1954
-- Name: website_promocao_titulo_uk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY website_promocao
    ADD CONSTRAINT website_promocao_titulo_uk UNIQUE (titulo);


--
-- TOC entry 1938 (class 2606 OID 17163)
-- Dependencies: 168 168 1954
-- Name: website_usuario_login_uk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY website_usuario
    ADD CONSTRAINT website_usuario_login_uk UNIQUE (login);


--
-- TOC entry 1940 (class 2606 OID 17165)
-- Dependencies: 168 168 1954
-- Name: website_usuario_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY website_usuario
    ADD CONSTRAINT website_usuario_pk PRIMARY KEY (id);


--
-- TOC entry 1945 (class 2606 OID 17166)
-- Dependencies: 168 1939 164 1954
-- Name: website_pagina_usuario_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY website_pagina
    ADD CONSTRAINT website_pagina_usuario_fk FOREIGN KEY (usuario_alteracao) REFERENCES website_usuario(id);


--
-- TOC entry 1946 (class 2606 OID 17171)
-- Dependencies: 168 166 1939 1954
-- Name: website_produto_usuario_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY website_produto
    ADD CONSTRAINT website_produto_usuario_fk FOREIGN KEY (usuario_alteracao) REFERENCES website_usuario(id);


--
-- TOC entry 1947 (class 2606 OID 17191)
-- Dependencies: 1939 170 168 1954
-- Name: website_promocao_usuario_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY website_promocao
    ADD CONSTRAINT website_promocao_usuario_fk FOREIGN KEY (usuario_alteracao) REFERENCES website_usuario(id);


-- Completed on 2012-11-13 09:01:57 BRST

--
-- PostgreSQL database dump complete
--

