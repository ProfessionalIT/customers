 CREATE OR REPLACE VIEW eventos AS 
 SELECT n.titulo, n.slug, n.intro, n.data_hora, ( SELECT usuario.login
           FROM usuario
          WHERE usuario.id = n.autor) AS autor
   FROM publicacao n
   JOIN publicacao f ON f.id = n.id AND f.status::text = 'A'::text
   JOIN publicacao_tipo_publicacao p ON p.publicacao = n.id AND p.tipo_publicacao = (( SELECT t.id
   FROM tipo_publicacao t
  WHERE t.titulo::text ~~ '%Eventos'::text));

ALTER TABLE eventos OWNER TO equine_website;

CREATE OR REPLACE VIEW artigos AS 
 SELECT n.titulo, n.slug, n.intro, n.data_hora, ( SELECT usuario.login
           FROM usuario
          WHERE usuario.id = n.autor) AS autor
   FROM publicacao n
   JOIN publicacao f ON f.id = n.id AND f.status::text = 'A'::text
   JOIN publicacao_tipo_publicacao p ON p.publicacao = n.id AND p.tipo_publicacao = (( SELECT t.id
   FROM tipo_publicacao t
  WHERE t.titulo::text ~~ '%Artigos'::text));

ALTER TABLE artigos OWNER TO equine_website;

CREATE OR REPLACE VIEW pesquisas AS 
 SELECT n.titulo, n.slug, n.intro, n.data_hora, ( SELECT usuario.login
           FROM usuario
          WHERE usuario.id = n.autor) AS autor
   FROM publicacao n
   JOIN publicacao f ON f.id = n.id AND f.status::text = 'A'::text
   JOIN publicacao_tipo_publicacao p ON p.publicacao = n.id AND p.tipo_publicacao = (( SELECT t.id
   FROM tipo_publicacao t
  WHERE t.titulo::text ~~ '%Pesquisas'::text));

ALTER TABLE pesquisas OWNER TO equine_website;