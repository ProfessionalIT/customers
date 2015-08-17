PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO "django_migrations" VALUES(1,'contenttypes','0001_initial','2015-07-26 12:31:27.675548');
INSERT INTO "django_migrations" VALUES(2,'auth','0001_initial','2015-07-26 12:31:27.975700');
INSERT INTO "django_migrations" VALUES(3,'admin','0001_initial','2015-07-26 12:31:28.253714');
INSERT INTO "django_migrations" VALUES(4,'sessions','0001_initial','2015-07-26 12:31:28.642400');
INSERT INTO "django_migrations" VALUES(5,'sites','0001_initial','2015-07-26 12:31:28.921455');
CREATE TABLE "website_calendario" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "titulo" varchar(200) NOT NULL,
    "slug" varchar(200) NOT NULL UNIQUE,
    "tipo" varchar(1) NOT NULL,
    "data_agendamento" datetime NOT NULL
);
INSERT INTO "website_calendario" VALUES(1,'Dia dos Pais','leandro-e-um-canalha','E','2015-08-09 12:41:10');
INSERT INTO "website_calendario" VALUES(2,'Independência do Brasil','independencia-do-brasil','N','2015-09-07 19:50:40');
INSERT INTO "website_calendario" VALUES(3,'Revolução Farroupilha','revolucao-farroupilha','N','2015-09-20 19:51:04');
INSERT INTO "website_calendario" VALUES(4,'Dia das Crianças','dia-das-criancas','N','2015-10-12 19:53:38');
INSERT INTO "website_calendario" VALUES(5,'Finados','finados','N','2015-11-02 09:16:03');
CREATE TABLE "website_cardapio" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "tipo" varchar(1) NOT NULL,
    "mes" varchar(2) NOT NULL,
    "ano" varchar(4) NOT NULL,
    "cardapio_file" varchar(100) NOT NULL
);
INSERT INTO "website_cardapio" VALUES(1,'1','08','2015','cardapios/250613_467146720013886_1775681694_n.jpg');
CREATE TABLE "website_galeria" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "titulo" varchar(200) NOT NULL,
    "slug" varchar(200) NOT NULL UNIQUE,
    "tipo" varchar(1) NOT NULL,
    "descricao" varchar(200) NOT NULL,
    "mes" varchar(2) NOT NULL,
    "ano" varchar(4) NOT NULL,
    "destaque" bool NOT NULL,
    "permite_comentario" bool NOT NULL
);
INSERT INTO "website_galeria" VALUES(1,'Teste de Galeria','teste-de-galeria','F','Esta a galeria de teste','08','2014',1,1);
INSERT INTO "website_galeria" VALUES(2,'Video Galeria','video-galeria','V','Galeria de Video','08','2014',1,0);
CREATE TABLE "website_galeriaresource" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "galeria_id" integer NOT NULL REFERENCES "website_galeria" ("id"),
    "url_resource" varchar(200),
    "upload_resource" varchar(100),
    "action_resource" varchar(200)
);
INSERT INTO "website_galeriaresource" VALUES(1,1,'','galerias/16080_637170036390442_5541803971739616782_n.jpg','www.maxigenios.com.br');
INSERT INTO "website_galeriaresource" VALUES(2,2,'<iframe width="100%" height="100%" src="https://www.youtube.com/embed/AJShCAPr4Zc" frameborder="0" allowfullscreen></iframe>','','');
CREATE TABLE "website_publicacao" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "titulo" varchar(200) NOT NULL,
    "slug" varchar(200) NOT NULL UNIQUE,
    "data_hora" datetime NOT NULL,
    "data_publicacao" datetime NOT NULL,
    "palavras_chaves" varchar(200) NOT NULL,
    "tipos" varchar(1) NOT NULL,
    "introducao" text NOT NULL,
    "completa" text NOT NULL,
    "miniatura_publicacao" varchar(100) NOT NULL,
    "galeria_id" integer REFERENCES "website_galeria" ("id"),
    "destaque" bool NOT NULL,
    "permite_comentario" bool NOT NULL,
    "rascunho" bool NOT NULL
);
INSERT INTO "website_publicacao" VALUES(1,'Novo site da Bambino Camponês','novo-site-da-bambino-campones','2015-07-26 12:35:57','2015-07-26 12:36:42.441934','noticia, lançamento do site','N','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vel nulla eget leo rhoncus dignissim nec vel sapien. Nam fermentum augue nec justo dapibus tempor. In et magna enim, vel faucibus augue. Donec purus dolor, dignissim quis iaculis ut, sollicitudin eget sapien. Vivamus ultricies, purus ut blandit accumsan, felis eros mattis ligula, eget fermentum lacus nunc in turpis. Nullam urna odio, facilisis ac fringilla sed, mollis et velit. Etiam interdum, augue et varius rutrum, augue neque pulvinar urna, vitae malesuada justo magna eu sapien. Phasellus sodales accumsan nisl eu ultricies. Nullam quam neque, convallis vel elementum vitae, porttitor eu ligula. Nunc tincidunt aliquam lorem, ac pulvinar ipsum aliquam eu. Nullam id ullamcorper neque. In mollis consectetur commodo. Vivamus magna tellus, scelerisque et iaculis ut, facilisis ac elit. ','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vel nulla eget leo rhoncus dignissim nec vel sapien. Nam fermentum augue nec justo dapibus tempor. In et magna enim, vel faucibus augue. Donec purus dolor, dignissim quis iaculis ut, sollicitudin eget sapien. Vivamus ultricies, purus ut blandit accumsan, felis eros mattis ligula, eget fermentum lacus nunc in turpis. Nullam urna odio, facilisis ac fringilla sed, mollis et velit. Etiam interdum, augue et varius rutrum, augue neque pulvinar urna, vitae malesuada justo magna eu sapien. Phasellus sodales accumsan nisl eu ultricies. Nullam quam neque, convallis vel elementum vitae, porttitor eu ligula. Nunc tincidunt aliquam lorem, ac pulvinar ipsum aliquam eu. Nullam id ullamcorper neque. In mollis consectetur commodo. Vivamus magna tellus, scelerisque et iaculis ut, facilisis ac elit. ','publicacao/1508553_10153289791862422_4395332534148329406_n.jpg',NULL,1,0,0);
INSERT INTO "website_publicacao" VALUES(2,'Pais Inteligentes Formam Sucessores, Não Herdeiros','pais-inteligentes-formam-sucessores','2015-08-01 18:09:48','2015-08-01 18:11:07.911536','dicas','D','Autor: Augusto Cury

Quando nos tornamos pais, assumimos o compromisso de criar um indivíduo que levará nossa herança para o mundo – não apenas a carga genética e os bens materiais, mas também, e principalmente, nossos valores e nossa cultura. Mas como saber que estamos acertando na criação de nossos filhos? A formação de sucessores é uma das áreas mais vitais da educação de mentes brilhantes. Neste livro, o conceituado psiquiatra e psicoterapeuta Augusto Cury aborda dois conceitos que dizem muito sobre a nova geração e o futuro das nações: herdeiros e sucessores.','Autor: Augusto Cury

Quando nos tornamos pais, assumimos o compromisso de criar um indivíduo que levará nossa herança para o mundo – não apenas a carga genética e os bens materiais, mas também, e principalmente, nossos valores e nossa cultura. Mas como saber que estamos acertando na criação de nossos filhos? A formação de sucessores é uma das áreas mais vitais da educação de mentes brilhantes. Neste livro, o conceituado psiquiatra e psicoterapeuta Augusto Cury aborda dois conceitos que dizem muito sobre a nova geração e o futuro das nações: herdeiros e sucessores.','publicacao/Livro.jpg',NULL,1,0,0);
INSERT INTO "website_publicacao" VALUES(3,'Dia do Brinquedo','dia-do-brinquedo','2015-08-16 18:44:57','2015-08-16 18:46:19.202399','avisos importantes','A','O dia do brinquedo é toda Segunda-Feira.','O dia do brinquedo é toda Segunda-Feira.','publicacao/bolinha.jpeg',NULL,0,0,0);
CREATE TABLE "website_menu" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "titulo" varchar(200) NOT NULL,
    "slug" varchar(200) NOT NULL UNIQUE,
    "endereco" varchar(200) NOT NULL,
    "ordem" integer NOT NULL,
    "nivel" integer NOT NULL,
    "pagina_id" integer REFERENCES "website_pagina" ("id"),
    "menu_pai_id" integer REFERENCES "website_menu" ("id"),
    "palavras_chaves" varchar(200) NOT NULL,
    "rascunho" bool NOT NULL
);
INSERT INTO "website_menu" VALUES(1,'Home','home','/',0,1,1,NULL,'pagina inicial',0);
CREATE TABLE "website_depoimento" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "conteudo" text NOT NULL,
    "autor" varchar(200) NOT NULL
);
INSERT INTO "website_depoimento" VALUES(1,'A Bambino Camponês é uma excelente escola, comprometida com a educação de minha filha e com os mesmos valores familiares que transmitimos em casa a nossa filhinha.','Leandro Severino');
CREATE TABLE "website_professor" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "nome" varchar(200) NOT NULL,
    "slug" varchar(200) NOT NULL UNIQUE
);
INSERT INTO "website_professor" VALUES(1,'Ana','ana');
CREATE TABLE "website_servico" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "titulo" varchar(200) NOT NULL,
    "slug" varchar(200) NOT NULL UNIQUE,
    "professor_id" integer NOT NULL REFERENCES "website_professor" ("id"),
    "conteudo_programatico" text NOT NULL,
    "atividades_incluidas" text NOT NULL,
    "atividades_extras" text NOT NULL,
    "rotina_diaria" text NOT NULL,
    "observacoes" text NOT NULL
);
INSERT INTO "website_servico" VALUES(1,'Berçario','bercario',1,'asdasd','asd','asd','asd','asd');
CREATE TABLE "website_materialescolar" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "ano" varchar(4) NOT NULL,
    "servico_id" integer NOT NULL REFERENCES "website_servico" ("id"),
    "miniatura" varchar(100) NOT NULL,
    "anexo_file" varchar(100) NOT NULL
);
CREATE TABLE "website_conteudodownload" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "titulo" varchar(200) NOT NULL,
    "slug" varchar(200) NOT NULL UNIQUE,
    "descricao" varchar(200) NOT NULL,
    "tipo" varchar(1) NOT NULL,
    "miniatura" varchar(100) NOT NULL,
    "conteudo_file" varchar(100) NOT NULL
);
INSERT INTO "website_conteudodownload" VALUES(1,'Agradece Informativo','agradece-informativo','Foto de Cabeçalho do site em 1200px X 300px.','2','downloads/33502.jpg','downloads/1508072_10203089182444301_7329244427232276168_n.jpg');
CREATE TABLE "website_recomendacao" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "tipo" varchar(1) NOT NULL,
    "descricao" varchar(200) NOT NULL,
    "acao_link" varchar(200),
    "miniatura" varchar(100) NOT NULL,
    "destaque" bool NOT NULL
);
INSERT INTO "website_recomendacao" VALUES(1,'1','Foto de Cabeçalho do site em 1200px X 300px.','http://www.maxigenios.com.br','imagens/37104_807810099240993_409873209248303298_n.jpg',1);
CREATE TABLE "website_parametro" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "valor" varchar(200) NOT NULL
);
CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL, UNIQUE ("app_label", "model"));
INSERT INTO "django_content_type" VALUES(1,'permission','auth','permission');
INSERT INTO "django_content_type" VALUES(2,'group','auth','group');
INSERT INTO "django_content_type" VALUES(3,'user','auth','user');
INSERT INTO "django_content_type" VALUES(4,'content type','contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES(5,'session','sessions','session');
INSERT INTO "django_content_type" VALUES(6,'site','sites','site');
INSERT INTO "django_content_type" VALUES(7,'log entry','admin','logentry');
INSERT INTO "django_content_type" VALUES(8,'calendario','website','calendario');
INSERT INTO "django_content_type" VALUES(9,'cardapio','website','cardapio');
INSERT INTO "django_content_type" VALUES(10,'galeria','website','galeria');
INSERT INTO "django_content_type" VALUES(11,'galeria resource','website','galeriaresource');
INSERT INTO "django_content_type" VALUES(12,'publicacao','website','publicacao');
INSERT INTO "django_content_type" VALUES(13,'pagina','website','pagina');
INSERT INTO "django_content_type" VALUES(14,'menu','website','menu');
INSERT INTO "django_content_type" VALUES(15,'depoimento','website','depoimento');
INSERT INTO "django_content_type" VALUES(16,'professor','website','professor');
INSERT INTO "django_content_type" VALUES(17,'servico','website','servico');
INSERT INTO "django_content_type" VALUES(18,'material escolar','website','materialescolar');
INSERT INTO "django_content_type" VALUES(19,'conteudo download','website','conteudodownload');
INSERT INTO "django_content_type" VALUES(20,'recomendacao','website','recomendacao');
INSERT INTO "django_content_type" VALUES(21,'parametro','website','parametro');
INSERT INTO "django_content_type" VALUES(22,'banner','website','banner');
CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id"), "codename" varchar(100) NOT NULL, UNIQUE ("content_type_id", "codename"));
INSERT INTO "auth_permission" VALUES(1,'Can add permission',1,'add_permission');
INSERT INTO "auth_permission" VALUES(2,'Can change permission',1,'change_permission');
INSERT INTO "auth_permission" VALUES(3,'Can delete permission',1,'delete_permission');
INSERT INTO "auth_permission" VALUES(4,'Can add group',2,'add_group');
INSERT INTO "auth_permission" VALUES(5,'Can change group',2,'change_group');
INSERT INTO "auth_permission" VALUES(6,'Can delete group',2,'delete_group');
INSERT INTO "auth_permission" VALUES(7,'Can add user',3,'add_user');
INSERT INTO "auth_permission" VALUES(8,'Can change user',3,'change_user');
INSERT INTO "auth_permission" VALUES(9,'Can delete user',3,'delete_user');
INSERT INTO "auth_permission" VALUES(10,'Can add content type',4,'add_contenttype');
INSERT INTO "auth_permission" VALUES(11,'Can change content type',4,'change_contenttype');
INSERT INTO "auth_permission" VALUES(12,'Can delete content type',4,'delete_contenttype');
INSERT INTO "auth_permission" VALUES(13,'Can add session',5,'add_session');
INSERT INTO "auth_permission" VALUES(14,'Can change session',5,'change_session');
INSERT INTO "auth_permission" VALUES(15,'Can delete session',5,'delete_session');
INSERT INTO "auth_permission" VALUES(16,'Can add site',6,'add_site');
INSERT INTO "auth_permission" VALUES(17,'Can change site',6,'change_site');
INSERT INTO "auth_permission" VALUES(18,'Can delete site',6,'delete_site');
INSERT INTO "auth_permission" VALUES(19,'Can add log entry',7,'add_logentry');
INSERT INTO "auth_permission" VALUES(20,'Can change log entry',7,'change_logentry');
INSERT INTO "auth_permission" VALUES(21,'Can delete log entry',7,'delete_logentry');
INSERT INTO "auth_permission" VALUES(22,'Can add calendario',8,'add_calendario');
INSERT INTO "auth_permission" VALUES(23,'Can change calendario',8,'change_calendario');
INSERT INTO "auth_permission" VALUES(24,'Can delete calendario',8,'delete_calendario');
INSERT INTO "auth_permission" VALUES(25,'Can add cardapio',9,'add_cardapio');
INSERT INTO "auth_permission" VALUES(26,'Can change cardapio',9,'change_cardapio');
INSERT INTO "auth_permission" VALUES(27,'Can delete cardapio',9,'delete_cardapio');
INSERT INTO "auth_permission" VALUES(28,'Can add galeria',10,'add_galeria');
INSERT INTO "auth_permission" VALUES(29,'Can change galeria',10,'change_galeria');
INSERT INTO "auth_permission" VALUES(30,'Can delete galeria',10,'delete_galeria');
INSERT INTO "auth_permission" VALUES(31,'Can add galeria resource',11,'add_galeriaresource');
INSERT INTO "auth_permission" VALUES(32,'Can change galeria resource',11,'change_galeriaresource');
INSERT INTO "auth_permission" VALUES(33,'Can delete galeria resource',11,'delete_galeriaresource');
INSERT INTO "auth_permission" VALUES(34,'Can add publicacao',12,'add_publicacao');
INSERT INTO "auth_permission" VALUES(35,'Can change publicacao',12,'change_publicacao');
INSERT INTO "auth_permission" VALUES(36,'Can delete publicacao',12,'delete_publicacao');
INSERT INTO "auth_permission" VALUES(37,'Can add pagina',13,'add_pagina');
INSERT INTO "auth_permission" VALUES(38,'Can change pagina',13,'change_pagina');
INSERT INTO "auth_permission" VALUES(39,'Can delete pagina',13,'delete_pagina');
INSERT INTO "auth_permission" VALUES(40,'Can add menu',14,'add_menu');
INSERT INTO "auth_permission" VALUES(41,'Can change menu',14,'change_menu');
INSERT INTO "auth_permission" VALUES(42,'Can delete menu',14,'delete_menu');
INSERT INTO "auth_permission" VALUES(43,'Can add depoimento',15,'add_depoimento');
INSERT INTO "auth_permission" VALUES(44,'Can change depoimento',15,'change_depoimento');
INSERT INTO "auth_permission" VALUES(45,'Can delete depoimento',15,'delete_depoimento');
INSERT INTO "auth_permission" VALUES(46,'Can add professor',16,'add_professor');
INSERT INTO "auth_permission" VALUES(47,'Can change professor',16,'change_professor');
INSERT INTO "auth_permission" VALUES(48,'Can delete professor',16,'delete_professor');
INSERT INTO "auth_permission" VALUES(49,'Can add servico',17,'add_servico');
INSERT INTO "auth_permission" VALUES(50,'Can change servico',17,'change_servico');
INSERT INTO "auth_permission" VALUES(51,'Can delete servico',17,'delete_servico');
INSERT INTO "auth_permission" VALUES(52,'Can add material escolar',18,'add_materialescolar');
INSERT INTO "auth_permission" VALUES(53,'Can change material escolar',18,'change_materialescolar');
INSERT INTO "auth_permission" VALUES(54,'Can delete material escolar',18,'delete_materialescolar');
INSERT INTO "auth_permission" VALUES(55,'Can add conteudo download',19,'add_conteudodownload');
INSERT INTO "auth_permission" VALUES(56,'Can change conteudo download',19,'change_conteudodownload');
INSERT INTO "auth_permission" VALUES(57,'Can delete conteudo download',19,'delete_conteudodownload');
INSERT INTO "auth_permission" VALUES(58,'Can add recomendacao',20,'add_recomendacao');
INSERT INTO "auth_permission" VALUES(59,'Can change recomendacao',20,'change_recomendacao');
INSERT INTO "auth_permission" VALUES(60,'Can delete recomendacao',20,'delete_recomendacao');
INSERT INTO "auth_permission" VALUES(61,'Can add parametro',21,'add_parametro');
INSERT INTO "auth_permission" VALUES(62,'Can change parametro',21,'change_parametro');
INSERT INTO "auth_permission" VALUES(63,'Can delete parametro',21,'delete_parametro');
INSERT INTO "auth_permission" VALUES(64,'Can add banner',22,'add_banner');
INSERT INTO "auth_permission" VALUES(65,'Can change banner',22,'change_banner');
INSERT INTO "auth_permission" VALUES(66,'Can delete banner',22,'delete_banner');
CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(80) NOT NULL UNIQUE);
CREATE TABLE "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id"), "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"), UNIQUE ("group_id", "permission_id"));
CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NOT NULL, "is_superuser" bool NOT NULL, "username" varchar(30) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "email" varchar(75) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL);
INSERT INTO "auth_user" VALUES(1,'pbkdf2_sha256$15000$WJ4Kl7K58tps$12n3vo1yvt3LyagOkWLiSYStx2CYuEvfrIiMUVoqZbM=','2015-08-16 17:39:57.362784',1,'admin','','','admin@admin.com.br',1,1,'2015-07-26 12:32:05.939172');
CREATE TABLE "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "group_id" integer NOT NULL REFERENCES "auth_group" ("id"), UNIQUE ("user_id", "group_id"));
CREATE TABLE "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"), UNIQUE ("user_id", "permission_id"));
CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "action_time" datetime NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL, "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id"), "user_id" integer NOT NULL REFERENCES "auth_user" ("id"));
INSERT INTO "django_admin_log" VALUES(1,'2015-07-26 12:36:42.480845','1','Publicacao object',1,'',12,1);
INSERT INTO "django_admin_log" VALUES(2,'2015-07-26 12:41:25.678010','1','Calendario object',1,'',8,1);
INSERT INTO "django_admin_log" VALUES(3,'2015-07-26 12:52:13.029557','1','Cardapio object',1,'',9,1);
INSERT INTO "django_admin_log" VALUES(4,'2015-07-26 12:52:43.142755','1','ConteudoDownload object',1,'',19,1);
INSERT INTO "django_admin_log" VALUES(5,'2015-07-26 12:52:56.567868','1','Depoimento object',1,'',15,1);
INSERT INTO "django_admin_log" VALUES(6,'2015-07-26 12:53:27.666458','1','Galeria object',1,'',10,1);
INSERT INTO "django_admin_log" VALUES(7,'2015-07-26 12:53:59.212913','1','GaleriaResource object',1,'',11,1);
INSERT INTO "django_admin_log" VALUES(8,'2015-07-26 12:55:36.118746','1','Pagina object',1,'',13,1);
INSERT INTO "django_admin_log" VALUES(9,'2015-07-26 12:55:40.876028','1','Menu object',1,'',14,1);
INSERT INTO "django_admin_log" VALUES(10,'2015-07-26 12:56:03.525879','1','Professor object',1,'',16,1);
INSERT INTO "django_admin_log" VALUES(11,'2015-07-26 12:56:18.817517','1','Publicacao object',2,'Modificado galeria.',12,1);
INSERT INTO "django_admin_log" VALUES(12,'2015-07-26 12:56:47.243759','1','Recomendacao object',1,'',20,1);
INSERT INTO "django_admin_log" VALUES(13,'2015-07-26 12:57:22.185727','1','Servico object',1,'',17,1);
INSERT INTO "django_admin_log" VALUES(14,'2015-07-26 13:33:13.538304','1','Banner object',1,'',22,1);
INSERT INTO "django_admin_log" VALUES(15,'2015-08-01 14:10:12.249221','1','Novo site da Bambino Camponês',2,'Modificado titulo, palavras_chaves, introducao, completa, galeria e destaque.',12,1);
INSERT INTO "django_admin_log" VALUES(16,'2015-08-01 14:17:19.688206','1','Novo site da Bambino Camponês',2,'Modificado miniatura_publicacao.',12,1);
INSERT INTO "django_admin_log" VALUES(17,'2015-08-01 14:41:20.678271','1','Festa da Indenpendêcia na Bambino',2,'Modificado titulo, descricao, url_resource e action_resource.',22,1);
INSERT INTO "django_admin_log" VALUES(18,'2015-08-01 14:51:51.228660','1','Festa da Indenpendêcia na Bambino',2,'Nenhum campo modificado.',22,1);
INSERT INTO "django_admin_log" VALUES(19,'2015-08-01 14:52:27.574153','2','Aviso Urgente',1,'',22,1);
INSERT INTO "django_admin_log" VALUES(20,'2015-08-01 14:53:05.166080','3','Participe da Campanha',1,'',22,1);
INSERT INTO "django_admin_log" VALUES(21,'2015-08-01 16:08:56.693839','2','Aviso Urgente',2,'Modificado ativo.',22,1);
INSERT INTO "django_admin_log" VALUES(22,'2015-08-01 16:09:00.966932','3','Participe da Campanha',2,'Nenhum campo modificado.',22,1);
INSERT INTO "django_admin_log" VALUES(23,'2015-08-01 16:09:04.474700','2','Aviso Urgente',2,'Nenhum campo modificado.',22,1);
INSERT INTO "django_admin_log" VALUES(24,'2015-08-01 16:09:09.911781','1','Festa da Indenpendêcia na Bambino',2,'Modificado ativo.',22,1);
INSERT INTO "django_admin_log" VALUES(25,'2015-08-01 18:08:26.777731','2','Video Galeria',1,'',10,1);
INSERT INTO "django_admin_log" VALUES(26,'2015-08-01 18:09:19.147951','2','GaleriaResource object',1,'',11,1);
INSERT INTO "django_admin_log" VALUES(27,'2015-08-01 18:11:07.945973','2','Dica de livor',1,'',12,1);
INSERT INTO "django_admin_log" VALUES(28,'2015-08-01 18:11:33.154634','2','Dica de livor',2,'Modificado rascunho.',12,1);
INSERT INTO "django_admin_log" VALUES(29,'2015-08-01 18:25:58.716042','2','GaleriaResource object',2,'Modificado url_resource.',11,1);
INSERT INTO "django_admin_log" VALUES(30,'2015-08-01 18:31:04.128831','1','Foto de Cabeçalho do site em 1200px X 300px.',2,'Modificado destaque.',20,1);
INSERT INTO "django_admin_log" VALUES(31,'2015-08-01 19:49:44.262786','1','Dia dos Pais',2,'Modificado titulo e data_agendamento.',8,1);
INSERT INTO "django_admin_log" VALUES(32,'2015-08-01 19:50:43.432626','2','Independência do Brasil',1,'',8,1);
INSERT INTO "django_admin_log" VALUES(33,'2015-08-01 19:51:06.766560','3','Revolução Farroupilha',1,'',8,1);
INSERT INTO "django_admin_log" VALUES(34,'2015-08-01 19:53:45.712603','3','Revolução Farroupilha',2,'Modificado tipo.',8,1);
INSERT INTO "django_admin_log" VALUES(35,'2015-08-01 19:53:52.130611','2','Independência do Brasil',2,'Modificado tipo.',8,1);
INSERT INTO "django_admin_log" VALUES(36,'2015-08-01 20:13:51.343251','4','Dia das Crianças',1,'',8,1);
INSERT INTO "django_admin_log" VALUES(37,'2015-08-01 20:18:45.288863','2','GaleriaResource object',2,'Modificado url_resource.',11,1);
INSERT INTO "django_admin_log" VALUES(38,'2015-08-01 20:31:04.549349','1','Depoimento object',2,'Modificado conteudo e autor.',15,1);
INSERT INTO "django_admin_log" VALUES(39,'2015-08-03 10:18:25.440559','2','Empresa Filosofia',1,'',13,1);
INSERT INTO "django_admin_log" VALUES(40,'2015-08-03 10:30:08.983610','2','Empresa Filosofia',2,'Modificado rascunho.',13,1);
INSERT INTO "django_admin_log" VALUES(41,'2015-08-03 10:30:30.667635','2','Empresa Filosofia',2,'Modificado rascunho.',13,1);
INSERT INTO "django_admin_log" VALUES(42,'2015-08-03 10:32:41.474068','2','Empresa Filosofia',2,'Modificado conteudo.',13,1);
INSERT INTO "django_admin_log" VALUES(43,'2015-08-03 10:47:28.433682','2','Filosofia',2,'Modificado titulo.',13,1);
INSERT INTO "django_admin_log" VALUES(44,'2015-08-03 10:47:37.576204','2','Filosofia',2,'Modificado slug.',13,1);
INSERT INTO "django_admin_log" VALUES(45,'2015-08-03 10:47:42.546877','2','Filosofia',2,'Nenhum campo modificado.',13,1);
INSERT INTO "django_admin_log" VALUES(46,'2015-08-03 10:57:32.101049','2','Filosofia',2,'Modificado descricao.',13,1);
INSERT INTO "django_admin_log" VALUES(47,'2015-08-03 10:57:36.011514','2','Filosofia',2,'Nenhum campo modificado.',13,1);
INSERT INTO "django_admin_log" VALUES(48,'2015-08-05 10:16:05.106286','5','Finados',1,'',8,1);
INSERT INTO "django_admin_log" VALUES(49,'2015-08-16 17:44:37.271722','2','Filosofia',2,'Modificado conteudo.',13,1);
INSERT INTO "django_admin_log" VALUES(50,'2015-08-16 17:53:11.346872','3','Nossa Equipe',1,'',13,1);
INSERT INTO "django_admin_log" VALUES(51,'2015-08-16 17:53:51.113272','3','Nossa Equipe',2,'Modificado conteudo.',13,1);
INSERT INTO "django_admin_log" VALUES(52,'2015-08-16 18:03:14.047384','4','Instalações',1,'',13,1);
INSERT INTO "django_admin_log" VALUES(53,'2015-08-16 18:05:09.140723','5','Nossa História',1,'',13,1);
INSERT INTO "django_admin_log" VALUES(54,'2015-08-16 18:09:38.516641','5','Nossa História',2,'Modificado conteudo.',13,1);
INSERT INTO "django_admin_log" VALUES(55,'2015-08-16 18:11:52.528227','6','Horários',1,'',13,1);
INSERT INTO "django_admin_log" VALUES(56,'2015-08-16 18:20:32.176909','7','Matrículas',1,'',13,1);
INSERT INTO "django_admin_log" VALUES(57,'2015-08-16 18:23:29.769117','8','Material Escolar',1,'',13,1);
INSERT INTO "django_admin_log" VALUES(58,'2015-08-16 18:23:51.436106','8','Material Escolar',2,'Modificado conteudo.',13,1);
INSERT INTO "django_admin_log" VALUES(59,'2015-08-16 18:24:41.511689','8','Material Escolar',2,'Modificado conteudo.',13,1);
INSERT INTO "django_admin_log" VALUES(60,'2015-08-16 18:25:47.172711','8','Material Escolar',2,'Modificado conteudo.',13,1);
INSERT INTO "django_admin_log" VALUES(61,'2015-08-16 18:29:43.849349','1','Cardapio object',2,'Modificado mes e ano.',9,1);
INSERT INTO "django_admin_log" VALUES(62,'2015-08-16 18:46:19.224496','3','Dia do Brinquedo',1,'',12,1);
INSERT INTO "django_admin_log" VALUES(63,'2015-08-16 18:56:04.446367','2','Pais Inteligentes Formam Sucessores, Não Herdeiros',2,'Modificado titulo, introducao, completa e miniatura_publicacao.',12,1);
INSERT INTO "django_admin_log" VALUES(64,'2015-08-16 18:56:58.569457','2','Pais Inteligentes Formam Sucessores, Não Herdeiros',2,'Modificado slug.',12,1);
INSERT INTO "django_admin_log" VALUES(65,'2015-08-16 18:57:27.937759','2','Pais Inteligentes Formam Sucessores, Não Herdeiros',2,'Modificado introducao e completa.',12,1);
INSERT INTO "django_admin_log" VALUES(66,'2015-08-16 18:57:36.628974','2','Pais Inteligentes Formam Sucessores, Não Herdeiros',2,'Nenhum campo modificado.',12,1);
INSERT INTO "django_admin_log" VALUES(67,'2015-08-16 19:01:57.506032','9','Proposta Pedagógica',1,'',13,1);
INSERT INTO "django_admin_log" VALUES(68,'2015-08-16 19:15:07.384558','1','Depoimento object',2,'Modificado conteudo e autor.',15,1);
INSERT INTO "django_admin_log" VALUES(69,'2015-08-16 19:17:27.911399','10','Berçario',1,'',13,1);
INSERT INTO "django_admin_log" VALUES(70,'2015-08-16 19:19:23.365062','11','Pré-Maternal',1,'',13,1);
INSERT INTO "django_admin_log" VALUES(71,'2015-08-16 19:26:00.873483','12','Maternal 1',1,'',13,1);
INSERT INTO "django_admin_log" VALUES(72,'2015-08-16 19:29:38.434008','13','Maternal 2',1,'',13,1);
INSERT INTO "django_admin_log" VALUES(73,'2015-08-16 19:31:54.851164','14','Jardim A',1,'',13,1);
INSERT INTO "django_admin_log" VALUES(74,'2015-08-16 19:33:03.147514','2','Filosofia',2,'Modificado conteudo.',13,1);
INSERT INTO "django_admin_log" VALUES(75,'2015-08-16 19:33:35.161075','2','Filosofia',2,'Modificado conteudo.',13,1);
INSERT INTO "django_admin_log" VALUES(76,'2015-08-16 19:34:55.785000','15','Jardim B',1,'',13,1);
INSERT INTO "django_admin_log" VALUES(77,'2015-08-16 19:38:17.344364','16','Atividades Extras',1,'',13,1);
INSERT INTO "django_admin_log" VALUES(78,'2015-08-16 19:40:11.945517','16','Atividades Extras',2,'Modificado conteudo.',13,1);
INSERT INTO "django_admin_log" VALUES(79,'2015-08-16 19:43:40.088624','16','Atividades Extras',2,'Modificado conteudo.',13,1);
INSERT INTO "django_admin_log" VALUES(80,'2015-08-16 19:46:18.998752','17','Músicas',1,'',13,1);
INSERT INTO "django_admin_log" VALUES(81,'2015-08-16 19:47:40.643201','18','Vídeos',1,'',13,1);
INSERT INTO "django_admin_log" VALUES(82,'2015-08-16 19:48:26.935429','19','Papeis de Parede',1,'',13,1);
INSERT INTO "django_admin_log" VALUES(83,'2015-08-16 19:49:15.610626','20','Desenhos para Pintar',1,'',13,1);
INSERT INTO "django_admin_log" VALUES(84,'2015-08-16 19:52:34.976468','21','Fale Conosco',1,'',13,1);
INSERT INTO "django_admin_log" VALUES(85,'2015-08-16 19:54:31.978119','22','Localização',1,'',13,1);
INSERT INTO "django_admin_log" VALUES(86,'2015-08-16 19:54:59.035027','22','Localização',2,'Modificado conteudo.',13,1);
INSERT INTO "django_admin_log" VALUES(87,'2015-08-16 19:55:22.786999','22','Localização',2,'Modificado conteudo.',13,1);
INSERT INTO "django_admin_log" VALUES(88,'2015-08-16 21:12:40.206076','22','Localização',2,'Nenhum campo modificado.',13,1);
INSERT INTO "django_admin_log" VALUES(89,'2015-08-16 21:14:44.374296','1','Novo site da Bambino Camponês',2,'Modificado slug.',12,1);
INSERT INTO "django_admin_log" VALUES(90,'2015-08-16 21:15:07.491742','3','Participe da Campanha',2,'Modificado action_resource.',22,1);
INSERT INTO "django_admin_log" VALUES(91,'2015-08-16 21:15:28.173305','2','Aviso Urgente',2,'Modificado action_resource.',22,1);
INSERT INTO "django_admin_log" VALUES(92,'2015-08-16 21:15:35.608723','1','Festa da Indenpendêcia na Bambino',2,'Modificado action_resource.',22,1);
INSERT INTO "django_admin_log" VALUES(93,'2015-08-16 21:30:50.202317','23','Responsabilidade Social',1,'',13,1);
CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
INSERT INTO "django_session" VALUES('yuerpeoywi62jjqu9sy2564ku8eeual6','NGY3NTBjZmU3ZTMwMzI0YzQzYTJlYjAzYWQzOTVjMGE3NDYwMGVhMjp7Il9hdXRoX3VzZXJfaGFzaCI6ImQ5NjljNzY4Nzk1NDYyNGM4Mzc5ZGIwOTlhOTJhY2UzZWJiNGVmYzUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-08-09 12:32:27.143755');
INSERT INTO "django_session" VALUES('7lwlqjgwdmbydt9s1xwqa7a1fpg9mm4z','NGY3NTBjZmU3ZTMwMzI0YzQzYTJlYjAzYWQzOTVjMGE3NDYwMGVhMjp7Il9hdXRoX3VzZXJfaGFzaCI6ImQ5NjljNzY4Nzk1NDYyNGM4Mzc5ZGIwOTlhOTJhY2UzZWJiNGVmYzUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-08-13 16:20:09.758915');
INSERT INTO "django_session" VALUES('vt28wqdqkd29reiej6q5r14w1e963f4y','NGY3NTBjZmU3ZTMwMzI0YzQzYTJlYjAzYWQzOTVjMGE3NDYwMGVhMjp7Il9hdXRoX3VzZXJfaGFzaCI6ImQ5NjljNzY4Nzk1NDYyNGM4Mzc5ZGIwOTlhOTJhY2UzZWJiNGVmYzUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-08-15 14:08:35.606280');
INSERT INTO "django_session" VALUES('o7m72ykvtsnjagcb6jadcrt0aca247n5','NGY3NTBjZmU3ZTMwMzI0YzQzYTJlYjAzYWQzOTVjMGE3NDYwMGVhMjp7Il9hdXRoX3VzZXJfaGFzaCI6ImQ5NjljNzY4Nzk1NDYyNGM4Mzc5ZGIwOTlhOTJhY2UzZWJiNGVmYzUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-08-17 10:16:53.866295');
INSERT INTO "django_session" VALUES('ehp1zh14kovzu963wy88fgn6xy27a614','NGY3NTBjZmU3ZTMwMzI0YzQzYTJlYjAzYWQzOTVjMGE3NDYwMGVhMjp7Il9hdXRoX3VzZXJfaGFzaCI6ImQ5NjljNzY4Nzk1NDYyNGM4Mzc5ZGIwOTlhOTJhY2UzZWJiNGVmYzUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-08-19 01:20:16.219757');
INSERT INTO "django_session" VALUES('x6ve1j7wvb2reoh7vykrykcbjozpwg09','NGY3NTBjZmU3ZTMwMzI0YzQzYTJlYjAzYWQzOTVjMGE3NDYwMGVhMjp7Il9hdXRoX3VzZXJfaGFzaCI6ImQ5NjljNzY4Nzk1NDYyNGM4Mzc5ZGIwOTlhOTJhY2UzZWJiNGVmYzUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-08-24 20:45:06.203641');
INSERT INTO "django_session" VALUES('xsjgxh9fa6t01nt2s2hv2pcyf692mxru','NGY3NTBjZmU3ZTMwMzI0YzQzYTJlYjAzYWQzOTVjMGE3NDYwMGVhMjp7Il9hdXRoX3VzZXJfaGFzaCI6ImQ5NjljNzY4Nzk1NDYyNGM4Mzc5ZGIwOTlhOTJhY2UzZWJiNGVmYzUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-08-30 17:39:57.543473');
CREATE TABLE "django_site" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "domain" varchar(100) NOT NULL, "name" varchar(50) NOT NULL);
INSERT INTO "django_site" VALUES(1,'example.com','example.com');
CREATE TABLE "website_banner" (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`titulo`	varchar(200) NOT NULL,
	`slug`	varchar(200) NOT NULL UNIQUE,
	`descricao`	varchar(200) NOT NULL,
	`url_resource`	varchar(200),
	`upload_resource`	varchar(100),
	`action_resource`	varchar(200)
, `ativo` bool);
INSERT INTO "website_banner" VALUES(1,'Festa da Indenpendêcia na Bambino','banner-do-leandro','A escola Bambino Camponês vai promover uma festa comemorativa ao 07 de Setembro...','http://lorempixel.com/1200/600/sports','banners/579311_633747976682282_1224046986_n.jpg','/publicacao/novo-site-da-bambino-campones',1);
INSERT INTO "website_banner" VALUES(2,'Aviso Urgente','aviso-urgente','Texto do aviso urgente.','http://lorempixel.com/1200/600/people','','/avisos-importantes',1);
INSERT INTO "website_banner" VALUES(3,'Participe da Campanha','participe-da-campanha','Estamos lançando a campanha do agasalho 2015.','http://lorempixel.com/1200/600/abstract','','publicacao/novo-site-da-bambino-campones',0);
CREATE TABLE "website_pagina" (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`titulo`	varchar(200) NOT NULL,
	`slug`	varchar(200) NOT NULL UNIQUE,
	`conteudo`	text NOT NULL,
	`palavras_chaves`	varchar(200) NOT NULL,
	`permite_comentario`	bool NOT NULL,
	`rascunho`	bool NOT NULL,
	`descricao`	varchar(200) NOT NULL
);
INSERT INTO "website_pagina" VALUES(1,'home','home','pagina home','pagina inicial',0,0,'asd');
INSERT INTO "website_pagina" VALUES(2,'Filosofia','filosofia','    <h2><span style="color:red;"> Filosofia</span></h2>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;">Nossa escola atende há 16 anos, alunos da Educação Infantil de faixa etária dos
    04 meses até aos 6 anos, pelos turnos da manhã e tarde. Temos como filosofia formar
    um cidadão crítico, participativo, solidário, comprometido com o contexto do país.
    Contamos com uma equipe de profissionais qualificados e material didático atualizado.
    Nosso objetivo é orientar, respeitando a individualidade de cada criança, como um
    cidadão em formação.</p>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;">Como primeira etapa da educação básica, a educação infantil, tem como
    finalidade o desenvolvimento das potencialidades da criança, até seis anos de idade,
    visando seus aspectos físico, psicológico, intelectual e social, complementando a ação
    da família e da comunidade.</p>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;">Oportunizamos aos nossos alunos à experimentação das diferentes formas de
    linguagem (oral e escrita), desenvolvendo assim, o raciocínio e a criatividade.</p>
<h4>MISSÃO</h4>
<p style="text-align: justify;text-indent:40px;margin-top: 05px;">Proporcionar um ambiente agradável, familiar e acolhedor, baseado num ensino de qualidade, para o desenvolvimento e formação de pequenos cidadãos com valores humanos e éticos.</p>
<h4>VISÃO</h4>
<p style="text-align: justify;text-indent:40px;margin-top: 05px;">Ser uma escola de educação infantil de referencia na cidade, pela excelência no ensino e pelo ambiente diferenciado.</p>
<h4>VALORES</h4>
<ul>
<li>Perseverança</li>
<li>Responsabilidade</li>
<li>Credibilidade</li>
<li>Respeito</li>
<li>Satisfação do cliente</li>
<li>Compromisso com a qualidade dos serviços</li>
<li>Respeito às diferenças</li>
<li>Igualdade de inclusão</li>
<li>Preservação do Meio Ambiente</li>
<li>Responsabilidade Social</li>
</ul>','empresa, filosofia',0,0,'Página descrevendo a filosofia da empresa.');
INSERT INTO "website_pagina" VALUES(3,'Nossa Equipe','nossa-equipe','<h2><span style="color:red;">Nossa Equipe</h2>
<p style="text-align: justify;text-indent:40px;margin-top: 05px;">Nossa 
Escola é composta por uma Equipe qualificada e, em constante atualização com treinamentos internos e monitoramento das gestoras.</p>
<p style="text-align: justify;text-indent:40px;margin-top: 
05px;">Abaixo listamos a <strong>Equipe da E.E.I. Bambino Camponês</strong>:</p>
<ul>
<li><strong>Berçário I:</strong> Professora Lisiane e atendentes Simone e Juliana;</li>
<li><strong>Berçário II:</strong> Professora Lisiane e atendente Francyele;</li>
<li><strong>Maternal I:</strong> Pedagoga Valderes e atendentes Kiane e Camila;</li>
<li><strong>Maternal II:</strong> Professora Rafaela e atendente Angela;</li>
<li><strong>Jardim A:</strong> Professora Daniele e atendentes Graziele e Fernanda;</li>
<li><strong>Jardim B:</strong> Professora Daniele.</li>
<li><strong>Cozinheira:</strong> Vera;</li>
<li><strong>Limpeza:</strong> Eliana;</li>
<li><strong>Nutricionista:</strong> Veronica;</li>
<li><strong>Atividades Extras:</strong> Professor Lolo (capoeira), Professora Natália (ballet) e Professora Carla (inglês);</li>
<li><strong>Consultora de Gestão de Pessoas:</strong> Grasiele;</li>
<li><strong>Financeiro:</strong> Alcindo;</li>
<li><strong>Direção:</strong> Tia Mari e Tia Salete</li>
</ul>','escola, equipe, trabalho',0,0,'Equipe de trabalho da Bambino Camponês');
INSERT INTO "website_pagina" VALUES(4,'Instalações','instalacoes','<h2><span style="color:red;">Instalações</h2>
<p style="text-align: justify;text-indent:40px;margin-top: 05px;">A E.E.I. Bambino Camponês funciona em amplo prédio, sediada na Rua Irmão Florêncio, 151, Bairro Harmonia, Canoas, com uma estrutura em constante melhoria para receber seus alunos, familiares e colaboradores.</p>
<p style="text-align: justify;text-indent:40px;margin-top: 05px;">A Bambino Camponês é uma das referências de Escola Infantil na cidade de Canoas pela sua infraestrutura, o qual atualmente dispõe dos seguintes recursos:</p>
<ul>
<li>Prédio com dois pavimentos, totalizando em média 355 metros quadrados;</li>
<li>Salas amplas, sendo algumas climatizadas, com recursos para a diversão e aconchego das nossas crianças (televisores, aparelhos de DVD, brinquedos, entre outros recursos);</li>
<li>Sala múltipla para diversos fins pedagógicos, recreativos e atividades extras;</li>
<li>Refeitório e uma cozinha equipada para a realização das saborosas e monitoradas refeições das nossas crianças e colaboradores;</li>
<li>Pracinha com diversos brinquedos por faixa etária e um amplo espaço para realização de atividades ao ar livre.</li>
</ul>
<p style="text-align: justify;text-indent:40px;margin-top: 05px;">Convidamos a todos interessados para conhecer nossas instalações que anualmente passa por constantes modificações para um atendimento adequado a nossa sociedade.</p>','instalações, infra-estrutura',0,0,'instalações da Bambino Campones');
INSERT INTO "website_pagina" VALUES(5,'Nossa História','nossa-historia','<h2><span style="color:red;">Nossa História</h2>

<p style="text-align: justify;text-indent:40px;margin-top: 05px;">Nossa 
história começou em 1999, com a necessidade de um local adequado para 
deixar meu filho, na época com 3 (três) anos. Sem encontrar nada que 
eu entendesse como um local ideal, resolvi convidar minha irmã para 
cuidarmos de algumas crianças em casa, e ela aceitou. Fizemos as 
devidas mudanças na casa em que eu morava, para isso tive que me 
mudar. A casa na época era de nosso pai. Começamos a trabalhar no dia 
03/02/1999 com uma criança, que era meu filho, ao final da primeira 
semana estávamos com 3 (três), um menino e duas meninas. Ao término 
do primeiro ano já contávamos com 11 (onze) crianças sob nosso 
cuidado. Fizemos nosso primeiro passeio ao jardim zoológico em outubro 
do mesmo ano em homenagem a semana da criança. Na volta do passeio todos participaram da primeira noite do pijama com direito a banho, janta, ceia, brincadeiras e ao acordarem foi servido um belo café da manhã. Festejamos nosso primeiro Natal com a montagem de uma árvore feita de filtros de papel, colocada no refeitório e saudamos a vinda de papai Noel com nossos bambinos a sua volta, a festa foi linda.</p>
<p style="text-align: justify;text-indent:40px;margin-top: 05px;">No 
ano de 2000 (dois mil), a escola foi assaltada, sendo levados, os 
uniformes das crianças e professores, merenda, mantimentos para as 
refeições, aparelhos eletroeletrônicos, material didático e 
pedagógico. Recuperamos quase tudo através de uma Festa Junina 
realizada pela comunidade. Tivemos a contribuição de cada família, 
da escola ou não. Fechamos a rua e nos divertimos muito. Com o aumento 
da procura, fizemos a primeira ampliação térrea. Passaram-se poucos 
anos, e precisamos novamente ampliar. Neste momento fizemos o primeiro 
andar. Por um período de 6 (seis) anos, atendemos a crianças 
conveniadas da prefeitura municipal de Canoas. Desde 2008 (dois mil e 
oito) somos autorizadas e credenciadas pelo Conselho Municipal de 
Educação. Novamente nos faltou espaço. Para onde ir? Fomos para o 
lado, pátio vizinho, com mais 4 (quatro) salas de aula, banheiro e pátio. Atendemos, hoje, 95 (noventa e cinco) crianças. Nosso corpo docente é composto por 16 (dezesseis) profissionais com titulação, se não concluída em curso, exigida por lei, pedagoga, nutricionista, capoeirista e professora de ballet. Todas as salas são bem arejadas e recebem a luz solar.</p>
<p style="text-align: justify;text-indent:40px;margin-top: 05px;">Hoje 
nossa escola conta com uma estrutura física de 354 (trezentos e 
cinquenta e quatro) m², sendo dividida em 10 (dez) salas, um refeitório, 5 (cinco) banheiros, áreas de circulação, cozinha e pracinha.</p>
<p style="text-align: justify;text-indent:40px;margin-top: 05px;">Somos 
muito felizes e realizadas, compramos nossos próprios imóveis, 
inclusive o da empresa, sempre trabalhamos com muito amor e dedicação, por isso nossa 
empresa é uma empresa de sucesso. Nossas festas de Natal hoje reúnem em média
450 (quatrocentos e cinquenta) pessoas. Agradecemos a nosso pai pelo inicio de tudo
isso, pois durante 7 (sete) anos nos apoiou e cedeu-nos o imóvel para trabalharmos,
onde hoje é a cede de nossa empresa. Temos muito a agradecer a Deus que mesmo em
momentos muito difíceis, nunca nos deixou esmorecer.</p>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;">“As manas”, como somos conhecidas hoje em nosso mercado de trabalho, só tem
a agradecer a confiança de todos os pais, que deixam conosco seu bem mais precioso.
Crianças de 04 (quatro) meses até 06 (seis) anos, que ficam sob nosso cuidado diário
e saem para seus compromissos com a certeza de que amamos a todos com se fossem
verdadeiramente nossos filhos.</p>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;">Para nós isto é um verdadeiro sucesso, pois fomos criadas na lavoura junto com
nossos pais e mais 3 (três) irmãos, somos de família muito humilde, mas que nunca teve
medo de trabalhar e ser feliz.</p>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;">Este é o resumo de nossa história, <strong>ontem um sonho, hoje uma realidade.</strong></p>','história',0,0,'Conheça a História da Bambino Camponês.');
INSERT INTO "website_pagina" VALUES(6,'Horários','horarios','<h2><span style="color:red;">Horários de Funcionamento</h2>
<h4 style="color: red; margin-top:35px;height: 10px !important;">Horário de entrada:</h4>
    <p style="display:block;width:100%;"><span style="font-weight:bold;">Turno da manhã:</span> <span style="font-weight:bold;color:black;">até</span> às <span style="font-weight:bold;color:black;">10h45min</span></p>
    <p style="margin-bottom: 20px;display:block;width:100%;"><span style="font-weight:bold;">Turno da tarde:</span> das <span style="font-weight:bold;color:black;">13h00min até às 14h00min</span></p>
    <h4 style="color: red; margin-top:35px;width:100%;display:table;">Horário de saída:</h4>
    <p style="display:block;width:100%;margin: 0px !important">De Segunda-feira a Quinta-feira – <span style="font-weight:bold;color:black;">até às 19h00min</span></p>
    <p style="display:block;width:100%;margin: 10px 0px !important; margin-bottom:20px;">Sexta-feira <span style="font-weight:bold;color:black;">até às 18h00min</span></p>
    <p style="margin-top: 30px;">Favor <span style="font-weight:bold;">não</span> procurar a escola nos seguintes horários:</p>
    <p>Das <span style="font-weight:bold;color:black;">10h45min</span> às <span style="font-weight:bold;color:black;">12h00min</span>. -&gt; hora do almoço, higiene e descanso das crianças;</p>
    <p>Das <span style="font-weight:bold;color:black;">12h</span> até às <span style="font-weight:bold;color:black;">13h</span> -&gt; almoço das professoras.</p>
    <p>Das <span style="font-weight:bold;color:black;">16h45min</span> às <span style="font-weight:bold;color:black;">17h45min</span> -&gt; Janta e higiene das crianças.</p>','horários, atendimento',0,0,'horários de funcionamento da escola');
INSERT INTO "website_pagina" VALUES(7,'Matrículas','matriculas','<h2><span style="color:red;">Matrículas</h2>
<p style="text-align: justify;text-indent:40px;margin-top: 05px;"><strong>As rematrículas</strong> de todas as turmas referente ao ano de 2016 serão realizadas no dia <strong>21 de Novembro de 2015, Sábado, das 8h às 11h</strong> na sede da Escola.</p>
<p style="text-align: justify;text-indent:40px;margin-top: 05px;">Para a <strong>efetivação da rematrícula</strong> de seu filho/sua filha é necessário entregar os seguintes documentos:</p>
<ul>
<li>Cópia da Certidão de Nascimento da criança;</li>
<li>Cópia da Carteira de Vacinação da criança;</li>
<li>2 fotos 3x4 da criança;</li>
<li>Cópia do Comprovante de Residência;</li>
<li>Cópia do RG e CPF do responsável da criança.</li>
</ul>
<h4>Alunos Novos</h4>
<p style="text-align: justify;text-indent:40px;margin-top: 05px;">Para as matriculas de <strong>alunos novos</strong> os documentos que deverão ser entregues são os mesmos listados acima e a data da realização de matrículas será no dia <strong>26 
de Novembro de 2015, Quinta-feira, das 18h às 19h na sede da Escola</strong>.
','matriculas, informações',0,0,'Informações sobre matrículas');
INSERT INTO "website_pagina" VALUES(8,'Material Escolar','material-escolar','<h2><span style="color:red;">Lista de Material Escolar para o ano de 
2015</h2>
<ul style="list-style:square;">
        <li style="padding-bottom: 5px;">
            <a href="http://media.bambinocampones.com.br/images/material_escolar/bercario_pre_maternal_2015.pdf" title="" target="_blank">Berçário e Pré-Maternal</a>
        </li>
        <li style="padding-bottom: 5px;">
            <a href="http://media.bambinocampones.com.br/images/material_escolar/maternal_1_2015.pdf" title="" target="_blank">Maternal I</a>
        </li>
        <li style="padding-bottom: 5px;">
            <a href="http://media.bambinocampones.com.br/images/material_escolar/maternal_2_2015.pdf" title="" target="_blank">Maternal II</a>
        </li>
        <li style="padding-bottom: 5px;">
            <a href="http://media.bambinocampones.com.br/images/material_escolar/jardim_1_e_2_2015.pdf" title="" target="_blank">Jardim 1 e 2</a>
        </li>
    </ul>','material escolar',0,0,'lista de material de escolar por turma no ano letivo corrente');
INSERT INTO "website_pagina" VALUES(9,'Proposta Pedagógica','proposta-pedagogica','<h2><span style="color:red;">Proposta Pedagógica</h2>


    <p style="text-align: justify;text-indent:40px;margin-top: 05px;"><strong>Observação: </strong>A Proposta Pedagógica completa da Bambino Camponês encontra-se a disposição dos pais na secretaria da escola.</p>
    <h3 style="float:left; width:100%;display:block;">ESCOLA DE EDUCAÇÃO INFANTIL</h3>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;">A escola de educação infantil passa por transformações, construindo e reconstruindo referenciais teóricos para melhor trabalhar com as crianças, objetivando a ênfase no lado humano, onde a criança seja o desafio e a prioridade de todos:</p>
    <ul type="a" style="float:left; width:100%;display:block;list-style:none;font-size:14px;">
        <li>a) Atender a criança visando os cuidados essenciais associados à sua sobrevivência e ao desenvolvimento de sua identidade.</li>
        <li>b) Promover um fazer pedagógico completando a ação da família atendendo aos cuidados essenciais e construído bases da personalidade humana, da inteligência, da vida emocional e da socialização.</li> 
    </ul>
    <h3 style="float:left; width:100%;display:block;">METODOLOGIA</h3>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;">Nossa escola vem trabalhando com projetos, construídos coletivamente com duração diferenciada em função ao assunto abordado e o interesse a que este venha despertar na maioria das crianças.</p>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;">As datas comemorativas são trabalhadas como projetos e oportunizam a integração entre turmas e a participação dos pais e familiares.</p>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;">As atividades são elaboradas de acordo com as faixas etárias, observando e respeitando o desenvolvimento individual de cada criança.</p>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;">Ao elaborarmos estas atividades priorizamos brincadeiras e experiências diversificadas, com objetivo de criar condições para o desenvolvimento integral da criança.</p>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;">Buscamos trabalhar numa linha de ação onde o aprender se constrói através das trocas, num processo dinâmico e desafiador, desta maneira levando-as ao conhecimento e a aprendizagem.</p>
    <h3 style="float:left; width:100%;display:block;">METAS</h3>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;">As metas são expressões práticas da necessidade da escola, do que foi observado durante o trabalho de construção da Proposta Político, Pedagógica.</p>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;">Foram utilizados os mais variados recursos, pesquisas, observações e as decisões traduzem a vontade dos sujeitos envolvidos com a educação das crianças:</p>
    <ul style="float:left; width:100%;display:block;font-size:14px;">
        <li>Respeitar e defender os direitos da criança;</li>
        <li>Flexibilidade na rotina escolar (hora de acordar, interromper a brincadeira);</li>
        <li>Rever as regras de acordo com as necessidades da turma;</li>
        <li>Colaboração do grupo quando vir algo que está passando despercebido, alertando o colega;</li>
        <li>Atualizar-se sempre, ir à busca da atualização e aperfeiçoamento, fazer cursos;</li>
        <li>Observar mais o desenvolvimento da criança (olhar mais apurado);</li>
        <li>Maior participação dos pais e conscientização dos papéis;</li>
        <li>Procurar melhorar a disposição para trabalhar, buscando o prazer de estar exercendo sua função;</li>
        <li>Realizar mais reuniões para reflexão sobre as atividades cotidianas;</li>
        <li>Observar, interpretar e registrar as ações e reações das crianças;</li>
        <li>Adequar progressivamente à escola conforme as exigências da lei.</li>
    </ul>
    <h3 style="float:left; width:100%;display:block;">ESTÁGIOS DO DESENVOLVIMENTO DAS CRIANÇAS</h3>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;">De acordo com Piaget, o desenvolvimento cognitivo é um processo de sucessivas mudanças qualitativas e quantitativas das estruturas cognitivas derivando cada estrutura de estruturas precedentes. Ou seja, o indivíduo constrói e reconstrói continuamente as estruturas que o tornam cada vez mais apto ao equilíbrio.</p>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;">Essas construções seguem um padrão denominado por Piaget de ESTÁGIOS que seguem idades mais ou menos determinadas. Todavia, o importante é a ordem dos estágios e não a idade de aparição destes.</p>
    <h3 style="float:left; width:100%;display:block;">As fases do desenvolvimento infantil segundo Piaget</h3>
    <h4 style="float:left; width:100%;display:block;">Período Sensório-Motor (0 a 2 anos)</h4>
    <ul style="float:left; width:100%;display:block;font-size:14px;">
        <li>Aprendizagem da coordenação motora elementar</li>
        <li>Aquisição da linguagem até a construção de frases simples</li>
        <li>Desenvolvimento da percepção</li>
        <li>Noção de permanência do objeto</li>
        <li>Preferências afetivas</li>
        <li>Início da compreensão de regras</li>
    </ul>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;">A partir de reflexos neurológicos básicos, o bebê começa a construir esquemas de ação para assimilar mentalmente um meio. A inteligência é prática. As noções de espaço e tempo são construídas pela ação. O contato com o meio é direto e imediato, sem representação ou pensamento.</p>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;">Exemplos:</p>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;">O bebê pega o que está em sua mão; “mama” o que é posto em sua boca; "vê" o que está diante de si. Aprimorando esses esquemas, é capaz de ver um objeto, pegá-lo e levá-lo a boca.</p>
    <h4 style="float:left; width:100%;display:block;">Período Pré-Operatório (2 a 7 anos)</h4>
    <ul style="float:left; width:100%;display:block;font-size:14px;">
        <li>Domínio da linguagem</li>
        <li>Animismo, finalismo e antropocentrismo/egocentrismo, isto é os objetos são percebidos como tendo intenções de afetar a vida da criança e dos outros seres humanos</li>
        <li>Brincadeiras individualizadas, limitação em se colocar no lugar dos outros</li>
        <li>Possibilidade da moral da obediência, isto é, que o certo e o errado é aquilo que dizem os adultos.</li>
        <li>Coordenação motora fina.</li>
    </ul>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;">Também chamado de estágio da <strong>Inteligência Simbólica</strong>. Caracteriza-se, principalmente, pela interiorização de esquemas de ação construídos no estágio anterior (sensório-motor).</p>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;">A criança desse estágio:</p>
    <ul style="float:left; width:100%;display:block;font-size:14px;">
        <li>É egocêntrica, centrada em si mesma e não consegue se colocar, abstratamente, no lugar do outro.</li>
        <li>Não aceita a idéia do acaso e tudo deve ter uma explicação (é fase dos "por quês").</li>
        <li>Já pode agir por simulação, "como se".</li>
        <li>Possui percepção global sem discriminar detalhes.</li>
        <li>Deixa-se levar pela aparência sem relacionar fatos.</li>
    </ul>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;">Exemplos:</p>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;">Mostram-se para a criança, duas bolinhas de massa iguais e dá-se a uma delas a forma de salsicha. A criança nega que a quantidade de massa continue igual, pois as formas são diferentes. Não relaciona situações. O desenvolvimento do indivíduo inicia-se no período intra-uterino e vai até aos 15 ou 16 anos. Piaget diz que a embriologia humana evolui também após o nascimento, criando estruturas cada vez mais complexas. A construção da Inteligência, dá-se portanto em etapas sucessivas, com complexidades crescentes, encadeadas umas às outras. A isto Piaget chamou de <strong>"construtivismo seqüencial"</strong>.</p>
    <h3 style="float:left; width:100%;display:block;">Períodos em que se dá o desenvolvimento motor, verbal e mental.</h3>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;"><strong>Período sensório-motor</strong> - do nascimento aos 2 anos aproximadamente. A ausência da função semi-ótica é a principal característica deste período. A inteligência trabalha através das percepções (simbólico) e das ações (motor) através dos deslocamentos do próprio corpo. É uma inteligência eminentemente prática. Sua linguagem vai da ecolalia (repetição de sílabas) à palavra-frase (“água” para dizer que quer beber água) já que não representa mentalmente o objeto e as ações. Sua conduta social, neste período, é de isolamento e indiferenciação (o mundo é ele).</p>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;"><strong>Período simbólico</strong> - dos 2 aos 4 anos, aproximadamente. Neste período surge a função semiótica que permite o surgimento da linguagem, do desenho, da imitação, da dramatização etc. Podendo criar imagens mentais na ausência do objeto ou da ação é o período da fantasia, do faz de conta, do jogo simbólico. Com a capacidade de formar imagens mentais pode transformar o objeto numa satisfação de seu prazer (uma caixa de fósforo em carrinho, por exemplo). É também o período em que o individuo "dá alma" (animismo) aos objetos ("o carro do papai foi dormir na garagem"). A linguagem está a nível de monólogo coletivo, ou seja, todos falam ao mesmo tempo sem que respondam as argumentações dos outros.  Duas crianças "conversando" dizem frases que não tem relação com a frase que o outro está dizendo. Sua socialização é vivida de forma isolada, mas dentro do coletivo. Não há liderança e os pares são constantemente trocados. Existem outras características do pensamento simbólico que não estão sendo mencionadas aqui, uma vez que a proposta é de sintetizar as ideias de Jean Piaget, como por exemplo o nominalismo (dar nomes as coisas das quais não sabe o nome ainda), superdeterminação ("teimosia") egocentrismo (tudo é "meu"), etc.</p>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;"><strong>Período intuitivo</strong> - dos 4 aos 7 anos, aproximadamente. Neste período já existe um desejo de explicação dos fenômenos. É a (<strong>idade dos por quês</strong>), pois o individuo pergunta o tempo todo. Distingue a fantasia do real, podendo dramatizar a fantasia sem que acredite nela. Seu pensamento continua centrado no seu próprio ponto de vista. Já é capaz de organizar coleções e conjuntos sem no entanto incluir conjuntos menores em conjuntos menores (rosas no conjunto de flores, por exemplo).</p>
    <p style="text-align: justify;text-indent:40px;margin-top: 05px;">Quanto a linguagem não mantém uma conversação longa, mas já é capaz de adaptar sua resposta as palavras do companheiro. Os períodos simbólico e intuitivo são também comumente apresentados como período pré-operatório.</p>','proposta pedagogica',0,0,'Proposta pedagógica da Bambino Campones');
INSERT INTO "website_pagina" VALUES(10,'Berçario','bercario','<h2><span style="color:red;">Berçário</h2>
<h4>Rotina Diária</h4>
    <ul style="list-style: square;">
        <li>07:00 – 09:00 -&gt; Entrada e troca de fraldas;</li>
        <li>09:00 – 09:30 -&gt; Lanche ou mamadeira;</li>
        <li>09:30 – 10:00 -&gt; Solárium;</li>
        <li>10:00 – 10:30 -&gt; Brinquedos com músicas;</li>
        <li>10:30 – 11:00 -&gt; Higiene e troca de fralda;</li>
        <li>11:00 – 12:00 -&gt; Almoço e higiene;</li>
        <li>12:00 – 13:00 -&gt; Descanso;</li>
        <li>13:00 – 14:00 -&gt; Chegada e música;</li>
        <li>14:00 – 15:00 -&gt; Troca de fralda e mamadeira;</li>
        <li>15:00 – 16:00 -&gt; Pracinha;</li>
        <li>16:00 – 16:30 -&gt; Brinquedos na sala de recreação;</li>
        <li>16:30 – 17:00 -&gt; Troca de fralda;</li>
        <li>17:00 – 18:00 -&gt; Pré-janta e higiene;</li>
        <li>18:00 – 19:00 -&gt; Saída e DVD;</li>
    </ul>
    <p style="float: left;font-weight:bold;">OBS: Durante o dia ocorrem soninhos ocasionais.</p>','serviços, berçário',0,0,'Serviço de Berçário');
INSERT INTO "website_pagina" VALUES(11,'Pré-Maternal','pre-maternal','<h2><span style="color:red;">Pré-Maternal</h2>
<h4>Rotina Diária</h4>
    <ul style="list-style: square;">
        <li>07:00 – 09:00 -&gt; Chegada;</li>
        <li>09:00 – 09:30 -&gt; Lanche;</li>
        <li>09:30 – 10:30 -&gt;Pracinha;</li>
        <li>10:30 – 11:00 -&gt;Troca de fraldas;</li>
        <li>11:00 – 11:30 -&gt; Almoço;</li>
        <li>11:30 – 12:00 -&gt; Higiene Bucal;</li>
        <li>12:00 – 13:00 -&gt; Soninho;</li>
        <li>13:00 – 14:00 -&gt; Pracinha;</li>
        <li>14:00 – 14:30 -&gt; Troca de fraldas;</li>
        <li>14:30 – 15:00 -&gt;Lanche;</li>
        <li>15:00 – 15:30 -&gt; Atividades pedagógicas;</li>
        <li>15:30 – 16:00 -&gt; Atividades dirigidas;</li>
        <li>16:00 – 17:00 -&gt; Trocas;</li>
        <li>17:00 – 17:30 -&gt; Janta;</li>
        <li>17:30 – 18:00 -&gt; Higiene Bucal;</li>
        <li>18:00 – 19:00 -&gt; DVD ou Pracinha e Saída;</li>
    </ul>
    <p style="float: left;font-weight:bold;">Sexta -&gt; Ed. Física.</p>','serviços, pré-maternal',0,0,'Serviço de Pré-Maternal');
INSERT INTO "website_pagina" VALUES(12,'Maternal 1','maternal-1','<h2><span style="color:red;">Maternal 1</h2>
<h4>Rotina Diária</h4>
    <ul style="list-style: square;">
        <li>07:00 -&gt; Entrada ;</li>
        <li>08:00 -&gt; Brinquedos e/ou jogos;</li>
        <li>09:00 -&gt; Lanche;</li>
        <li>09:30 -&gt; Higiene;</li>
        <li>10:00 -&gt; Pracinha; *</li>
        <li>11:00 -&gt; Higiene;</li>
        <li>11:20 -&gt; Almoço;</li>
        <li>11:40 -&gt; Higiene Bucal e Descanso;</li>
        <li>13:00 -&gt; Entrada e Livre;</li>
        <li>13:30 -&gt; Higiene;</li>
        <li>14:00 -&gt; Atividade pedagógica e/ou dirigida;</li>
        <li>15:00 -&gt; Lanche;</li>
        <li>15:30 -&gt; Pracinha; *</li>
        <li>16:00 -&gt; Jogos e/ou brincadeiras;</li>
        <li>16:30 -&gt; Higiene;</li>
        <li>17:00 -&gt; Janta;</li>
        <li>17:30 -&gt; Higiene Bucal;</li>
        <li>18:00 -&gt; Jogos ou DVD;</li>
        <li>19:00 -&gt; Saída;</li>
    </ul>
    <p style="float: left;font-weight:bold;width:100%;">Informações Complementares:</p>
    <ul style="float:left;">
        <li>Segunda, quarta e quinta -&gt; Atividade pedagógica;</li>
        <li>Terça -&gt; Hora do conto;</li>
        <li>Terça -&gt; Capoeira (14:00 às 14:30);</li>
        <li>Quarta -&gt; Ballet (15:00 às 15:30);</li>
        <li>Sexta -&gt; Ed. Física, brinquedo livre de casa e lanche coletivo.</li>
    </ul>
    <p style="float: left;font-weight:bold;width:100%;">Observações:</p>
    <p style="float: left;font-weight:bold;color:red;width:100%;">* Dias de chuva atividade na sala no horário da pracinha.</p>','serviços, maternal 1',0,0,'Serviço de Maternal 1');
INSERT INTO "website_pagina" VALUES(13,'Maternal 2','maternal-2','<h2><span style="color:red;">Maternal 2</h2>
<h4>Rotina Diária</h4>
    <h5>Manhãs:</h5>
    <ul style="list-style: square;">
        <li>07:00 -&gt; Entrada;</li>
        <li>08:00 -&gt; Brinquedos e/ou jogos;</li>
        <li>09:00 -&gt; Lanche;</li>
        <li>09:30 -&gt; Higiene;</li>
        <li>10:00 -&gt; Pracinha; *</li>
        <li>11:00 -&gt; Higiene;</li>
        <li>11:20 -&gt; Almoço;</li>
        <li>11:40 -&gt; Higiene Bucal e Descanso;</li>
        <li>13:00 -&gt; Entrada e Livre;</li>
    </ul>
    <h5>Tardes:</h5>
    <h6>Segunda-feira:</h6>
    <ul style="list-style: square;">
        <li>14:00 -&gt; Como foi o final de semana ? (oralidade e desenho);</li>
        <li>15:00 -&gt; Lanche;</li>
        <li>15:30 -&gt; Pracinha ou pátio;</li>
        <li>16:00 -&gt; Coordenando movimentos;</li>
        <li>16:15 -&gt; Momento 1,2,3;</li>
        <li>17:20 -&gt; Janta e higiene;</li>
        <li>18:00 -&gt; Hora do DVD;</li>
        <li>19:00 -&gt; Saída.</li>
    </ul>
    <h6>Terça-feira:</h6>
    <ul style="list-style: square;">
        <li>13:00 -&gt; Brinquedos ou jogos;</li>
        <li>14:00 -&gt; Capoeira;</li>
        <li>14:30 -&gt; hora do conto;</li>
        <li>15:00 -&gt; Lanche;</li>
        <li>15:30 -&gt; Pracinha ou pátio;</li>
        <li>16:00 -&gt; Música;</li>
        <li>16:15 -&gt; Momento A,B,C;</li>
        <li>17:20 -&gt; Janta e higiene;</li>
        <li>18:00 -&gt; Massinha de modelar;</li>
        <li>19:00 -&gt; Saída.</li>
    </ul>
    <h6>Quarta-feira:</h6>
    <ul style="list-style: square;">
        <li>13:00 -&gt; Brinquedos ou jogos;</li>
        <li>14:00 -&gt; Vamos colorir ?;</li>
        <li>14:30 -&gt; Lanche;</li>
        <li>15:00 -&gt; Pracinha ou pátio;</li>
        <li>15:30 -&gt; Ballet;</li>
        <li>16:00 -&gt; Alongamento e relaxamento;</li>
        <li>16:30 -&gt; Recorte e colagem;</li>
        <li>17:20 -&gt; Janta e higiene;</li>
        <li>18:00 -&gt; Hora do DVD;</li>
        <li>19:00 -&gt; Saída.</li>
    </ul>
    <h6>Quinta-feira:</h6>
    <ul style="list-style: square;">
        <li>13:00 -&gt; Brinquedos ou jogos;</li>
        <li>14:00 -&gt; Caderno;</li>
        <li>15:00 -&gt; Lanche;</li>
        <li>15:30 -&gt; Pracinha;</li>
        <li>16:00 -&gt; Coordenando movimentos;</li>
        <li>16:15 -&gt; Música;</li>
        <li>16:30 -&gt; Pintura com tinta;</li>
        <li>17:20 -&gt; Janta e higiene;</li>
        <li>18:00 -&gt; Hora do conto;</li>
        <li>18:30 -&gt; Massinha de modelar;</li>
        <li>19:00 -&gt; Saída.</li>
    </ul>
    <h6>Sexta-feira:</h6>
    <ul style="list-style: square;">
        <li>Brinquedos de casa;</li>
        <li>Ed.Física;</li>
        <li>Lanche coletivo;</li>
        <li>Hora do DVD.</li>
    </ul>
    <p style="float: left;font-weight:bold;width:100%;">Observações:</p>
    <p style="float: left;font-weight:bold;color:red;width:100%;">* Dias de chuva atividade na sala no horário da pracinha.</p>','serviços, maternal 2',0,0,'Serviço de Maternal 2');
INSERT INTO "website_pagina" VALUES(14,'Jardim A','jardim-a','<h2><span style="color:red;">Jardim A</h2>
<h4>Rotina Diária</h4>
    <ul style="list-style: square;">
        <li>07:00 – 08:00 -&gt; Chegada;</li>
        <li>08:00 – 09:00 -&gt; Jogos dirigidos ou praça;</li>
        <li>09:00 – 09:30 -&gt; Lanche;</li>
        <li>09:30 – 10:30 -&gt; Brinquedo livre;</li>
        <li>10:30 – 11:00 -&gt; DVD ou livros (hora do conto);</li>
        <li>11:00 – 12:00 -&gt; Almoço e Higiene;</li>
        <li>12:00 – 13:00 -&gt; Descanso;</li>
        <li>13:00 – 14:00 -&gt; Entrada e Brinquedos ou jogos;</li>
        <li>14:00 – 15:00 -&gt; Atividade pedagógica;</li>
        <li>15:00 – 15:30 -&gt; Lanche;</li>
        <li>15:30 – 16:00 -&gt; Música e história;</li>
        <li>16:00 – 16:30 -&gt; Pracinha;</li>
        <li>16:30 – 17:00 -&gt; Rodízio de jogos ou kits carro e cozinha;</li>
        <li>17:00 – 18:00 -&gt; Jante e higiene;</li>
        <li>18:00 – 19:00 -&gt; Saída, DVD, massa de modelar ou Lego.</li>
    </ul>
    <p style="float: left;font-weight:bold;width:100%;">Informações Complementares:</p>
    <ul style="float:left;">
        <li>Segunda, quarta e quinta -&gt; Cartilha;</li>
        <li>Terça -&gt; Caderno;</li>
        <li>Terça -&gt; Capoeira (14:30 às 15:00);</li>
        <li>Quarta -&gt; Ballet (16:00 às 16:30);</li>
        <li>Sexta -&gt; Ed. Física (14:30 às 15:00);</li>
        <li>Sexta -&gt; Brinquedo livre de casa e lanche coletivo.</li>
    </ul>
','serviços, jardim a',0,0,'Serviço de Jardim A');
INSERT INTO "website_pagina" VALUES(15,'Jardim B','jardim-b','<h2><span style="color:red;">Jardim B</h2>
<h4>Rotina Diária</h4>
    <ul style="list-style: square;">
        <li>07:00 – 08:00 -&gt; Chegada;</li>
        <li>08:00 – 09:00 -&gt; Jogos dirigidos ou praça;</li>
        <li>09:00 – 09:30 -&gt; Lanche;</li>
        <li>09:30 – 10:30 -&gt; Brinquedo livre;</li>
        <li>10:30 – 11:00 -&gt; DVD ou livros (hora do conto);</li>
        <li>11:00 – 12:00 -&gt; Almoço e Higiene;</li>
        <li>12:00 – 13:00 -&gt; Descanso;</li>
        <li>13:00 – 14:00 -&gt; Chegada;</li>
        <li>14:00 – 15:00 -&gt; Atividades pedagógicas ;</li>
        <li>15:00 – 15:30 -&gt; Lanche;</li>
        <li>15:30 – 16:30 -&gt; Jogos pedagógicos ou brincadeiras;</li>
        <li>16:30 – 17:00 -&gt; Pracinha ou roda de música e canto;</li>
        <li>17:00 – 17:30 -&gt; Janta;</li>
        <li>17:30 – 18:30 -&gt; Jogos pedagógicos ou DVD;</li>
        <li>18:30 – 19:00 -&gt; Saída.</li>
    </ul>
    <p style="float: left;font-weight:bold;width:100%;">Informações Complementares:</p>
    <ul style="float:left;">
        <li>Segunda e quarta -&gt; Atividades na folha;</li>
        <li>Terça e quinta -&gt; Atividades no caderno;</li>
        <li>Terça -&gt; Capoeira (14:30 às 15:00);</li>
        <li>Quinta -&gt; Ballet (16:00 às 16:30);</li>
        <li>Sexta -&gt; Ed. Física (14:00 às 14:30);</li>
        <li>Sexta -&gt; Brinquedo livre de casa e lanche coletivo.</li>
    </ul>','serviços, jardim b',0,0,'Serviço de Jardim B');
INSERT INTO "website_pagina" VALUES(16,'Atividades Extras','atividades-extras','<div style="width:100%;text-align:right;margin-bottom: -10px;margin-top:10px;font-size:120%;">Você está em: <a href="/servicos/atividades-extras" title="Atividades Extras na Bambino Camponês">Serviços - Atividades Extras</a></div>
<h2><span style="color:red;">Atividades Extras</h2>
<h4>Inglês</h4>
    <h5>Objetivos</h5>
    <p style="width: 100%;margin-bottom:10px;margin-top:-10px;">
                </p><ul>
                        <li>Apresentar a língua inglesa como mais uma forma de comunicação</li>
                        <li>Reconhecer a língua inglesa como uma habilidade comunicativa característica de outros povos</li>
                        <li>Perceber a importância do aprendizado da língua inglesa para a apreciação dos costumes e valores de outras culturas</li>
                        <li>Ampliar a capacidade de memória, raciocínio, criatividade, imaginação, desenvolvimento cognitivo, potencializar o desenvolvimento e aprendizagem da linguagem</li>
                        <li>Estabelecer uma base para estudos posteriores de aprendizagem da língua inglesa.</li>
                </ul>
    <p></p>
    <h5>Como são as aulas</h5>
    <p style="width: 100%;margin-bottom:10px;margin-top:-10px;">As aulas de Inglês se baseiam em atividades diversificadas, como: histórias, dramatizações, músicas, brincadeiras, jogos e desenhos, introduzindo o inglês através da compreensão de estruturas básicas e uso de vocabulário, que fazem parte do cotidiano e da realidade das crianças, atividades que estimulam a memória, o raciocínio, a observação e a atenção, enfatizando o aspecto lúdico e despertando o prazer de aprender inglês de forma mais significativa, gradual e espontânea, aos poucos a criança se familiariza e assimila os elementos da nova linguagem, seguindo o mesmo processo de aprendizagem da língua materna.</p>
    <h5>Quem da Aula</h5>
    <p style="width: 100%;margin-bottom:10px;margin-top:-10px;">Carla Cristiane Boeckel, formação Inglês (CCAA), Pedagogia (Ulbra). Professora há 23 anos na Educação Infantil e Ensino Fundamental (1º a 4º ano), já lecionou em 24 escolas de Educação Infantil, atualmente leciona em 6 escolas em Canoas e na Escola de Educação Infantil Bambino Camponês desde 2014.</p>
    <h4>Ballet</h4>
    <h5>Objetivo</h5>
    <p style="width: 100%;margin-bottom:10px;margin-top:-10px;">O Ballet é uma atividade que traz benefícios tanto no aspecto físico (postura, trabalho muscular, alongamento), quanto no social (disciplina, organização, atenção). De forma lúdica são apresentados valores que serão de extrema importância para a vida toda. É uma atividade inteligente que faz a criança pensar. Além disso, desperta o gosto pela arte ampliando a cultura das crianças desde cedo.</p>
    <h5>Outros Objetivos</h5>
    <p style="width: 100%;margin-bottom:10px;margin-top:-10px;">desenvolver a orientação espacial, independência segmentária, esquema corporal, lateralidade, equilíbrio, coordenação dinâmica geral e coordenação motora fina.</p>
    <h5>Como Funciona</h5>
    <p style="width: 100%;margin-bottom:10px;margin-top:-10px;">A aula é realizada com uso de músicas infantis e músicas clássicas. Utiliza-se o "faz-de-conta" para chamar a atenção e manter a concentração das crianças. Possui etapas de: aquecimento e alongamento, ritmo e musicalização, localização espacial e noção de grupo, salto e coordenação motora, e volta à calma (relaxamento ou história de bailarina). Dentro dessas etapas se desenvolve a introdução a técnica do ballet, o fortalecimento muscular, postura, disciplina, organização e atenção. Propõe-se uma aula rica em estímulos para que a criança possa desenvolver ao máximo suas potencialidades físicas e cognitivas.</p>
    <h5>Quem da Aula</h5>
    <p style="width: 100%;margin-bottom:10px;margin-top:-10px;">Natália Birck Gazzo. Dança ballet desde os 4 anos de idade. Formada em ballet acadêmico pela Escola de Ballet Erenita Parmeggiani Teixeira – Canoas (2000), onde começou a lecionar desde então. Foi bailarina e professora do Ballet Vera Bublitz. Participou de diversos festivais de dança (São Leopoldo, Porto Alegre, Santa Maria, Bento Gonçalves) onde obteve premiações de 3°, 2° e 1° lugar. Graduada em dança pela Universidade Luterana do Brasil (ULBRA - 2009). É professora de educação física do Colégio Espírito Santo desde 2007, e já trabalhou em outras 8 escolas de educação infantil de Canoas. Trabalha na Escola de Educação Infantil Bambino Camponês desde 2005.</p>
    <h4>Capoeira</h4>
    <div class="photo_box" style="text-align:center;display:block;float:left;width:100%;margin:0px auto;margin-bottom:170px;">
        <a href="http://media.bambinocampones.com.br/images/eventos/esportes/lolo.jpg" title="Foto do mestre Lolo" class="lightbox" target="_blank"><img src="http://media.bambinocampones.com.br/images/eventos/esportes/lolo_thumb.jpg" alt="Foto do mestre lolo." title="Foto do mestre lolo." height="240px" width="320px"></a>
        <br>
        <span>Mestre Lolo.</span>
    </div>
    <h5>Objetivo</h5>
    <p style="width: 100%;margin-bottom:10px;margin-top:-10px;">Desenvolver de forma lúdica e descontraída, a flexibilidade a coordenação motora e a resistência. Despertar as potencialidades na área musical e artística, ritmo, expressão corporal e motricidade fina (como berimbal, pandeiro e atabaque).</p>
    <h5>Como Funciona</h5>
    <p style="width: 100%;margin-bottom:10px;margin-top:-10px;">Procedimento das aulas. Iniciamos com alongamento, após aquecimento, desenvolvimento e relaxamento no final (volta calma).</p>
    <h5>Quem da Aula</h5>
    <p style="width: 100%;margin-bottom:10px;margin-top:-10px;">Julio Cesar (mestrando Lolo). Pratico capoeira a 26 anos e trabalho com crianças a 18 anos (cursos de psicomotricidade, recreação e psicologia da criança, especialista em capoeira infantil).</p>
','atividades extras, balet, capoeira, inglês',0,0,'Atividades Extras na Bambino Camponês');
INSERT INTO "website_pagina" VALUES(17,'Músicas','musicas','<h2><span style="color:red;">Músicas para Download</h2>
<p style="text-align: justify;text-indent:40px;margin-top: 05px;">Página em Construção</p>
','downloads, músicas',0,0,'Downloads de Músicas');
INSERT INTO "website_pagina" VALUES(18,'Vídeos','videos','<h2><span style="color:red;">Download de Vídeos</h2>
<p style="text-align: justify;text-indent:40px;margin-top: 05px;">Página em Construção</p>','downloads, vídeos',0,0,'Downloads de Vídeos');
INSERT INTO "website_pagina" VALUES(19,'Papeis de Parede','papeis-de-parede','<h2><span style="color:red;">Download de Papéis de Parede</h2>
<p style="text-align: justify;text-indent:40px;margin-top: 05px;">Página em Construção</p>','downloads, papéis de parede',0,0,'Downloads de Papéis de Parede');
INSERT INTO "website_pagina" VALUES(20,'Desenhos para Pintar','desenhos-para-pintar','<h2><span style="color:red;">Download de Desenhos para Pintar</h2>
<p style="text-align: justify;text-indent:40px;margin-top: 05px;">Página em Construção</p>','downloads, desenhos para pintar',0,0,'Downloads de Desenhos para Pintar');
INSERT INTO "website_pagina" VALUES(21,'Fale Conosco','fale-conosco','<h2><span style="color:red;">Fale Conosco</h2>
<p>Deixe o seu recado que em breve entraremos em contato.</p>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
    <div class="contato">
      <form id="contato_form" action="/fale-conosco" method="post" onsubmit="return valida_contato();">
          <span>Nome:</span>
          <input id="nome" title="Informe o seu nome." name="nome" type="text" size="50">
          <span>Telefone:</span>
          <input id="telefone" title="Informe o seu telefone." name="telefone" type="text" size="50">
          <span>E-mail:</span>
          <input id="email" title="Informe o seu e-mail." name="email" type="text" size="50">
          <span>Mensagem:</span>
          <textarea id="mensagem" title="Deixe sua mensagem." cols="40" rows="10" name="mensagem"></textarea>
          <button style="width: 120px;" onclick="return valida_contato();" type="submit">Enviar</button>
      </form>
    </div>','fale conosco, contato',0,0,'Entre em contato com a Bambino.');
INSERT INTO "website_pagina" VALUES(22,'Localização','localizacao','<h2><span style="color:red;">Localização</h2>
<div align="center">
        <iframe width="100%" height="400px" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com.br/maps?q=Rua+Irm%C3%A3o+Flor%C3%AAncio,+n%C2%BA+151+-+Bairro+Harmonia+-+Canoas+-+RS+-+Brasil&amp;client=ubuntu&amp;channel=cs&amp;ie=UTF8&amp;hq=&amp;hnear=R.+Irm%C3%A3o+Flor%C3%AAncio,+151+-+Harmonia,+Canoas+-+Rio+Grande+do+Sul,+92310-490&amp;t=m&amp;ll=-29.901303,-51.193542&amp;spn=0.035715,0.054932&amp;z=14&amp;iwloc=A&amp;output=embed"></iframe><br><small><a href="https://maps.google.com.br/maps?q=Rua+Irm%C3%A3o+Flor%C3%AAncio,+n%C2%BA+151+-+Bairro+Harmonia+-+Canoas+-+RS+-+Brasil&amp;client=ubuntu&amp;channel=cs&amp;ie=UTF8&amp;hq=&amp;hnear=R.+Irm%C3%A3o+Flor%C3%AAncio,+151+-+Harmonia,+Canoas+-+Rio+Grande+do+Sul,+92310-490&amp;t=m&amp;ll=-29.901303,-51.193542&amp;spn=0.035715,0.054932&amp;z=14&amp;iwloc=A&amp;source=embed" style="color:#0000FF;text-align:left">Exibir mapa ampliado</a></small>
        <br>
        <br>
        <a href="https://maps.google.com.br/maps?q=Rua+Irm%C3%A3o+Flor%C3%AAncio,+n%C2%BA+151+-+Bairro+Harmonia+-+Canoas+-+RS+-+Brasil&amp;client=ubuntu&amp;channel=cs&amp;ie=UTF-8&amp;ei=w05SUfPrHsny0wH7lYFQ&amp;ved=0CAsQ_AUoAg" target="_blank" title="Exibir mapa ampliado." style="font-size:20px;">Exibir mapa no Google Maps</a>
    </div>','localização, mapa',0,0,'Localize a Bambino Camponês');
INSERT INTO "website_pagina" VALUES(23,'Responsabilidade Social','responsabilidade-social','<h2><span style="color:red;">Responsabilidade Social</h2>
<p style="text-align: justify;text-indent:40px;margin-top: 05px;">Página em construção.</p>','responsabilidade social',0,0,'Responsabilidade Social');
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('django_content_type',22);
INSERT INTO "sqlite_sequence" VALUES('django_migrations',5);
INSERT INTO "sqlite_sequence" VALUES('auth_permission',66);
INSERT INTO "sqlite_sequence" VALUES('django_site',1);
INSERT INTO "sqlite_sequence" VALUES('auth_user',1);
INSERT INTO "sqlite_sequence" VALUES('website_publicacao',3);
INSERT INTO "sqlite_sequence" VALUES('django_admin_log',93);
INSERT INTO "sqlite_sequence" VALUES('website_calendario',5);
INSERT INTO "sqlite_sequence" VALUES('website_cardapio',1);
INSERT INTO "sqlite_sequence" VALUES('website_conteudodownload',1);
INSERT INTO "sqlite_sequence" VALUES('website_depoimento',1);
INSERT INTO "sqlite_sequence" VALUES('website_galeria',2);
INSERT INTO "sqlite_sequence" VALUES('website_galeriaresource',2);
INSERT INTO "sqlite_sequence" VALUES('website_menu',1);
INSERT INTO "sqlite_sequence" VALUES('website_professor',1);
INSERT INTO "sqlite_sequence" VALUES('website_recomendacao',1);
INSERT INTO "sqlite_sequence" VALUES('website_servico',1);
INSERT INTO "sqlite_sequence" VALUES('website_banner',3);
INSERT INTO "sqlite_sequence" VALUES('website_pagina',23);
CREATE INDEX "website_galeriaresource_7f1b53df" ON "website_galeriaresource" ("galeria_id");
CREATE INDEX "website_publicacao_7f1b53df" ON "website_publicacao" ("galeria_id");
CREATE INDEX "website_menu_38aa5a4d" ON "website_menu" ("pagina_id");
CREATE INDEX "website_menu_89a6d304" ON "website_menu" ("menu_pai_id");
CREATE INDEX "website_servico_b9498a38" ON "website_servico" ("professor_id");
CREATE INDEX "website_materialescolar_190c6353" ON "website_materialescolar" ("servico_id");
CREATE INDEX "auth_permission_417f1b1c" ON "auth_permission" ("content_type_id");
CREATE INDEX "auth_group_permissions_0e939a4f" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_8373b171" ON "auth_group_permissions" ("permission_id");
CREATE INDEX "auth_user_groups_e8701ad4" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_0e939a4f" ON "auth_user_groups" ("group_id");
CREATE INDEX "auth_user_user_permissions_e8701ad4" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_8373b171" ON "auth_user_user_permissions" ("permission_id");
CREATE INDEX "django_admin_log_417f1b1c" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_e8701ad4" ON "django_admin_log" ("user_id");
CREATE INDEX "django_session_de54fa62" ON "django_session" ("expire_date");
COMMIT;
