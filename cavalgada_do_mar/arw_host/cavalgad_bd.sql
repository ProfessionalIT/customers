-- phpMyAdmin SQL Dump
-- version 3.4.10.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 08, 2012 at 06:37 PM
-- Server version: 5.5.23
-- PHP Version: 5.2.17

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `cavalgad_bd`
--

-- --------------------------------------------------------

--
-- Stand-in structure for view `artigos`
--
CREATE TABLE IF NOT EXISTS `artigos` (
`titulo` varchar(250)
,`slug` varchar(255)
,`intro` text
,`data_hora` timestamp
,`autor` varchar(255)
);
-- --------------------------------------------------------

--
-- Table structure for table `aviso`
--

CREATE TABLE IF NOT EXISTS `aviso` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `slug` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `data_publicacao` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `data_expiracao` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `autor` int(11) NOT NULL,
  `texto` text COLLATE utf8_unicode_ci NOT NULL,
  `ativo` varchar(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `locked` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'N',
  `status` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'A',
  `moderate_id` int(11) DEFAULT NULL,
  `draft` varchar(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `aviso_titulo_uk` (`titulo`),
  KEY `aviso_moderate_fk` (`moderate_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=2 ;

--
-- Dumping data for table `aviso`
--

INSERT INTO `aviso` (`id`, `titulo`, `slug`, `data_publicacao`, `data_expiracao`, `autor`, `texto`, `ativo`, `locked`, `status`, `moderate_id`, `draft`) VALUES
(1, 'Teste', 'teste', '2012-05-02 18:25:34', '2012-05-02 18:25:35', 1, '<p><span style="font-family: Arial, Helvetica, sans; font-size: 11px; line-height: 14px; text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vel nulla eget leo rhoncus dignissim nec vel sapien. Nam fermentum augue nec justo dapibus tempor. In et magna enim, vel faucibus augue. Donec purus dolor, dignissim quis iaculis ut, sollicitudin eget sapien. Vivamus ultricies, purus ut blandit accumsan, felis eros mattis ligula, eget fermentum lacus nunc in turpis. Nullam urna odio, facilisis ac fringilla sed, mollis et velit. Etiam interdum, augue et varius rutrum, augue neque pulvinar urna, vitae malesuada justo magna eu sapien. Phasellus sodales accumsan nisl eu ultricies. Nullam quam neque, convallis vel elementum vitae, porttitor eu ligula. Nunc tincidunt aliquam lorem, ac pulvinar ipsum aliquam eu. Nullam id ullamcorper neque. In mollis consectetur commodo. Vivamus magna tellus, scelerisque et iaculis ut, facilisis ac elit.</span></p>', 'S', 'N', 'A', NULL, 'N');

-- --------------------------------------------------------

--
-- Table structure for table `banner`
--

CREATE TABLE IF NOT EXISTS `banner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `slug` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `autor` int(11) NOT NULL,
  `tipo` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `foto_banner` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `link_banner` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `exibir_pagina_inicial` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `ativo` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `locked` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'N',
  `status` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'A',
  `moderate_id` int(11) DEFAULT NULL,
  `count_clicks` int(11) DEFAULT NULL,
  `custom_banner_code` text COLLATE utf8_unicode_ci,
  `draft` varchar(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `banner_titulo_uk` (`titulo`),
  KEY `banner_moderate_fk` (`moderate_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=10 ;

--
-- Dumping data for table `banner`
--

INSERT INTO `banner` (`id`, `titulo`, `slug`, `autor`, `tipo`, `foto_banner`, `link_banner`, `exibir_pagina_inicial`, `ativo`, `locked`, `status`, `moderate_id`, `count_clicks`, `custom_banner_code`, `draft`) VALUES
(2, 'Clínica de Hipiatria', 'clinica-de-hipiatria', 1, 'S', '/static/images/assessoria_.jpg', '/servicos#clinica-hipiatria', 'S', 'S', 'N', 'A', NULL, NULL, '', NULL),
(3, 'Fisioterapia', 'fisioterapia', 1, 'S', '/static/images/fisioterapia_2.jpg', '/servicos#fisioterapia', 'S', 'S', 'N', 'A', NULL, NULL, '', NULL),
(4, 'Cirurgia', 'cirurgia', 1, 'S', '/static/images/cirurgia_5.jpg', '/servicos#cirurgia', 'S', 'S', 'N', 'A', NULL, NULL, '', NULL),
(5, 'Odontologia', 'odontologia', 1, 'S', '/static/images/odontologia_.jpg', '/servicos#odontologia', 'S', 'S', 'N', 'A', NULL, NULL, '', NULL),
(6, 'Internação', 'internacao', 1, 'S', '/static/images/assessoria_.jpg', '/servicos#internacao', 'S', 'S', 'N', 'A', NULL, NULL, '', NULL),
(7, 'Atendimento à Domicilio', 'atendimento-a-domicilio', 1, 'S', '/static/images/atendimento_domicilio_.png', '/servicos#atendimento-a-domicilio', 'S', 'S', 'N', 'A', NULL, NULL, '', NULL),
(8, 'Consultoria à Eventos', 'consultoria-a-eventos', 1, 'S', '/static/images/consultoria_eventos.jpg', '/servicos#consultoria-a-eventos', 'S', 'S', 'N', 'A', NULL, NULL, '', NULL),
(9, 'Formação Continuada', 'formacao-continuada', 1, 'S', '/static/images/formacao_continuada.png', '/servicos#formacao-continuada', 'S', 'S', 'N', 'A', NULL, NULL, '', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `documento`
--

CREATE TABLE IF NOT EXISTS `documento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `slug` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `data_publicacao` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `autor` int(11) NOT NULL,
  `thumb_arquivo` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `link_arquivo` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `ativo` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `locked` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'N',
  `status` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'A',
  `moderate_id` int(11) DEFAULT NULL,
  `tipo` int(11) NOT NULL,
  `draft` varchar(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `publicacao_titulo_uk` (`titulo`),
  KEY `documento_moderate_fk` (`moderate_id`),
  KEY `documento_tipo_fk` (`tipo`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=2 ;

--
-- Dumping data for table `documento`
--

INSERT INTO `documento` (`id`, `titulo`, `slug`, `data_publicacao`, `autor`, `thumb_arquivo`, `link_arquivo`, `ativo`, `locked`, `status`, `moderate_id`, `tipo`, `draft`) VALUES
(1, 'Manual do Produto XYZ', 'manual-do-produto-xyz', '2012-05-02 18:32:17', 1, 'http://www.equine_websiteurbo.com.br/static/docs/manual_xyz.png', 'http://www.equine_websiteurbo.com.br/static/docs/manual_xyz.pdf', 'S', 'N', 'A', NULL, 1, 'N');

-- --------------------------------------------------------

--
-- Table structure for table `enquete`
--

CREATE TABLE IF NOT EXISTS `enquete` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pergunta` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `slug` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `resposta_01` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `votos_resposta_01` int(11) NOT NULL,
  `resposta_02` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `votos_resposta_02` int(11) NOT NULL,
  `resposta_03` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `votos_resposta_03` int(11) DEFAULT NULL,
  `ativo` varchar(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `locked` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'N',
  `status` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'A',
  `moderate_id` int(11) DEFAULT NULL,
  `autor` int(11) NOT NULL,
  `draft` varchar(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `enquete_pergunta_uk` (`pergunta`),
  KEY `enquete_moderate_fk` (`moderate_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=2 ;

--
-- Dumping data for table `enquete`
--

INSERT INTO `enquete` (`id`, `pergunta`, `slug`, `resposta_01`, `votos_resposta_01`, `resposta_02`, `votos_resposta_02`, `resposta_03`, `votos_resposta_03`, `ativo`, `locked`, `status`, `moderate_id`, `autor`, `draft`) VALUES
(1, 'Você gostou do novo site ?', 'voc-gostou-do-novo-site', 'Sim', 0, 'Não', 0, '', 0, 'S', 'S', 'A', NULL, 1, 'N');

-- --------------------------------------------------------

--
-- Stand-in structure for view `eventos`
--
CREATE TABLE IF NOT EXISTS `eventos` (
`titulo` varchar(250)
,`slug` varchar(255)
,`intro` text
,`data_hora` timestamp
,`autor` varchar(255)
);
-- --------------------------------------------------------

--
-- Table structure for table `galeria`
--

CREATE TABLE IF NOT EXISTS `galeria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `slug` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `data_criacao` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `autor` int(11) NOT NULL,
  `tipo` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `midia` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `url_galeria` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `locked` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'N',
  `status` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'A',
  `moderate_id` int(11) DEFAULT NULL,
  `permite_comentario` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'N',
  `draft` varchar(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `galeria_titulo_uk` (`titulo`),
  KEY `galeria_moderate_fk` (`moderate_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=2 ;

--
-- Dumping data for table `galeria`
--

INSERT INTO `galeria` (`id`, `titulo`, `slug`, `data_criacao`, `autor`, `tipo`, `midia`, `url_galeria`, `locked`, `status`, `moderate_id`, `permite_comentario`, `draft`) VALUES
(1, 'Fotos do Produto XYZ', 'fotos-do-produto-xyz', '2012-05-02 18:33:21', 1, 'S', 'F', 'https://picasaweb.google.com/106640973776692814000/Imagens_web?authuser=0&feat=directlink', 'N', 'A', NULL, 'N', 'N');

-- --------------------------------------------------------

--
-- Table structure for table `log`
--

CREATE TABLE IF NOT EXISTS `log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario` int(11) DEFAULT NULL,
  `operacao` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `endereco_ip` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `log` text COLLATE utf8_unicode_ci NOT NULL,
  `data` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `menu` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=80 ;

--
-- Dumping data for table `log`
--

INSERT INTO `log` (`id`, `usuario`, `operacao`, `endereco_ip`, `log`, `data`, `menu`) VALUES
(1, 1, 'LOGIN', '189.114.71.202', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-05-02 18:16:22', 'Home'),
(2, 1, 'LOGOFF', '189.114.71.202', 'O usuario saiu do Modulo Administrativo', '2012-05-02 18:37:05', 'Home'),
(3, 1, 'LOGIN', '189.114.71.202', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-05-02 18:50:14', 'Home'),
(4, 1, 'LOGOFF', '189.114.71.202', 'O usuario saiu do Modulo Administrativo', '2012-05-02 18:50:38', 'Home'),
(5, 1, 'LOGIN', '189.27.190.95', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-05-03 11:00:39', 'Home'),
(6, 1, 'LOGIN', '200.143.70.37', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-05-24 17:08:33', 'Home'),
(7, 1, 'LOGIN', '200.143.70.37', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-05-29 12:46:04', 'Home'),
(8, 1, 'LOGIN', '189.27.204.108', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-06-16 18:02:39', 'Home'),
(9, 1, 'LOGOFF', '189.27.204.108', 'O usuario saiu do Modulo Administrativo', '2012-06-16 20:55:03', 'Home'),
(10, 1, 'LOGIN', '200.143.70.37', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-23 15:43:25', 'Home'),
(11, 1, 'LOGOFF', '200.143.70.37', 'O usuario saiu do Modulo Administrativo', '2012-08-23 16:06:57', 'Home'),
(12, 1, 'LOGIN', '177.18.161.254', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-26 20:49:36', 'Home'),
(13, 1, 'LOGOFF', '177.18.161.254', 'O usuario saiu do Modulo Administrativo', '2012-08-26 23:07:07', 'Home'),
(14, 1, 'LOGIN', '177.18.160.166', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-28 02:00:12', 'Home'),
(15, 1, 'LOGIN', '177.18.160.166', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-28 10:53:41', 'Home'),
(16, 1, 'LOGOFF', '177.18.160.166', 'O usuario saiu do Modulo Administrativo', '2012-08-28 10:54:27', 'Home'),
(17, 2, 'LOGIN', '177.18.160.166', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-28 10:54:50', 'Home'),
(18, 2, 'LOGIN', '177.18.160.166', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-28 11:04:06', 'Home'),
(19, 2, 'LOGOFF', '177.18.160.166', 'O usuario saiu do Modulo Administrativo', '2012-08-28 11:04:19', 'Home'),
(20, 1, 'LOGIN', '200.143.70.37', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-28 12:51:58', 'Home'),
(21, 1, 'LOGOFF', '200.143.70.37', 'O usuario saiu do Modulo Administrativo', '2012-08-28 13:37:33', 'Home'),
(22, 2, 'LOGIN', '187.36.41.195', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-28 17:21:50', 'Home'),
(23, 2, 'LOGOFF', '187.36.41.195', 'O usuario saiu do Modulo Administrativo', '2012-08-28 17:43:28', 'Home'),
(24, 2, 'LOGIN', '187.36.41.195', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-28 17:43:58', 'Home'),
(25, 2, 'LOGOFF', '187.36.41.195', 'O usuario saiu do Modulo Administrativo', '2012-08-28 18:05:07', 'Home'),
(26, 1, 'LOGIN', '200.143.70.37', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-28 18:07:54', 'Home'),
(27, 2, 'LOGIN', '177.18.135.19', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-28 19:36:47', 'Home'),
(28, 1, 'LOGIN', '177.18.135.19', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-29 00:43:10', 'Home'),
(29, 2, 'LOGIN', '177.18.135.19', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-29 01:38:11', 'Home'),
(30, 2, 'LOGIN', '177.18.135.19', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-29 12:12:17', 'Home'),
(31, 1, 'LOGIN', '200.143.70.37', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-08-29 12:21:16', 'Home'),
(32, 1, 'LOGOFF', '200.143.70.37', 'O usuario saiu do Modulo Administrativo', '2012-08-29 12:47:22', 'Home'),
(33, 2, 'LOGIN', '187.36.41.195', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-04 19:15:35', 'Home'),
(34, 2, 'LOGOFF', '187.36.41.195', 'O usuario saiu do Modulo Administrativo', '2012-09-04 19:22:08', 'Home'),
(35, 2, 'LOGIN', '187.36.41.195', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-06 17:31:36', 'Home'),
(36, 1, 'LOGIN', '189.114.75.66', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-10 13:32:03', 'Home'),
(37, 1, 'LOGIN', '189.114.85.84', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-15 22:16:49', 'Home'),
(38, 1, 'LOGIN', '189.114.85.84', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-15 22:25:20', 'Home'),
(39, 1, 'LOGIN', '189.114.85.84', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-15 22:56:52', 'Home'),
(40, 1, 'LOGIN', '189.114.85.84', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-15 23:08:48', 'Home'),
(41, 1, 'LOGIN', '189.114.85.84', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-15 23:39:51', 'Home'),
(42, 1, 'LOGIN', '189.114.85.84', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-16 00:20:32', 'Home'),
(43, 1, 'LOGOFF', '189.114.85.84', 'O usuario saiu do Modulo Administrativo', '2012-09-16 00:21:33', 'Home'),
(44, 1, 'LOGIN', '189.114.85.84', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-16 00:38:12', 'Home'),
(45, 1, 'LOGIN', '189.114.85.84', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-16 00:48:06', 'Home'),
(46, 1, 'LOGOFF', '189.114.85.84', 'O usuario saiu do Modulo Administrativo', '2012-09-16 00:48:56', 'Home'),
(47, 1, 'LOGIN', '189.114.85.84', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-17 01:20:03', 'Home'),
(48, 1, 'LOGIN', '189.114.75.66', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-17 12:23:50', 'Home'),
(49, 1, 'LOGIN', '187.115.98.237', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-18 00:10:21', 'Home'),
(50, 1, 'LOGIN', '177.18.128.199', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-20 01:29:46', 'Home'),
(51, 1, 'LOGIN', '189.114.75.66', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-21 17:35:20', 'Home'),
(52, 1, 'LOGOFF', '189.114.75.66', 'O usuario saiu do Modulo Administrativo', '2012-09-21 17:35:41', 'Home'),
(53, 2, 'LOGIN', '187.36.40.134', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-24 13:01:23', 'Home'),
(54, 1, 'LOGIN', '189.114.75.66', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-24 16:04:47', 'Home'),
(55, 1, 'LOGOFF', '189.114.75.66', 'O usuario saiu do Modulo Administrativo', '2012-09-24 16:05:05', 'Home'),
(56, 1, 'LOGIN', '200.175.127.107', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-25 00:35:55', 'Home'),
(57, 1, 'LOGOFF', '200.175.127.107', 'O usuario saiu do Modulo Administrativo', '2012-09-25 01:04:54', 'Home'),
(58, 2, 'LOGIN', '200.175.127.107', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-25 01:05:07', 'Home'),
(59, 2, 'LOGOFF', '200.175.127.107', 'O usuario saiu do Modulo Administrativo', '2012-09-25 01:17:28', 'Home'),
(60, 1, 'LOGIN', '189.114.75.66', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-25 13:36:52', 'Home'),
(61, 1, 'LOGIN', '200.175.127.196', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-26 00:09:23', 'Home'),
(62, 1, 'LOGIN', '200.175.127.196', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-09-26 00:24:54', 'Home'),
(63, 1, 'LOGOFF', '200.175.127.196', 'O usuario saiu do Modulo Administrativo', '2012-09-26 00:25:35', 'Home'),
(64, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-11-01 12:47:19', 'Home'),
(65, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-11-01 12:48:32', 'Home'),
(66, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-11-03 20:16:03', 'Home'),
(67, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-11-03 20:16:13', 'Home'),
(68, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-11-06 01:48:47', 'Home'),
(69, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-11-06 01:48:52', 'Home'),
(70, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-11-13 21:02:11', 'Home'),
(71, 1, 'LOGIN', '127.0.0.1', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-11-14 14:42:09', 'Home'),
(72, 3, 'LOGIN', '189.114.75.66', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-12-07 15:57:19', 'Home'),
(73, 3, 'LOGOFF', '189.114.75.66', 'O usuario saiu do Modulo Administrativo', '2012-12-07 15:58:22', 'Home'),
(74, 3, 'LOGIN', '189.114.75.66', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-12-07 15:58:46', 'Home'),
(75, 3, 'LOGOFF', '189.114.75.66', 'O usuario saiu do Modulo Administrativo', '2012-12-07 16:00:07', 'Home'),
(76, 3, 'LOGIN', '189.114.75.66', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-12-07 16:15:00', 'Home'),
(77, 3, 'LOGOFF', '189.114.75.66', 'O usuario saiu do Modulo Administrativo', '2012-12-07 16:15:05', 'Home'),
(78, 3, 'LOGIN', '187.58.172.132', 'O usuario realizou o LOGIN no Modulo Administrativo', '2012-12-08 18:48:57', 'Home'),
(79, 3, 'LOGOFF', '187.58.172.132', 'O usuario saiu do Modulo Administrativo', '2012-12-08 18:49:56', 'Home');

-- --------------------------------------------------------

--
-- Table structure for table `menu`
--

CREATE TABLE IF NOT EXISTS `menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ordem` int(11) NOT NULL,
  `titulo` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `descricao` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `slug` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `data_criacao` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ultima_alteracao` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `autor` int(11) NOT NULL,
  `pagina` int(11) NOT NULL,
  `endereco` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `menu_pai` int(11) DEFAULT NULL,
  `nivel` int(11) NOT NULL,
  `key_words` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `locked` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'N',
  `status` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'A',
  `moderate_id` int(11) DEFAULT NULL,
  `draft` varchar(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `menu_slug_unique` (`slug`),
  KEY `menu_moderate_fk` (`moderate_id`),
  KEY `menu_pagina_fk` (`pagina`),
  KEY `menu_usuario_fk` (`autor`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=10 ;

--
-- Dumping data for table `menu`
--

INSERT INTO `menu` (`id`, `ordem`, `titulo`, `descricao`, `slug`, `data_criacao`, `ultima_alteracao`, `autor`, `pagina`, `endereco`, `menu_pai`, `nivel`, `key_words`, `locked`, `status`, `moderate_id`, `draft`) VALUES
(1, 0, 'MenuBar', 'Barra de Menus', 'menubar', '2012-09-18 00:18:39', '2012-09-18 00:18:39', 1, 155, '#', 1, 0, 'menu', 'N', 'A', NULL, NULL),
(2, 1, 'Index', 'Página Inicial do Site', 'index', '2012-09-18 00:19:32', '2012-09-18 00:19:32', 1, 5, '/index', 1, 0, 'Página Inicial do Site', 'N', 'A', NULL, NULL),
(3, 2, 'Empresa', 'Empresa', 'empresa', '2012-09-18 00:20:14', '2012-09-18 00:20:14', 1, 6, '/empresa', 1, 0, 'empresa', 'N', 'A', NULL, NULL),
(4, 3, 'Produtos', 'Produtos', 'produtos', '2012-09-18 00:20:51', '2012-09-18 00:20:51', 1, 7, '/produtos', 1, 0, 'produtos', 'N', 'A', NULL, NULL),
(5, 4, 'Serviços', 'Serviços', 'servicos', '2012-09-18 00:21:20', '2012-09-18 00:21:20', 1, 4, '/servicos', 1, 0, 'serviços', 'N', 'A', NULL, NULL),
(6, 5, 'Dicas', 'Dicas', 'dicas', '2012-09-18 00:21:44', '2012-09-18 00:21:44', 1, 9, '/dicas', 1, 0, 'dicas', 'N', 'A', NULL, NULL),
(7, 6, 'Fotos', 'Fotos', 'fotos', '2012-09-18 00:22:19', '2012-09-18 00:22:19', 1, 10, '/fotos', 1, 0, 'fotos', 'N', 'A', NULL, NULL),
(8, 7, 'Vídeos', 'Vídeos', 'videos', '2012-09-18 00:22:49', '2012-09-18 00:22:49', 1, 10, '/videos', 1, 0, 'videos', 'N', 'A', NULL, NULL),
(9, 8, 'Contato', 'Contato', 'contato', '2012-09-18 00:23:14', '2012-09-18 00:23:14', 1, 12, '/contato', 1, 0, 'contato', 'N', 'A', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `moderacao`
--

CREATE TABLE IF NOT EXISTS `moderacao` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data_hora` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `autor` int(11) NOT NULL,
  `onde` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `operacao` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `moderador` int(11) DEFAULT NULL,
  `data_hora_operacao` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `acao` varchar(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `detalhamento` text COLLATE utf8_unicode_ci,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=2 ;

--
-- Dumping data for table `moderacao`
--

INSERT INTO `moderacao` (`id`, `data_hora`, `autor`, `onde`, `operacao`, `moderador`, `data_hora_operacao`, `acao`, `detalhamento`) VALUES
(1, '2012-05-02 18:23:32', 1, '<a href=''javascript: void(0)'' onclick="popup(''http://www.equine_websiteurbo.com.br/site.fcgi/admin/editar/Pagina/1?op=moderate_on'')">Pagina</a>', 'Inserir', NULL, '2012-12-06 00:29:48', NULL, 'Inseriu a Pagina Empresa');

-- --------------------------------------------------------

--
-- Table structure for table `modulo`
--

CREATE TABLE IF NOT EXISTS `modulo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `class_name` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `slug` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `ativo` varchar(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `perfil_acesso` varchar(5) COLLATE utf8_unicode_ci DEFAULT 'A',
  `locked` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'N',
  `status` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'A',
  `moderate_id` int(11) DEFAULT NULL,
  `draft` varchar(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `modulo_titulo_uk` (`titulo`),
  KEY `modulo_moderate_fk` (`moderate_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=13 ;

--
-- Dumping data for table `modulo`
--

INSERT INTO `modulo` (`id`, `titulo`, `class_name`, `slug`, `ativo`, `perfil_acesso`, `locked`, `status`, `moderate_id`, `draft`) VALUES
(6, 'Enquetes', 'Enquete', 'enquetes', 'S', 'A', 'N', 'A', NULL, 'N'),
(5, 'Avisos', 'Aviso', 'avisos', 'S', 'A', 'N', 'A', NULL, 'N'),
(4, 'Páginas', 'Pagina', 'paginas', 'S', 'AO', 'N', 'A', NULL, 'N'),
(3, 'Menus', 'Menu', 'menus', 'S', 'A', 'N', 'A', NULL, 'N'),
(2, 'Templates', 'Template', 'templates', 'S', 'A', 'N', 'A', NULL, 'N'),
(1, 'Usuários', 'Usuario', 'usuarios', 'S', 'A', 'N', 'A', NULL, 'N'),
(8, 'Publicações', 'Publicacao', 'publicacoes', 'S', 'A', 'N', 'A', NULL, 'N'),
(9, 'Documentos', 'Documento', 'documentos', 'S', 'A', 'N', 'A', NULL, 'N'),
(10, 'Galerias', 'Galeria', 'galerias', 'S', 'A', 'N', 'A', NULL, 'N'),
(11, 'Parâmetros', 'Parametro', 'parametros', 'S', 'A', 'N', 'A', NULL, 'N'),
(12, 'Moderação', 'Moderacao', 'moderacao', 'S', 'AM', 'N', 'A', NULL, 'N'),
(7, 'Banners', 'Banner', 'banners', 'S', 'AO', 'N', 'A', NULL, 'N');

-- --------------------------------------------------------

--
-- Stand-in structure for view `noticias`
--
CREATE TABLE IF NOT EXISTS `noticias` (
`titulo` varchar(250)
,`slug` varchar(255)
,`intro` text
,`data_hora` timestamp
,`autor` varchar(255)
);
-- --------------------------------------------------------

--
-- Table structure for table `pagina`
--

CREATE TABLE IF NOT EXISTS `pagina` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `slug` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `data_criacao` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ultima_alteracao` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `autor` int(11) NOT NULL,
  `conteudo` text COLLATE utf8_unicode_ci NOT NULL,
  `descricao_completa` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `palavras_chaves` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `locked` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'N',
  `status` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'A',
  `moderate_id` int(11) DEFAULT NULL,
  `permite_comentario` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'N',
  `draft` varchar(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `pagina_titulo_uk` (`titulo`),
  KEY `pagina_moderate_fk` (`moderate_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=220 ;

--
-- Dumping data for table `pagina`
--

INSERT INTO `pagina` (`id`, `titulo`, `slug`, `data_criacao`, `ultima_alteracao`, `autor`, `conteudo`, `descricao_completa`, `palavras_chaves`, `locked`, `status`, `moderate_id`, `permite_comentario`, `draft`) VALUES
(93, 'Kit para Turbinamento Cod KT 1002', 'kit-para-turbinamento-cod-kt-1002', '2012-08-29 01:57:41', '2012-08-29 01:57:41', 1, '<p>P&aacute;gina em constru&ccedil;&atilde;o KT 1002</p>', 'Kit para Turbinamento de veículos KT 1002', 'kit, turbinamento, motores', 'N', 'A', NULL, 'S', 'N'),
(25, 'Kit para reparo', 'kit-para-reparo', '2012-05-18 01:21:46', '2012-08-29 02:04:23', 1, '<h1>Kits para Reparo</h1>\n<p>P&aacute;gina em constru&ccedil;&atilde;o.</p>', 'Produtos', 'produtos, turbos, turbinamento, peças', 'N', 'A', NULL, 'S', 'N'),
(22, 'Turbos Remanufaturados', 'turbos-remanufaturados', '2012-05-18 01:20:22', '2012-05-18 01:20:22', 1, '<p>P&aacute;gina em constru&ccedil;&atilde;o.</p>', 'Produtos', 'produtos, turbos, turbinamento, peças', 'N', 'A', NULL, 'N', 'N'),
(23, 'Turbos novos para diversas linhas', 'turbos-novos-para-diversas-linhas', '2012-05-18 01:21:00', '2012-05-18 01:21:00', 1, '<p>P&aacute;gina em constru&ccedil;&atilde;o.</p>', 'Produtos', 'produtos, turbos, turbinamento, peças', 'N', 'A', NULL, 'S', 'N'),
(26, 'Remanufatura de Turbos', 'remanufatura-de-turbos', '2012-05-18 01:23:04', '2012-05-18 01:23:04', 1, '<p>P&aacute;gina em constru&ccedil;&atilde;o.</p>', 'Serviços', 'Remanufatura de Turbos', 'N', 'A', NULL, 'N', 'N'),
(27, 'Instalação de Turbos', 'instalacao-de-turbos', '2012-05-18 01:23:36', '2012-05-18 01:23:36', 1, '<p>P&aacute;gina em constru&ccedil;&atilde;o.</p>', 'Serviços', 'instação, turbo', 'N', 'A', NULL, 'N', 'N'),
(29, 'Returbinamento de Caminhonetes Importadas', 'returbinamento-de-caminhonetes-importadas', '2012-05-18 01:25:26', '2012-05-18 01:25:26', 1, '<p>P&aacute;gina em constru&ccedil;&atilde;o.</p>', 'Serviços', 'serviços', 'N', 'A', NULL, 'N', 'N'),
(30, 'Testes de intercooler', 'testes-de-intercooler', '2012-05-18 01:26:00', '2012-05-18 01:26:00', 1, '<p>P&aacute;gina em constru&ccedil;&atilde;o.</p>', 'Serviços', 'serviços', 'N', 'A', NULL, 'N', 'N'),
(28, 'Turbinamento de Caminhonetes e Caminhões', 'turbinamento-de-caminhonetes-e-caminhoes', '2012-05-18 01:24:50', '2012-05-18 01:24:50', 1, '<p>P&aacute;gina em constru&ccedil;&atilde;o.</p>', 'Serviços', 'serviços', 'N', 'A', NULL, 'N', 'N'),
(17, 'Suporte Rede SOS', 'suporte-rede-sos', '2012-05-18 01:02:23', '2012-06-16 18:13:10', 1, '<h1><span>Suporte</span></h1>\n<p>Com uma equipe altamente qualificada e preparada, o suporte &eacute; dado diretamente na oficina.</p>\n<p>Venha nos fazer uma visita.</p>', 'Suporte da Rede SOS Turbo', 'suporte, formulário de contato', 'N', 'A', NULL, 'N', 'N'),
(21, 'Mangueiras para turbos e intercoolers', 'mangueiras-para-turbos-e-intercoolers', '2012-05-18 01:19:54', '2012-08-23 16:03:48', 1, '<h1><span>Mangueiras para Turbos e Intercoolers</span></h1>\n<p>P&aacute;gina em constru&ccedil;&atilde;o.</p>', 'Produtos', 'produtos, turbos, turbinamento, peças', 'N', 'A', NULL, 'S', 'N'),
(24, 'Peças para remanufaturas', 'pecas-para-remanufaturas', '2012-05-18 01:21:24', '2012-08-26 21:49:25', 1, '<p>P&aacute;gina em constru&ccedil;&atilde;o.</p>', 'Produtos', 'produtos, turbos, turbinamento, peças', 'N', 'A', NULL, 'N', 'N'),
(19, 'Juntas para Turbo', 'juntas-para-turbo', '2012-05-18 01:18:15', '2012-08-26 22:03:36', 1, '<h1><span>Juntas para Turbo</span></h1>\n<p><strong>Descri&ccedil;&atilde;o do produto</strong>: XYZ</p>\n<p><strong>Especifica&ccedil;&atilde;o T&eacute;cnica</strong>: XYX</p>\n<p style="text-align: center;">&nbsp;</p>\n<p style="text-align: center;">Aqui deve inserir videos ou fotos.</p>\n<p>&nbsp;</p>', 'Juntas para Turbo', 'juntas, turbo, peça para turbo', 'N', 'A', NULL, 'N', 'N'),
(16, 'Informe Rede SOS Turbo', 'informe-rede-sos-turbo', '2012-05-18 01:01:21', '2012-08-26 22:08:31', 1, '<h1><span>Informativo Rede SOS Turbo</span></h1>\n<p>Assine o nosso informativo e mantenha-se informado com as &uacute;ltimas novidades da nossa empresa.</p>\n<div style="width: 370px; margin: 0px auto; margin-top: 50px;"><form id="informe" action="/informe-rede-sos-turbo" method="post"> <span class="nome_field">Nome:</span> <input id="nome" class="fields" title="Informe o seu nome." name="nome" size="50" type="text" /> <br /><br /> <span class="fields">E-mail:</span> <input id="email" class="fields" title="Informe o seu e-mail." name="email" size="50" type="text" /> <br /><br /> <button> Enviar </button> </form></div>', 'Informativo da Rede SOS Turbo', 'informe, informativo', 'N', 'A', NULL, 'N', 'N'),
(15, 'Trabalhe Conosco', 'trabalhe-conosco', '2012-05-18 01:00:23', '2012-08-26 22:47:53', 1, '<h1><span>Trabalhe Conosco</span></h1>\n<div style="width: 370px; margin: 0px auto; margin-top: 50px;"><form id="contato" action="/trabalhe-conosco" enctype="multipart/form-data" method="post"> <span class="nome_field">Nome:</span> <input id="nome" class="fields" title="Informe o seu nome." name="nome" size="50" type="text" /> <br /><br /> <span class="fields">Telefone:</span> <input id="telefone" class="fields" title="Informe o seu telefone." name="telefone" size="50" type="text" /> <br /><br /> <span class="fields">E-mail:</span> <input id="email" class="fields" title="Informe o seu e-mail." name="email" size="50" type="text" /> <br /><br /> <span class="fields">Curriculo:</span> <input id="curriculo" class="fields" title="Envie o seu cirriculo." name="curriculo" size="50" type="file" /> <br /><br /> <span class="fields">Mensagem:</span> <textarea id="mensagem" title="Deixe sua mensagem." cols="50" rows="10" name="mensagem"></textarea> <br /><br /> <button> Enviar </button> </form></div>', 'Trabalhe Conosco', 'curriculo, trabalhe conosco, formulário de cadastro de curriculo, rh', 'N', 'A', NULL, 'N', 'N'),
(13, 'Localização', 'localizacao', '2012-05-18 00:57:06', '2012-08-28 10:56:08', 2, '<h1><span>Contato</span></h1>\n<p>P&aacute;gina em constru&ccedil;&atilde;o.</p>', 'Mapa de Localização', 'mapa, localização, endereço', 'N', 'A', NULL, 'N', 'N'),
(9, 'Dicas', 'dicas', '2012-05-18 00:54:41', '2012-08-28 11:00:11', 2, '<h1><span>Dicas</span></h1>\n<p><span>P&aacute;gina em Constru&ccedil;&atilde;o.</span></p>', 'Dicas sobre o nosso segmento de mercado', 'dicas', 'N', 'A', NULL, 'N', 'N'),
(11, 'Vendas', 'vendas', '2012-05-18 00:55:44', '2012-05-18 00:55:44', 1, '<p>P&aacute;gina em constru&ccedil;&atilde;o.</p>', 'Nosso setor comercial', 'vendas, comercial, setor comercial, setor de vendas', 'N', 'A', NULL, 'N', 'N'),
(14, 'Responsabilidade Ambiental', 'responsabilidade-ambiental', '2012-05-18 00:59:27', '2012-05-29 14:48:23', 1, '<h1><span>Rede Sos Turbo - Responsabilidade com o Meio Ambiente</span></h1>\n<p>A Rede Sos Turbo tem como um de seus princ&iacute;pios basilares a permanente aten&ccedil;&atilde;o e responsabilidade com o meio ambiente em que vivemos. Consciente de que a natureza &eacute; um bem de todos e que deve ser preservada para as gera&ccedil;&otilde;es futuras, a empresa assume seu compromisso atrav&eacute;s de iniciativas totalmente orientadas para a responsabilidade s&oacute;cio-ambiental, o desenvolvimento sustent&aacute;vel e a qualidade de vida.</p>\n<p>S&atilde;o m&uacute;ltiplos os programas desenvolvidos pela Rede Sos Turbo que visam reduzir, reutilizar e reciclar os res&iacute;duos industriais, garantir a preven&ccedil;&atilde;o da polui&ccedil;&atilde;o de suas fontes geradoras, e promover a educa&ccedil;&atilde;o ambiental entre seus colaboradores e a comunidade. Al&eacute;m disso, as a&ccedil;&otilde;es atendem rigorosamente &agrave; legisla&ccedil;&atilde;o em todos os &acirc;mbitos, Federal, Estadual e Municipal.</p>\n<p>&nbsp;</p>\n<p style="text-align: center;"><img style="margin: 0px auto;" title="Responsabilidade Ambiental." src="../../../../static/images/img-respamb.jpg" alt="Responsabilidade Ambiental." /></p>', 'Responsabilidade Ambiental da Rede SOS Turbo', 'responsabilidade, ambiental, meio ambiente, preservação da natureza', 'N', 'A', NULL, 'N', 'N'),
(5, 'index', 'index', '2012-05-18 00:32:04', '2012-09-06 18:10:34', 2, ' ', 'Clínica de Hipiatria, com serviços de cirurgia e fisioterapia em Viamão - RS', 'hipiatria, clinica, cirurgia, fisioterapia, equino', 'N', 'A', NULL, 'N', 'N'),
(12, 'Contato', 'contato', '2012-05-18 00:56:37', '2012-05-24 17:26:46', 1, '<p>$def with ()  $var title:  Rede SOS Turbo - Turbinamento de autom&oacute;veis e turbinamento industrial em Porto Alegre/RS $var full_description: Turbinamento de autom&oacute;veis, caminh&otilde;es e caminhonetes em Porto Alegre - RS. $var keywords_tags: turbo, turbinamento, caminh&atilde;o, caminhonete, autom&oacute;vel</p>\n<div id="contact_panel">\n<div id="contact_panel_left">\n<div id="contact_panel_left_body"><span id="intro">Tire suas d&uacute;vidas, d&ecirc; opini&otilde;es. Todos os canais da Rede SOS Turbo est&atilde;o abertos para atend&ecirc;-lo.</span>\n<div id="contact_panel_left_body_top"><span class="contato_field">Contato</span> <img src="../../../static/images/img_fone.gif" alt="" width="140" height="22" /> <span class="contato_email_field"> <a title="E-mail geral da Rede SOS Turbo." href="mailto:contato@equine_websiteurbo.com.br">contato@equine_websiteurbo.com.br</a> </span></div>\n<div id="contact_panel_left_body_bottom"><span class="localizacao_field">Localiza&ccedil;&atilde;o</span> <span class="endereco_field">Rua Augusto Severo, 652 - Bairro S&atilde;o Jo&atilde;o<br />Cep 90240-480 - Porto Alegre - RS</span> <br /> <small><a class="link_mapa" href="http://maps.google.com.br/maps?q=-30.001678,-51.188899&amp;num=1&amp;sll=-14.179186,-50.449219&amp;sspn=44.419463,47.900391&amp;ie=UTF8&amp;ll=-30.00169,-51.188908&amp;spn=0.004646,0.006931&amp;z=15&amp;source=embed" target="_blank">Exibir mapa ampliado</a></small></div>\n</div>\n<div>\n<div id="contact_panel_right">\n<div id="contact_panel_right_body"><span class="intro">Envie sugest&otilde;es e fa&ccedil;a suas solicita&ccedil;&otilde;es preenchendo o formul&aacute;rio:</span> <form id="contato" action="/contato" method="post"> <span class="nome_field">Nome:</span> <input id="nome" class="fields" title="Informe o seu nome." name="nome" type="text" /> <span class="fields">Telefone:</span> <input id="telefone" class="fields" title="Informe o seu telefone." name="telefone" type="text" /> <span class="fields">E-mail:</span> <input id="email" class="fields" title="Informe o seu e-mail." name="email" type="text" /> <span class="fields">Departamento:</span> <select id="departamento" class="fields" title="Selecione o departamento." name="departamento"> <option value="vendas@equine_websiteurbo.com.br">Vendas</option> <option value="mauro@equine_websiteurbo.com.br">Oficina</option> <option value="logistica@equine_websiteurbo.com.br">Log&iacute;stica</option> <option value="contato@equine_websiteurbo.com.br">RH</option> <option value="nfe@equine_websiteurbo.com.br">Fin&acirc;nceiro</option> </select> <span class="fields">Assunto:</span> <input id="assunto" class="fields" title="Informe o assunto." name="assunto" type="text" /> <span class="fields">Mensagem:</span> <textarea id="mensagem" title="Deixe sua mensagem." cols="20" rows="10" name="mensagem"></textarea> <button>Enviar</button> </form></div>\n</div>\n</div>\n</div>\n</div>', 'Formulário de Contato', 'contato, form', 'N', 'A', NULL, 'N', 'N'),
(2, 'Agradece', 'agradece', '2012-05-24 17:29:03', '2012-08-28 18:02:32', 2, '<h1><span>Obrigado pelo seu contato</span></h1>\n<p>Obrigado pela mensagem !. Em breve estaremos entrando em contato.</p>', 'Agradecimento do contato', 'agradecimento', 'N', 'A', NULL, 'N', 'N'),
(62, 'Kit para Turbinamento Cod KT 1001', 'kit-para-turbinamento-cod-kt-1001', '2012-08-29 01:48:49', '2012-08-29 01:48:49', 1, '<h1>Kit para Turbinamento de ve&iacute;culos KT 1001</h1>\n<p>&nbsp;</p>\n<table border="0" align="center">\n<tbody>\n<tr>\n<td><img title="Kit de Turbinamento." src="../../../static/images/001.jpg" alt="Foto do Kit" width="98" height="90" /></td>\n<td style="text-align: center;"><strong>Detalhes T&eacute;cnicos</strong></td>\n</tr>\n<tr>\n<td>&nbsp;</td>\n<td>&nbsp;50 X 10 cor preta.</td>\n</tr>\n</tbody>\n</table>', 'Kit para Turbinamento de veículos KT 1001', 'kit, turbinamento, motores', 'N', 'A', NULL, 'S', 'N'),
(18, 'Kit para Turbinamento', 'kit-para-turbinamento', '2012-05-18 01:16:47', '2012-08-29 02:08:24', 1, '<h1>Kits para Turbinamento</h1>\n<p>&nbsp;</p>\n<table style="text-align: center;" border="1">\n<tbody>\n<tr>\n<td><img src="../../../static/images/001.jpg" alt="" width="98" height="90" /></td>\n<td>&nbsp;<img src="../../../static/images/014.jpg" alt="" width="98" height="90" /></td>\n<td>&nbsp;</td>\n<td>&nbsp;</td>\n<td>&nbsp;</td>\n<td>&nbsp;</td>\n<td>&nbsp;</td>\n<td>&nbsp;</td>\n<td>&nbsp;</td>\n<td>&nbsp;</td>\n<td>&nbsp;</td>\n<td>&nbsp;</td>\n<td>&nbsp;</td>\n<td>&nbsp;</td>\n<td>&nbsp;</td>\n</tr>\n<tr>\n<td style="text-align: center;"><a href="../../../produto/kit-para-turbinamento-cod-kt-1001">KT 1001</a></td>\n<td><a href="../../../produto/kit-para-turbinamento-cod-kt-1002">KT 1002&nbsp;</a></td>\n<td>&nbsp;</td>\n<td>&nbsp;</td>\n<td>&nbsp;</td>\n<td>&nbsp;</td>\n<td>&nbsp;</td>\n<td>&nbsp;</td>\n<td>&nbsp;</td>\n<td>&nbsp;</td>\n<td>&nbsp;</td>\n<td>&nbsp;</td>\n<td>&nbsp;</td>\n<td>&nbsp;</td>\n<td>&nbsp;</td>\n</tr>\n</tbody>\n</table>', 'Kit para Turbinamento de veículos', 'kit, turbinamento, motores', 'N', 'A', NULL, 'N', 'N'),
(7, 'produtos', 'produtos', '2012-05-18 00:53:00', '2012-08-29 02:12:42', 1, '<h1>Produtos</h1>\n<p>Conhe&ccedil;a a nossa completa linha de produtos.</p>\n<table style="margin: 0px auto; width: 90%;" border="0">\n<tbody>\n<tr style="height: 150px; text-align: center;" align="center">\n<td style="vertical-align: top; width: 110px; text-align: center;"><img style="background-color: #eeeeee; padding: 3px; border: 1px solid #ccc; display: block;margin:0px auto;margin-bottom:10px;" title="Kit para turbinamento" src="../../../static/images/001.jpg" alt="Kit para turbinamento" /><a style="text-decoration:none;font-weight:bold;font-size:13px;" title="Kit para turbinamento" href="../../../produto/kit-para-turbinamento">Kits para tubinamento</a></td>\n<td style="vertical-align: top; width: 110px; text-align: center;"><img style="background-color: #eee;padding: 03px;border:01px solid #ccc; display: block;margin:0px auto;margin-bottom:10px;" title="Juntas para turbo" src="../../../static/images/002.jpg" alt="Juntas para turbo" width="98" height="90" /><a style="text-decoration:none;font-weight:bold;font-size:13px;" title="Juntas para turbo" href="../../../produto/juntas-para-turbo">Juntas para turbo</a></td>\n<td style="vertical-align: top; width: 110px; text-align: center;"><img style="background-color: #eee;padding: 03px;border:01px solid #ccc; display: block;margin:0px auto;margin-bottom:10px;" title="Man&ocirc;metros" src="../../../static/images/003.jpg" alt="Man&ocirc;metros" width="98" height="90" /><a style="text-decoration:none;font-weight:bold;font-size:13px;" title="Man&ocirc;metros" href="../../../produto/manometros">Man&ocirc;metros</a></td>\n<td style="vertical-align: top; width: 110px; text-align: center;"><img style="background-color: #eee;padding: 03px;border:01px solid #ccc; display: block;margin:0px auto;margin-bottom:10px;" title="Mangueiras para turbos e intercoolers" src="../../../static/images/001.jpg" alt="Mangueiras para turbos e intercoolers" /><a style="text-decoration:none;font-weight:bold;font-size:13px;" title="Mangueiras para turbos e intercoolers" href="../../../produto/mangueiras-para-turbos-e-intercoolers">Mangueiras para turbos e intercoolers</a></td>\n</tr>\n<tr style="height: 150px;">\n<td style="vertical-align: top; width: 110px; text-align: center;"><img style="background-color: #eee;padding: 03px;border:01px solid #ccc;display: block;margin:0px auto;margin-bottom:10px;" title="Turbos remanufaturados" src="../../../static/images/51.jpg" alt="Turbos remanufaturados" width="98" height="90" /><a style="text-decoration:none;font-weight:bold;font-size:13px;" title="Turbos remanufaturados" href="../../../produto/turbos-remanufaturados">Turbos remanufaturados</a></td>\n<td style="vertical-align: top; width: 110px; text-align: center;"><img style="background-color: #eee;padding: 03px;border:01px solid #ccc;display: block;margin:0px auto;margin-bottom:10px;" title="Turbos novos para diversas linhas" src="../../../static/images/turbos_novos.jpg" alt="Turbos novos para diversas linhas" /><a style="text-decoration:none;font-weight:bold;font-size:13px;" title="Turbos novos para diversas linhas" href="../../../produto/turbos-novos-para-diversas-linhas">Turbos novos para diversas linhas</a></td>\n<td style="vertical-align: top; width: 110px; text-align: center;"><img style="background-color: #eee;padding: 03px;border:01px solid #ccc;display: block;margin:0px auto;margin-bottom:10px;" title="Pe&ccedil;as para remanufaturas" src="../../../static/images/peca_remanufaturada.jpg" alt="Pe&ccedil;as para remanufaturas" width="98" height="90" /><a style="text-decoration: none; font-weight: bold; font-size: 13px;" title="Pe&ccedil;as para remanufaturas" href="../../../produto/pecas-para-remanufaturas">Pe&ccedil;as para remanufaturas</a></td>\n<td style="vertical-align: top; width: 110px; text-align: center;"><img style="background-color: #eee;padding: 03px;border:01px solid #ccc;display: block;margin:0px auto;margin-bottom:10px;" title="Kit para reparo" src="../../../static/images/kit_para_reparo.jpg" alt="Kit para reparo" width="98" height="90" /><a style="text-decoration:none;font-weight:bold;font-size:13px;" title="Kit para reparo" href="../../../produto/kit-para-reparo">Kit para reparo</a></td>\n</tr>\n</tbody>\n</table>', 'Listagem de Produtos da Rede SOS Turbo', 'produtos, turbos, turbinamento, peças', 'N', 'A', NULL, 'N', 'N'),
(124, 'Manômetro Foto 06', 'manometro-foto-06', '2012-08-29 02:18:19', '2012-08-29 02:18:19', 1, '<p>P&aacute;gina de detalhe do manometro foto 06</p>', 'Manômetros', 'manometros', 'N', 'A', NULL, 'S', 'N'),
(31, 'Manômetros', 'manometros', '2012-08-28 13:30:15', '2012-08-29 02:19:01', 1, '<h1><span>Man&ocirc;metros</span></h1>\n<table border="1" align="center">\n<tbody>\n<tr>\n<td>foto 01</td>\n<td>foto 02</td>\n<td>foto 03</td>\n<td>foto 04</td>\n<td>foto 05</td>\n<td>foto 06</td>\n<td>foto 07</td>\n<td>foto 08</td>\n</tr>\n<tr>\n<td>codigo 01</td>\n<td>codigo 02</td>\n<td>codigo</td>\n<td>codigo03</td>\n<td>codigo 04</td>\n<td><a href="../../../produto/manometro-foto-06">detalhe</a></td>\n<td>detalhe</td>\n<td>detalhe</td>\n</tr>\n</tbody>\n</table>', 'Manômetros', 'manometros', 'N', 'A', NULL, 'S', 'N'),
(3, 'Agradece Informativo', 'agradece-informativo', '2012-06-16 18:27:49', '2012-09-15 23:40:09', 1, '<h1><span>Obrigado pelo seu cadastro</span></h1>\n<p>Em breve voc&ecirc; estar&aacute; recebendo o nosso informativo.</p>', 'Agradece pelo cadastro no informativo', 'agradecimento, contato, contato pelo site', 'N', 'A', NULL, 'S', 'N'),
(155, 'no-page', 'no-page', '2012-09-18 00:17:55', '2012-09-18 00:17:55', 1, '<p>no page.</p>', 'no-page', 'no page', 'N', 'A', NULL, 'N', 'N'),
(186, 'Vídeos', 'videos', '2012-09-25 00:50:42', '2012-09-25 00:52:18', 1, '<h1><span>V&iacute;deos</span></h1>\n<p><span>P&aacute;gina em Constru&ccedil;&atilde;o.</span></p>', 'Galeria de Vídeos', 'galerias, vídeos', 'N', 'A', NULL, 'N', 'N');
INSERT INTO `pagina` (`id`, `titulo`, `slug`, `data_criacao`, `ultima_alteracao`, `autor`, `conteudo`, `descricao_completa`, `palavras_chaves`, `locked`, `status`, `moderate_id`, `permite_comentario`, `draft`) VALUES
(10, 'Fotos', 'fotos', '2012-05-18 00:55:07', '2012-09-25 00:48:23', 1, '<p style="text-align: center;"><strong><span style="font-family: arial black,avant garde;"><span style="font-size: large;">Balanceadora de Conjunto rotativo Equipamento de &uacute;ltima gera&ccedil;&atilde;o Marca Turbo Technics</span></span></strong></p>\n<p style="text-align: center;"><br /><img src="data:image/jpeg;base64,/9j/4TS2RXhpZgAATU0AKgAAAAgACwEOAAIAAAAgAAAIngEPAAIAAAAFAAAIvgEQAAIAAAAJAAAIxAESAAMAAAABAAEAAAEyAAIAAAAUAAAIzgITAAMAAAABAAI/gIdpAAQAAAABAAAI4pybAAEAAABAAAA0EpyfAAEAAABAAAA0UsSlAAcAAAAcAAA0kuocAAcAAAgMAAAAkgAAAAAc6gAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAAU09OWQAARFNDLVcxMjAAADIwMDg6MDE6MDQgMjM6MDI6MjQAACGCmgAFAAAAAQAAEoCCnQAFAAAAAQAAEoiIIgADAAAAAQACAACIJwADAAAAAQGQAACQAAAHAAAABDAyMjGQAwACAAAAFAAAEpCQBAACAAAAFAAAEqSRAQAHAAAABAECAwCRAgAFAAAAAQAAEriSBAAFAAAAAQAAEsCSBQAFAAAAAQAAEsiSBwADAAAAAQAFAACSCAADAAAAAQAAAACSCQADAAAAAQAPAACSCgAFAAAAAQAAEtCSfAAHAAAhOAAAEtiSkQACAAAAAzAwAACSkgACAAAAAzAwAACgAAAHAAAABDAxMDCgAQADAAAAAQABAACgAgAEAAAAAQAAAoCgAwAEAAAAAQAAAeCjAAAHAAAAAQMAUwCjAQAHAAAAAQEAYQCkAQADAAAAAQAAAGOkAgADAAAAAQAAAG2kAwADAAAAAQAAAACkBgADAAAAAQAAAEakCAADAAAAAQAAAACkCQADAAAAAQAAAACkCgADAAAAAQAAAADqHAAHAAAIDAAACnTqHQAJAAAAAQAAEFwAAAAAHOoAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA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dCBiZWdpbj0n77u/JyBpZD0nVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkJz8+DQo8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIj48cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPjxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSJ1dWlkOmZhZjViZGQ1LWJhM2QtMTFkYS1hZDMxLWQzM2Q3NTE4MmYxYiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIj48eG1wOkNyZWF0ZURhdGU+MjAwOC0wMS0wNFQyMzowMjoyNDwveG1wOkNyZWF0ZURhdGU+PC9yZGY6RGVzY3JpcHRpb24+PHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9InV1aWQ6ZmFmNWJkZDUtYmEzZC0xMWRhLWFkMzEtZDMzZDc1MTgyZjFiIiB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iLz48cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0idXVpZDpmYWY1YmRkNS1iYTNkLTExZGEtYWQzMS1kMzNkNzUxODJmMWIiIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyI+PGRjOnRpdGxlPjxyZGY6QWx0IHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+PHJkZjpsaSB4bWw6bGFuZz0ieC1kZWZhdWx0Ij4NCgkJCQkJPC9yZGY6bGk+PC9yZGY6QWx0Pg0KCQkJPC9kYzp0aXRsZT48ZGM6ZGVzY3JpcHRpb24+PHJkZjpBbHQgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj48cmRmOmxpIHhtbDpsYW5nPSJ4LWRlZmF1bHQiPg0KCQkJCQk8L3JkZjpsaT48L3JkZjpBbHQ+DQoJCQk8L2RjOmRlc2NyaXB0aW9uPjwvcmRmOkRlc2NyaXB0aW9uPjwvcmRmOlJERj48L3g6eG1wbWV0YT4NCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgPD94cGFja2V0IGVuZD0ndyc/Pv/bAEMAAQEBAQEBAQEBAQEBAQICAwICAgICBAMDAgMFBAUFBQQEBAUGBwYFBQcGBAQGCQYHCAgICAgFBgkKCQgKBwgICP/bAEMBAQEBAgICBAICBAgFBAUICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICP/AABEIAeACgAMBIQACEQEDEQH/xAAfAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgv/xAC1EAACAQMDAgQDBQUEBAAAAX0BAgMABBEFEiExQQYTUWEHInEUMoGRoQgjQrHBFVLR8CQzYnKCCQoWFxgZGiUmJygpKjQ1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4eLj5OXm5+jp6vHy8/T19vf4+fr/xAAfAQADAQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgv/xAC1EQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2gAMAwEAAhEDEQA/AP1Qt4sDKYVOuB3FWktiW3BcZ7Z6+/8A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', 'fotos', 'galerias, fotos', 'N', 'A', NULL, 'N', 'N');
INSERT INTO `pagina` (`id`, `titulo`, `slug`, `data_criacao`, `ultima_alteracao`, `autor`, `conteudo`, `descricao_completa`, `palavras_chaves`, `locked`, `status`, `moderate_id`, `permite_comentario`, `draft`) VALUES
(4, 'Serviços', 'servicos', '2012-08-28 13:03:39', '2012-11-03 20:59:42', 1, '<h1>Servi&ccedil;os</h1>\n<ul id="menu_servicos">\n<li> <a id="clinica-hipiatria" style="color:#DB4308;" title="Cl&iacute;nica de hipiatria." onclick="return activeTab(this, ''panelClinica'');" href="#">Cl&iacute;nica</a> </li>\n<li> <a id="fisioterapia" title="Servi&ccedil;o de fisioterapia." onclick="return activeTab(this, ''panelFisioterapia'');" href="#">Fisioterapia</a> </li>\n<li> <a id="cirurgia" title="Cl&iacute;nica de cirurgia." onclick="return activeTab(this, ''panelCirurgia'');" href="#">Cirurgia</a> </li>\n<li> <a id="odontologia" title="Cl&iacute;nica de odontologia." onclick="return activeTab(this, ''panelOdontologia'');" href="#">Odontologia</a> </li>\n<li> <a id="internacao" title="Cl&iacute;nica de interna&ccedil;&atilde;o." onclick="return activeTab(this, ''panelInternacao'');" href="#">Interna&ccedil;&atilde;o</a> </li>\n<li> <a id="atendimento-a-domicilio" title="Servi&ccedil;o de atendimento &agrave; domic&iacute;lio." onclick="return activeTab(this, ''panelAtendimento'');" href="#">Atendimento a Domicilio</a> </li>\n<li> <a id="consultoria-a-eventos" title="Servi&ccedil;o de consultoria &agrave; eventos." onclick="return activeTab(this, ''panelConsultoria'');" href="#">Consultoria a Eventos</a> </li>\n<li> <a id="formacao-continuada" title="Servi&ccedil;o de forma&ccedil;&atilde;o continuada." onclick="return activeTab(this, ''panelFormacao'');" href="#">Forma&ccedil;&atilde;o Continuada</a> </li>\n</ul>\n<p id="panelClinica" class="servico_description" style="display:block;">A Equine Clinic disp&otilde;e de M&eacute;dicos Veterin&aacute;rios especialistas em cl&iacute;inica de equinos, com larga experi&ecirc;ncia nesta &aacute;rea, adquirida atrav&eacute;s de anos de trabalho e diversos cursos de aprimoramento. O que faz da Equine Clinic uma refer&ecirc;ncia nesta &aacute;rea.                     <img style="width: 90%; height: 90%; display: block; margin: 0px auto; padding: 05px; background-color: white; border: 01px solid #ccc; margin-top: 10px;" src="../../../static/images/assessoria_.jpg" alt="" /></p>\n<p id="panelFisioterapia" class="servico_description">A Equine Clinic tem uma moderna estrutura voltada a fisioterapia, dispondo de t&eacute;cnicas e de aparelhagem de &uacute;ltima gera&ccedil;&atilde;o, proporcionando aos clientes um trabalho diferenciado na fisioterapia e na reabilita&ccedil;&atilde;o de equinos.</p>\n<p id="panelCirurgia" class="servico_description">A cirurgia em equinos tem um papel de destaque na Equine Clinic. Com o objetivo de garantir o Bem Estar Animal e a satisfa&ccedil;&atilde;o dos clientes, nos qualificamos para a realiza&ccedil;&atilde;o de cirurgias nas diversas &aacute;reas, como locomotor e g&aacute;strico, entre outros.</p>\n<p id="panelOdontologia" class="servico_description">A Equine Clinic presta um servi&ccedil;o de excel&ecirc;ncia na &aacute;rea odontol&oacute;gica, dispondo de moderna aparelhagem, realizando diversos servi&ccedil;os, como ajustes de oclus&atilde;o dent&aacute;ria e at&eacute; extra&ccedil;&otilde;es cir&uacute;rgicas.</p>\n<p id="panelInternacao" class="servico_description">A Equine Clinic disp&otilde;e de uma &oacute;tima estrutura de interna&ccedil;&atilde;o para equinos, com baias amplas e ventiladas, contando ainda com estruturas de manejo e conten&ccedil;&atilde;o de equinos. A Equine Clinic ainda conta com uma equipe de apoio capacitada para os plant&otilde;es de interna&ccedil;&atilde;o.</p>\n<p id="panelAtendimento" class="servico_description">A equipe da Equine Clinic est&aacute; preparada para este modelo de atendimento, prestando diversos servi&ccedil;os nesta modalidade, favorecendo o conforto do animal e a facilidade do propriet&aacute;rio. A &aacute;rea de atua&ccedil;&atilde;o para atendimento a domicilio est&aacute; restrita aos estados do Rio Grande do Sul e Santa Catarina.</p>\n<p id="panelConsultoria" class="servico_description">A Equine Clinic tem desenvolvido diversos trabalhos em Cavalgadas, Rodeios, Concursos H&iacute;picos, Cinema e outros eventos, com atividades cl&iacute;nicas e principalmente na garantia do Bem Estar animal.</p>\n<p id="panelFormacao" class="servico_description">A Equine Clinic est&aacute; organizada de maneira a oferecer oportunidades diversas de forma&ccedil;&atilde;o continuada, atrav&eacute;s de work shop, palestras e est&aacute;gios vivenciais, usando a atividade di&aacute;ria da cl&iacute;nica como base pedag&oacute;gica no desenvolvimento deste trabalho.</p>\n<p>\n<script type="text/javascript">// <![CDATA[\n        function activeTab(obj, panel){\n            menu = document.getElementById(''menu_servicos'');\n            itens = menu.getElementsByTagName(''a'');\n            for(var x=0;x<itens.length;x++){\n                if (itens[x].id==obj.id){\n                    itens[x].style.color=''#DB4308'';\n                } else {\n                    itens[x].style.color=''blue'';\n                }\n            }\n            left_panel = document.getElementById(''left_panel'');\n            pes = left_panel.getElementsByTagName(''p'');\n            for(var i=0;i<pes.length;i++){\n                if (pes[i].id==panel){\n                    //alert(panel);\n                    pes[i].style.display=''block'';\n                } else {\n                    //alert(pes[i]);\n                    pes[i].style.display=''none'';\n                };\n            }\n            return false;\n        }\n// ]]></script>\n</p>', 'Clínica de Hipiatria, com serviços de cirurgia e fisioterapia em Viamão - RS', 'hipiatria, clinica, cirurgia, fisioterapia, equino', 'N', 'A', NULL, 'S', 'N'),
(6, 'Quem Somos', 'quem-somos', '2012-12-07 15:58:14', '2012-12-07 15:58:14', 3, '<h1>A Empresa</h1>\r\n<p>Somos uma cl&iacute;nica veterin&aacute;ria especializada no atendimento a equinos de diversas ra&ccedil;as e finalidades, h&aacute; mais de 5 anos no mercado de Equinos. A Equine Clinic &eacute; composta por dois m&eacute;dicos veterin&aacute;rios, especialistas em Hipiatria, e ainda conta com a participa&ccedil;&atilde;o de outros m&eacute;dicos veterin&aacute;rios, em distintas &aacute;reas da Hipiatria, com a finalidade de prestar servi&ccedil;os t&eacute;cnicos especializados, como nas &aacute;reas de Diagn&oacute;stico por imagem, por exemplo.</p>\r\n<p>Com a finalidade de atender a crescente demanda do mercado de equinos, principalmente no que se refere aos equinos como animal de companhia, a Equine Clinic oferece diversos servi&ccedil;os como Cl&iacute;nica, Cirugia, Fisioterapia, Odontologia e ainda Emerg&ecirc;ncias e Interna&ccedil;&atilde;o hospitalar.</p>\r\n<p>&nbsp;</p>\r\n<div id="painel_fotos"><a title="Foto da EquineClinic." href="../../../static/images/clinica_01.jpg"><img title="Foto da EquineClinic." src="../../../static/images/clinica_01_thumb.jpg" alt="Foto da EquineClinic." /></a> <a title="Foto da EquineClinic." href="../../../static/images/clinica_02.jpg"><img title="Foto da EquineClinic." src="../../../static/images/clinica_02_thumb.jpg" alt="Foto da EquineClinic." /></a> <a title="Foto da EquineClinic." href="../../../static/images/clinica_03.jpg"><img title="Foto da EquineClinic." src="../../../static/images/clinica_03_thumb.jpg" alt="Foto da EquineClinic." /></a> <a title="Foto da EquineClinic." href="../../../static/images/clinica_04.jpg"><img title="Foto da EquineClinic." src="../../../static/images/clinica_04_thumb.jpg" alt="Foto da EquineClinic." /></a> <a title="Foto da EquineClinic." href="../../../static/images/clinica_05.jpg"><img title="Foto da EquineClinic." src="../../../static/images/clinica_05_thumb.jpg" alt="Foto da EquineClinic." /></a> <a title="Foto da EquineClinic." href="../../../static/images/clinica_06.jpg"><img title="Foto da EquineClinic." src="../../../static/images/clinica_06_thumb.jpg" alt="Foto da EquineClinic." /></a> <br /> <a title="Foto da EquineClinic." href="../../../static/images/clinica_07.jpg"><img title="Foto da EquineClinic." src="../../../static/images/clinica_07_thumb.jpg" alt="Foto da EquineClinic." /></a> <a title="Foto da EquineClinic." href="../../../static/images/clinica_08.jpg"><img title="Foto da EquineClinic." src="../../../static/images/clinica_08_thumb.jpg" alt="Foto da EquineClinic." /></a> <a title="Foto da EquineClinic." href="../../../static/images/clinica_09.jpg"><img title="Foto da EquineClinic." src="../../../static/images/clinica_09_thumb.jpg" alt="Foto da EquineClinic." /></a> <a title="Foto da EquineClinic." href="../../../static/images/clinica_10.jpg"><img title="Foto da EquineClinic." src="../../../static/images/clinica_10_thumb.jpg" alt="Foto da EquineClinic." /></a> <a title="Foto da EquineClinic." href="../../../static/images/clinica_11.jpg"><img title="Foto da EquineClinic." src="../../../static/images/clinica_11_thumb.jpg" alt="Foto da EquineClinic." /></a> <a title="Foto da EquineClinic." href="../../../static/images/clinica_12.jpg"><img title="Foto da EquineClinic." src="../../../static/images/clinica_12_thumb.jpg" alt="Foto da EquineClinic." /></a> <br /> <span>Clique na foto para ampliar.</span></div>\r\n<p>\r\n<script type="text/javascript">// <![CDATA[\r\n        jQuery(function() { jQuery(''#painel_fotos a'').lightBox(); });\r\n// ]]></script>\r\n</p>', 'Clínica de Hipiatria, com serviços de cirurgia e fisioterapia em Viamão - RS', 'hipiatria, clinica, cirurgia, fisioterapia, equino', 'N', 'A', NULL, 'N', 'N'),
(217, 'Veterinários', 'veterinarios', '2012-11-03 20:54:39', '2012-11-03 20:54:39', 1, '<h1>Veterin&aacute;rios</h1>\n<p><strong>Alexandre Carvalho Monteverde</strong> CRMV RS 05344, formado pela Universidade Federal do Rio Grande do Sul, especialista em equinos, atuando nas &aacute;reas de cl&iacute;nica, cirurgia e odontologia. Sempre trabalhando com equinos, atuou no Jockey Club do Rio Grande do Sul, Sociedade H&iacute;pica Porto Alegrense, e em diversos Haras e Cabanhas do Rio Grande do Sul e Santa Catarina.</p>\n<p><strong>Henrique dos Reis Noronha</strong> CRMV RS 09144, formado pela Universidade Luterana do Rio Grande do Sul, especialista em equinos, atuando nas &aacute;reas de cl&iacute;nica, odontologia e fisioterapia. Sempre voltado a cl&iacute;nica de equinos, trabalhou no Jockey Club do Rio Grande do Sul, na Sociedade H&iacute;pica Porto Alegrense, e na Ferme 7 Chutes em Queb&eacute;c, Canad&aacute;, e ainda em diversos Haras e Cabanhas do Rio Grande do Sul.</p>', 'Clínica de Hipiatria, com serviços de cirurgia e fisioterapia em Viamão - RS', 'veterinarios, pessoal técnico, especialistas', 'N', 'A', NULL, 'S', 'N'),
(218, 'Clientes', 'clientes', '2012-11-03 21:47:25', '2012-11-03 21:47:25', 1, '<h1>Principais Clientes</h1>\n<p>Sem dados.</p>', 'Clínica de Hipiatria, com serviços de cirurgia e fisioterapia em Viamão - RS', 'clientes', 'N', 'A', NULL, 'S', 'N'),
(219, 'Parceiros', 'parceiros', '2012-11-03 21:48:07', '2012-11-03 21:48:07', 1, '<h1>Parceiros</h1>\n<p>A Equine Clinic tem desenvolvido parcerias com Laborat&oacute;rios e outras empresas do setor da Equinocultura, a fim de promover o interc&acirc;mbio e o desenvolvimento de tecnologia que favore&ccedil;am a Sa&uacute;de e o Bem Estar Animal.</p>', 'Clínica de Hipiatria, com serviços de cirurgia e fisioterapia em Viamão - RS', 'parceiros', 'N', 'A', NULL, 'S', 'N');

-- --------------------------------------------------------

--
-- Table structure for table `parametro`
--

CREATE TABLE IF NOT EXISTS `parametro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `valor` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `locked` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'N',
  `status` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'A',
  `moderate_id` int(11) DEFAULT NULL,
  `autor` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `parametro_titulo_uk` (`titulo`),
  KEY `parametro_moderate_fk` (`moderate_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=2 ;

--
-- Dumping data for table `parametro`
--

INSERT INTO `parametro` (`id`, `titulo`, `valor`, `locked`, `status`, `moderate_id`, `autor`) VALUES
(1, 'REPORT TITLE', 'Rede SOS Turbo', 'N', 'A', NULL, 1);

-- --------------------------------------------------------

--
-- Stand-in structure for view `pesquisas`
--
CREATE TABLE IF NOT EXISTS `pesquisas` (
`titulo` varchar(250)
,`slug` varchar(255)
,`intro` text
,`data_hora` timestamp
,`autor` varchar(255)
);
-- --------------------------------------------------------

--
-- Table structure for table `publicacao`
--

CREATE TABLE IF NOT EXISTS `publicacao` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `slug` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `data_hora` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `autor` int(11) NOT NULL,
  `data_publicacao` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `palavras_chaves` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `intro` text COLLATE utf8_unicode_ci NOT NULL,
  `completa` text COLLATE utf8_unicode_ci NOT NULL,
  `thumb_publicacao` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `slug_galeria` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `destaque` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  `locked` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'N',
  `status` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'A',
  `moderate_id` int(11) DEFAULT NULL,
  `permite_comentario` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'N',
  `draft` varchar(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `publicacao_uk` (`titulo`),
  KEY `publicacao_moderate_fk` (`moderate_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=6 ;

--
-- Dumping data for table `publicacao`
--

INSERT INTO `publicacao` (`id`, `titulo`, `slug`, `data_hora`, `autor`, `data_publicacao`, `palavras_chaves`, `intro`, `completa`, `thumb_publicacao`, `slug_galeria`, `destaque`, `locked`, `status`, `moderate_id`, `permite_comentario`, `draft`) VALUES
(1, 'Convênio com o Qualittas', 'conv-nio-com-o-qualittas', '2012-05-02 18:30:44', 3, '2012-05-02 18:30:51', 'noticia, convênio, qualittas', '<p>A Equine Clinic e o Qualittas &ndash; Instituto de P&oacute;s-gradua&ccedil;&atilde;o fecham conv&ecirc;nio para realiza&ccedil;&atilde;o de cursos ligados a Equinocultura, nos moldes de capacita&ccedil;&atilde;o, aperfei&ccedil;oamento e P&oacute;s-gradua&ccedil;&atilde;o.</p>\r\n<p>asdasd</p>\r\n<p>asdasd</p>\r\n<p>asdasdqw</p>', '<p>qweewe</p>\r\n<p>asdasd</p>\r\n<p>&nbsp;</p>\r\n<p>asdsad</p>\r\n<p>A Equine Clinic e o Qualittas &ndash; Instituto de P&oacute;s-gradua&ccedil;&atilde;o fecham conv&ecirc;nio para realiza&ccedil;&atilde;o de cursos ligados a Equinocultura, nos moldes de capacita&ccedil;&atilde;o, aperfei&ccedil;oamento e P&oacute;s-gradua&ccedil;&atilde;o.</p>\r\n<p>As duas institui&ccedil;&otilde;es passam a somar for&ccedil;as no intuito de difundir o conhecimento nesta crescente &aacute;rea, com foco em M&eacute;dicos Veterin&aacute;rios e tamb&eacute;m acad&ecirc;micos de Medicina Veterin&aacute;ria. Os cursos poder&atilde;o utilizar as estruturas das duas institui&ccedil;&otilde;es, favorecendo um melhor desempenho do ponto de vista pedag&oacute;gico, integrando a teoria e a pr&aacute;tica, associada &agrave; rotina cl&iacute;nica da Equine Clinic, e o &ldquo;know how&rdquo; do Qualittas no ensino da Medicina Veterin&aacute;ria.</p>\r\n<p>Os primeiro frutos deste conv&ecirc;nio j&aacute; devem surgir no mercado ainda em julho, com cursos nas &aacute;reas de Odontologia Equina, Organiza&ccedil;&atilde;o de Eventos Equestres &ndash; Bem estar e Responsabilidade T&eacute;cnica, e diversos outros, ainda em fase "embrion&aacute;ria".</p>', 'http://www.equineclinic.com.br/static/images/icone.png', 'Sem Galeria', 'S', 'N', 'A', NULL, 'N', 'N'),
(3, 'teste 2', 'teste-2', '2012-11-13 21:04:03', 1, '2012-11-13 21:04:04', 'teste', '<p><span style="font-family: Arial, Helvetica, sans; font-size: 11px; line-height: 14px; text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vitae est risus. Curabitur porta volutpat est, in facilisis ante varius id. Nunc est mauris, mattis non luctus in, consectetur sit amet mauris. Donec semper nisi ac enim varius sit amet varius ipsum feugiat. Maecenas malesuada luctus nisl id ultrices. Quisque vel sem eu purus dapibus pellentesque sit amet et diam. Fusce eget sapien eget dui vulputate cursus. Aliquam vitae lorem augue. Donec a nibh orci, in consectetur lacus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent lacus arcu, porttitor vitae imperdiet et, malesuada a eros. Quisque congue bibendum metus, ac placerat urna pretium eu. Nunc id purus sed orci dignissim pretium ut vel risus. Phasellus hendrerit bibendum accumsan. Vivamus ante ligula, ornare nec euismod nec, fermentum nec nisl. Nunc eu rutrum ante.</span></p>', '<p style="text-align: justify; font-size: 11px; line-height: 14px; margin: 0px 0px 14px; padding: 0px; font-family: Arial, Helvetica, sans;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vitae est risus. Curabitur porta volutpat est, in facilisis ante varius id. Nunc est mauris, mattis non luctus in, consectetur sit amet mauris. Donec semper nisi ac enim varius sit amet varius ipsum feugiat. Maecenas malesuada luctus nisl id ultrices. Quisque vel sem eu purus dapibus pellentesque sit amet et diam. Fusce eget sapien eget dui vulputate cursus. Aliquam vitae lorem augue. Donec a nibh orci, in consectetur lacus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent lacus arcu, porttitor vitae imperdiet et, malesuada a eros. Quisque congue bibendum metus, ac placerat urna pretium eu. Nunc id purus sed orci dignissim pretium ut vel risus. Phasellus hendrerit bibendum accumsan. Vivamus ante ligula, ornare nec euismod nec, fermentum nec nisl. Nunc eu rutrum ante.</p>\n<p style="text-align: justify; font-size: 11px; line-height: 14px; margin: 0px 0px 14px; padding: 0px; font-family: Arial, Helvetica, sans;">Maecenas bibendum lacus molestie urna tincidunt porttitor. Aliquam sed diam diam, sed ultricies lectus. Curabitur pharetra porttitor vehicula. Nam eu dignissim augue. Vestibulum a ipsum nulla. Nam eget enim dolor. Nunc in dapibus felis. Nam nisl turpis, volutpat eget sagittis eget, bibendum nec dui. Mauris dui odio, ornare a aliquam in, tempor id arcu. Proin vitae neque ante. In hac habitasse platea dictumst. Phasellus euismod, nisi eget condimentum lobortis, dolor justo posuere est, sed consectetur massa enim nec massa. Maecenas tempor eros vitae lacus imperdiet in blandit nibh euismod. Proin sed nulla tellus.</p>\n<p style="text-align: justify; font-size: 11px; line-height: 14px; margin: 0px 0px 14px; padding: 0px; font-family: Arial, Helvetica, sans;">Proin molestie metus sed lectus elementum sodales. Cras nec lacus nec purus tincidunt condimentum sed id augue. Aliquam aliquet commodo dui vitae lacinia. Maecenas interdum justo quis risus porttitor aliquet. Donec a magna enim, in auctor mi. Etiam at quam condimentum enim scelerisque condimentum. Integer mollis scelerisque odio quis tincidunt.</p>', '3', 'Sem Galeria', 'S', 'N', 'A', NULL, 'N', 'N'),
(2, 'teste', 'teste', '2012-11-13 21:02:53', 1, '2012-11-13 21:02:55', 'teste', '<p>teste de publica&ccedil;&atilde;o no espelho de ca&ccedil;a as bruxas e tamb&eacute;m ao trap&eacute;zio.</p>', '<p style="text-align: justify; font-size: 11px; line-height: 14px; margin: 0px 0px 14px; padding: 0px; font-family: Arial, Helvetica, sans;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vitae est risus. Curabitur porta volutpat est, in facilisis ante varius id. Nunc est mauris, mattis non luctus in, consectetur sit amet mauris. Donec semper nisi ac enim varius sit amet varius ipsum feugiat. Maecenas malesuada luctus nisl id ultrices. Quisque vel sem eu purus dapibus pellentesque sit amet et diam. Fusce eget sapien eget dui vulputate cursus. Aliquam vitae lorem augue. Donec a nibh orci, in consectetur lacus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent lacus arcu, porttitor vitae imperdiet et, malesuada a eros. Quisque congue bibendum metus, ac placerat urna pretium eu. Nunc id purus sed orci dignissim pretium ut vel risus. Phasellus hendrerit bibendum accumsan. Vivamus ante ligula, ornare nec euismod nec, fermentum nec nisl. Nunc eu rutrum ante.</p>\n<p style="text-align: justify; font-size: 11px; line-height: 14px; margin: 0px 0px 14px; padding: 0px; font-family: Arial, Helvetica, sans;">Maecenas bibendum lacus molestie urna tincidunt porttitor. Aliquam sed diam diam, sed ultricies lectus. Curabitur pharetra porttitor vehicula. Nam eu dignissim augue. Vestibulum a ipsum nulla. Nam eget enim dolor. Nunc in dapibus felis. Nam nisl turpis, volutpat eget sagittis eget, bibendum nec dui. Mauris dui odio, ornare a aliquam in, tempor id arcu. Proin vitae neque ante. In hac habitasse platea dictumst. Phasellus euismod, nisi eget condimentum lobortis, dolor justo posuere est, sed consectetur massa enim nec massa. Maecenas tempor eros vitae lacus imperdiet in blandit nibh euismod. Proin sed nulla tellus.</p>\n<p style="text-align: justify; font-size: 11px; line-height: 14px; margin: 0px 0px 14px; padding: 0px; font-family: Arial, Helvetica, sans;">Proin molestie metus sed lectus elementum sodales. Cras nec lacus nec purus tincidunt condimentum sed id augue. Aliquam aliquet commodo dui vitae lacinia. Maecenas interdum justo quis risus porttitor aliquet. Donec a magna enim, in auctor mi. Etiam at quam condimentum enim scelerisque condimentum. Integer mollis scelerisque odio quis tincidunt.</p>', '#', 'Sem Galeria', 'S', 'N', 'A', NULL, 'N', 'N'),
(5, 'teste 4', 'teste-4', '2012-11-13 21:33:11', 1, '2012-11-13 21:33:12', 'teste', '<p><span style="font-family: Arial, Helvetica, sans; font-size: 11px; line-height: 14px; text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vitae est risus. Curabitur porta volutpat est, in facilisis ante varius id. Nunc est mauris, mattis non luctus in, consectetur sit amet mauris. Donec semper nisi ac enim varius sit amet varius ipsum feugiat. Maecenas malesuada luctus nisl id ultrices. Quisque vel sem eu purus dapibus pellentesque sit amet et diam. Fusce eget sapien eget dui vulputate cursus. Aliquam vitae lorem augue. Donec a nibh orci, in consectetur lacus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent lacus arcu, porttitor vitae imperdiet et, malesuada a eros. Quisque congue bibendum metus, ac placerat urna pretium eu. Nunc id purus sed orci dignissim pretium ut vel risus. Phasellus hendrerit bibendum accumsan. Vivamus ante ligula, ornare nec euismod nec, fermentum nec nisl. Nunc eu rutrum ante.</span></p>', '<p style="text-align: justify; font-size: 11px; line-height: 14px; margin: 0px 0px 14px; padding: 0px; font-family: Arial, Helvetica, sans;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vitae est risus. Curabitur porta volutpat est, in facilisis ante varius id. Nunc est mauris, mattis non luctus in, consectetur sit amet mauris. Donec semper nisi ac enim varius sit amet varius ipsum feugiat. Maecenas malesuada luctus nisl id ultrices. Quisque vel sem eu purus dapibus pellentesque sit amet et diam. Fusce eget sapien eget dui vulputate cursus. Aliquam vitae lorem augue. Donec a nibh orci, in consectetur lacus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent lacus arcu, porttitor vitae imperdiet et, malesuada a eros. Quisque congue bibendum metus, ac placerat urna pretium eu. Nunc id purus sed orci dignissim pretium ut vel risus. Phasellus hendrerit bibendum accumsan. Vivamus ante ligula, ornare nec euismod nec, fermentum nec nisl. Nunc eu rutrum ante.</p>\n<p style="text-align: justify; font-size: 11px; line-height: 14px; margin: 0px 0px 14px; padding: 0px; font-family: Arial, Helvetica, sans;">Maecenas bibendum lacus molestie urna tincidunt porttitor. Aliquam sed diam diam, sed ultricies lectus. Curabitur pharetra porttitor vehicula. Nam eu dignissim augue. Vestibulum a ipsum nulla. Nam eget enim dolor. Nunc in dapibus felis. Nam nisl turpis, volutpat eget sagittis eget, bibendum nec dui. Mauris dui odio, ornare a aliquam in, tempor id arcu. Proin vitae neque ante. In hac habitasse platea dictumst. Phasellus euismod, nisi eget condimentum lobortis, dolor justo posuere est, sed consectetur massa enim nec massa. Maecenas tempor eros vitae lacus imperdiet in blandit nibh euismod. Proin sed nulla tellus.</p>\n<p style="text-align: justify; font-size: 11px; line-height: 14px; margin: 0px 0px 14px; padding: 0px; font-family: Arial, Helvetica, sans;">Proin molestie metus sed lectus elementum sodales. Cras nec lacus nec purus tincidunt condimentum sed id augue. Aliquam aliquet commodo dui vitae lacinia. Maecenas interdum justo quis risus porttitor aliquet. Donec a magna enim, in auctor mi. Etiam at quam condimentum enim scelerisque condimentum. Integer mollis scelerisque odio quis tincidunt.</p>', '#', 'Sem Galeria', 'S', 'N', 'A', NULL, 'N', 'N'),
(4, 'teste3', 'teste3', '2012-11-13 21:04:34', 1, '2012-11-13 21:04:35', 'teste', '<p><span style="font-family: Arial, Helvetica, sans; font-size: 11px; line-height: 14px; text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vitae est risus. Curabitur porta volutpat est, in facilisis ante varius id. Nunc est mauris, mattis non luctus in, consectetur sit amet mauris. Donec semper nisi ac enim varius sit amet varius ipsum feugiat. Maecenas malesuada luctus nisl id ultrices. Quisque vel sem eu purus dapibus pellentesque sit amet et diam. Fusce eget sapien eget dui vulputate cursus. Aliquam vitae lorem augue. Donec a nibh orci, in consectetur lacus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent lacus arcu, porttitor vitae imperdiet et, malesuada a eros. Quisque congue bibendum metus, ac placerat urna pretium eu. Nunc id purus sed orci dignissim pretium ut vel risus. Phasellus hendrerit bibendum accumsan. Vivamus ante ligula, ornare nec euismod nec, fermentum nec nisl. Nunc eu rutrum ante.</span></p>', '<p style="text-align: justify; font-size: 11px; line-height: 14px; margin: 0px 0px 14px; padding: 0px; font-family: Arial, Helvetica, sans;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vitae est risus. Curabitur porta volutpat est, in facilisis ante varius id. Nunc est mauris, mattis non luctus in, consectetur sit amet mauris. Donec semper nisi ac enim varius sit amet varius ipsum feugiat. Maecenas malesuada luctus nisl id ultrices. Quisque vel sem eu purus dapibus pellentesque sit amet et diam. Fusce eget sapien eget dui vulputate cursus. Aliquam vitae lorem augue. Donec a nibh orci, in consectetur lacus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent lacus arcu, porttitor vitae imperdiet et, malesuada a eros. Quisque congue bibendum metus, ac placerat urna pretium eu. Nunc id purus sed orci dignissim pretium ut vel risus. Phasellus hendrerit bibendum accumsan. Vivamus ante ligula, ornare nec euismod nec, fermentum nec nisl. Nunc eu rutrum ante.</p>\n<p style="text-align: justify; font-size: 11px; line-height: 14px; margin: 0px 0px 14px; padding: 0px; font-family: Arial, Helvetica, sans;">Maecenas bibendum lacus molestie urna tincidunt porttitor. Aliquam sed diam diam, sed ultricies lectus. Curabitur pharetra porttitor vehicula. Nam eu dignissim augue. Vestibulum a ipsum nulla. Nam eget enim dolor. Nunc in dapibus felis. Nam nisl turpis, volutpat eget sagittis eget, bibendum nec dui. Mauris dui odio, ornare a aliquam in, tempor id arcu. Proin vitae neque ante. In hac habitasse platea dictumst. Phasellus euismod, nisi eget condimentum lobortis, dolor justo posuere est, sed consectetur massa enim nec massa. Maecenas tempor eros vitae lacus imperdiet in blandit nibh euismod. Proin sed nulla tellus.</p>\n<p style="text-align: justify; font-size: 11px; line-height: 14px; margin: 0px 0px 14px; padding: 0px; font-family: Arial, Helvetica, sans;">Proin molestie metus sed lectus elementum sodales. Cras nec lacus nec purus tincidunt condimentum sed id augue. Aliquam aliquet commodo dui vitae lacinia. Maecenas interdum justo quis risus porttitor aliquet. Donec a magna enim, in auctor mi. Etiam at quam condimentum enim scelerisque condimentum. Integer mollis scelerisque odio quis tincidunt.</p>', '#', 'Sem Galeria', 'S', 'N', 'A', NULL, 'N', 'N');

-- --------------------------------------------------------

--
-- Table structure for table `publicacao_tipo_publicacao`
--

CREATE TABLE IF NOT EXISTS `publicacao_tipo_publicacao` (
  `publicacao` int(11) NOT NULL,
  `tipo_publicacao` int(11) NOT NULL,
  PRIMARY KEY (`publicacao`,`tipo_publicacao`),
  KEY `publicacao_tipo_publicacao_tipo_fk` (`tipo_publicacao`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `publicacao_tipo_publicacao`
--

INSERT INTO `publicacao_tipo_publicacao` (`publicacao`, `tipo_publicacao`) VALUES
(1, 1),
(2, 1),
(2, 2),
(2, 3),
(2, 4),
(3, 1),
(3, 2),
(3, 3),
(3, 4),
(4, 1),
(5, 1),
(5, 2),
(5, 3),
(5, 4);

-- --------------------------------------------------------

--
-- Table structure for table `template`
--

CREATE TABLE IF NOT EXISTS `template` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `slug` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `data_publicacao` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `autor` int(11) NOT NULL,
  `path` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `ativo` varchar(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `locked` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'N',
  `status` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'A',
  `moderate_id` int(11) DEFAULT NULL,
  `draft` varchar(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `template_titulo_uk` (`titulo`),
  KEY `template_moderate_fk` (`moderate_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=2 ;

--
-- Dumping data for table `template`
--

INSERT INTO `template` (`id`, `titulo`, `slug`, `data_publicacao`, `autor`, `path`, `ativo`, `locked`, `status`, `moderate_id`, `draft`) VALUES
(1, 'Default', 'default', '2012-09-18 00:07:49', 1, 'site', 'S', 'N', 'A', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `tipo_documento`
--

CREATE TABLE IF NOT EXISTS `tipo_documento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `locked` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'N',
  `status` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'A',
  `moderate_id` int(11) DEFAULT NULL,
  `autor` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `tipo_documento_uk` (`titulo`),
  KEY `tipo_documento_moderate_fk` (`moderate_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=2 ;

--
-- Dumping data for table `tipo_documento`
--

INSERT INTO `tipo_documento` (`id`, `titulo`, `locked`, `status`, `moderate_id`, `autor`) VALUES
(1, 'Manual do Produto', 'N', 'A', NULL, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tipo_publicacao`
--

CREATE TABLE IF NOT EXISTS `tipo_publicacao` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `locked` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'N',
  `status` varchar(1) COLLATE utf8_unicode_ci DEFAULT 'A',
  `moderate_id` int(11) DEFAULT NULL,
  `autor` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `tipo_publicacao_uk` (`titulo`),
  KEY `tipo_publicacao_moderate_fk` (`moderate_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=5 ;

--
-- Dumping data for table `tipo_publicacao`
--

INSERT INTO `tipo_publicacao` (`id`, `titulo`, `locked`, `status`, `moderate_id`, `autor`) VALUES
(1, 'Notícia', 'N', 'A', NULL, 1),
(2, 'Eventos', 'N', 'A', NULL, 1),
(3, 'Artigos', 'N', 'A', NULL, 1),
(4, 'Pesquisas', 'N', 'A', NULL, 1);

-- --------------------------------------------------------

--
-- Table structure for table `usuario`
--

CREATE TABLE IF NOT EXISTS `usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `senha` varchar(8) COLLATE utf8_unicode_ci NOT NULL,
  `nivel_acesso` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario_login_uk` (`login`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=4 ;

--
-- Dumping data for table `usuario`
--

INSERT INTO `usuario` (`id`, `login`, `senha`, `nivel_acesso`) VALUES
(1, 'leandro@professionalit.com.br', 'website', 1),
(3, 'site@equineclinic.com.br', 'website', 1),
(2, 'admin@equineclinic.com.br', 'website', 2);

-- --------------------------------------------------------

--
-- Structure for view `artigos`
--
DROP TABLE IF EXISTS `artigos`;

CREATE ALGORITHM=UNDEFINED DEFINER=`cavalgad`@`localhost` SQL SECURITY DEFINER VIEW `artigos` AS select `n`.`titulo` AS `titulo`,`n`.`slug` AS `slug`,`n`.`intro` AS `intro`,`n`.`data_hora` AS `data_hora`,(select `usuario`.`login` from `usuario` where (`usuario`.`id` = `n`.`autor`)) AS `autor` from ((`publicacao` `n` join `publicacao` `f` on(((`f`.`id` = `n`.`id`) and (`f`.`status` = 'A')))) join `publicacao_tipo_publicacao` `p` on(((`p`.`publicacao` = `n`.`id`) and (`p`.`tipo_publicacao` = (select `t`.`id` from `tipo_publicacao` `t` where (`t`.`titulo` = 'Artigos'))))));

-- --------------------------------------------------------

--
-- Structure for view `eventos`
--
DROP TABLE IF EXISTS `eventos`;

CREATE ALGORITHM=UNDEFINED DEFINER=`cavalgad`@`localhost` SQL SECURITY DEFINER VIEW `eventos` AS select `n`.`titulo` AS `titulo`,`n`.`slug` AS `slug`,`n`.`intro` AS `intro`,`n`.`data_hora` AS `data_hora`,(select `usuario`.`login` from `usuario` where (`usuario`.`id` = `n`.`autor`)) AS `autor` from ((`publicacao` `n` join `publicacao` `f` on(((`f`.`id` = `n`.`id`) and (`f`.`status` = 'A')))) join `publicacao_tipo_publicacao` `p` on(((`p`.`publicacao` = `n`.`id`) and (`p`.`tipo_publicacao` = (select `t`.`id` from `tipo_publicacao` `t` where (`t`.`titulo` = 'Eventos'))))));

-- --------------------------------------------------------

--
-- Structure for view `noticias`
--
DROP TABLE IF EXISTS `noticias`;

CREATE ALGORITHM=UNDEFINED DEFINER=`cavalgad`@`localhost` SQL SECURITY DEFINER VIEW `noticias` AS select `n`.`titulo` AS `titulo`,`n`.`slug` AS `slug`,`n`.`intro` AS `intro`,`n`.`data_hora` AS `data_hora`,(select `usuario`.`login` from `usuario` where (`usuario`.`id` = `n`.`autor`)) AS `autor` from ((`publicacao` `n` join `publicacao` `f` on(((`f`.`id` = `n`.`id`) and (`f`.`status` = 'A')))) join `publicacao_tipo_publicacao` `p` on(((`p`.`publicacao` = `n`.`id`) and (`p`.`tipo_publicacao` = (select `t`.`id` from `tipo_publicacao` `t` where (`t`.`titulo` = 'Notícia'))))));

-- --------------------------------------------------------

--
-- Structure for view `pesquisas`
--
DROP TABLE IF EXISTS `pesquisas`;

CREATE ALGORITHM=UNDEFINED DEFINER=`cavalgad`@`localhost` SQL SECURITY DEFINER VIEW `pesquisas` AS select `n`.`titulo` AS `titulo`,`n`.`slug` AS `slug`,`n`.`intro` AS `intro`,`n`.`data_hora` AS `data_hora`,(select `usuario`.`login` from `usuario` where (`usuario`.`id` = `n`.`autor`)) AS `autor` from ((`publicacao` `n` join `publicacao` `f` on(((`f`.`id` = `n`.`id`) and (`f`.`status` = 'A')))) join `publicacao_tipo_publicacao` `p` on(((`p`.`publicacao` = `n`.`id`) and (`p`.`tipo_publicacao` = (select `t`.`id` from `tipo_publicacao` `t` where (`t`.`titulo` = 'Pesquisas'))))));

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
