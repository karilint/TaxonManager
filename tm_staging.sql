-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: mysql.luomus.fi
-- Generation Time: 06.03.2022 klo 10:24
-- Palvelimen versio: 10.5.9-MariaDB
-- PHP Version: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tm_staging`
--

-- --------------------------------------------------------

--
-- Rakenne taululle `account_emailaddress`
--

CREATE TABLE `account_emailaddress` (
  `id` int(11) NOT NULL,
  `email` varchar(254) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `primary` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Vedos taulusta `account_emailaddress`
--

INSERT INTO `account_emailaddress` (`id`, `email`, `verified`, `primary`, `user_id`) VALUES
(1, 'tietotuomas@gmail.com', 1, 1, 1),
(2, 'seppo.kajantie@helsinki.fi', 1, 1, 2),
(3, 'kari.lintulaakso@gmail.com', 1, 1, 3),
(4, 'Cecilia.salpaoja@helsinki.fi', 1, 1, 4),
(5, 'juhana.karhunen@helsinki.fi', 1, 1, 5),
(6, 'ari.kauppi@helsinki.fi', 1, 1, 6),
(7, 'anne.kuivanen@helsinki.fi', 1, 1, 7),
(13, 'jonne.sotala@gmail.com', 1, 1, 13),
(18, 'tuomas.b.aaltonen@helsinki.fi', 1, 1, 18);

-- --------------------------------------------------------

--
-- Rakenne taululle `account_emailconfirmation`
--

CREATE TABLE `account_emailconfirmation` (
  `id` int(11) NOT NULL,
  `created` datetime(6) NOT NULL,
  `sent` datetime(6) DEFAULT NULL,
  `key` varchar(64) NOT NULL,
  `email_address_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Rakenne taululle `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Vedos taulusta `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'contributors');

-- --------------------------------------------------------

--
-- Rakenne taululle `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Rakenne taululle `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Vedos taulusta `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add site', 7, 'add_site'),
(26, 'Can change site', 7, 'change_site'),
(27, 'Can delete site', 7, 'delete_site'),
(28, 'Can view site', 7, 'view_site'),
(29, 'Can add email address', 8, 'add_emailaddress'),
(30, 'Can change email address', 8, 'change_emailaddress'),
(31, 'Can delete email address', 8, 'delete_emailaddress'),
(32, 'Can view email address', 8, 'view_emailaddress'),
(33, 'Can add email confirmation', 9, 'add_emailconfirmation'),
(34, 'Can change email confirmation', 9, 'change_emailconfirmation'),
(35, 'Can delete email confirmation', 9, 'delete_emailconfirmation'),
(36, 'Can view email confirmation', 9, 'view_emailconfirmation'),
(37, 'Can add social account', 10, 'add_socialaccount'),
(38, 'Can change social account', 10, 'change_socialaccount'),
(39, 'Can delete social account', 10, 'delete_socialaccount'),
(40, 'Can view social account', 10, 'view_socialaccount'),
(41, 'Can add social application', 11, 'add_socialapp'),
(42, 'Can change social application', 11, 'change_socialapp'),
(43, 'Can delete social application', 11, 'delete_socialapp'),
(44, 'Can view social application', 11, 'view_socialapp'),
(45, 'Can add social application token', 12, 'add_socialtoken'),
(46, 'Can change social application token', 12, 'change_socialtoken'),
(47, 'Can delete social application token', 12, 'delete_socialtoken'),
(48, 'Can view social application token', 12, 'view_socialtoken'),
(49, 'Can add taxon unit type', 13, 'add_taxonunittype'),
(50, 'Can change taxon unit type', 13, 'change_taxonunittype'),
(51, 'Can delete taxon unit type', 13, 'delete_taxonunittype'),
(52, 'Can view taxon unit type', 13, 'view_taxonunittype'),
(53, 'Can add kingdom', 14, 'add_kingdom'),
(54, 'Can change kingdom', 14, 'change_kingdom'),
(55, 'Can delete kingdom', 14, 'delete_kingdom'),
(56, 'Can view kingdom', 14, 'view_kingdom'),
(57, 'Can add ref', 15, 'add_ref'),
(58, 'Can change ref', 15, 'change_ref'),
(59, 'Can delete ref', 15, 'delete_ref'),
(60, 'Can view ref', 15, 'view_ref'),
(61, 'Can add comment', 16, 'add_comment'),
(62, 'Can change comment', 16, 'change_comment'),
(63, 'Can delete comment', 16, 'delete_comment'),
(64, 'Can view comment', 16, 'view_comment'),
(65, 'Can add expert', 17, 'add_expert'),
(66, 'Can change expert', 17, 'change_expert'),
(67, 'Can delete expert', 17, 'delete_expert'),
(68, 'Can view expert', 17, 'view_expert'),
(69, 'Can add experts geographic div', 18, 'add_expertsgeographicdiv'),
(70, 'Can change experts geographic div', 18, 'change_expertsgeographicdiv'),
(71, 'Can delete experts geographic div', 18, 'delete_expertsgeographicdiv'),
(72, 'Can view experts geographic div', 18, 'view_expertsgeographicdiv'),
(73, 'Can add publication', 19, 'add_publication'),
(74, 'Can change publication', 19, 'change_publication'),
(75, 'Can delete publication', 19, 'delete_publication'),
(76, 'Can view publication', 19, 'view_publication'),
(77, 'Can add taxon author lkp', 20, 'add_taxonauthorlkp'),
(78, 'Can change taxon author lkp', 20, 'change_taxonauthorlkp'),
(79, 'Can delete taxon author lkp', 20, 'delete_taxonauthorlkp'),
(80, 'Can view taxon author lkp', 20, 'view_taxonauthorlkp'),
(81, 'Can add taxonomic unit', 21, 'add_taxonomicunit'),
(82, 'Can change taxonomic unit', 21, 'change_taxonomicunit'),
(83, 'Can delete taxonomic unit', 21, 'delete_taxonomicunit'),
(84, 'Can view taxonomic unit', 21, 'view_taxonomicunit'),
(85, 'Can add tu comment link', 22, 'add_tucommentlink'),
(86, 'Can change tu comment link', 22, 'change_tucommentlink'),
(87, 'Can delete tu comment link', 22, 'delete_tucommentlink'),
(88, 'Can view tu comment link', 22, 'view_tucommentlink'),
(89, 'Can add synonym link', 23, 'add_synonymlink'),
(90, 'Can change synonym link', 23, 'change_synonymlink'),
(91, 'Can delete synonym link', 23, 'delete_synonymlink'),
(92, 'Can view synonym link', 23, 'view_synonymlink'),
(93, 'Can add hierarchy', 24, 'add_hierarchy'),
(94, 'Can change hierarchy', 24, 'change_hierarchy'),
(95, 'Can delete hierarchy', 24, 'delete_hierarchy'),
(96, 'Can view hierarchy', 24, 'view_hierarchy'),
(97, 'Can add geographic div', 25, 'add_geographicdiv'),
(98, 'Can change geographic div', 25, 'change_geographicdiv'),
(99, 'Can delete geographic div', 25, 'delete_geographicdiv'),
(100, 'Can view geographic div', 25, 'view_geographicdiv'),
(101, 'Can add reference link', 26, 'add_referencelink'),
(102, 'Can change reference link', 26, 'change_referencelink'),
(103, 'Can delete reference link', 26, 'delete_referencelink'),
(104, 'Can view reference link', 26, 'view_referencelink'),
(105, 'Can add reference', 27, 'add_reference'),
(106, 'Can change reference', 27, 'change_reference'),
(107, 'Can delete reference', 27, 'delete_reference'),
(108, 'Can view reference', 27, 'view_reference'),
(109, 'Can add historical reference', 28, 'add_historicalreference'),
(110, 'Can change historical reference', 28, 'change_historicalreference'),
(111, 'Can delete historical reference', 28, 'delete_historicalreference'),
(112, 'Can view historical reference', 28, 'view_historicalreference');

-- --------------------------------------------------------

--
-- Rakenne taululle `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Vedos taulusta `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, '!602QVEv8NggSY1C6UVRxdKWQsD3j06rsfWGE4aM3', '2022-03-05 18:50:44.726845', 1, 'Tuomas', 'Tuomas', 'Aaltonen', 'tietotuomas@gmail.com', 1, 1, '2022-02-02 09:23:58.000000'),
(2, '!qUXVZ6mCWICdNt3e0mieXqTuBrG3A7ykvbF0NQpT', '2022-02-26 08:06:38.712202', 1, 'skajanti', 'Seppo', 'Kajantie', 'seppo.kajantie@helsinki.fi', 1, 1, '2022-02-02 09:23:04.000000'),
(3, '!8wkCsQ5K1tjO0FAYAcZ7z6G1ZbnJdJ3k65OJZK8z', '2022-02-28 07:47:28.348253', 1, 'karilint', 'Kari', 'Lintulaakso', 'kari.lintulaakso@gmail.com', 1, 1, '2022-02-02 10:46:51.000000'),
(4, '!xXbvvXxoldZ5dWD3fr6B3aarXy1oXrJOPCltN5pv', '2022-02-19 17:16:01.000000', 1, 'Cecilia', 'Cecilia', '', 'Cecilia.salpaoja@helsinki.fi', 1, 1, '2022-02-03 07:48:49.000000'),
(5, '!nMujKlUgJhS0SeJ5fWA6zdhnC2UXIVYW90jw7XVl', '2022-02-23 11:15:40.056457', 1, 'juhanaka', 'Juhana', 'Karhunen', 'juhana.karhunen@helsinki.fi', 1, 1, '2022-02-03 08:47:32.000000'),
(6, '!6GbumprVeLa58KuOtQRYaNOgA0EVYckAxXC5vKIt', '2022-02-03 10:05:21.000000', 1, 'arikauppi', 'Ari', 'Kauppi', 'ari.kauppi@helsinki.fi', 1, 1, '2022-02-03 09:33:14.000000'),
(7, '!RTSxgslS15HBCPuRkeg2TO7ISvCHo0cO1oycN7eC', '2022-02-21 07:59:19.517611', 1, 'anne', 'Anne', '', 'anne.kuivanen@helsinki.fi', 1, 1, '2022-02-03 10:42:59.000000'),
(13, '!c35S5ohdrrxU75VAvJKOeI1adEji8q0GMw28AUtF', '2022-02-21 12:38:14.151204', 0, 'jonsotal', 'Jonne', 'Sotala', 'jonne.sotala@gmail.com', 0, 1, '2022-02-21 12:36:56.134000'),
(18, '!YY2lUOSilaCdhvoFeHMYEMgsGdOKN0WAFxQwr2sP', '2022-03-01 13:58:03.314969', 0, 'Demooja', 'Tuomas', 'Testaaja', 'tuomas.b.aaltonen@helsinki.fi', 0, 1, '2022-03-01 12:59:25.000000');

-- --------------------------------------------------------

--
-- Rakenne taululle `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Vedos taulusta `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(7, 1, 1),
(6, 2, 1),
(5, 3, 1),
(1, 4, 1),
(4, 5, 1),
(3, 6, 1),
(2, 7, 1),
(9, 18, 1);

-- --------------------------------------------------------

--
-- Rakenne taululle `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Rakenne taululle `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Vedos taulusta `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2022-02-03 08:59:53.252915', '4', 'Cecilia', 2, '[{\"changed\": {\"fields\": [\"Staff status\", \"Superuser status\"]}}]', 4, 1),
(2, '2022-02-03 09:00:07.233188', '5', 'juhanaka', 2, '[{\"changed\": {\"fields\": [\"Staff status\", \"Superuser status\"]}}]', 4, 1),
(3, '2022-02-03 09:36:50.412223', '6', 'arikauppi', 2, '[{\"changed\": {\"fields\": [\"Staff status\", \"Superuser status\"]}}]', 4, 1),
(4, '2022-02-03 10:49:44.312771', '7', 'anne', 2, '[{\"changed\": {\"fields\": [\"Staff status\", \"Superuser status\"]}}]', 4, 1),
(5, '2022-02-07 07:13:55.453717', '8', 'Testaaja', 3, '', 4, 1),
(6, '2022-02-07 07:30:10.713410', '9', 'Testaaja', 3, '', 4, 1),
(7, '2022-02-07 08:57:44.781889', '10', 'testaaja1', 3, '', 4, 1),
(8, '2022-02-12 09:03:53.030940', '1', 'contributors', 1, '[{\"added\": {}}]', 3, 4),
(9, '2022-02-18 14:09:07.360423', '11', 'Testaaja', 3, '', 4, 1),
(10, '2022-02-18 20:06:02.906320', '1', 'Bacteria', 1, '[{\"added\": {}}]', 14, 1),
(11, '2022-02-18 20:06:32.748966', '2', 'Protozoa', 1, '[{\"added\": {}}]', 14, 1),
(12, '2022-02-18 20:06:46.852440', '3', 'Plantae', 1, '[{\"added\": {}}]', 14, 1),
(13, '2022-02-18 20:06:57.584964', '4', 'Fungi', 1, '[{\"added\": {}}]', 14, 1),
(14, '2022-02-18 20:07:13.876589', '5', 'Animalia', 1, '[{\"added\": {}}]', 14, 1),
(15, '2022-02-20 08:14:58.103466', '4', 'Cecilia', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 4),
(16, '2022-02-21 06:40:28.907786', '7', 'anne', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 4),
(17, '2022-02-21 06:40:47.908316', '6', 'arikauppi', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 4),
(18, '2022-02-21 06:41:01.824362', '5', 'juhanaka', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 4),
(19, '2022-02-21 06:41:12.251617', '3', 'karilint', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 4),
(20, '2022-02-21 06:41:23.022522', '2', 'skajanti', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 4),
(21, '2022-02-21 06:41:31.137725', '1', 'Tuomas', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 4),
(22, '2022-02-27 08:17:15.123582', '1', 'Bacteria', 1, '[{\"added\": {}}]', 14, 2),
(23, '2022-02-27 08:18:39.974084', '2', 'Protozoa', 1, '[{\"added\": {}}]', 14, 2),
(24, '2022-02-27 08:18:52.135408', '3', 'Plantae', 1, '[{\"added\": {}}]', 14, 2),
(25, '2022-02-27 08:18:58.177745', '4', 'Fungi', 1, '[{\"added\": {}}]', 14, 2),
(26, '2022-02-27 08:19:06.694659', '5', 'Animalia', 1, '[{\"added\": {}}]', 14, 2),
(27, '2022-02-27 08:19:33.940908', '6', 'Chromista', 1, '[{\"added\": {}}]', 14, 2),
(28, '2022-02-27 08:19:43.839524', '7', 'Archaea', 1, '[{\"added\": {}}]', 14, 2),
(29, '2022-02-27 08:20:49.079257', '1', 'Test Author', 1, '[{\"added\": {}}]', 20, 2),
(30, '2022-02-27 08:21:01.524702', '1', 'Homo, Kingdom: Animalia (tsn_id: 1, parent_tsn: 180091)', 1, '[{\"added\": {}}]', 21, 2),
(31, '2022-02-27 08:29:15.046393', '2', 'Homo, Kingdom: Animalia (tsn_id: 2, parent_tsn: 943805)', 1, '[{\"added\": {}}]', 21, 2),
(32, '2022-02-27 08:29:27.632328', '1', 'Homo, Kingdom: Animalia (tsn_id: 1, parent_tsn: 2)', 2, '[{\"changed\": {\"fields\": [\"Parent tsn\"]}}]', 21, 2),
(33, '2022-02-27 08:31:51.046489', '3', 'Homininae, Kingdom: Animalia (tsn_id: 3, parent_tsn: 180090)', 1, '[{\"added\": {}}]', 21, 2),
(34, '2022-02-27 08:32:16.540728', '2', 'Homo, Kingdom: Animalia (tsn_id: 2, parent_tsn: 3)', 2, '[{\"changed\": {\"fields\": [\"Parent tsn\"]}}]', 21, 2),
(35, '2022-02-27 08:33:40.315433', '4', 'Hominidae, Kingdom: Animalia (tsn_id: 4, parent_tsn: 943782)', 1, '[{\"added\": {}}]', 21, 2),
(36, '2022-02-27 08:33:56.263197', '3', 'Homininae, Kingdom: Animalia (tsn_id: 3, parent_tsn: 4)', 2, '[{\"changed\": {\"fields\": [\"Parent tsn\"]}}]', 21, 2),
(37, '2022-02-27 08:35:35.852319', '5', 'Hominoidea, Kingdom: Animalia (tsn_id: 5, parent_tsn: 943778)', 1, '[{\"added\": {}}]', 21, 2),
(38, '2022-02-27 08:35:45.121763', '4', 'Hominidae, Kingdom: Animalia (tsn_id: 4, parent_tsn: 5)', 2, '[{\"changed\": {\"fields\": [\"Parent tsn\"]}}]', 21, 2),
(39, '2022-02-27 08:39:34.256585', '6', 'Simiiformes, Kingdom: Animalia (tsn_id: 6, parent_tsn: 943773)', 1, '[{\"added\": {}}]', 21, 2),
(40, '2022-02-27 08:39:46.158913', '5', 'Hominoidea, Kingdom: Animalia (tsn_id: 5, parent_tsn: 6)', 2, '[{\"changed\": {\"fields\": [\"Parent tsn\"]}}]', 21, 2),
(41, '2022-02-27 08:39:53.110858', '7', 'Animalia, Kingdom: Animalia (tsn_id: 7, parent_tsn: 0)', 1, '[{\"added\": {}}]', 21, 4),
(42, '2022-02-27 08:40:43.336598', '8', 'Bilateria, Kingdom: Animalia (tsn_id: 8, parent_tsn: 202423)', 1, '[{\"added\": {}}]', 21, 4),
(43, '2022-02-27 08:41:20.276783', '9', 'Haplorrhini, Kingdom: Animalia (tsn_id: 9, parent_tsn: 180089)', 1, '[{\"added\": {}}]', 21, 2),
(44, '2022-02-27 08:41:34.456377', '6', 'Simiiformes, Kingdom: Animalia (tsn_id: 6, parent_tsn: 9)', 2, '[{\"changed\": {\"fields\": [\"Parent tsn\"]}}]', 21, 2),
(45, '2022-02-27 08:43:02.200400', '10', 'Deuterostomia, Kingdom: Animalia (tsn_id: 10, parent_tsn: 914154)', 1, '[{\"added\": {}}]', 21, 4),
(46, '2022-02-27 08:43:21.412148', '11', 'Primates, Kingdom: Animalia (tsn_id: 11, parent_tsn: 179925)', 1, '[{\"added\": {}}]', 21, 2),
(47, '2022-02-27 08:43:33.977356', '9', 'Haplorrhini, Kingdom: Animalia (tsn_id: 9, parent_tsn: 11)', 2, '[{\"changed\": {\"fields\": [\"Parent tsn\"]}}]', 21, 2),
(48, '2022-02-27 08:45:26.812332', '8', 'Bilateria, Kingdom: Animalia (tsn_id: 8, parent_tsn: 7)', 2, '[{\"changed\": {\"fields\": [\"Parent tsn\"]}}]', 21, 4),
(49, '2022-02-27 08:45:34.526853', '12', 'Eutheria, Kingdom: Animalia (tsn_id: 12, parent_tsn: 179916)', 1, '[{\"added\": {}}]', 21, 2),
(50, '2022-02-27 08:45:43.146968', '10', 'Deuterostomia, Kingdom: Animalia (tsn_id: 10, parent_tsn: 8)', 2, '[{\"changed\": {\"fields\": [\"Parent tsn\"]}}]', 21, 4),
(51, '2022-02-27 08:45:45.769345', '11', 'Primates, Kingdom: Animalia (tsn_id: 11, parent_tsn: 12)', 2, '[{\"changed\": {\"fields\": [\"Parent tsn\"]}}]', 21, 2),
(52, '2022-02-27 08:47:02.819315', '12', 'Eutheria, Kingdom: Animalia (tsn_id: 12, parent_tsn: 179916)', 2, '[{\"changed\": {\"fields\": [\"Rank id\"]}}]', 21, 2),
(53, '2022-02-27 08:47:05.291906', '13', 'Chordata, Kingdom: Animalia (tsn_id: 13, parent_tsn: 10)', 1, '[{\"added\": {}}]', 21, 4),
(54, '2022-02-27 08:47:45.920609', '14', 'Vertebrata, Kingdom: Animalia (tsn_id: 14, parent_tsn: 13)', 1, '[{\"added\": {}}]', 21, 4),
(55, '2022-02-27 08:48:27.883237', '15', 'Theria, Kingdom: Animalia (tsn_id: 15, parent_tsn: 179913)', 1, '[{\"added\": {}}]', 21, 2),
(56, '2022-02-27 08:48:41.186967', '16', 'Gnathostomata, Kingdom: Animalia (tsn_id: 16, parent_tsn: 14)', 1, '[{\"added\": {}}]', 21, 4),
(57, '2022-02-27 08:48:41.496495', '12', 'Eutheria, Kingdom: Animalia (tsn_id: 12, parent_tsn: 15)', 2, '[{\"changed\": {\"fields\": [\"Parent tsn\"]}}]', 21, 2),
(58, '2022-02-27 08:49:13.488061', '17', 'Tetrapoda, Kingdom: Animalia (tsn_id: 17, parent_tsn: 16)', 1, '[{\"added\": {}}]', 21, 4),
(59, '2022-02-27 08:49:44.819370', '18', 'Mammalia, Kingdom: Animalia (tsn_id: 18, parent_tsn: 17)', 1, '[{\"added\": {}}]', 21, 4),
(60, '2022-02-27 08:50:10.271420', '15', 'Theria, Kingdom: Animalia (tsn_id: 15, parent_tsn: 18)', 2, '[{\"changed\": {\"fields\": [\"Parent tsn\"]}}]', 21, 2),
(61, '2022-02-27 08:51:53.535468', '18', 'Mammalia, Kingdom: Animalia (tsn_id: 18, parent_tsn: 17)', 2, '[{\"changed\": {\"fields\": [\"Name usage\", \"Credibility rtng\", \"Completeness rtng\", \"Currency rating\", \"Phylo sort seq\", \"Rank id\", \"Uncertain prnt ind\", \"N usage\", \"Complete name\"]}}]', 21, 2),
(62, '2022-02-27 08:52:23.691834', '17', 'Tetrapoda, Kingdom: Animalia (tsn_id: 17, parent_tsn: 16)', 2, '[{\"changed\": {\"fields\": [\"Rank id\"]}}]', 21, 2),
(63, '2022-02-27 08:52:38.936304', '16', 'Gnathostomata, Kingdom: Animalia (tsn_id: 16, parent_tsn: 14)', 2, '[{\"changed\": {\"fields\": [\"Rank id\"]}}]', 21, 2),
(64, '2022-02-27 08:52:59.782129', '14', 'Vertebrata, Kingdom: Animalia (tsn_id: 14, parent_tsn: 13)', 2, '[{\"changed\": {\"fields\": [\"Rank id\"]}}]', 21, 2),
(65, '2022-02-27 08:53:33.529684', '13', 'Chordata, Kingdom: Animalia (tsn_id: 13, parent_tsn: 10)', 2, '[{\"changed\": {\"fields\": [\"Rank id\"]}}]', 21, 2),
(66, '2022-02-27 08:53:58.237855', '10', 'Deuterostomia, Kingdom: Animalia (tsn_id: 10, parent_tsn: 8)', 2, '[{\"changed\": {\"fields\": [\"Rank id\"]}}]', 21, 2),
(67, '2022-02-27 08:54:14.318286', '8', 'Bilateria, Kingdom: Animalia (tsn_id: 8, parent_tsn: 7)', 2, '[{\"changed\": {\"fields\": [\"Rank id\"]}}]', 21, 2),
(68, '2022-02-27 08:54:27.750168', '7', 'Animalia, Kingdom: Animalia (tsn_id: 7, parent_tsn: 0)', 2, '[{\"changed\": {\"fields\": [\"Rank id\"]}}]', 21, 2),
(69, '2022-02-27 08:59:45.139772', '1', 'hiearchy_string: 7-8-10-13-14-16-17-18-15-12-11-9-6-5-4-3-2-1)', 1, '[{\"added\": {}}]', 24, 2),
(70, '2022-02-28 19:13:17.203742', '12', 'SannaMarin', 3, '', 4, 1),
(71, '2022-02-28 19:47:33.504295', '14', 'Demooja', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1),
(72, '2022-02-28 21:41:22.551977', '14', 'Demooja', 3, '', 4, 1),
(73, '2022-02-28 22:02:00.828164', '15', 'Demooja', 3, '', 4, 1),
(74, '2022-03-01 12:13:12.141414', '16', 'Demooja', 3, '', 4, 1),
(75, '2022-03-01 12:51:29.885814', '17', 'Demooja', 3, '', 4, 1),
(76, '2022-03-01 13:05:10.103555', '18', 'Demooja', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1),
(77, '2022-03-01 13:27:10.167247', '3', '3: Yehoshua, Dinosaur bones: fossils or pseudomorphs? The pitfalls of physiology reconstruction from apatitic fossils.', 3, '', 27, 1),
(78, '2022-03-01 13:57:08.449490', '4', '4: Yehoshua, Kolodnya, BoazLuza, MartinSanderb, W.A.Clemensc, Dinosaur bones: fossils or pseudomorphs? The pitfalls of physiology reconstruction from apatitic fossils.', 3, '', 27, 1),
(79, '2022-03-03 07:26:40.950454', '1', 'Kingdom: Bacteria, rank_name: Kingdom, rank_id:10', 1, '[{\"added\": {}}]', 13, 5),
(80, '2022-03-03 07:26:58.598086', '2', 'Kingdom: Bacteria, rank_name: Subkingdom, rank_id:20', 1, '[{\"added\": {}}]', 13, 5),
(81, '2022-03-03 07:27:11.374709', '3', 'Kingdom: Bacteria, rank_name: Phylum, rank_id:30', 1, '[{\"added\": {}}]', 13, 5),
(82, '2022-03-03 07:27:27.703196', '4', 'Kingdom: Bacteria, rank_name: Subphylum, rank_id:40', 1, '[{\"added\": {}}]', 13, 5),
(83, '2022-03-03 07:28:27.118279', '5', 'Kingdom: Bacteria, rank_name: Superclass, rank_id:50', 1, '[{\"added\": {}}]', 13, 5),
(84, '2022-03-03 07:28:42.888063', '6', 'Kingdom: Bacteria, rank_name: Class, rank_id:60', 1, '[{\"added\": {}}]', 13, 5),
(85, '2022-03-03 07:28:59.774013', '7', 'Kingdom: Bacteria, rank_name: Subclass, rank_id:70', 1, '[{\"added\": {}}]', 13, 5),
(86, '2022-03-03 07:29:15.515411', '8', 'Kingdom: Bacteria, rank_name: Infraclass, rank_id:80', 1, '[{\"added\": {}}]', 13, 5),
(87, '2022-03-03 07:29:32.915644', '9', 'Kingdom: Bacteria, rank_name: Superorder, rank_id:90', 1, '[{\"added\": {}}]', 13, 5),
(88, '2022-03-03 07:29:46.603067', '10', 'Kingdom: Bacteria, rank_name: Order, rank_id:100', 1, '[{\"added\": {}}]', 13, 5),
(89, '2022-03-03 07:30:08.326584', '11', 'Kingdom: Bacteria, rank_name: Suborder, rank_id:110', 1, '[{\"added\": {}}]', 13, 5),
(90, '2022-03-03 07:30:45.100575', '12', 'Kingdom: Bacteria, rank_name: Infraorder, rank_id:120', 1, '[{\"added\": {}}]', 13, 5),
(91, '2022-03-03 07:31:03.830286', '13', 'Kingdom: Bacteria, rank_name: Superfamily, rank_id:130', 1, '[{\"added\": {}}]', 13, 5),
(92, '2022-03-03 07:31:16.067831', '14', 'Kingdom: Bacteria, rank_name: Family, rank_id:140', 1, '[{\"added\": {}}]', 13, 5),
(93, '2022-03-03 07:31:29.439068', '15', 'Kingdom: Bacteria, rank_name: Subfamily, rank_id:150', 1, '[{\"added\": {}}]', 13, 5),
(94, '2022-03-03 07:31:41.598582', '16', 'Kingdom: Bacteria, rank_name: Tribe, rank_id:160', 1, '[{\"added\": {}}]', 13, 5),
(95, '2022-03-03 07:32:02.417902', '17', 'Kingdom: Bacteria, rank_name: Subtribe, rank_id:170', 1, '[{\"added\": {}}]', 13, 5),
(96, '2022-03-03 07:32:15.702240', '18', 'Kingdom: Bacteria, rank_name: Genus, rank_id:180', 1, '[{\"added\": {}}]', 13, 5),
(97, '2022-03-03 07:32:30.044450', '19', 'Kingdom: Bacteria, rank_name: Subgenus, rank_id:190', 1, '[{\"added\": {}}]', 13, 5),
(98, '2022-03-03 07:32:41.425948', '20', 'Kingdom: Bacteria, rank_name: Species, rank_id:220', 1, '[{\"added\": {}}]', 13, 5),
(99, '2022-03-03 07:32:56.597076', '21', 'Kingdom: Bacteria, rank_name: Subspecies, rank_id:230', 1, '[{\"added\": {}}]', 13, 5),
(100, '2022-03-03 07:48:39.699325', '22', 'Kingdom: Protozoa, rank_name: Kingdom, rank_id:10', 1, '[{\"added\": {}}]', 13, 5),
(101, '2022-03-03 07:48:50.604068', '23', 'Kingdom: Protozoa, rank_name: Subkingdom, rank_id:20', 1, '[{\"added\": {}}]', 13, 5),
(102, '2022-03-03 07:49:15.417568', '24', 'Kingdom: Protozoa, rank_name: Infrakingdom, rank_id:25', 1, '[{\"added\": {}}]', 13, 5),
(103, '2022-03-03 07:49:33.227214', '24', 'Kingdom: Protozoa, rank_name: Infrakingdom, rank_id:25', 2, '[{\"changed\": {\"fields\": [\"Dir parent rank id\", \"Req parent rank id\", \"Update date\"]}}]', 13, 5),
(104, '2022-03-03 07:49:55.360133', '25', 'Kingdom: Protozoa, rank_name: Phylum, rank_id:30', 1, '[{\"added\": {}}]', 13, 5),
(105, '2022-03-03 07:50:08.885215', '26', 'Kingdom: Protozoa, rank_name: Subphylum, rank_id:40', 1, '[{\"added\": {}}]', 13, 5),
(106, '2022-03-03 07:50:22.850669', '27', 'Kingdom: Protozoa, rank_name: Infraphylum, rank_id:45', 1, '[{\"added\": {}}]', 13, 5),
(107, '2022-03-03 07:50:40.168314', '28', 'Kingdom: Protozoa, rank_name: Parvphylum, rank_id:47', 1, '[{\"added\": {}}]', 13, 5),
(108, '2022-03-03 07:50:54.701552', '29', 'Kingdom: Protozoa, rank_name: Superclass, rank_id:50', 1, '[{\"added\": {}}]', 13, 5),
(109, '2022-03-03 07:51:15.621813', '30', 'Kingdom: Protozoa, rank_name: Class, rank_id:60', 1, '[{\"added\": {}}]', 13, 5),
(110, '2022-03-03 07:51:28.511995', '31', 'Kingdom: Protozoa, rank_name: Subclass, rank_id:70', 1, '[{\"added\": {}}]', 13, 5),
(111, '2022-03-03 07:51:39.722172', '32', 'Kingdom: Protozoa, rank_name: Infraclass, rank_id:80', 1, '[{\"added\": {}}]', 13, 5),
(112, '2022-03-03 07:51:57.037603', '33', 'Kingdom: Protozoa, rank_name: Superorder, rank_id:90', 1, '[{\"added\": {}}]', 13, 5),
(113, '2022-03-03 07:55:46.331524', '34', 'Kingdom: Protozoa, rank_name: Order, rank_id:100', 1, '[{\"added\": {}}]', 13, 5),
(114, '2022-03-03 07:55:57.977230', '35', 'Kingdom: Protozoa, rank_name: Suborder, rank_id:110', 1, '[{\"added\": {}}]', 13, 5),
(115, '2022-03-03 07:56:12.708778', '36', 'Kingdom: Protozoa, rank_name: Infraorder, rank_id:120', 1, '[{\"added\": {}}]', 13, 5),
(116, '2022-03-03 07:56:27.279783', '37', 'Kingdom: Protozoa, rank_name: Superfamily, rank_id:130', 1, '[{\"added\": {}}]', 13, 5),
(117, '2022-03-03 07:56:39.945507', '38', 'Kingdom: Protozoa, rank_name: Family, rank_id:140', 1, '[{\"added\": {}}]', 13, 5),
(118, '2022-03-03 07:56:53.714321', '39', 'Kingdom: Protozoa, rank_name: Subfamily, rank_id:150', 1, '[{\"added\": {}}]', 13, 5),
(119, '2022-03-03 07:57:05.736240', '40', 'Kingdom: Protozoa, rank_name: Tribe, rank_id:160', 1, '[{\"added\": {}}]', 13, 5),
(120, '2022-03-03 07:57:27.348550', '41', 'Kingdom: Protozoa, rank_name: Subtribe, rank_id:170', 1, '[{\"added\": {}}]', 13, 5),
(121, '2022-03-03 07:57:40.005675', '42', 'Kingdom: Protozoa, rank_name: Genus, rank_id:180', 1, '[{\"added\": {}}]', 13, 5),
(122, '2022-03-03 07:57:52.827590', '43', 'Kingdom: Protozoa, rank_name: Subgenus, rank_id:190', 1, '[{\"added\": {}}]', 13, 5),
(123, '2022-03-03 07:58:12.672935', '44', 'Kingdom: Protozoa, rank_name: Species, rank_id:220', 1, '[{\"added\": {}}]', 13, 5),
(124, '2022-03-03 07:58:26.605137', '45', 'Kingdom: Protozoa, rank_name: Subspecies, rank_id:230', 1, '[{\"added\": {}}]', 13, 5),
(125, '2022-03-03 07:58:52.836630', '46', 'Kingdom: Protozoa, rank_name: Variety, rank_id:240', 1, '[{\"added\": {}}]', 13, 5),
(126, '2022-03-03 08:31:34.770756', '47', 'Kingdom: Plantae, rank_name: Kingdom, rank_id:10', 1, '[{\"added\": {}}]', 13, 5),
(127, '2022-03-03 08:31:46.176534', '48', 'Kingdom: Plantae, rank_name: Subkingdom, rank_id:20', 1, '[{\"added\": {}}]', 13, 5),
(128, '2022-03-03 08:32:00.004045', '49', 'Kingdom: Plantae, rank_name: Infrakingdom, rank_id:25', 1, '[{\"added\": {}}]', 13, 5),
(129, '2022-03-03 08:32:12.775257', '50', 'Kingdom: Plantae, rank_name: Superdivision, rank_id:27', 1, '[{\"added\": {}}]', 13, 5),
(130, '2022-03-03 08:32:24.393487', '51', 'Kingdom: Plantae, rank_name: Division, rank_id:30', 1, '[{\"added\": {}}]', 13, 5),
(131, '2022-03-03 08:32:34.627838', '52', 'Kingdom: Plantae, rank_name: Subdivision, rank_id:40', 1, '[{\"added\": {}}]', 13, 5),
(132, '2022-03-03 08:32:49.607869', '53', 'Kingdom: Plantae, rank_name: Infradivision, rank_id:45', 1, '[{\"added\": {}}]', 13, 5),
(133, '2022-03-03 08:32:58.600315', '54', 'Kingdom: Plantae, rank_name: Superclass, rank_id:50', 1, '[{\"added\": {}}]', 13, 5),
(134, '2022-03-03 08:33:07.444362', '55', 'Kingdom: Plantae, rank_name: Class, rank_id:60', 1, '[{\"added\": {}}]', 13, 5),
(135, '2022-03-03 08:33:17.875487', '56', 'Kingdom: Plantae, rank_name: Subclass, rank_id:70', 1, '[{\"added\": {}}]', 13, 5),
(136, '2022-03-03 08:33:29.489122', '57', 'Kingdom: Plantae, rank_name: Infraclass, rank_id:80', 1, '[{\"added\": {}}]', 13, 5),
(137, '2022-03-03 08:33:41.074633', '58', 'Kingdom: Plantae, rank_name: Superorder, rank_id:90', 1, '[{\"added\": {}}]', 13, 5),
(138, '2022-03-03 08:33:49.979079', '59', 'Kingdom: Plantae, rank_name: Order, rank_id:100', 1, '[{\"added\": {}}]', 13, 5),
(139, '2022-03-03 08:33:57.551438', '60', 'Kingdom: Plantae, rank_name: Suborder, rank_id:110', 1, '[{\"added\": {}}]', 13, 5),
(140, '2022-03-03 08:34:10.407067', '61', 'Kingdom: Plantae, rank_name: Family, rank_id:140', 1, '[{\"added\": {}}]', 13, 5),
(141, '2022-03-03 08:34:23.411051', '62', 'Kingdom: Plantae, rank_name: Subfamily, rank_id:150', 1, '[{\"added\": {}}]', 13, 5),
(142, '2022-03-03 08:34:42.232143', '63', 'Kingdom: Plantae, rank_name: Tribe, rank_id:160', 1, '[{\"added\": {}}]', 13, 5),
(143, '2022-03-03 08:35:00.566719', '64', 'Kingdom: Plantae, rank_name: Subtribe, rank_id:170', 1, '[{\"added\": {}}]', 13, 5),
(144, '2022-03-03 08:35:10.828631', '65', 'Kingdom: Plantae, rank_name: Genus, rank_id:180', 1, '[{\"added\": {}}]', 13, 5),
(145, '2022-03-03 08:35:55.801282', '66', 'Kingdom: Plantae, rank_name: Subgenus, rank_id:190', 1, '[{\"added\": {}}]', 13, 5),
(146, '2022-03-03 08:36:09.834655', '67', 'Kingdom: Plantae, rank_name: Section, rank_id:200', 1, '[{\"added\": {}}]', 13, 5),
(147, '2022-03-03 08:36:22.716649', '68', 'Kingdom: Plantae, rank_name: Subsection, rank_id:210', 1, '[{\"added\": {}}]', 13, 5),
(148, '2022-03-03 08:36:34.407362', '69', 'Kingdom: Plantae, rank_name: Species, rank_id:220', 1, '[{\"added\": {}}]', 13, 5),
(149, '2022-03-03 08:36:45.623573', '70', 'Kingdom: Plantae, rank_name: Subspecies, rank_id:230', 1, '[{\"added\": {}}]', 13, 5),
(150, '2022-03-03 08:37:01.537200', '71', 'Kingdom: Plantae, rank_name: Variety, rank_id:240', 1, '[{\"added\": {}}]', 13, 5),
(151, '2022-03-03 08:37:18.033396', '72', 'Kingdom: Plantae, rank_name: Subvariety, rank_id:250', 1, '[{\"added\": {}}]', 13, 5),
(152, '2022-03-03 08:37:27.947805', '73', 'Kingdom: Plantae, rank_name: Form, rank_id:260', 1, '[{\"added\": {}}]', 13, 5),
(153, '2022-03-03 08:37:38.642690', '74', 'Kingdom: Plantae, rank_name: Subform, rank_id:270', 1, '[{\"added\": {}}]', 13, 5),
(154, '2022-03-03 10:20:13.492499', '75', 'Kingdom: Fungi, rank_name: Kingdom, rank_id:10', 1, '[{\"added\": {}}]', 13, 5),
(155, '2022-03-03 10:20:23.029478', '76', 'Kingdom: Fungi, rank_name: Subkingdom, rank_id:20', 1, '[{\"added\": {}}]', 13, 5),
(156, '2022-03-03 10:20:30.506779', '77', 'Kingdom: Fungi, rank_name: Division, rank_id:30', 1, '[{\"added\": {}}]', 13, 5),
(157, '2022-03-03 10:20:47.007038', '78', 'Kingdom: Fungi, rank_name: Subdivision, rank_id:40', 1, '[{\"added\": {}}]', 13, 5),
(158, '2022-03-03 10:20:56.316958', '79', 'Kingdom: Fungi, rank_name: Class, rank_id:60', 1, '[{\"added\": {}}]', 13, 5),
(159, '2022-03-03 10:21:06.886257', '80', 'Kingdom: Fungi, rank_name: Subclass, rank_id:70', 1, '[{\"added\": {}}]', 13, 5),
(160, '2022-03-03 10:21:20.141251', '81', 'Kingdom: Fungi, rank_name: Superorder, rank_id:90', 1, '[{\"added\": {}}]', 13, 5),
(161, '2022-03-03 10:21:27.944016', '82', 'Kingdom: Fungi, rank_name: Order, rank_id:100', 1, '[{\"added\": {}}]', 13, 5),
(162, '2022-03-03 10:21:35.973443', '83', 'Kingdom: Fungi, rank_name: Suborder, rank_id:110', 1, '[{\"added\": {}}]', 13, 5),
(163, '2022-03-03 10:21:44.418467', '84', 'Kingdom: Fungi, rank_name: Family, rank_id:140', 1, '[{\"added\": {}}]', 13, 5),
(164, '2022-03-03 10:21:54.709714', '85', 'Kingdom: Fungi, rank_name: Subfamily, rank_id:150', 1, '[{\"added\": {}}]', 13, 5),
(165, '2022-03-03 10:22:06.708769', '86', 'Kingdom: Fungi, rank_name: Tribe, rank_id:160', 1, '[{\"added\": {}}]', 13, 5),
(166, '2022-03-03 10:22:26.909992', '87', 'Kingdom: Fungi, rank_name: Subtribe, rank_id:170', 1, '[{\"added\": {}}]', 13, 5),
(167, '2022-03-03 10:22:34.789303', '88', 'Kingdom: Fungi, rank_name: Genus, rank_id:180', 1, '[{\"added\": {}}]', 13, 5),
(168, '2022-03-03 10:22:45.380122', '89', 'Kingdom: Fungi, rank_name: Subgenus, rank_id:190', 1, '[{\"added\": {}}]', 13, 5),
(169, '2022-03-03 10:22:58.090720', '90', 'Kingdom: Fungi, rank_name: Section, rank_id:200', 1, '[{\"added\": {}}]', 13, 5),
(170, '2022-03-03 10:23:07.817017', '91', 'Kingdom: Fungi, rank_name: Subsection, rank_id:210', 1, '[{\"added\": {}}]', 13, 5),
(171, '2022-03-03 10:23:15.643854', '92', 'Kingdom: Fungi, rank_name: Species, rank_id:220', 1, '[{\"added\": {}}]', 13, 5),
(172, '2022-03-03 10:23:27.025081', '93', 'Kingdom: Fungi, rank_name: Subspecies, rank_id:230', 1, '[{\"added\": {}}]', 13, 5),
(173, '2022-03-03 10:23:35.819197', '94', 'Kingdom: Fungi, rank_name: Variety, rank_id:240', 1, '[{\"added\": {}}]', 13, 5),
(174, '2022-03-03 10:23:53.439528', '95', 'Kingdom: Fungi, rank_name: Subvariety, rank_id:250', 1, '[{\"added\": {}}]', 13, 5),
(175, '2022-03-03 10:24:01.219684', '96', 'Kingdom: Fungi, rank_name: Form, rank_id:260', 1, '[{\"added\": {}}]', 13, 5),
(176, '2022-03-03 10:24:11.322651', '97', 'Kingdom: Fungi, rank_name: Subform, rank_id:270', 1, '[{\"added\": {}}]', 13, 5),
(177, '2022-03-03 10:24:37.931071', '98', 'Kingdom: Animalia, rank_name: Kingdom, rank_id:10', 1, '[{\"added\": {}}]', 13, 5),
(178, '2022-03-03 10:24:50.553351', '99', 'Kingdom: Animalia, rank_name: Subkingdom, rank_id:20', 1, '[{\"added\": {}}]', 13, 5),
(179, '2022-03-03 10:25:01.780324', '100', 'Kingdom: Animalia, rank_name: Infrakingdom, rank_id:25', 1, '[{\"added\": {}}]', 13, 5),
(180, '2022-03-03 10:25:17.664361', '101', 'Kingdom: Animalia, rank_name: Superphylum, rank_id:27', 1, '[{\"added\": {}}]', 13, 5),
(181, '2022-03-03 10:25:26.407311', '102', 'Kingdom: Animalia, rank_name: Phylum, rank_id:30', 1, '[{\"added\": {}}]', 13, 5),
(182, '2022-03-03 10:25:36.837763', '103', 'Kingdom: Animalia, rank_name: Subphylum, rank_id:40', 1, '[{\"added\": {}}]', 13, 5),
(183, '2022-03-03 10:26:08.510286', '104', 'Kingdom: Animalia, rank_name: Infraphylum, rank_id:45', 1, '[{\"added\": {}}]', 13, 5),
(184, '2022-03-03 10:26:18.618275', '105', 'Kingdom: Animalia, rank_name: Superclass, rank_id:50', 1, '[{\"added\": {}}]', 13, 5),
(185, '2022-03-03 10:26:28.070225', '106', 'Kingdom: Animalia, rank_name: Class, rank_id:60', 1, '[{\"added\": {}}]', 13, 5),
(186, '2022-03-03 10:26:41.714768', '107', 'Kingdom: Animalia, rank_name: Subclass, rank_id:70', 1, '[{\"added\": {}}]', 13, 5),
(187, '2022-03-03 10:26:53.019059', '108', 'Kingdom: Animalia, rank_name: Infraclass, rank_id:80', 1, '[{\"added\": {}}]', 13, 5),
(188, '2022-03-03 10:27:06.954174', '109', 'Kingdom: Animalia, rank_name: Superorder, rank_id:90', 1, '[{\"added\": {}}]', 13, 5),
(189, '2022-03-03 10:27:16.349814', '110', 'Kingdom: Animalia, rank_name: Order, rank_id:100', 1, '[{\"added\": {}}]', 13, 5),
(190, '2022-03-03 10:27:26.599961', '111', 'Kingdom: Animalia, rank_name: Suborder, rank_id:110', 1, '[{\"added\": {}}]', 13, 5),
(191, '2022-03-03 10:27:41.944224', '112', 'Kingdom: Animalia, rank_name: Infraorder, rank_id:120', 1, '[{\"added\": {}}]', 13, 5),
(192, '2022-03-03 10:27:56.338242', '111', 'Kingdom: Animalia, rank_name: Suborder, rank_id:110', 2, '[{\"changed\": {\"fields\": [\"Req parent rank id\"]}}]', 13, 5),
(193, '2022-03-03 10:28:26.921876', '112', 'Kingdom: Animalia, rank_name: Infraorder, rank_id:120', 2, '[]', 13, 5),
(194, '2022-03-03 10:28:38.696390', '113', 'Kingdom: Animalia, rank_name: Section, rank_id:124', 1, '[{\"added\": {}}]', 13, 5),
(195, '2022-03-03 10:28:57.078250', '114', 'Kingdom: Animalia, rank_name: Subsection, rank_id:126', 1, '[{\"added\": {}}]', 13, 5),
(196, '2022-03-03 10:29:07.918659', '115', 'Kingdom: Animalia, rank_name: Superfamily, rank_id:130', 1, '[{\"added\": {}}]', 13, 5),
(197, '2022-03-03 10:29:16.046369', '116', 'Kingdom: Animalia, rank_name: Family, rank_id:140', 1, '[{\"added\": {}}]', 13, 5),
(198, '2022-03-03 10:29:31.684973', '117', 'Kingdom: Animalia, rank_name: Subfamily, rank_id:150', 1, '[{\"added\": {}}]', 13, 5),
(199, '2022-03-03 10:29:39.832278', '118', 'Kingdom: Animalia, rank_name: Tribe, rank_id:160', 1, '[{\"added\": {}}]', 13, 5),
(200, '2022-03-03 10:29:49.263716', '119', 'Kingdom: Animalia, rank_name: Subtribe, rank_id:170', 1, '[{\"added\": {}}]', 13, 5),
(201, '2022-03-03 10:30:08.065482', '120', 'Kingdom: Animalia, rank_name: Genus, rank_id:180', 1, '[{\"added\": {}}]', 13, 5),
(202, '2022-03-03 10:30:23.729551', '121', 'Kingdom: Animalia, rank_name: Subgenus, rank_id:190', 1, '[{\"added\": {}}]', 13, 5),
(203, '2022-03-03 10:30:32.825997', '122', 'Kingdom: Animalia, rank_name: Species, rank_id:220', 1, '[{\"added\": {}}]', 13, 5),
(204, '2022-03-03 10:30:43.020640', '123', 'Kingdom: Animalia, rank_name: Subspecies, rank_id:230', 1, '[{\"added\": {}}]', 13, 5),
(205, '2022-03-03 10:30:57.532086', '124', 'Kingdom: Animalia, rank_name: Variety, rank_id:240', 1, '[{\"added\": {}}]', 13, 5),
(206, '2022-03-03 10:31:07.136777', '125', 'Kingdom: Animalia, rank_name: Form, rank_id:245', 1, '[{\"added\": {}}]', 13, 5),
(207, '2022-03-03 10:31:21.095351', '126', 'Kingdom: Animalia, rank_name: Race, rank_id:250', 1, '[{\"added\": {}}]', 13, 5),
(208, '2022-03-03 10:31:33.303771', '127', 'Kingdom: Animalia, rank_name: Stirp, rank_id:255', 1, '[{\"added\": {}}]', 13, 5),
(209, '2022-03-03 10:31:40.769809', '128', 'Kingdom: Animalia, rank_name: Morph, rank_id:260', 1, '[{\"added\": {}}]', 13, 5),
(210, '2022-03-03 10:31:49.533356', '129', 'Kingdom: Animalia, rank_name: Aberration, rank_id:265', 1, '[{\"added\": {}}]', 13, 5),
(211, '2022-03-03 10:32:00.082377', '130', 'Kingdom: Animalia, rank_name: Unspecified, rank_id:300', 1, '[{\"added\": {}}]', 13, 5),
(212, '2022-03-03 10:32:20.618147', '131', 'Kingdom: Chromista, rank_name: Kingdom, rank_id:10', 1, '[{\"added\": {}}]', 13, 5),
(213, '2022-03-03 10:32:38.717327', '132', 'Kingdom: Chromista, rank_name: Subkingdom, rank_id:20', 1, '[{\"added\": {}}]', 13, 5),
(214, '2022-03-03 10:32:50.179947', '133', 'Kingdom: Chromista, rank_name: Infrakingdom, rank_id:25', 1, '[{\"added\": {}}]', 13, 5),
(215, '2022-03-03 10:33:00.124360', '134', 'Kingdom: Chromista, rank_name: Superdivision, rank_id:27', 1, '[{\"added\": {}}]', 13, 5),
(216, '2022-03-03 10:33:07.421084', '135', 'Kingdom: Chromista, rank_name: Division, rank_id:30', 1, '[{\"added\": {}}]', 13, 5),
(217, '2022-03-03 10:33:20.084058', '136', 'Kingdom: Chromista, rank_name: Subdivision, rank_id:40', 1, '[{\"added\": {}}]', 13, 5),
(218, '2022-03-03 10:33:30.827048', '137', 'Kingdom: Chromista, rank_name: Infradivision, rank_id:45', 1, '[{\"added\": {}}]', 13, 5),
(219, '2022-03-03 10:33:45.584750', '138', 'Kingdom: Chromista, rank_name: Parvdivision, rank_id:47', 1, '[{\"added\": {}}]', 13, 5),
(220, '2022-03-03 10:33:58.904823', '139', 'Kingdom: Chromista, rank_name: Superclass, rank_id:50', 1, '[{\"added\": {}}]', 13, 5),
(221, '2022-03-03 10:34:12.943117', '140', 'Kingdom: Chromista, rank_name: Class, rank_id:60', 1, '[{\"added\": {}}]', 13, 5),
(222, '2022-03-03 10:34:23.943016', '141', 'Kingdom: Chromista, rank_name: Subclass, rank_id:70', 1, '[{\"added\": {}}]', 13, 5),
(223, '2022-03-03 10:34:33.746858', '142', 'Kingdom: Chromista, rank_name: Infraclass, rank_id:80', 1, '[{\"added\": {}}]', 13, 5),
(224, '2022-03-03 10:34:43.091119', '143', 'Kingdom: Chromista, rank_name: Superorder, rank_id:90', 1, '[{\"added\": {}}]', 13, 5),
(225, '2022-03-03 10:34:49.841618', '144', 'Kingdom: Chromista, rank_name: Order, rank_id:100', 1, '[{\"added\": {}}]', 13, 5),
(226, '2022-03-03 10:35:03.705988', '145', 'Kingdom: Chromista, rank_name: Suborder, rank_id:110', 1, '[{\"added\": {}}]', 13, 5),
(227, '2022-03-03 10:35:14.942280', '146', 'Kingdom: Chromista, rank_name: Family, rank_id:140', 1, '[{\"added\": {}}]', 13, 5),
(228, '2022-03-03 10:35:47.916229', '147', 'Kingdom: Chromista, rank_name: Subfamily, rank_id:150', 1, '[{\"added\": {}}]', 13, 5),
(229, '2022-03-03 10:35:56.402443', '148', 'Kingdom: Chromista, rank_name: Tribe, rank_id:160', 1, '[{\"added\": {}}]', 13, 5),
(230, '2022-03-03 10:36:05.954846', '149', 'Kingdom: Chromista, rank_name: Subtribe, rank_id:170', 1, '[{\"added\": {}}]', 13, 5),
(231, '2022-03-03 10:36:14.372001', '150', 'Kingdom: Chromista, rank_name: Genus, rank_id:180', 1, '[{\"added\": {}}]', 13, 5),
(232, '2022-03-03 10:36:22.991470', '151', 'Kingdom: Chromista, rank_name: Subgenus, rank_id:190', 1, '[{\"added\": {}}]', 13, 5),
(233, '2022-03-03 10:36:30.944993', '152', 'Kingdom: Chromista, rank_name: Section, rank_id:200', 1, '[{\"added\": {}}]', 13, 5),
(234, '2022-03-03 10:36:39.516308', '153', 'Kingdom: Chromista, rank_name: Subsection, rank_id:210', 1, '[{\"added\": {}}]', 13, 5),
(235, '2022-03-03 10:36:52.686123', '154', 'Kingdom: Chromista, rank_name: Species, rank_id:220', 1, '[{\"added\": {}}]', 13, 5),
(236, '2022-03-03 10:37:10.057433', '155', 'Kingdom: Chromista, rank_name: Subspecies, rank_id:230', 1, '[{\"added\": {}}]', 13, 5),
(237, '2022-03-03 10:37:17.393760', '156', 'Kingdom: Chromista, rank_name: Variety, rank_id:240', 1, '[{\"added\": {}}]', 13, 5),
(238, '2022-03-03 10:37:27.701015', '157', 'Kingdom: Chromista, rank_name: Subvariety, rank_id:250', 1, '[{\"added\": {}}]', 13, 5),
(239, '2022-03-03 10:37:38.558497', '158', 'Kingdom: Chromista, rank_name: Form, rank_id:260', 1, '[{\"added\": {}}]', 13, 5),
(240, '2022-03-03 10:37:48.561224', '159', 'Kingdom: Chromista, rank_name: Subform, rank_id:270', 1, '[{\"added\": {}}]', 13, 5),
(241, '2022-03-03 10:38:06.270844', '160', 'Kingdom: Archaea, rank_name: Kingdom, rank_id:10', 1, '[{\"added\": {}}]', 13, 5),
(242, '2022-03-03 10:38:18.984474', '161', 'Kingdom: Archaea, rank_name: Subkingdom, rank_id:20', 1, '[{\"added\": {}}]', 13, 5),
(243, '2022-03-03 10:38:31.573124', '162', 'Kingdom: Archaea, rank_name: Phylum, rank_id:30', 1, '[{\"added\": {}}]', 13, 5),
(244, '2022-03-03 10:38:41.472015', '163', 'Kingdom: Archaea, rank_name: Subphylum, rank_id:40', 1, '[{\"added\": {}}]', 13, 5),
(245, '2022-03-03 10:38:50.442338', '164', 'Kingdom: Archaea, rank_name: Superclass, rank_id:50', 1, '[{\"added\": {}}]', 13, 5),
(246, '2022-03-03 10:39:03.019945', '165', 'Kingdom: Archaea, rank_name: Class, rank_id:60', 1, '[{\"added\": {}}]', 13, 5),
(247, '2022-03-03 10:39:16.145403', '166', 'Kingdom: Archaea, rank_name: Subclass, rank_id:70', 1, '[{\"added\": {}}]', 13, 5),
(248, '2022-03-03 10:39:28.572636', '167', 'Kingdom: Archaea, rank_name: Infraclass, rank_id:80', 1, '[{\"added\": {}}]', 13, 5),
(249, '2022-03-03 10:39:40.145033', '168', 'Kingdom: Archaea, rank_name: Superorder, rank_id:90', 1, '[{\"added\": {}}]', 13, 5),
(250, '2022-03-03 10:39:50.049024', '169', 'Kingdom: Archaea, rank_name: Order, rank_id:100', 1, '[{\"added\": {}}]', 13, 5),
(251, '2022-03-03 10:40:01.854720', '170', 'Kingdom: Archaea, rank_name: Suborder, rank_id:110', 1, '[{\"added\": {}}]', 13, 5),
(252, '2022-03-03 10:40:13.293721', '171', 'Kingdom: Archaea, rank_name: Infraorder, rank_id:120', 1, '[{\"added\": {}}]', 13, 5),
(253, '2022-03-03 10:40:22.259067', '172', 'Kingdom: Archaea, rank_name: Superfamily, rank_id:130', 1, '[{\"added\": {}}]', 13, 5),
(254, '2022-03-03 10:41:14.724339', '173', 'Kingdom: Archaea, rank_name: Family, rank_id:140', 1, '[{\"added\": {}}]', 13, 5),
(255, '2022-03-03 10:41:28.382242', '174', 'Kingdom: Archaea, rank_name: Subfamily, rank_id:150', 1, '[{\"added\": {}}]', 13, 5),
(256, '2022-03-03 10:41:50.436137', '175', 'Kingdom: Archaea, rank_name: Tribe, rank_id:160', 1, '[{\"added\": {}}]', 13, 5),
(257, '2022-03-03 10:41:59.404017', '176', 'Kingdom: Archaea, rank_name: Subtribe, rank_id:170', 1, '[{\"added\": {}}]', 13, 5),
(258, '2022-03-03 10:42:07.091532', '177', 'Kingdom: Archaea, rank_name: Genus, rank_id:180', 1, '[{\"added\": {}}]', 13, 5),
(259, '2022-03-03 10:42:15.399491', '178', 'Kingdom: Archaea, rank_name: Subgenus, rank_id:190', 1, '[{\"added\": {}}]', 13, 5),
(260, '2022-03-03 10:42:25.890240', '179', 'Kingdom: Archaea, rank_name: Species, rank_id:220', 1, '[{\"added\": {}}]', 13, 5),
(261, '2022-03-03 10:42:34.793305', '180', 'Kingdom: Archaea, rank_name: Subspecies, rank_id:230', 1, '[{\"added\": {}}]', 13, 5);

-- --------------------------------------------------------

--
-- Rakenne taululle `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Vedos taulusta `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(8, 'account', 'emailaddress'),
(9, 'account', 'emailconfirmation'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(16, 'front', 'comment'),
(17, 'front', 'expert'),
(18, 'front', 'expertsgeographicdiv'),
(25, 'front', 'geographicdiv'),
(24, 'front', 'hierarchy'),
(28, 'front', 'historicalreference'),
(14, 'front', 'kingdom'),
(19, 'front', 'publication'),
(27, 'front', 'reference'),
(26, 'front', 'referencelink'),
(23, 'front', 'synonymlink'),
(20, 'front', 'taxonauthorlkp'),
(21, 'front', 'taxonomicunit'),
(13, 'front', 'taxonunittype'),
(22, 'front', 'tucommentlink'),
(15, 'refs', 'ref'),
(6, 'sessions', 'session'),
(7, 'sites', 'site'),
(10, 'socialaccount', 'socialaccount'),
(11, 'socialaccount', 'socialapp'),
(12, 'socialaccount', 'socialtoken');

-- --------------------------------------------------------

--
-- Rakenne taululle `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Vedos taulusta `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-11-30 17:44:03.354132'),
(2, 'auth', '0001_initial', '2021-11-30 17:44:04.308789'),
(3, 'account', '0001_initial', '2021-11-30 17:44:04.565934'),
(4, 'account', '0002_email_max_length', '2021-11-30 17:44:04.606598'),
(5, 'admin', '0001_initial', '2021-11-30 17:44:04.849947'),
(6, 'admin', '0002_logentry_remove_auto_add', '2021-11-30 17:44:04.880934'),
(7, 'admin', '0003_logentry_add_action_flag_choices', '2021-11-30 17:44:04.912305'),
(8, 'contenttypes', '0002_remove_content_type_name', '2021-11-30 17:44:05.142224'),
(9, 'auth', '0002_alter_permission_name_max_length', '2021-11-30 17:44:05.185140'),
(10, 'auth', '0003_alter_user_email_max_length', '2021-11-30 17:44:05.241413'),
(11, 'auth', '0004_alter_user_username_opts', '2021-11-30 17:44:05.271243'),
(12, 'auth', '0005_alter_user_last_login_null', '2021-11-30 17:44:05.344829'),
(13, 'auth', '0006_require_contenttypes_0002', '2021-11-30 17:44:05.367634'),
(14, 'auth', '0007_alter_validators_add_error_messages', '2021-11-30 17:44:05.398479'),
(15, 'auth', '0008_alter_user_username_max_length', '2021-11-30 17:44:05.468792'),
(16, 'auth', '0009_alter_user_last_name_max_length', '2021-11-30 17:44:05.539716'),
(17, 'auth', '0010_alter_group_name_max_length', '2021-11-30 17:44:05.590581'),
(18, 'auth', '0011_update_proxy_permissions', '2021-11-30 17:44:05.667448'),
(19, 'auth', '0012_alter_user_first_name_max_length', '2021-11-30 17:44:05.708041'),
(20, 'sessions', '0001_initial', '2021-11-30 17:44:05.810118'),
(21, 'sites', '0001_initial', '2021-11-30 17:44:05.899235'),
(22, 'sites', '0002_alter_domain_unique', '2021-11-30 17:44:05.946144'),
(23, 'socialaccount', '0001_initial', '2021-11-30 17:44:06.651953'),
(24, 'socialaccount', '0002_token_max_lengths', '2021-11-30 17:44:06.742796'),
(25, 'socialaccount', '0003_extra_data_default_dict', '2021-11-30 17:44:06.776456'),
(30, 'front', '0001_initial', '2022-02-24 12:05:32.624140'),
(31, 'refs', '0001_initial', '2022-02-24 12:05:32.945006');

-- --------------------------------------------------------

--
-- Rakenne taululle `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Vedos taulusta `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('2lffs8lkfrb0xwk13efah6b9n2913475', '.eJxVjMEOwiAQRP-FsyGg3S140x8hCyyB2NBE4GT8d1vTgx7nzcx7CUejZzcaP12J4io0itMv9BQeXPeGlmXHkkJYR-3yuznqJm9b4tpLoF7Wej9ef6pMLW8emFXSgaNFg8jKpjmwShhtNNaT99OUGEgnNOAxciRIyl6M0WTOHhDE-wMCLD0v:1nP1JL:Qxd1uR6MFDB9cZNmIfXHUu3fAiZg16NlGg1GM3_f2FQ', '2022-03-15 12:08:59.172634'),
('42t246t2hmrgcbkfa5kognk2cmxmmq4f', 'eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sIlJ3RkdrbjJZQWV6OSJdfQ:1nNLwr:IcdHuYrv1yNy8pAbMz45k7b3bO8WDwYVIC69D50UAi8', '2022-03-10 21:46:53.095519'),
('9l12tdcj1zv1c07wrdqqli5ywoquq0uv', 'eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sIk9FdEVVcXdDVUhWaSJdfQ:1nLixe:qNEoHjV6t8d3p4Orxg-65KELzReK0PkpDeu_d0cL_TE', '2022-03-06 09:56:58.682934'),
('au88q8sxvvffjnzderk2z4z6mdagl0tn', '.eJxVjMEOwiAQRP-Fs2kWKVC82R8hC-ymjQ1NBE7Gf7eYHvQ4b2beS3hsdfGt0NOvSdyEFZdfFjA-KPcCt63jAWPcW67Dd3PWZbgfiXJdI9Z1z_P5-lMtWJbu0dGaRMAYDGjlDgVYLaVyMCJTmACScUgTB1I0ScdBXskC6ziakUm8P9RiPQY:1nGykz:uiUhyFDx7GYE3E48MYNhahXTl4HwGvRM33pxNjbylQg', '2022-02-21 07:48:17.769527'),
('b4odg6p6m01u82vhd1szcm09daylg20n', 'eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sImhkSzVaa250ckdoSSJdfQ:1nOxZL:Qyd-HxbJ9yQNKA9tUhN4Eq-Etu7sMyL2CKfcVKkQYB4', '2022-03-15 08:09:15.206940'),
('e0yzuwj5caph8m3y1w5hdnz5p9sr4tmk', '.eJxVjMEOwiAQRP-FsyEtW1rwpj9ClmUJxIYmAifjv9uaHvQ4b2beSzjsLble-elyEFcxi8sv80gPLkeB63pgiURbL01-N2dd5W1PXFombHkr9_P1p0pY0-6BIUTtQS12wYnVrD0BmWAgWlAWGZlDBDBWG08ToVcjjj5qM4wW56jF-wPMjjzg:1nFYzR:rvlTId8IG_thWaegS0cYQ0ZFgJbKbfu746pGw14Vqwg', '2022-02-17 10:05:21.422208'),
('ej84ir8acy8julzhk2hn49o9bldqkbzp', '.eJxVjMEOwiAQRP-Fs2lwFwp4sz9ClgUCsaGJpSfjv9uaHvQ4b2beS3jaevHbmp6-RnETKC6_LBA_UjsKmucDD8S8bK0P381Zr8N9T6n1ytTr0qbz9acqtJbdo5NMxmFkCUbJUdpgIGqlkLXNiJEILCARI1knwY0ZMykjlb2CMRDE-wOcqztO:1nOaki:i_nWsPqmoiA5tpypR-ksWU49JJtTS4Zx_MsHDCsnuL0', '2022-03-14 07:47:28.362524'),
('f45bz360hdet6mnpvtk2w0pl3ldj4axk', '.eJxVjMEOgyAQRP-Fc2O6iwp6qz9C1nWJpBQThV6a_nu18eJx3sy8jyLmpaTs3rIGH2Ry8qIQVZ9KjDflqOTZlU1WFybVq1pd2Ej8lHQUFOOBq1NX_TdnvVWPPUnKgSmHJQ3n66KaaZt3T0dIusOxgdpgo0Fbw_cGLDIAWqxJa2RtRyAwHVr23jPRJK31rYBB9f0BSAlG3w:1nFa5D:3LmjjnGqyNskSvoeIdPe89fX5INkyzfvTellr-pzIew', '2022-02-17 11:15:23.197552'),
('hwz381bbxct8w5purfss52imeno32g5b', '.eJxVjEEOwiAURO_C2pAPhQru9CLN8PsTiA1NLF013t3WdKHLeW9mNjVgbXlYF3kNZVQ3ZdTllyXwU-ohME0H1mCe19r0t3PqRd_3JLUVRitzfZyrv6uMJR8_hsbeRE8OQsEz9RBjYBO56Dnswblog0XqjfiOhFjQ4SrB27T31fsDovk78A:1nQZUK:dBULWbRl7PdiK3arsVcIRzxmZudrwpVM_RYqnA2LOPo', '2022-03-19 18:50:44.740852'),
('idf4jviugrot7rwi4ptxoh71y1mxf7zk', '.eJxVjEsOwjAMRO-SNapSyM_s4CKR7bpKRJVKNFkh7k6KuoDlvDczLxWx1RTbJs-YJ3VVVp1-GSE_pOwCl2XHAzKvrdTh2zn0Ntx6klIzY81ruR-rv6uEW-o_xCSTY2CyxMFo4EuYDAU_gwZy7qyNF-geDYHhcZTZa9GBtAe0ltX7A-XBPOo:1nM3cc:aM4GVu1TP35MFuIlwQpVZot2joMyl0DtvyepF0zSvKo', '2022-03-07 08:00:38.459065'),
('j6i38d0qq3kwehl9lkdqmd6y36d76y9r', '.eJxVjEsOwjAMRO-SNapSyM_s4CKR7bpKRJVKNFkh7k6KuoDlvDczLxWx1RTbJs-YJ3VVVp1-GSE_pOwCl2XHAzKvrdTh2zn0Ntx6klIzY81ruR-rv6uEW-o_xCSTY2CyxMFo4EuYDAU_gwZy7qyNF-geDYHhcZTZa9GBtAe0ltX7A-XBPOo:1nMpcS:y_EixoQ5BWN3d89HHlAVzOqEx4sInFF3eHcj4vWl_Ik', '2022-03-09 11:15:40.073519'),
('kbmrm83c6gqdhjyarqnjptcbtid3wb0m', '.eJxVjEEOgyAQRe_C2hixMoC79iJkgDGSUkwEuml696oxTVzOe3_eh6FzS03FvGkNUyBv6IUhsjHVGJu_rZlWNjLPGmawlvkAJviN8dsVWnRPSrvBGHfcnpH22Jw6t_ftolSCwxKW9Di_LqkZ87x1pBDKKZy0F53lDrXl5Dn0CNBr6pAkIQxCWQSpQYFVJMVAyImDV1aw7w9ki06C:1nM7xG:VJ_WBaD6rUECKuZ9lWC4nJNomXiO0mSa44cIaOOz0JM', '2022-03-07 12:38:14.163523'),
('kkvjryl9s3po78m1cugmf2mexy9f2ii9', '.eJxVjMEOgyAQRP-Fc2MQWWB7a3_ErMsSTA0mFU5N_73aeGiP82bmvdRIreaxbfIc56iuyqjLL5uIH1KOgpblwB0xr63U7rs566277UlKnZnqvJb7-fpTZdry7glJg4mQjDfWTQG1xoF1QkBGcKGXIXE_IFhP3kYbxUfmMEUAhyRe1PsDmW08Dw:1nGybh:dQ6Nn6oSLWONnzIhCYBcbCtq7m_00ssB75y6jgcW9_Q', '2022-02-21 07:38:41.931726'),
('ktc3e7a3tankmltiu0xqrveopcj1pq6l', '.eJxVjDsOgzAQRO_iOkKsMf7QJRex1uu1sOIYiU-aKHcPRDSU82bmfQQSTVtd_ZvnnDJHzy_MRQx1K-UmPG7r6LeFZ5-jGAQYcYEB6cn1aLCUAzenr_lvznpp7nviumbCNU_1cb4uqhGXcffYaGXbBtkiBFBku6BM7xIbk4i6PrCySTnQEsAo7WJk1EkDkXQqIoD4_gCmlUev:1nP1kr:NIJAYsELVYg0hsNf5MgxqXcJ2FUMTlYwZ0ddkGUkl2Q', '2022-03-15 12:37:25.227182'),
('mqoitmy8gk7menx50tnpz2pjbeqivmsc', 'eyJzb2NpYWxhY2NvdW50X3N0YXRlIjpbeyJwcm9jZXNzIjoibG9naW4iLCJzY29wZSI6IiIsImF1dGhfcGFyYW1zIjoiIn0sInJIODI1ckVOWXY5dyJdfQ:1nMlqz:W2mAvRVp7N-6kTU8JhdIPLiCEubbN7jAJNM1-qnCy3g', '2022-03-09 07:14:25.497967'),
('s4b928baobfind8h3vvof025eb0s3mbn', '.eJytVtuO2zYQ_ZbyudzVzbo9pnUXLZpFummCoEUh0NLI4q4kqiTlrLDwv3eom-2uE7ZADBuwyDPnzIyGw3khSuSc1SzPRd_qbHqqxZ63JH0h87L5ywuStn1df096BTI7PXZSHHgBkqREyBzXEWF2iYMfij-XbsLYp0ngxbhXM6WzWWAiKJiG7FHwFlZOeNaSZbjBjPRIS1Gj1bzkRumF9JKjRKV1p9Lb2xFxI-T-9rpox3T1RY8qofTivOEgRxMUlCChzUEZtVrkrAYEbe_NbsWVFnIwO7kEprloaQO6Eibst9u3b7YP2cP2p-3Dw_ZHFMhF09UwokysS5Cq3zVcqdPyCzmwusc_buhFjreJosSN_OOUM9qIwkRfvAYHfpT4sRf7YYTgvGa8ManUsgdUEb3MV80CWK75gb1y5gByYoeG8XoxXlc7yRsmh_NdkyWQSoyFcs3DibhlDayJuub9EmoQOPZQL8F7foCWGgV1hiK_iLYF855K1vB6oIsLy_57obHiDQCdKrieAfNbucjXgSu-4zXX-LLJuw9vfv35h6-XE5IKXYE8efXl1JyAJP3zr5X2Wg3fnpOixo6LvWRdNSxcEhQwmRtQL2uL8CXYLv5vcnRgLASLzFwsNvYJhpysKFBJ2dI2w-zECxCpn2D4LGRhYZ5RduaV7jj2KpAtq88alC0vry3-Q5auyRy_bjOfT5Nac-q55qCo6htzlC0uFn0-NglbKAvuRGsN5EQ91lFXi6HBkKzFtAD_h9QZuWkHfVvwdm8R2kvRd3bulWzsg3gyJBw4fP425BeEKIDF9vRtmCcmS92cqsWCJMfjNA9cTggdU2o6SOS7u-ExuWs_3b-Lht823eOncNhWHz9s__44qGDv3Q-8er4LJd6r10YDrjLVYxVPEiWrFUx6U9MkaFRyiVbz89T5Z6Z5be72azsyRoZXs7JcOXFhDBqWm-9iKCGe43nUMd_fnST1_DRIbtyN-4dJDxJNlxQOQvnYl8gUA27lopvdZL2uso5J1hjA2kGzs55nXp0WT9BeJpN13dm0tQxqp5XZhACUrldELvUYS2iwA4cmReJTPwz93HVir4x2ZIZnCvDqM1NPXARREichzd2ooEEUO5T5aOXBznfjwC1ZvDG5e-44-pkxPWYjWLOxSf0kdcKbYONgNo7HfwCIxUjz:1nFBrh:n8dUvJp4MSajnfAlEBq2dsTwQtMw9exmjxJPLtPa1zw', '2022-02-16 09:23:49.274322'),
('vsboigu0z013h0pwz0f0h5hcqo7ztsyz', '.eJxVjMEOgjAQRP-lZ0Pc3ZYWb_IjZFjaQCQlkXIy_rtgOOhx3sy8l-mwlbHb1vjspsHcjDWXX9ZDHzEfBeb5wBVUly2X6rs567W67ynmMinKtOT2fP2pRqzj7mnAkIZ7R9azE5Lg9eoosBJxYAsRVgk9gXzDQVNKCgyxDqmO5Nm8P4GjO3k:1nLTKz:ekmlJZ0VBHyX3ehRTUtPbmiR8URv2BvepsowrBbTCys', '2022-03-05 17:16:01.036567'),
('wkpuf7y425yr7eyafalxrvd4tvx3489s', '.eJxVjMEOwiAQRP-Fs2kWKVC82R8hC-ymjQ1NBE7Gf7eYHvQ4b2beS3hsdfGt0NOvSdyEFZdfFjA-KPcCt63jAWPcW67Dd3PWZbgfiXJdI9Z1z_P5-lMtWJbu0dGaRMAYDGjlDgVYLaVyMCJTmACScUgTB1I0ScdBXskC6ziakUm8P9RiPQY:1nM3bL:pt2JZ0xIGEz46lyHBkRdoPAMAm4fI1OnU8sBrgNb_O8', '2022-03-07 07:59:19.555382'),
('x2jdsi160wzetnss8uapybxt2n4i6wba', '.eJxVjMEOgyAQRP-Fc2MQWWB7a3_ErMsSTA0mFU5N_73aeGiP82bmvdRIreaxbfIc56iuyqjLL5uIH1KOgpblwB0xr63U7rs566277UlKnZnqvJb7-fpTZdry7glJg4mQjDfWTQG1xoF1QkBGcKGXIXE_IFhP3kYbxUfmMEUAhyRe1PsDmW08Dw:1nNs6A:pxeMg_CgXYoRTGKGqFpq56yXLK4PfwywopthHZY6d3E', '2022-03-12 08:06:38.728424');

-- --------------------------------------------------------

--
-- Rakenne taululle `django_site`
--

CREATE TABLE `django_site` (
  `id` int(11) NOT NULL,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Vedos taulusta `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'taxonmanager.it.helsinki.fi', 'NOW Taxon Manager');

-- --------------------------------------------------------

--
-- Rakenne taululle `front_comment`
--

CREATE TABLE `front_comment` (
  `id` bigint(20) NOT NULL,
  `commentator` varchar(100) NOT NULL,
  `comment_detail` longtext NOT NULL,
  `comment_time_stamp` datetime(6) DEFAULT NULL,
  `update_date` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Rakenne taululle `front_expert`
--

CREATE TABLE `front_expert` (
  `id` bigint(20) NOT NULL,
  `expert` varchar(100) NOT NULL,
  `exp_comment` varchar(500) NOT NULL,
  `update_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Rakenne taululle `front_expertsgeographicdiv`
--

CREATE TABLE `front_expertsgeographicdiv` (
  `id` bigint(20) NOT NULL,
  `expert_id_id` bigint(20) NOT NULL,
  `geographic_tsn_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Rakenne taululle `front_geographicdiv`
--

CREATE TABLE `front_geographicdiv` (
  `id` bigint(20) NOT NULL,
  `geographic_value` varchar(45) DEFAULT NULL,
  `update_date` datetime(6) DEFAULT NULL,
  `tsn_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Rakenne taululle `front_hierarchy`
--

CREATE TABLE `front_hierarchy` (
  `id` bigint(20) NOT NULL,
  `hierarchy_string` varchar(128) DEFAULT NULL,
  `parent_tsn` int(11) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `childrencount` int(11) DEFAULT NULL,
  `tsn_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Vedos taulusta `front_hierarchy`
--

INSERT INTO `front_hierarchy` (`id`, `hierarchy_string`, `parent_tsn`, `level`, `childrencount`, `tsn_id`) VALUES
(1, '7-8-10-13-14-16-17-18-15-12-11-9-6-5-4-3-2-1', 2, 220, 0, 1);

-- --------------------------------------------------------

--
-- Rakenne taululle `front_historicalreference`
--

CREATE TABLE `front_historicalreference` (
  `id` int(11) NOT NULL,
  `authors` longtext NOT NULL,
  `title` longtext NOT NULL,
  `title_html` longtext NOT NULL,
  `title_latex` longtext NOT NULL,
  `journal` varchar(500) NOT NULL,
  `volume` varchar(10) NOT NULL,
  `page_start` varchar(10) NOT NULL,
  `page_end` varchar(10) NOT NULL,
  `article_number` varchar(16) NOT NULL,
  `year` int(11) DEFAULT NULL,
  `note` longtext NOT NULL,
  `note_html` longtext NOT NULL,
  `note_latex` longtext NOT NULL,
  `doi` varchar(100) NOT NULL,
  `bibcode` varchar(19) NOT NULL,
  `url` varchar(200) NOT NULL,
  `bibtex` longtext DEFAULT NULL,
  `ris` longtext DEFAULT NULL,
  `citeproc_json` longtext DEFAULT NULL,
  `visible` int(11) NOT NULL,
  `history_id` int(11) NOT NULL,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Vedos taulusta `front_historicalreference`
--

INSERT INTO `front_historicalreference` (`id`, `authors`, `title`, `title_html`, `title_latex`, `journal`, `volume`, `page_start`, `page_end`, `article_number`, `year`, `note`, `note_html`, `note_latex`, `doi`, `bibcode`, `url`, `bibtex`, `ris`, `citeproc_json`, `visible`, `history_id`, `history_date`, `history_change_reason`, `history_type`, `history_user_id`) VALUES
(1, 'T. Test', 'Test Title', 'Test Title html', 'Test Title latex', 'testjournal', '1', '2', '3', '4', 1991, 'note', 'note html', 'note latex', 'fakedoi.000', '', 'https://www.google.com', '', NULL, NULL, 1, 1, '2022-02-26 08:09:22.735098', NULL, '+', 2),
(2, '', '', '', '', '', '', '', '', '', NULL, '', '', '', '', '', '', '@article{handa2018brachypotherium,\r\n  title={Brachypotherium (Perissodactyla, Rhinocerotidae) from the late Miocene of Samburu Hills, Kenya},\r\n  author={Handa, Naoto and Nakatsukasa, Masato and Kunimatsu, Yutaka and Nakaya, Hideo},\r\n  journal={Geobios},\r\n  volume={51},\r\n  number={5},\r\n  pages={391--399},\r\n  year={2018},\r\n  publisher={Elsevier}\r\n}', NULL, NULL, 1, 2, '2022-02-28 07:49:37.212813', NULL, '+', 3),
(1, 'T. Test', 'Test Title', 'Test Title html', 'Test Title latex', 'testjournal', '1', '2', '3', '4', 1991, 'note', 'note html', 'note lahex', 'fakedoi.000', '', 'https://www.google.com', '', NULL, NULL, 1, 3, '2022-02-28 08:06:37.915139', NULL, '~', 5),
(3, 'Yehoshua, Kolodnya, BoazLuza, MartinSanderb, W.A.Clemensc', 'Dinosaur bones: fossils or pseudomorphs? The pitfalls of physiology reconstruction from apatitic fossils.', '', '', '', '', '', '', '', NULL, '', '', '', '10.1016/S0031-0182(96)00112-5', '', '', '', NULL, NULL, 1, 4, '2022-02-28 21:14:11.929781', NULL, '+', 1),
(2, '', '', '', '', '', '', '', '', '', NULL, '', '', '', '', '', '', '@article{handa2018brachypotherium,\r\n  title={Brachypotherium (Perissodactyla, Rhinocerotidae) from the late Miocene of Samburu Hills, Kenya},\r\n  author={Handa, Naoto and Nakatsukasa, Masato and Kunimatsu, Yutaka and Nakaya, Hideo},\r\n  journal={Geobios},\r\n  volume={51},\r\n  number={5},\r\n  pages={391--399},\r\n  year={2018},\r\n  publisher={Elsevier}\r\n}', NULL, NULL, 0, 5, '2022-02-28 21:16:30.895160', NULL, '~', 1),
(1, 'T. Test', 'Test Title', 'Test Title html', 'Test Title latex', 'testjournal', '1', '2', '3', '4', 1991, 'note', 'note html', 'note lahex', 'fakedoi.000', '', 'https://www.google.com', '', NULL, NULL, 0, 6, '2022-02-28 21:16:33.322992', NULL, '~', 1),
(3, 'Yehoshua, Kolodnya, BoazLuza, MartinSanderb, W.A.Clemensc', 'Dinosaur bones: fossils or pseudomorphs? The pitfalls of physiology reconstruction from apatitic fossils.', '', '', '', '', '', '', '', NULL, '', '', '', '10.1016/S0031-0182(96)00112-5', '', '', '', NULL, NULL, 1, 7, '2022-03-01 10:52:36.501805', NULL, '~', 1),
(3, 'Yehoshua', 'Dinosaur bones: fossils or pseudomorphs? The pitfalls of physiology reconstruction from apatitic fossils.', '', '', '', '', '', '', '', NULL, '', '', '', '10.1016/S0031-0182(96)00112-5', '', '', '', NULL, NULL, 1, 8, '2022-03-01 11:56:05.943832', NULL, '~', 1),
(3, 'Yehoshua', 'Dinosaur bones: fossils or pseudomorphs? The pitfalls of physiology reconstruction from apatitic fossils.', '', '', '', '', '', '', '', NULL, '', '', '', '10.1016/S0031-0182(96)00112-5', '', '', '', NULL, NULL, 0, 9, '2022-03-01 12:08:10.004494', NULL, '~', 1),
(3, 'Yehoshua', 'Dinosaur bones: fossils or pseudomorphs? The pitfalls of physiology reconstruction from apatitic fossils.', '', '', '', '', '', '', '', NULL, '', '', '', '10.1016/S0031-0182(96)00112-5', '', '', '', NULL, NULL, 0, 10, '2022-03-01 13:27:10.221629', NULL, '-', 1),
(4, 'Yehoshua', 'Dinosaur bones: fossils or pseudomorphs? The pitfalls of physiology reconstruction from apatitic fossils.', '', '', 'Palaeogeography, Palaeoclimatology, Palaeoecology', '', '', '', '', NULL, '', '', '', '10.1016/S0031-0182(96)00112-5', '', '', '', NULL, NULL, 1, 11, '2022-03-01 13:41:46.194227', NULL, '+', 18),
(4, 'Yehoshua, Kolodnya, BoazLuza, MartinSanderb, W.A.Clemensc', 'Dinosaur bones: fossils or pseudomorphs? The pitfalls of physiology reconstruction from apatitic fossils.', '', '', 'Palaeogeography, Palaeoclimatology, Palaeoecology', '', '', '', '', NULL, '', '', '', '10.1016/S0031-0182(96)00112-5', '', '', '', NULL, NULL, 1, 12, '2022-03-01 13:42:11.639592', NULL, '~', 18),
(4, 'Yehoshua, Kolodnya, BoazLuza, MartinSanderb, W.A.Clemensc', 'Dinosaur bones: fossils or pseudomorphs? The pitfalls of physiology reconstruction from apatitic fossils.', '', '', 'Palaeogeography, Palaeoclimatology, Palaeoecology', '', '', '', '', NULL, '', '', '', '10.1016/S0031-0182(96)00112-5', '', '', '', NULL, NULL, 0, 13, '2022-03-01 13:42:39.513594', NULL, '~', 18),
(4, 'Yehoshua, Kolodnya, BoazLuza, MartinSanderb, W.A.Clemensc', 'Dinosaur bones: fossils or pseudomorphs? The pitfalls of physiology reconstruction from apatitic fossils.', '', '', 'Palaeogeography, Palaeoclimatology, Palaeoecology', '', '', '', '', NULL, '', '', '', '10.1016/S0031-0182(96)00112-5', '', '', '', NULL, NULL, 0, 14, '2022-03-01 13:57:08.522999', NULL, '-', 1),
(5, 'Yehoshua', 'Dinosaur bones: fossils or pseudomorphs? The pitfalls of physiology reconstruction from apatitic fossils.', '', '', 'Palaeogeography, Palaeoclimatology, Palaeoecology', '', '', '', '', NULL, '', '', '', '10.1016/S0031-0182(96)00112-5', '', '', '', NULL, NULL, 1, 15, '2022-03-01 13:59:16.112241', NULL, '+', 18),
(5, 'Yehoshua, Kolodnya, BoazLuza, MartinSanderb, W.A.Clemensc', 'Dinosaur bones: fossils or pseudomorphs? The pitfalls of physiology reconstruction from apatitic fossils.', '', '', 'Palaeogeography, Palaeoclimatology, Palaeoecology', '', '', '', '', NULL, '', '', '', '10.1016/S0031-0182(96)00112-5', '', '', '', NULL, NULL, 1, 16, '2022-03-01 14:07:40.530023', NULL, '~', 18),
(5, 'Yehoshua, Kolodnya, BoazLuza, MartinSanderb, W.A.Clemensc', 'Dinosaur bones: fossils or pseudomorphs? The pitfalls of physiology reconstruction from apatitic fossils.', '', '', 'Palaeogeography, Palaeoclimatology, Palaeoecology', '', '', '', '', NULL, '', '', '', '10.1016/S0031-0182(96)00112-5', '', '', '', NULL, NULL, 0, 17, '2022-03-01 14:08:05.836925', NULL, '~', 18);

-- --------------------------------------------------------

--
-- Rakenne taululle `front_kingdom`
--

CREATE TABLE `front_kingdom` (
  `id` bigint(20) NOT NULL,
  `kingdom_name` varchar(20) NOT NULL,
  `update_date` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Vedos taulusta `front_kingdom`
--

INSERT INTO `front_kingdom` (`id`, `kingdom_name`, `update_date`) VALUES
(1, 'Bacteria', NULL),
(2, 'Protozoa', NULL),
(3, 'Plantae', NULL),
(4, 'Fungi', NULL),
(5, 'Animalia', NULL),
(6, 'Chromista', NULL),
(7, 'Archaea', NULL);

-- --------------------------------------------------------

--
-- Rakenne taululle `front_publication`
--

CREATE TABLE `front_publication` (
  `pub_id_prefix` varchar(3) NOT NULL,
  `publication_id` int(11) NOT NULL,
  `reference_author` varchar(100) DEFAULT NULL,
  `title` varchar(255) NOT NULL,
  `publication_name` varchar(255) DEFAULT NULL,
  `listed_pub_date` datetime(6) DEFAULT NULL,
  `actual_pub_date` datetime(6) DEFAULT NULL,
  `publisher` varchar(80) DEFAULT NULL,
  `pub_place` varchar(40) DEFAULT NULL,
  `isbn` varchar(16) DEFAULT NULL,
  `issn` varchar(40) DEFAULT NULL,
  `pages` varchar(15) DEFAULT NULL,
  `pub_comment` varchar(500) DEFAULT NULL,
  `update_date` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Rakenne taululle `front_reference`
--

CREATE TABLE `front_reference` (
  `id` int(11) NOT NULL,
  `authors` longtext NOT NULL,
  `title` longtext NOT NULL,
  `title_html` longtext NOT NULL,
  `title_latex` longtext NOT NULL,
  `journal` varchar(500) NOT NULL,
  `volume` varchar(10) NOT NULL,
  `page_start` varchar(10) NOT NULL,
  `page_end` varchar(10) NOT NULL,
  `article_number` varchar(16) NOT NULL,
  `year` int(11) DEFAULT NULL,
  `note` longtext NOT NULL,
  `note_html` longtext NOT NULL,
  `note_latex` longtext NOT NULL,
  `doi` varchar(100) NOT NULL,
  `bibcode` varchar(19) NOT NULL,
  `url` varchar(200) NOT NULL,
  `bibtex` longtext DEFAULT NULL,
  `ris` longtext DEFAULT NULL,
  `citeproc_json` longtext DEFAULT NULL,
  `visible` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Vedos taulusta `front_reference`
--

INSERT INTO `front_reference` (`id`, `authors`, `title`, `title_html`, `title_latex`, `journal`, `volume`, `page_start`, `page_end`, `article_number`, `year`, `note`, `note_html`, `note_latex`, `doi`, `bibcode`, `url`, `bibtex`, `ris`, `citeproc_json`, `visible`) VALUES
(1, 'T. Test', 'Test Title', 'Test Title html', 'Test Title latex', 'testjournal', '1', '2', '3', '4', 1991, 'note', 'note html', 'note lahex', 'fakedoi.000', '', 'https://www.google.com', '', NULL, NULL, 0),
(2, '', '', '', '', '', '', '', '', '', NULL, '', '', '', '', '', '', '@article{handa2018brachypotherium,\r\n  title={Brachypotherium (Perissodactyla, Rhinocerotidae) from the late Miocene of Samburu Hills, Kenya},\r\n  author={Handa, Naoto and Nakatsukasa, Masato and Kunimatsu, Yutaka and Nakaya, Hideo},\r\n  journal={Geobios},\r\n  volume={51},\r\n  number={5},\r\n  pages={391--399},\r\n  year={2018},\r\n  publisher={Elsevier}\r\n}', NULL, NULL, 0),
(5, 'Yehoshua, Kolodnya, BoazLuza, MartinSanderb, W.A.Clemensc', 'Dinosaur bones: fossils or pseudomorphs? The pitfalls of physiology reconstruction from apatitic fossils.', '', '', 'Palaeogeography, Palaeoclimatology, Palaeoecology', '', '', '', '', NULL, '', '', '', '10.1016/S0031-0182(96)00112-5', '', '', '', NULL, NULL, 0);

-- --------------------------------------------------------

--
-- Rakenne taululle `front_referencelink`
--

CREATE TABLE `front_referencelink` (
  `id` bigint(20) NOT NULL,
  `doc_id_prefix` varchar(3) NOT NULL,
  `original_desc_ind` varchar(1) NOT NULL,
  `init_itis_desc_ind` varchar(1) NOT NULL,
  `change_track_id` int(11) NOT NULL,
  `vernacular_name` varchar(80) NOT NULL,
  `update_date` datetime(6) NOT NULL,
  `documentation_id_id` int(11) NOT NULL,
  `tsn_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Rakenne taululle `front_synonymlink`
--

CREATE TABLE `front_synonymlink` (
  `id` bigint(20) NOT NULL,
  `tsn` int(11) NOT NULL,
  `update_date` datetime(6) NOT NULL,
  `tsn_accepted_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Rakenne taululle `front_taxonauthorlkp`
--

CREATE TABLE `front_taxonauthorlkp` (
  `taxon_author_id` int(11) NOT NULL,
  `taxon_author` varchar(100) DEFAULT NULL,
  `update_date` datetime(6) DEFAULT NULL,
  `short_author` varchar(100) DEFAULT NULL,
  `kingdom_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Vedos taulusta `front_taxonauthorlkp`
--

INSERT INTO `front_taxonauthorlkp` (`taxon_author_id`, `taxon_author`, `update_date`, `short_author`, `kingdom_id`) VALUES
(1, 'Test Author', NULL, 'Test', 5);

-- --------------------------------------------------------

--
-- Rakenne taululle `front_taxonomicunit`
--

CREATE TABLE `front_taxonomicunit` (
  `tsn` int(11) NOT NULL,
  `unit_ind1` varchar(1) DEFAULT NULL,
  `unit_name1` varchar(35) NOT NULL,
  `unit_ind2` varchar(1) DEFAULT NULL,
  `unit_name2` varchar(35) DEFAULT NULL,
  `unit_ind3` varchar(7) DEFAULT NULL,
  `unit_name3` varchar(35) DEFAULT NULL,
  `unit_ind4` varchar(7) DEFAULT NULL,
  `unit_name4` varchar(35) DEFAULT NULL,
  `unnamed_taxon_ind` varchar(1) DEFAULT NULL,
  `name_usage` varchar(12) DEFAULT NULL,
  `unaccept_reason` varchar(50) DEFAULT NULL,
  `credibility_rtng` varchar(40) DEFAULT NULL,
  `completeness_rtng` varchar(10) DEFAULT NULL,
  `currency_rating` varchar(7) DEFAULT NULL,
  `phylo_sort_seq` int(11) DEFAULT NULL,
  `initial_time_stamp` datetime(6) DEFAULT NULL,
  `parent_tsn` int(11) NOT NULL,
  `rank_id` int(11) DEFAULT NULL,
  `hybrid_author_id` int(11) DEFAULT NULL,
  `update_date` datetime(6) DEFAULT NULL,
  `uncertain_prnt_ind` varchar(3) DEFAULT NULL,
  `n_usage` varchar(12) DEFAULT NULL,
  `complete_name` varchar(300) DEFAULT NULL,
  `kingdom_id` bigint(20) NOT NULL,
  `taxon_author_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Vedos taulusta `front_taxonomicunit`
--

INSERT INTO `front_taxonomicunit` (`tsn`, `unit_ind1`, `unit_name1`, `unit_ind2`, `unit_name2`, `unit_ind3`, `unit_name3`, `unit_ind4`, `unit_name4`, `unnamed_taxon_ind`, `name_usage`, `unaccept_reason`, `credibility_rtng`, `completeness_rtng`, `currency_rating`, `phylo_sort_seq`, `initial_time_stamp`, `parent_tsn`, `rank_id`, `hybrid_author_id`, `update_date`, `uncertain_prnt_ind`, `n_usage`, `complete_name`, `kingdom_id`, `taxon_author_id_id`) VALUES
(1, NULL, 'Homo', NULL, 'Sapiens', NULL, NULL, NULL, NULL, NULL, 'valid', NULL, 'TWG standards met', NULL, NULL, NULL, NULL, 2, 220, NULL, NULL, 'No', 'valid', 'Homo Sapiens', 5, 1),
(2, NULL, 'Homo', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'valid', NULL, 'TWG standards met', 'complete', '2021', 0, NULL, 3, 180, NULL, NULL, 'No', 'valid', 'Homo', 5, 1),
(3, NULL, 'Homininae', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'valid', NULL, 'TWG standards met', 'complete', '2021', 0, NULL, 4, 150, NULL, NULL, 'No', 'valid', 'Homininae', 5, 1),
(4, NULL, 'Hominidae', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'valid', NULL, 'TWG standards met', 'complete', '2021', 0, NULL, 5, 140, NULL, NULL, 'No', 'valid', 'Hominidae', 5, 1),
(5, NULL, 'Hominoidea', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'valid', NULL, 'TWG standards met', 'complete', '2021', 0, NULL, 6, 130, NULL, NULL, 'No', 'valid', 'Hominoidea', 5, 1),
(6, NULL, 'Simiiformes', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'valid', NULL, 'TWG standards met', 'complete', '2021', 0, NULL, 9, 120, NULL, NULL, 'No', 'valid', 'Simiiformes', 5, 1),
(7, NULL, 'Animalia', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 10, NULL, NULL, NULL, NULL, NULL, 5, 1),
(8, NULL, 'Bilateria', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 7, 10, NULL, NULL, NULL, NULL, NULL, 5, 1),
(9, NULL, 'Haplorrhini', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'valid', NULL, 'TWG standards met', 'complete', '2021', 0, NULL, 11, 110, NULL, NULL, 'No', 'valid', 'Haplorrhini', 5, 1),
(10, NULL, 'Deuterostomia', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 8, 25, NULL, NULL, NULL, NULL, NULL, 5, 1),
(11, NULL, 'Primates', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'valid', NULL, 'TWG standards met', 'complete', '2021', 0, NULL, 12, 100, NULL, NULL, 'No', 'valid', 'Primates', 5, 1),
(12, NULL, 'Eutheria', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'valid', NULL, 'TWG standards met', 'complete', '2014', 0, NULL, 15, 80, NULL, NULL, 'No', 'valid', 'Eutheria', 5, 1),
(13, NULL, 'Chordata', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 10, 30, NULL, NULL, NULL, NULL, NULL, 5, 1),
(14, NULL, 'Vertebrata', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 13, 40, NULL, NULL, NULL, NULL, NULL, 5, 1),
(15, NULL, 'Theria', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'valid', NULL, 'TWG standards met', 'complete', '2014', NULL, NULL, 18, 70, NULL, NULL, 'No', 'valid', 'Theria', 5, 1),
(16, NULL, 'Gnathostomata', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 14, 45, NULL, NULL, NULL, NULL, NULL, 5, 1),
(17, NULL, 'Tetrapoda', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 16, 50, NULL, NULL, NULL, NULL, NULL, 5, 1),
(18, NULL, 'Mammalia', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'valid', NULL, 'TWG standards met', 'complete', '2014', 0, NULL, 17, 60, NULL, NULL, 'No', 'valid', 'Mammalia', 5, 1);

-- --------------------------------------------------------

--
-- Rakenne taululle `front_taxonunittype`
--

CREATE TABLE `front_taxonunittype` (
  `id` bigint(20) NOT NULL,
  `rank_id` int(11) DEFAULT NULL,
  `rank_name` varchar(15) NOT NULL,
  `dir_parent_rank_id` int(11) DEFAULT NULL,
  `req_parent_rank_id` int(11) DEFAULT NULL,
  `update_date` datetime(6) DEFAULT NULL,
  `kingdom_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Vedos taulusta `front_taxonunittype`
--

INSERT INTO `front_taxonunittype` (`id`, `rank_id`, `rank_name`, `dir_parent_rank_id`, `req_parent_rank_id`, `update_date`, `kingdom_id`) VALUES
(1, 10, 'Kingdom', 10, 10, '2022-03-03 07:26:38.000000', 1),
(2, 20, 'Subkingdom', 10, 10, '2022-03-03 07:26:55.000000', 1),
(3, 30, 'Phylum', 20, 10, '2022-03-03 07:27:08.000000', 1),
(4, 40, 'Subphylum', 30, 30, NULL, 1),
(5, 50, 'Superclass', 40, 30, '2022-03-03 07:28:25.000000', 1),
(6, 60, 'Class', 50, 30, '2022-03-03 07:28:41.000000', 1),
(7, 70, 'Subclass', 60, 60, '2022-03-03 07:28:58.000000', 1),
(8, 80, 'Infraclass', 70, 60, '2022-03-03 07:29:13.000000', 1),
(9, 90, 'Superorder', 80, 60, '2022-03-03 07:29:30.000000', 1),
(10, 100, 'Order', 90, 60, '2022-03-03 07:29:42.000000', 1),
(11, 110, 'Suborder', 100, 100, '2022-03-03 07:30:04.000000', 1),
(12, 120, 'Infraorder', 110, 100, '2022-03-03 07:30:43.000000', 1),
(13, 130, 'Superfamily', 120, 100, '2022-03-03 07:31:01.000000', 1),
(14, 140, 'Family', 130, 100, '2022-03-03 07:31:14.000000', 1),
(15, 150, 'Subfamily', 140, 140, '2022-03-03 07:31:27.000000', 1),
(16, 160, 'Tribe', 150, 140, '2022-03-03 07:31:39.000000', 1),
(17, 170, 'Subtribe', 160, 140, '2022-03-03 07:32:00.000000', 1),
(18, 180, 'Genus', 170, 140, '2022-03-03 07:32:14.000000', 1),
(19, 190, 'Subgenus', 180, 180, '2022-03-03 07:32:27.000000', 1),
(20, 220, 'Species', 190, 180, '2022-03-03 07:32:39.000000', 1),
(21, 230, 'Subspecies', 220, 180, '2022-03-03 07:32:51.000000', 1),
(22, 10, 'Kingdom', 10, 10, '2022-03-03 07:48:36.000000', 2),
(23, 20, 'Subkingdom', 10, 10, '2022-03-03 07:48:47.000000', 2),
(24, 25, 'Infrakingdom', 20, 10, '2022-03-03 07:49:29.000000', 2),
(25, 30, 'Phylum', 25, 10, '2022-03-03 07:49:50.000000', 2),
(26, 40, 'Subphylum', 30, 30, '2022-03-03 07:50:06.000000', 2),
(27, 45, 'Infraphylum', 40, 30, '2022-03-03 07:50:20.000000', 2),
(28, 47, 'Parvphylum', 45, 30, '2022-03-03 07:50:37.000000', 2),
(29, 50, 'Superclass', 47, 30, '2022-03-03 07:50:52.000000', 2),
(30, 60, 'Class', 50, 30, '2022-03-03 07:51:05.000000', 2),
(31, 70, 'Subclass', 60, 60, '2022-03-03 07:51:26.000000', 2),
(32, 80, 'Infraclass', 70, 60, '2022-03-03 07:51:37.000000', 2),
(33, 90, 'Superorder', 80, 60, '2022-03-03 07:51:55.000000', 2),
(34, 100, 'Order', 90, 60, '2022-03-03 07:52:15.000000', 2),
(35, 110, 'Suborder', 100, 100, '2022-03-03 07:55:55.000000', 2),
(36, 120, 'Infraorder', 110, 100, '2022-03-03 07:56:10.000000', 2),
(37, 130, 'Superfamily', 120, 100, '2022-03-03 07:56:25.000000', 2),
(38, 140, 'Family', 130, 100, '2022-03-03 07:56:38.000000', 2),
(39, 150, 'Subfamily', 140, 140, '2022-03-03 07:56:49.000000', 2),
(40, 160, 'Tribe', 130, 100, '2022-03-03 07:57:03.000000', 2),
(41, 170, 'Subtribe', 160, 140, '2022-03-03 07:57:23.000000', 2),
(42, 180, 'Genus', 170, 140, '2022-03-03 07:57:38.000000', 2),
(43, 190, 'Subgenus', 180, 180, '2022-03-03 07:57:50.000000', 2),
(44, 220, 'Species', 190, 180, '2022-03-03 07:58:07.000000', 2),
(45, 230, 'Subspecies', 220, 180, NULL, 2),
(46, 240, 'Variety', 230, 180, '2022-03-03 07:58:49.000000', 2),
(47, 10, 'Kingdom', 10, 10, NULL, 3),
(48, 20, 'Subkingdom', 10, 10, NULL, 3),
(49, 25, 'Infrakingdom', 20, 10, NULL, 3),
(50, 27, 'Superdivision', 25, 10, NULL, 3),
(51, 30, 'Division', 27, 10, NULL, 3),
(52, 40, 'Subdivision', 30, 30, NULL, 3),
(53, 45, 'Infradivision', 40, 30, NULL, 3),
(54, 50, 'Superclass', 45, 30, NULL, 3),
(55, 60, 'Class', 50, 30, NULL, 3),
(56, 70, 'Subclass', 60, 60, NULL, 3),
(57, 80, 'Infraclass', 70, 60, NULL, 3),
(58, 90, 'Superorder', 80, 60, NULL, 3),
(59, 100, 'Order', 90, 60, NULL, 3),
(60, 110, 'Suborder', 100, 100, NULL, 3),
(61, 140, 'Family', 110, 100, NULL, 3),
(62, 150, 'Subfamily', 140, 140, NULL, 3),
(63, 160, 'Tribe', 150, 140, NULL, 3),
(64, 170, 'Subtribe', 160, 140, NULL, 3),
(65, 180, 'Genus', 170, 140, NULL, 3),
(66, 190, 'Subgenus', 180, 180, NULL, 3),
(67, 200, 'Section', 190, 180, NULL, 3),
(68, 210, 'Subsection', 200, 180, NULL, 3),
(69, 220, 'Species', 210, 180, NULL, 3),
(70, 230, 'Subspecies', 220, 180, NULL, 3),
(71, 240, 'Variety', 220, 180, NULL, 3),
(72, 250, 'Subvariety', 240, 180, NULL, 3),
(73, 260, 'Form', 220, 180, NULL, 3),
(74, 270, 'Subform', 260, 180, NULL, 3),
(75, 10, 'Kingdom', 10, 10, NULL, 4),
(76, 20, 'Subkingdom', 10, 10, NULL, 4),
(77, 30, 'Division', 20, 10, NULL, 4),
(78, 40, 'Subdivision', 30, 30, NULL, 4),
(79, 60, 'Class', 40, 30, NULL, 4),
(80, 70, 'Subclass', 60, 60, NULL, 4),
(81, 90, 'Superorder', 70, 60, NULL, 4),
(82, 100, 'Order', 90, 60, NULL, 4),
(83, 110, 'Suborder', 100, 100, NULL, 4),
(84, 140, 'Family', 110, 100, NULL, 4),
(85, 150, 'Subfamily', 140, 140, NULL, 4),
(86, 160, 'Tribe', 150, 140, NULL, 4),
(87, 170, 'Subtribe', 160, 140, NULL, 4),
(88, 180, 'Genus', 170, 140, NULL, 4),
(89, 190, 'Subgenus', 180, 180, NULL, 4),
(90, 200, 'Section', 190, 180, NULL, 4),
(91, 210, 'Subsection', 200, 180, NULL, 4),
(92, 220, 'Species', 210, 180, NULL, 4),
(93, 230, 'Subspecies', 220, 180, NULL, 4),
(94, 240, 'Variety', 220, 180, NULL, 4),
(95, 250, 'Subvariety', 240, 180, NULL, 4),
(96, 260, 'Form', 220, 180, NULL, 4),
(97, 270, 'Subform', 260, 180, NULL, 4),
(98, 10, 'Kingdom', 10, 10, NULL, 5),
(99, 20, 'Subkingdom', 10, 10, NULL, 5),
(100, 25, 'Infrakingdom', 20, 10, NULL, 5),
(101, 27, 'Superphylum', 25, 10, NULL, 5),
(102, 30, 'Phylum', 27, 10, NULL, 5),
(103, 40, 'Subphylum', 30, 30, NULL, 5),
(104, 45, 'Infraphylum', 40, 30, NULL, 5),
(105, 50, 'Superclass', 45, 30, NULL, 5),
(106, 60, 'Class', 50, 30, NULL, 5),
(107, 70, 'Subclass', 60, 60, NULL, 5),
(108, 80, 'Infraclass', 70, 60, NULL, 5),
(109, 90, 'Superorder', 80, 60, NULL, 5),
(110, 100, 'Order', 90, 60, NULL, 5),
(111, 110, 'Suborder', 100, 100, NULL, 5),
(112, 120, 'Infraorder', 110, 100, NULL, 5),
(113, 124, 'Section', 120, 100, NULL, 5),
(114, 126, 'Subsection', 124, 100, NULL, 5),
(115, 130, 'Superfamily', 126, 100, NULL, 5),
(116, 140, 'Family', 130, 100, NULL, 5),
(117, 150, 'Subfamily', 140, 140, NULL, 5),
(118, 160, 'Tribe', 150, 140, NULL, 5),
(119, 170, 'Subtribe', 160, 140, NULL, 5),
(120, 180, 'Genus', 170, 140, NULL, 5),
(121, 190, 'Subgenus', 180, 180, NULL, 5),
(122, 220, 'Species', 190, 180, NULL, 5),
(123, 230, 'Subspecies', 220, 220, NULL, 5),
(124, 240, 'Variety', 220, 220, NULL, 5),
(125, 245, 'Form', 220, 220, NULL, 5),
(126, 250, 'Race', 220, 220, NULL, 5),
(127, 255, 'Stirp', 220, 220, NULL, 5),
(128, 260, 'Morph', 220, 220, NULL, 5),
(129, 265, 'Aberration', 220, 220, NULL, 5),
(130, 300, 'Unspecified', 220, 220, NULL, 5),
(131, 10, 'Kingdom', 10, 10, NULL, 6),
(132, 20, 'Subkingdom', 10, 10, NULL, 6),
(133, 25, 'Infrakingdom', 20, 10, NULL, 6),
(134, 27, 'Superdivision', 25, 10, NULL, 6),
(135, 30, 'Division', 27, 10, NULL, 6),
(136, 40, 'Subdivision', 30, 30, NULL, 6),
(137, 45, 'Infradivision', 40, 30, NULL, 6),
(138, 47, 'Parvdivision', 45, 30, NULL, 6),
(139, 50, 'Superclass', 47, 30, NULL, 6),
(140, 60, 'Class', 50, 30, NULL, 6),
(141, 70, 'Subclass', 60, 60, NULL, 6),
(142, 80, 'Infraclass', 70, 60, NULL, 6),
(143, 90, 'Superorder', 80, 60, NULL, 6),
(144, 100, 'Order', 90, 60, NULL, 6),
(145, 110, 'Suborder', 100, 100, NULL, 6),
(146, 140, 'Family', 110, 100, NULL, 6),
(147, 150, 'Subfamily', 140, 140, NULL, 6),
(148, 160, 'Tribe', 150, 140, NULL, 6),
(149, 170, 'Subtribe', 160, 140, NULL, 6),
(150, 180, 'Genus', 170, 140, NULL, 6),
(151, 190, 'Subgenus', 180, 180, NULL, 6),
(152, 200, 'Section', 190, 180, NULL, 6),
(153, 210, 'Subsection', 200, 180, NULL, 6),
(154, 220, 'Species', 210, 180, NULL, 6),
(155, 230, 'Subspecies', 220, 180, NULL, 6),
(156, 240, 'Variety', 230, 180, NULL, 6),
(157, 250, 'Subvariety', 240, 180, NULL, 6),
(158, 260, 'Form', 250, 180, NULL, 6),
(159, 270, 'Subform', 260, 180, NULL, 6),
(160, 10, 'Kingdom', 10, 10, NULL, 7),
(161, 20, 'Subkingdom', 10, 10, NULL, 7),
(162, 30, 'Phylum', 20, 10, NULL, 7),
(163, 40, 'Subphylum', 30, 30, NULL, 7),
(164, 50, 'Superclass', 40, 30, NULL, 7),
(165, 60, 'Class', 50, 30, NULL, 7),
(166, 70, 'Subclass', 60, 60, NULL, 7),
(167, 80, 'Infraclass', 70, 60, NULL, 7),
(168, 90, 'Superorder', 80, 60, NULL, 7),
(169, 100, 'Order', 90, 60, NULL, 7),
(170, 110, 'Suborder', 100, 100, NULL, 7),
(171, 120, 'Infraorder', 110, 100, NULL, 7),
(172, 130, 'Superfamily', 120, 100, NULL, 7),
(173, 140, 'Family', 130, 100, NULL, 7),
(174, 150, 'Subfamily', 140, 140, NULL, 7),
(175, 160, 'Tribe', 150, 140, NULL, 7),
(176, 170, 'Subtribe', 160, 140, NULL, 7),
(177, 180, 'Genus', 170, 140, NULL, 7),
(178, 190, 'Subgenus', 180, 180, NULL, 7),
(179, 220, 'Species', 190, 180, NULL, 7),
(180, 230, 'Subspecies', 220, 180, NULL, 7);

-- --------------------------------------------------------

--
-- Rakenne taululle `front_tucommentlink`
--

CREATE TABLE `front_tucommentlink` (
  `id` bigint(20) NOT NULL,
  `update_date` datetime(6) DEFAULT NULL,
  `comment_id_id` bigint(20) NOT NULL,
  `tsn_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Rakenne taululle `refs_ref`
--

CREATE TABLE `refs_ref` (
  `id` int(11) NOT NULL,
  `authors` longtext NOT NULL,
  `title` longtext NOT NULL,
  `title_html` longtext NOT NULL,
  `title_latex` longtext NOT NULL,
  `journal` varchar(500) NOT NULL,
  `volume` varchar(10) NOT NULL,
  `page_start` varchar(10) NOT NULL,
  `page_end` varchar(10) NOT NULL,
  `article_number` varchar(16) NOT NULL,
  `year` int(11) DEFAULT NULL,
  `note` longtext NOT NULL,
  `note_html` longtext NOT NULL,
  `note_latex` longtext NOT NULL,
  `doi` varchar(100) NOT NULL,
  `bibcode` varchar(19) NOT NULL,
  `url` varchar(200) NOT NULL,
  `bibtex` longtext DEFAULT NULL,
  `ris` longtext DEFAULT NULL,
  `citeproc_json` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Rakenne taululle `socialaccount_socialaccount`
--

CREATE TABLE `socialaccount_socialaccount` (
  `id` int(11) NOT NULL,
  `provider` varchar(30) NOT NULL,
  `uid` varchar(191) NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `extra_data` longtext NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Vedos taulusta `socialaccount_socialaccount`
--

INSERT INTO `socialaccount_socialaccount` (`id`, `provider`, `uid`, `last_login`, `date_joined`, `extra_data`, `user_id`) VALUES
(1, 'orcid', '0000-0001-8828-3006', '2022-03-05 18:50:44.610627', '2022-02-02 09:25:07.944905', '{\"orcid-identifier\": {\"uri\": \"https://orcid.org/0000-0001-8828-3006\", \"path\": \"0000-0001-8828-3006\", \"host\": \"orcid.org\"}, \"preferences\": {\"locale\": \"EN\"}, \"history\": {\"creation-method\": \"DIRECT\", \"completion-date\": null, \"submission-date\": {\"value\": 1643369193753}, \"last-modified-date\": {\"value\": 1646506243839}, \"claimed\": true, \"source\": null, \"deactivation-date\": null, \"verified-email\": true, \"verified-primary-email\": true}, \"person\": {\"last-modified-date\": null, \"name\": {\"created-date\": {\"value\": 1643369194024}, \"last-modified-date\": {\"value\": 1643369194024}, \"given-names\": {\"value\": \"Tuomas\"}, \"family-name\": {\"value\": \"Aaltonen\"}, \"credit-name\": null, \"source\": null, \"visibility\": \"PUBLIC\", \"path\": \"0000-0001-8828-3006\"}, \"other-names\": {\"last-modified-date\": null, \"other-name\": [], \"path\": \"/0000-0001-8828-3006/other-names\"}, \"biography\": null, \"researcher-urls\": {\"last-modified-date\": null, \"researcher-url\": [], \"path\": \"/0000-0001-8828-3006/researcher-urls\"}, \"emails\": {\"last-modified-date\": null, \"email\": [], \"path\": \"/0000-0001-8828-3006/email\"}, \"addresses\": {\"last-modified-date\": null, \"address\": [], \"path\": \"/0000-0001-8828-3006/address\"}, \"keywords\": {\"last-modified-date\": null, \"keyword\": [], \"path\": \"/0000-0001-8828-3006/keywords\"}, \"external-identifiers\": {\"last-modified-date\": null, \"external-identifier\": [], \"path\": \"/0000-0001-8828-3006/external-identifiers\"}, \"path\": \"/0000-0001-8828-3006/person\"}, \"activities-summary\": {\"last-modified-date\": null, \"educations\": {\"last-modified-date\": null, \"education-summary\": [], \"path\": \"/0000-0001-8828-3006/educations\"}, \"employments\": {\"last-modified-date\": null, \"employment-summary\": [], \"path\": \"/0000-0001-8828-3006/employments\"}, \"fundings\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0001-8828-3006/fundings\"}, \"peer-reviews\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0001-8828-3006/peer-reviews\"}, \"works\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0001-8828-3006/works\"}, \"path\": \"/0000-0001-8828-3006/activities\"}, \"path\": \"/0000-0001-8828-3006\"}', 1),
(2, 'orcid', '0000-0002-9573-3295', '2022-02-26 08:06:38.579648', '2022-02-02 09:27:41.378210', '{\"orcid-identifier\": {\"uri\": \"https://orcid.org/0000-0002-9573-3295\", \"path\": \"0000-0002-9573-3295\", \"host\": \"orcid.org\"}, \"preferences\": {\"locale\": \"EN\"}, \"history\": {\"creation-method\": \"DIRECT\", \"completion-date\": null, \"submission-date\": {\"value\": 1643116893675}, \"last-modified-date\": {\"value\": 1645862797559}, \"claimed\": true, \"source\": null, \"deactivation-date\": null, \"verified-email\": true, \"verified-primary-email\": true}, \"person\": {\"last-modified-date\": null, \"name\": {\"created-date\": {\"value\": 1643116893952}, \"last-modified-date\": {\"value\": 1643116893952}, \"given-names\": {\"value\": \"Seppo\"}, \"family-name\": {\"value\": \"Kajantie\"}, \"credit-name\": null, \"source\": null, \"visibility\": \"PUBLIC\", \"path\": \"0000-0002-9573-3295\"}, \"other-names\": {\"last-modified-date\": null, \"other-name\": [], \"path\": \"/0000-0002-9573-3295/other-names\"}, \"biography\": null, \"researcher-urls\": {\"last-modified-date\": null, \"researcher-url\": [], \"path\": \"/0000-0002-9573-3295/researcher-urls\"}, \"emails\": {\"last-modified-date\": null, \"email\": [], \"path\": \"/0000-0002-9573-3295/email\"}, \"addresses\": {\"last-modified-date\": null, \"address\": [], \"path\": \"/0000-0002-9573-3295/address\"}, \"keywords\": {\"last-modified-date\": null, \"keyword\": [], \"path\": \"/0000-0002-9573-3295/keywords\"}, \"external-identifiers\": {\"last-modified-date\": null, \"external-identifier\": [], \"path\": \"/0000-0002-9573-3295/external-identifiers\"}, \"path\": \"/0000-0002-9573-3295/person\"}, \"activities-summary\": {\"last-modified-date\": null, \"educations\": {\"last-modified-date\": null, \"education-summary\": [], \"path\": \"/0000-0002-9573-3295/educations\"}, \"employments\": {\"last-modified-date\": null, \"employment-summary\": [], \"path\": \"/0000-0002-9573-3295/employments\"}, \"fundings\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0002-9573-3295/fundings\"}, \"peer-reviews\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0002-9573-3295/peer-reviews\"}, \"works\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0002-9573-3295/works\"}, \"path\": \"/0000-0002-9573-3295/activities\"}, \"path\": \"/0000-0002-9573-3295\"}', 2);
INSERT INTO `socialaccount_socialaccount` (`id`, `provider`, `uid`, `last_login`, `date_joined`, `extra_data`, `user_id`) VALUES
(3, 'orcid', '0000-0001-9627-8821', '2022-02-28 07:47:28.143252', '2022-02-02 10:47:03.533810', '{\"orcid-identifier\": {\"uri\": \"https://orcid.org/0000-0001-9627-8821\", \"path\": \"0000-0001-9627-8821\", \"host\": \"orcid.org\"}, \"preferences\": {\"locale\": \"EN\"}, \"history\": {\"creation-method\": \"WEBSITE\", \"completion-date\": null, \"submission-date\": {\"value\": 1386965645999}, \"last-modified-date\": {\"value\": 1646034447237}, \"claimed\": true, \"source\": null, \"deactivation-date\": null, \"verified-email\": true, \"verified-primary-email\": true}, \"person\": {\"last-modified-date\": {\"value\": 1561208272899}, \"name\": {\"created-date\": {\"value\": 1460756243754}, \"last-modified-date\": {\"value\": 1484897974700}, \"given-names\": {\"value\": \"Kari\"}, \"family-name\": {\"value\": \"Lintulaakso\"}, \"credit-name\": {\"value\": \"Kari-Erik Johannes Lintulaakso\"}, \"source\": null, \"visibility\": \"PUBLIC\", \"path\": \"0000-0001-9627-8821\"}, \"other-names\": {\"last-modified-date\": {\"value\": 1487319728934}, \"other-name\": [{\"created-date\": {\"value\": 1487319728934}, \"last-modified-date\": {\"value\": 1487319728934}, \"source\": {\"source-orcid\": {\"uri\": \"https://orcid.org/0000-0001-9627-8821\", \"path\": \"0000-0001-9627-8821\", \"host\": \"orcid.org\"}, \"source-client-id\": null, \"source-name\": {\"value\": \"Kari-Erik Johannes Lintulaakso\"}}, \"content\": \"Kari Lintulaakso\", \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/other-names/900268\", \"put-code\": 900268, \"display-index\": 1}], \"path\": \"/0000-0001-9627-8821/other-names\"}, \"biography\": null, \"researcher-urls\": {\"last-modified-date\": {\"value\": 1561208272899}, \"researcher-url\": [{\"created-date\": {\"value\": 1561208272899}, \"last-modified-date\": {\"value\": 1561208272899}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/APP-5E1VKQXON4GX3LS0\", \"path\": \"APP-5E1VKQXON4GX3LS0\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"University of Helsinki\"}}, \"url-name\": \"University of Helsinki profile page\", \"url\": {\"value\": \"https://researchportal.helsinki.fi/en/persons/2eca574e-161c-4d24-9a80-c5039c873631\"}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/researcher-urls/1762649\", \"put-code\": 1762649, \"display-index\": 0}], \"path\": \"/0000-0001-9627-8821/researcher-urls\"}, \"emails\": {\"last-modified-date\": null, \"email\": [], \"path\": \"/0000-0001-9627-8821/email\"}, \"addresses\": {\"last-modified-date\": {\"value\": 1487319635587}, \"address\": [{\"created-date\": {\"value\": 1487319635587}, \"last-modified-date\": {\"value\": 1487319635587}, \"source\": {\"source-orcid\": {\"uri\": \"https://orcid.org/0000-0001-9627-8821\", \"path\": \"0000-0001-9627-8821\", \"host\": \"orcid.org\"}, \"source-client-id\": null, \"source-name\": {\"value\": \"Kari-Erik Johannes Lintulaakso\"}}, \"country\": {\"value\": \"FI\"}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/address/634405\", \"put-code\": 634405, \"display-index\": 1}], \"path\": \"/0000-0001-9627-8821/address\"}, \"keywords\": {\"last-modified-date\": null, \"keyword\": [], \"path\": \"/0000-0001-9627-8821/keywords\"}, \"external-identifiers\": {\"last-modified-date\": {\"value\": 1517869567419}, \"external-identifier\": [{\"created-date\": {\"value\": 1386965682875}, \"last-modified-date\": {\"value\": 1517869567419}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/0000-0003-1377-5676\", \"path\": \"0000-0003-1377-5676\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"ResearcherID\"}}, \"external-id-type\": \"ResearcherID\", \"external-id-value\": \"N-7775-2013\", \"external-id-url\": {\"value\": \"http://www.researcherid.com/rid/N-7775-2013\"}, \"external-id-relationship\": \"SELF\", \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/external-identifiers/64151\", \"put-code\": 64151, \"display-index\": 0}], \"path\": \"/0000-0001-9627-8821/external-identifiers\"}, \"path\": \"/0000-0001-9627-8821/person\"}, \"activities-summary\": {\"last-modified-date\": {\"value\": 1639815068817}, \"educations\": {\"last-modified-date\": {\"value\": 1639815068174}, \"education-summary\": [{\"created-date\": {\"value\": 1599906974714}, \"last-modified-date\": {\"value\": 1639815068174}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/APP-5E1VKQXON4GX3LS0\", \"path\": \"APP-5E1VKQXON4GX3LS0\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"University of Helsinki\"}}, \"department-name\": null, \"role-title\": null, \"start-date\": null, \"end-date\": null, \"organization\": {\"name\": \"University of Helsinki\", \"address\": {\"city\": \"Helsinki\", \"region\": \"\", \"country\": \"FI\"}, \"disambiguated-organization\": null}, \"visibility\": \"PUBLIC\", \"put-code\": 12664723, \"path\": \"/0000-0001-9627-8821/education/12664723\"}], \"path\": \"/0000-0001-9627-8821/educations\"}, \"employments\": {\"last-modified-date\": {\"value\": 1639815068817}, \"employment-summary\": [{\"created-date\": {\"value\": 1498950433620}, \"last-modified-date\": {\"value\": 1639815068817}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/APP-5E1VKQXON4GX3LS0\", \"path\": \"APP-5E1VKQXON4GX3LS0\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"University of Helsinki\"}}, \"department-name\": null, \"role-title\": null, \"start-date\": null, \"end-date\": null, \"organization\": {\"name\": \"University of Helsinki\", \"address\": {\"city\": \"Helsinki\", \"region\": \"\", \"country\": \"FI\"}, \"disambiguated-organization\": null}, \"visibility\": \"PUBLIC\", \"put-code\": 4186555, \"path\": \"/0000-0001-9627-8821/employment/4186555\"}, {\"created-date\": {\"value\": 1576741216509}, \"last-modified-date\": {\"value\": 1605194858916}, \"source\": {\"source-orcid\": {\"uri\": \"https://orcid.org/0000-0001-9627-8821\", \"path\": \"0000-0001-9627-8821\", \"host\": \"orcid.org\"}, \"source-client-id\": null, \"source-name\": {\"value\": \"Kari-Erik Johannes Lintulaakso\"}}, \"department-name\": \"Natural Sciences Unit\", \"role-title\": \"Collection Coordinator\", \"start-date\": {\"year\": {\"value\": \"2017\"}, \"month\": {\"value\": \"08\"}, \"day\": {\"value\": \"01\"}}, \"end-date\": null, \"organization\": {\"name\": \"Finnish Museum of Natural History LUOMUS\", \"address\": {\"city\": \"Helsinki\", \"region\": \"\", \"country\": \"FI\"}, \"disambiguated-organization\": null}, \"visibility\": \"PUBLIC\", \"put-code\": 9398344, \"path\": \"/0000-0001-9627-8821/employment/9398344\"}], \"path\": \"/0000-0001-9627-8821/employments\"}, \"fundings\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0001-9627-8821/fundings\"}, \"peer-reviews\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0001-9627-8821/peer-reviews\"}, \"works\": {\"last-modified-date\": {\"value\": 1637213608980}, \"group\": [{\"last-modified-date\": {\"value\": 1637213608980}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"doi\", \"external-id-value\": \"10.3897/rio.7.e76875\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"source-work-id\", \"external-id-value\": \"240a837c-f1bb-40af-855e-407049e56cd9\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"work-summary\": [{\"put-code\": 103359597, \"created-date\": {\"value\": 1637213608980}, \"last-modified-date\": {\"value\": 1637213608980}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/APP-5E1VKQXON4GX3LS0\", \"path\": \"APP-5E1VKQXON4GX3LS0\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"University of Helsinki\"}}, \"title\": {\"title\": {\"value\": \"Geology collection policy of the Finnish Museum of Natural History\"}, \"subtitle\": null, \"translated-title\": null}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"source-work-id\", \"external-id-value\": \"240a837c-f1bb-40af-855e-407049e56cd9\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.3897/rio.7.e76875\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"type\": \"JOURNAL_ARTICLE\", \"publication-date\": {\"year\": {\"value\": \"2021\"}, \"month\": {\"value\": \"10\"}, \"day\": {\"value\": \"25\"}, \"media-type\": null}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/work/103359597\", \"display-index\": \"0\"}]}, {\"last-modified-date\": {\"value\": 1560854430473}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"doi\", \"external-id-value\": \"10.3897/biss.3.36981\", \"external-id-url\": {\"value\": \"https://doi.org/10.3897/biss.3.36981\"}, \"external-id-relationship\": \"SELF\"}]}, \"work-summary\": [{\"put-code\": 58599416, \"created-date\": {\"value\": 1560854430473}, \"last-modified-date\": {\"value\": 1560854430473}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/0000-0001-9884-1913\", \"path\": \"0000-0001-9884-1913\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"Crossref\"}}, \"title\": {\"title\": {\"value\": \"The Problem of Stratigraphical Time Grouping of Earth Science Data\"}, \"subtitle\": null, \"translated-title\": null}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"doi\", \"external-id-value\": \"10.3897/biss.3.36981\", \"external-id-url\": {\"value\": \"https://doi.org/10.3897/biss.3.36981\"}, \"external-id-relationship\": \"SELF\"}]}, \"type\": \"JOURNAL_ARTICLE\", \"publication-date\": {\"year\": {\"value\": \"2019\"}, \"month\": {\"value\": \"06\"}, \"day\": {\"value\": \"18\"}, \"media-type\": null}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/work/58599416\", \"display-index\": \"0\"}]}, {\"last-modified-date\": {\"value\": 1623160451067}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"doi\", \"external-id-value\": \"10.1111/jbi.13480\", \"external-id-url\": {\"value\": \"https://doi.org/10.1111/jbi.13480\"}, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"wosuid\", \"external-id-value\": \"000456346000015\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"source-work-id\", \"external-id-value\": \"3847b868-4101-435b-8d64-c27393e77e52\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-85057967997\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"work-summary\": [{\"put-code\": 51327572, \"created-date\": {\"value\": 1543973878061}, \"last-modified-date\": {\"value\": 1623160451067}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/0000-0001-9884-1913\", \"path\": \"0000-0001-9884-1913\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"Crossref\"}}, \"title\": {\"title\": {\"value\": \"Land mammals form eight functionally and climatically distinct faunas in North America but only one in Europe\"}, \"subtitle\": null, \"translated-title\": null}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"doi\", \"external-id-value\": \"10.1111/jbi.13480\", \"external-id-url\": {\"value\": \"https://doi.org/10.1111/jbi.13480\"}, \"external-id-relationship\": \"SELF\"}]}, \"type\": \"JOURNAL_ARTICLE\", \"publication-date\": {\"year\": {\"value\": \"2019\"}, \"month\": {\"value\": \"01\"}, \"day\": {\"value\": \"04\"}, \"media-type\": null}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/work/51327572\", \"display-index\": \"0\"}, {\"put-code\": 53828542, \"created-date\": {\"value\": 1549687921707}, \"last-modified-date\": {\"value\": 1599906979308}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/APP-5E1VKQXON4GX3LS0\", \"path\": \"APP-5E1VKQXON4GX3LS0\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"University of Helsinki\"}}, \"title\": {\"title\": {\"value\": \"Land mammals form eight functionally and climatically distinct faunas in North America but only one in Europe\"}, \"subtitle\": null, \"translated-title\": null}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"source-work-id\", \"external-id-value\": \"3847b868-4101-435b-8d64-c27393e77e52\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-85057967997\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"wosuid\", \"external-id-value\": \"000456346000015\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.1111/jbi.13480\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"type\": \"JOURNAL_ARTICLE\", \"publication-date\": {\"year\": {\"value\": \"2019\"}, \"month\": {\"value\": \"01\"}, \"day\": null, \"media-type\": null}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/work/53828542\", \"display-index\": \"0\"}]}, {\"last-modified-date\": {\"value\": 1599906980064}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"isbn\", \"external-id-value\": \"978-951-51-3983-2\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"source-work-id\", \"external-id-value\": \"ef58a719-f8d5-4252-98fe-c14a8e782f36\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"isbn\", \"external-id-value\": \"978-951-51-3982-5\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"work-summary\": [{\"put-code\": 54151499, \"created-date\": {\"value\": 1550296484538}, \"last-modified-date\": {\"value\": 1599906980064}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/APP-5E1VKQXON4GX3LS0\", \"path\": \"APP-5E1VKQXON4GX3LS0\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"University of Helsinki\"}}, \"title\": {\"title\": {\"value\": \"Taxon free analysis of mammalian communities in relation to evolutionary survivorship and environmental factors\"}, \"subtitle\": null, \"translated-title\": null}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"source-work-id\", \"external-id-value\": \"ef58a719-f8d5-4252-98fe-c14a8e782f36\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"isbn\", \"external-id-value\": \"978-951-51-3983-2\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"isbn\", \"external-id-value\": \"978-951-51-3982-5\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"type\": \"DISSERTATION\", \"publication-date\": {\"year\": {\"value\": \"2018\"}, \"month\": {\"value\": \"10\"}, \"day\": {\"value\": \"24\"}, \"media-type\": null}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/work/54151499\", \"display-index\": \"0\"}]}, {\"last-modified-date\": {\"value\": 1601078481113}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-85055735560\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.1007/978-3-319-94265-0_16\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"source-work-id\", \"external-id-value\": \"0e81b24b-d25c-46ab-a48c-0a2ab8c1a5f7\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"work-summary\": [{\"put-code\": 46651304, \"created-date\": {\"value\": 1531882936472}, \"last-modified-date\": {\"value\": 1601078481113}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/APP-5E1VKQXON4GX3LS0\", \"path\": \"APP-5E1VKQXON4GX3LS0\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"University of Helsinki\"}}, \"title\": {\"title\": {\"value\": \"Mammal community structure analysis\"}, \"subtitle\": null, \"translated-title\": null}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"source-work-id\", \"external-id-value\": \"0e81b24b-d25c-46ab-a48c-0a2ab8c1a5f7\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-85055735560\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.1007/978-3-319-94265-0_16\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"isbn\", \"external-id-value\": \"978-3-319-94265-0\", \"external-id-url\": null, \"external-id-relationship\": \"PART_OF\"}, {\"external-id-type\": \"isbn\", \"external-id-value\": \"978-3-319-94264-3\", \"external-id-url\": null, \"external-id-relationship\": \"PART_OF\"}]}, \"type\": \"BOOK_CHAPTER\", \"publication-date\": {\"year\": {\"value\": \"2018\"}, \"month\": null, \"day\": null, \"media-type\": null}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/work/46651304\", \"display-index\": \"0\"}]}, {\"last-modified-date\": {\"value\": 1599906978808}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-85017417119\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"wosuid\", \"external-id-value\": \"000419756400011\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"source-work-id\", \"external-id-value\": \"7b505a03-cf92-4cff-a861-52ee048bbb78\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.26879/729\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"work-summary\": [{\"put-code\": 33532159, \"created-date\": {\"value\": 1496531297507}, \"last-modified-date\": {\"value\": 1599906978808}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/APP-5E1VKQXON4GX3LS0\", \"path\": \"APP-5E1VKQXON4GX3LS0\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"University of Helsinki\"}}, \"title\": {\"title\": {\"value\": \"RNames, a stratigraphical database designed for the statistical analysis of fossil occurrences\"}, \"subtitle\": null, \"translated-title\": null}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"source-work-id\", \"external-id-value\": \"7b505a03-cf92-4cff-a861-52ee048bbb78\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-85017417119\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"wosuid\", \"external-id-value\": \"000419756400011\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.26879/729\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"type\": \"JOURNAL_ARTICLE\", \"publication-date\": {\"year\": {\"value\": \"2017\"}, \"month\": {\"value\": \"04\"}, \"day\": null, \"media-type\": null}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/work/33532159\", \"display-index\": \"0\"}]}, {\"last-modified-date\": {\"value\": 1599906976631}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"source-work-id\", \"external-id-value\": \"2d6f7cc6-3c9b-419f-a02d-b739c85c66b1\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.1016/j.palaeo.2016.04.012\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"wosuid\", \"external-id-value\": \"000377732200003\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-84963808237\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"work-summary\": [{\"put-code\": 24680511, \"created-date\": {\"value\": 1465799828145}, \"last-modified-date\": {\"value\": 1496531297507}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/0000-0001-9884-1913\", \"path\": \"0000-0001-9884-1913\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"Crossref\"}}, \"title\": {\"title\": {\"value\": \"Diet and locomotion, but not body size, differentiate mammal communities in worldwide tropical ecosystems\"}, \"subtitle\": null, \"translated-title\": null}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"doi\", \"external-id-value\": \"10.1016/j.palaeo.2016.04.012\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"type\": \"JOURNAL_ARTICLE\", \"publication-date\": {\"year\": {\"value\": \"2016\"}, \"month\": {\"value\": \"07\"}, \"day\": null, \"media-type\": null}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/work/24680511\", \"display-index\": \"0\"}, {\"put-code\": 29631420, \"created-date\": {\"value\": 1484897973552}, \"last-modified-date\": {\"value\": 1599906976631}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/APP-5E1VKQXON4GX3LS0\", \"path\": \"APP-5E1VKQXON4GX3LS0\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"University of Helsinki\"}}, \"title\": {\"title\": {\"value\": \"Diet and locomotion, but not body size, differentiate mammal communities in worldwide tropical ecosystems\"}, \"subtitle\": null, \"translated-title\": null}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"source-work-id\", \"external-id-value\": \"2d6f7cc6-3c9b-419f-a02d-b739c85c66b1\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"wosuid\", \"external-id-value\": \"000377732200003\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-84963808237\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.1016/j.palaeo.2016.04.012\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"type\": \"JOURNAL_ARTICLE\", \"publication-date\": {\"year\": {\"value\": \"2016\"}, \"month\": {\"value\": \"07\"}, \"day\": {\"value\": \"15\"}, \"media-type\": null}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/work/29631420\", \"display-index\": \"0\"}]}, {\"last-modified-date\": {\"value\": 1599906979788}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"wosuid\", \"external-id-value\": \"000335382700001\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.1098/rspb.2013.2049\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"source-work-id\", \"external-id-value\": \"f665f2fc-f238-4854-b901-f5f7b4954532\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-84898670961\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"work-summary\": [{\"put-code\": 29631421, \"created-date\": {\"value\": 1484897973553}, \"last-modified-date\": {\"value\": 1599906979788}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/APP-5E1VKQXON4GX3LS0\", \"path\": \"APP-5E1VKQXON4GX3LS0\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"University of Helsinki\"}}, \"title\": {\"title\": {\"value\": \"Patterns of maximum body size evolution in Cenozoic land mammals\"}, \"subtitle\": null, \"translated-title\": null}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"source-work-id\", \"external-id-value\": \"f665f2fc-f238-4854-b901-f5f7b4954532\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"wosuid\", \"external-id-value\": \"000335382700001\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"wosuid\", \"external-id-value\": \"000335382700001\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-84898670961\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.1098/rspb.2013.2049\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"type\": \"JOURNAL_ARTICLE\", \"publication-date\": {\"year\": {\"value\": \"2014\"}, \"month\": {\"value\": \"06\"}, \"day\": {\"value\": \"07\"}, \"media-type\": null}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/work/29631421\", \"display-index\": \"0\"}]}, {\"last-modified-date\": {\"value\": 1599906976152}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"wosuid\", \"external-id-value\": \"000320649400011\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.1098/rspb.2013.1007\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"source-work-id\", \"external-id-value\": \"da3b03ad-0f9b-48cd-a632-fe45d4aefe01\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-84878851824\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"work-summary\": [{\"put-code\": 11259185, \"created-date\": {\"value\": 1386966142407}, \"last-modified-date\": {\"value\": 1496531297507}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/0000-0002-3054-1567\", \"path\": \"0000-0002-3054-1567\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"Crossref Metadata Search\"}}, \"title\": {\"title\": {\"value\": \"Effects of allometry, productivity and lifestyle on rates and limits of body size evolution\"}, \"subtitle\": null, \"translated-title\": null}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"issn\", \"external-id-value\": \"0962-8452\", \"external-id-url\": null, \"external-id-relationship\": \"PART_OF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.1098/rspb.2013.1007\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"type\": \"JOURNAL_ARTICLE\", \"publication-date\": {\"year\": {\"value\": \"2013\"}, \"month\": null, \"day\": null, \"media-type\": null}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/work/11259185\", \"display-index\": \"0\"}, {\"put-code\": 29631422, \"created-date\": {\"value\": 1484897973553}, \"last-modified-date\": {\"value\": 1599906976152}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/APP-5E1VKQXON4GX3LS0\", \"path\": \"APP-5E1VKQXON4GX3LS0\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"University of Helsinki\"}}, \"title\": {\"title\": {\"value\": \"Effects of allometry, productivity and lifestyle on rates and limits of body size evolution\"}, \"subtitle\": null, \"translated-title\": null}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"source-work-id\", \"external-id-value\": \"da3b03ad-0f9b-48cd-a632-fe45d4aefe01\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"wosuid\", \"external-id-value\": \"000320649400011\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-84878851824\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.1098/rspb.2013.1007\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"type\": \"JOURNAL_ARTICLE\", \"publication-date\": {\"year\": {\"value\": \"2013\"}, \"month\": {\"value\": \"08\"}, \"day\": {\"value\": \"07\"}, \"media-type\": null}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/work/29631422\", \"display-index\": \"0\"}]}, {\"last-modified-date\": {\"value\": 1575719375521}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"source-work-id\", \"external-id-value\": \"328d8002-debb-4514-a1d8-8343ade3d4cb\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"wosuid\", \"external-id-value\": \"000301426700037\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.1073/pnas.1120774109\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-84863229913\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"work-summary\": [{\"put-code\": 11259186, \"created-date\": {\"value\": 1386966153783}, \"last-modified-date\": {\"value\": 1496531297507}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/0000-0002-3054-1567\", \"path\": \"0000-0002-3054-1567\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"Crossref Metadata Search\"}}, \"title\": {\"title\": {\"value\": \"The maximum rate of mammal evolution\"}, \"subtitle\": null, \"translated-title\": null}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"issn\", \"external-id-value\": \"0027-8424\", \"external-id-url\": null, \"external-id-relationship\": \"PART_OF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.1073/pnas.1120774109\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"type\": \"JOURNAL_ARTICLE\", \"publication-date\": {\"year\": {\"value\": \"2012\"}, \"month\": null, \"day\": null, \"media-type\": null}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/work/11259186\", \"display-index\": \"0\"}, {\"put-code\": 29631423, \"created-date\": {\"value\": 1484897973553}, \"last-modified-date\": {\"value\": 1575719375521}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/APP-5E1VKQXON4GX3LS0\", \"path\": \"APP-5E1VKQXON4GX3LS0\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"University of Helsinki\"}}, \"title\": {\"title\": {\"value\": \"The maximum rate of mammal evolution\"}, \"subtitle\": null, \"translated-title\": null}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"source-work-id\", \"external-id-value\": \"328d8002-debb-4514-a1d8-8343ade3d4cb\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"wosuid\", \"external-id-value\": \"000301426700037\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-84863229913\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.1073/pnas.1120774109\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"type\": \"JOURNAL_ARTICLE\", \"publication-date\": {\"year\": {\"value\": \"2012\"}, \"month\": null, \"day\": null, \"media-type\": null}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/work/29631423\", \"display-index\": \"0\"}]}, {\"last-modified-date\": {\"value\": 1575719375095}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-77949795277\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"source-work-id\", \"external-id-value\": \"68d70b54-ead9-4916-8c59-3c7fcaa3bfd4\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"wosuid\", \"external-id-value\": \"000277014500005\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"work-summary\": [{\"put-code\": 29631426, \"created-date\": {\"value\": 1484897973554}, \"last-modified-date\": {\"value\": 1575719375095}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/APP-5E1VKQXON4GX3LS0\", \"path\": \"APP-5E1VKQXON4GX3LS0\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"University of Helsinki\"}}, \"title\": {\"title\": {\"value\": \"Precipitation and large herbivorous mammals I\"}, \"subtitle\": null, \"translated-title\": null}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"source-work-id\", \"external-id-value\": \"68d70b54-ead9-4916-8c59-3c7fcaa3bfd4\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"wosuid\", \"external-id-value\": \"000277014500005\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-77949795277\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"type\": \"JOURNAL_ARTICLE\", \"publication-date\": {\"year\": {\"value\": \"2010\"}, \"month\": null, \"day\": null, \"media-type\": null}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/work/29631426\", \"display-index\": \"0\"}]}, {\"last-modified-date\": {\"value\": 1575719375313}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-77949818641\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"wosuid\", \"external-id-value\": \"000277014500006\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"source-work-id\", \"external-id-value\": \"8842ce4b-1a81-491b-807b-63ddbb1bc468\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"work-summary\": [{\"put-code\": 29631425, \"created-date\": {\"value\": 1484897973554}, \"last-modified-date\": {\"value\": 1575719375313}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/APP-5E1VKQXON4GX3LS0\", \"path\": \"APP-5E1VKQXON4GX3LS0\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"University of Helsinki\"}}, \"title\": {\"title\": {\"value\": \"Precipitation and large herbivorous mammals II\"}, \"subtitle\": null, \"translated-title\": null}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"source-work-id\", \"external-id-value\": \"8842ce4b-1a81-491b-807b-63ddbb1bc468\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"wosuid\", \"external-id-value\": \"000277014500006\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-77949818641\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"type\": \"JOURNAL_ARTICLE\", \"publication-date\": {\"year\": {\"value\": \"2010\"}, \"month\": null, \"day\": null, \"media-type\": null}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/work/29631425\", \"display-index\": \"0\"}]}, {\"last-modified-date\": {\"value\": 1575719374045}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"doi\", \"external-id-value\": \"10.1126/science.1194830\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"source-work-id\", \"external-id-value\": \"62ec4c31-10ce-425a-b9b5-ab87b36b3bf0\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"wosuid\", \"external-id-value\": \"000284613700034\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-78649433830\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"work-summary\": [{\"put-code\": 11259105, \"created-date\": {\"value\": 1386966096327}, \"last-modified-date\": {\"value\": 1496531297507}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/0000-0002-3054-1567\", \"path\": \"0000-0002-3054-1567\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"Crossref Metadata Search\"}}, \"title\": {\"title\": {\"value\": \"The Evolution of Maximum Body Size of Terrestrial Mammals\"}, \"subtitle\": null, \"translated-title\": null}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"issn\", \"external-id-value\": \"0036-8075\", \"external-id-url\": null, \"external-id-relationship\": \"PART_OF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.1126/science.1194830\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"type\": \"JOURNAL_ARTICLE\", \"publication-date\": {\"year\": {\"value\": \"2010\"}, \"month\": null, \"day\": null, \"media-type\": null}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/work/11259105\", \"display-index\": \"0\"}, {\"put-code\": 29631424, \"created-date\": {\"value\": 1484897973554}, \"last-modified-date\": {\"value\": 1575719374045}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/APP-5E1VKQXON4GX3LS0\", \"path\": \"APP-5E1VKQXON4GX3LS0\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"University of Helsinki\"}}, \"title\": {\"title\": {\"value\": \"The Evolution of Maximum Body Size of Terrestrial Mammals\"}, \"subtitle\": null, \"translated-title\": null}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"source-work-id\", \"external-id-value\": \"62ec4c31-10ce-425a-b9b5-ab87b36b3bf0\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"wosuid\", \"external-id-value\": \"000284613700034\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-78649433830\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.1126/science.1194830\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"type\": \"JOURNAL_ARTICLE\", \"publication-date\": {\"year\": {\"value\": \"2010\"}, \"month\": null, \"day\": null, \"media-type\": null}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/work/29631424\", \"display-index\": \"0\"}]}, {\"last-modified-date\": {\"value\": 1575719374883}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"doi\", \"external-id-value\": \"10.1086/595756\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"source-work-id\", \"external-id-value\": \"288a3564-2e08-49a0-a6c5-a39513943a61\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"wosuid\", \"external-id-value\": \"000262704600012\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-61849141203\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"work-summary\": [{\"put-code\": 11259100, \"created-date\": {\"value\": 1386966046824}, \"last-modified-date\": {\"value\": 1496531297507}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/0000-0002-3054-1567\", \"path\": \"0000-0002-3054-1567\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"Crossref Metadata Search\"}}, \"title\": {\"title\": {\"value\": \"Lower Extinction Risk in Sleep\\u2010or\\u2010Hide Mammals\"}, \"subtitle\": null, \"translated-title\": null}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"issn\", \"external-id-value\": \"0003-0147\", \"external-id-url\": null, \"external-id-relationship\": \"PART_OF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.1086/595756\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"type\": \"JOURNAL_ARTICLE\", \"publication-date\": {\"year\": {\"value\": \"2009\"}, \"month\": null, \"day\": null, \"media-type\": null}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/work/11259100\", \"display-index\": \"0\"}, {\"put-code\": 29631427, \"created-date\": {\"value\": 1484897973555}, \"last-modified-date\": {\"value\": 1575719374883}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/APP-5E1VKQXON4GX3LS0\", \"path\": \"APP-5E1VKQXON4GX3LS0\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"University of Helsinki\"}}, \"title\": {\"title\": {\"value\": \"Lower Extinction Risk in Sleep-or-Hide Mammals\"}, \"subtitle\": null, \"translated-title\": null}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"source-work-id\", \"external-id-value\": \"288a3564-2e08-49a0-a6c5-a39513943a61\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"wosuid\", \"external-id-value\": \"000262704600012\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-61849141203\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.1086/595756\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"type\": \"JOURNAL_ARTICLE\", \"publication-date\": {\"year\": {\"value\": \"2009\"}, \"month\": null, \"day\": null, \"media-type\": null}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/work/29631427\", \"display-index\": \"0\"}]}, {\"last-modified-date\": {\"value\": 1575719376371}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"source-work-id\", \"external-id-value\": \"440269c3-b4f6-463d-9395-329ff65e21ee\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-43149112064\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.1073/pnas.0709763105\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"wosuid\", \"external-id-value\": \"000255356000028\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"work-summary\": [{\"put-code\": 11259101, \"created-date\": {\"value\": 1386966059522}, \"last-modified-date\": {\"value\": 1496531297507}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/0000-0002-3054-1567\", \"path\": \"0000-0002-3054-1567\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"Crossref Metadata Search\"}}, \"title\": {\"title\": {\"value\": \"Higher origination and extinction rates in larger mammals\"}, \"subtitle\": null, \"translated-title\": null}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"issn\", \"external-id-value\": \"0027-8424\", \"external-id-url\": null, \"external-id-relationship\": \"PART_OF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.1073/pnas.0709763105\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"type\": \"JOURNAL_ARTICLE\", \"publication-date\": {\"year\": {\"value\": \"2008\"}, \"month\": null, \"day\": null, \"media-type\": null}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/work/11259101\", \"display-index\": \"0\"}, {\"put-code\": 29631429, \"created-date\": {\"value\": 1484897973555}, \"last-modified-date\": {\"value\": 1575719376371}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/APP-5E1VKQXON4GX3LS0\", \"path\": \"APP-5E1VKQXON4GX3LS0\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"University of Helsinki\"}}, \"title\": {\"title\": {\"value\": \"Higher origination and extinction rates  in larger mammals\"}, \"subtitle\": null, \"translated-title\": null}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"source-work-id\", \"external-id-value\": \"440269c3-b4f6-463d-9395-329ff65e21ee\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"wosuid\", \"external-id-value\": \"000255356000028\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-43149112064\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.1073/pnas.0709763105\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"type\": \"JOURNAL_ARTICLE\", \"publication-date\": {\"year\": {\"value\": \"2008\"}, \"month\": null, \"day\": null, \"media-type\": null}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/work/29631429\", \"display-index\": \"0\"}]}, {\"last-modified-date\": {\"value\": 1575719376805}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"wosuid\", \"external-id-value\": \"000259343000002\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"source-work-id\", \"external-id-value\": \"30f58623-4bc0-4426-ac10-aa97c142007e\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.1073/pnas.0806021105\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-51349142313\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"work-summary\": [{\"put-code\": 11259103, \"created-date\": {\"value\": 1386966074402}, \"last-modified-date\": {\"value\": 1496531297507}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/0000-0002-3054-1567\", \"path\": \"0000-0002-3054-1567\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"Crossref Metadata Search\"}}, \"title\": {\"title\": {\"value\": \"Reply to Vilar et al.: Sleep or hide, better for survival anytime\"}, \"subtitle\": null, \"translated-title\": null}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"issn\", \"external-id-value\": \"0027-8424\", \"external-id-url\": null, \"external-id-relationship\": \"PART_OF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.1073/pnas.0806021105\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"type\": \"JOURNAL_ARTICLE\", \"publication-date\": {\"year\": {\"value\": \"2008\"}, \"month\": null, \"day\": null, \"media-type\": null}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/work/11259103\", \"display-index\": \"0\"}, {\"put-code\": 29631428, \"created-date\": {\"value\": 1484897973555}, \"last-modified-date\": {\"value\": 1575719376805}, \"source\": {\"source-orcid\": null, \"source-client-id\": {\"uri\": \"https://orcid.org/client/APP-5E1VKQXON4GX3LS0\", \"path\": \"APP-5E1VKQXON4GX3LS0\", \"host\": \"orcid.org\"}, \"source-name\": {\"value\": \"University of Helsinki\"}}, \"title\": {\"title\": {\"value\": \"Reply to Vilar et al\"}, \"subtitle\": null, \"translated-title\": null}, \"external-ids\": {\"external-id\": [{\"external-id-type\": \"source-work-id\", \"external-id-value\": \"30f58623-4bc0-4426-ac10-aa97c142007e\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"wosuid\", \"external-id-value\": \"000259343000002\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"eid\", \"external-id-value\": \"2-s2.0-51349142313\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}, {\"external-id-type\": \"doi\", \"external-id-value\": \"10.1073/pnas.0806021105\", \"external-id-url\": null, \"external-id-relationship\": \"SELF\"}]}, \"type\": \"JOURNAL_ARTICLE\", \"publication-date\": {\"year\": {\"value\": \"2008\"}, \"month\": null, \"day\": null, \"media-type\": null}, \"visibility\": \"PUBLIC\", \"path\": \"/0000-0001-9627-8821/work/29631428\", \"display-index\": \"0\"}]}], \"path\": \"/0000-0001-9627-8821/works\"}, \"path\": \"/0000-0001-9627-8821/activities\"}, \"path\": \"/0000-0001-9627-8821\"}', 3);
INSERT INTO `socialaccount_socialaccount` (`id`, `provider`, `uid`, `last_login`, `date_joined`, `extra_data`, `user_id`) VALUES
(4, 'orcid', '0000-0002-5299-1729', '2022-02-19 17:16:00.894722', '2022-02-03 08:07:35.230704', '{\"orcid-identifier\": {\"uri\": \"https://orcid.org/0000-0002-5299-1729\", \"path\": \"0000-0002-5299-1729\", \"host\": \"orcid.org\"}, \"preferences\": {\"locale\": \"EN\"}, \"history\": {\"creation-method\": \"DIRECT\", \"completion-date\": null, \"submission-date\": {\"value\": 1643874057738}, \"last-modified-date\": {\"value\": 1645290960177}, \"claimed\": true, \"source\": null, \"deactivation-date\": null, \"verified-email\": true, \"verified-primary-email\": true}, \"person\": {\"last-modified-date\": null, \"name\": {\"created-date\": {\"value\": 1643874058006}, \"last-modified-date\": {\"value\": 1643874058006}, \"given-names\": {\"value\": \"Cecilia\"}, \"family-name\": null, \"credit-name\": null, \"source\": null, \"visibility\": \"PUBLIC\", \"path\": \"0000-0002-5299-1729\"}, \"other-names\": {\"last-modified-date\": null, \"other-name\": [], \"path\": \"/0000-0002-5299-1729/other-names\"}, \"biography\": null, \"researcher-urls\": {\"last-modified-date\": null, \"researcher-url\": [], \"path\": \"/0000-0002-5299-1729/researcher-urls\"}, \"emails\": {\"last-modified-date\": null, \"email\": [], \"path\": \"/0000-0002-5299-1729/email\"}, \"addresses\": {\"last-modified-date\": null, \"address\": [], \"path\": \"/0000-0002-5299-1729/address\"}, \"keywords\": {\"last-modified-date\": null, \"keyword\": [], \"path\": \"/0000-0002-5299-1729/keywords\"}, \"external-identifiers\": {\"last-modified-date\": null, \"external-identifier\": [], \"path\": \"/0000-0002-5299-1729/external-identifiers\"}, \"path\": \"/0000-0002-5299-1729/person\"}, \"activities-summary\": {\"last-modified-date\": null, \"educations\": {\"last-modified-date\": null, \"education-summary\": [], \"path\": \"/0000-0002-5299-1729/educations\"}, \"employments\": {\"last-modified-date\": null, \"employment-summary\": [], \"path\": \"/0000-0002-5299-1729/employments\"}, \"fundings\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0002-5299-1729/fundings\"}, \"peer-reviews\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0002-5299-1729/peer-reviews\"}, \"works\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0002-5299-1729/works\"}, \"path\": \"/0000-0002-5299-1729/activities\"}, \"path\": \"/0000-0002-5299-1729\"}', 4),
(5, 'orcid', '0000-0002-7939-4692', '2022-02-23 11:15:39.906229', '2022-02-03 08:47:49.224332', '{\"orcid-identifier\": {\"uri\": \"https://orcid.org/0000-0002-7939-4692\", \"path\": \"0000-0002-7939-4692\", \"host\": \"orcid.org\"}, \"preferences\": {\"locale\": \"EN\"}, \"history\": {\"creation-method\": \"MEMBER_REFERRED\", \"completion-date\": null, \"submission-date\": {\"value\": 1643877942122}, \"last-modified-date\": {\"value\": 1645614939320}, \"claimed\": true, \"source\": null, \"deactivation-date\": null, \"verified-email\": true, \"verified-primary-email\": true}, \"person\": {\"last-modified-date\": null, \"name\": {\"created-date\": {\"value\": 1643877942413}, \"last-modified-date\": {\"value\": 1643877942413}, \"given-names\": {\"value\": \"Juhana\"}, \"family-name\": {\"value\": \"Karhunen\"}, \"credit-name\": null, \"source\": null, \"visibility\": \"PUBLIC\", \"path\": \"0000-0002-7939-4692\"}, \"other-names\": {\"last-modified-date\": null, \"other-name\": [], \"path\": \"/0000-0002-7939-4692/other-names\"}, \"biography\": null, \"researcher-urls\": {\"last-modified-date\": null, \"researcher-url\": [], \"path\": \"/0000-0002-7939-4692/researcher-urls\"}, \"emails\": {\"last-modified-date\": null, \"email\": [], \"path\": \"/0000-0002-7939-4692/email\"}, \"addresses\": {\"last-modified-date\": null, \"address\": [], \"path\": \"/0000-0002-7939-4692/address\"}, \"keywords\": {\"last-modified-date\": null, \"keyword\": [], \"path\": \"/0000-0002-7939-4692/keywords\"}, \"external-identifiers\": {\"last-modified-date\": null, \"external-identifier\": [], \"path\": \"/0000-0002-7939-4692/external-identifiers\"}, \"path\": \"/0000-0002-7939-4692/person\"}, \"activities-summary\": {\"last-modified-date\": null, \"educations\": {\"last-modified-date\": null, \"education-summary\": [], \"path\": \"/0000-0002-7939-4692/educations\"}, \"employments\": {\"last-modified-date\": null, \"employment-summary\": [], \"path\": \"/0000-0002-7939-4692/employments\"}, \"fundings\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0002-7939-4692/fundings\"}, \"peer-reviews\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0002-7939-4692/peer-reviews\"}, \"works\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0002-7939-4692/works\"}, \"path\": \"/0000-0002-7939-4692/activities\"}, \"path\": \"/0000-0002-7939-4692\"}', 5),
(6, 'orcid', '0000-0001-7895-5809', '2022-02-03 10:05:21.295135', '2022-02-03 09:33:33.775404', '{\"orcid-identifier\": {\"uri\": \"https://orcid.org/0000-0001-7895-5809\", \"path\": \"0000-0001-7895-5809\", \"host\": \"orcid.org\"}, \"preferences\": {\"locale\": \"EN\"}, \"history\": {\"creation-method\": \"DIRECT\", \"completion-date\": null, \"submission-date\": {\"value\": 1643880586045}, \"last-modified-date\": {\"value\": 1643882720406}, \"claimed\": true, \"source\": null, \"deactivation-date\": null, \"verified-email\": true, \"verified-primary-email\": false}, \"person\": {\"last-modified-date\": null, \"name\": {\"created-date\": {\"value\": 1643880586562}, \"last-modified-date\": {\"value\": 1643880586562}, \"given-names\": {\"value\": \"Ari\"}, \"family-name\": {\"value\": \"Kauppi\"}, \"credit-name\": null, \"source\": null, \"visibility\": \"PUBLIC\", \"path\": \"0000-0001-7895-5809\"}, \"other-names\": {\"last-modified-date\": null, \"other-name\": [], \"path\": \"/0000-0001-7895-5809/other-names\"}, \"biography\": null, \"researcher-urls\": {\"last-modified-date\": null, \"researcher-url\": [], \"path\": \"/0000-0001-7895-5809/researcher-urls\"}, \"emails\": {\"last-modified-date\": null, \"email\": [], \"path\": \"/0000-0001-7895-5809/email\"}, \"addresses\": {\"last-modified-date\": null, \"address\": [], \"path\": \"/0000-0001-7895-5809/address\"}, \"keywords\": {\"last-modified-date\": null, \"keyword\": [], \"path\": \"/0000-0001-7895-5809/keywords\"}, \"external-identifiers\": {\"last-modified-date\": null, \"external-identifier\": [], \"path\": \"/0000-0001-7895-5809/external-identifiers\"}, \"path\": \"/0000-0001-7895-5809/person\"}, \"activities-summary\": {\"last-modified-date\": null, \"educations\": {\"last-modified-date\": null, \"education-summary\": [], \"path\": \"/0000-0001-7895-5809/educations\"}, \"employments\": {\"last-modified-date\": null, \"employment-summary\": [], \"path\": \"/0000-0001-7895-5809/employments\"}, \"fundings\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0001-7895-5809/fundings\"}, \"peer-reviews\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0001-7895-5809/peer-reviews\"}, \"works\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0001-7895-5809/works\"}, \"path\": \"/0000-0001-7895-5809/activities\"}, \"path\": \"/0000-0001-7895-5809\"}', 6),
(7, 'orcid', '0000-0003-3541-1144', '2022-02-21 07:59:19.390212', '2022-02-03 10:43:22.019760', '{\"orcid-identifier\": {\"uri\": \"https://orcid.org/0000-0003-3541-1144\", \"path\": \"0000-0003-3541-1144\", \"host\": \"orcid.org\"}, \"preferences\": {\"locale\": \"EN\"}, \"history\": {\"creation-method\": \"DIRECT\", \"completion-date\": null, \"submission-date\": {\"value\": 1643884894561}, \"last-modified-date\": {\"value\": 1645430358409}, \"claimed\": true, \"source\": null, \"deactivation-date\": null, \"verified-email\": true, \"verified-primary-email\": true}, \"person\": {\"last-modified-date\": null, \"name\": {\"created-date\": {\"value\": 1643884894856}, \"last-modified-date\": {\"value\": 1643884894856}, \"given-names\": {\"value\": \"Anne\"}, \"family-name\": null, \"credit-name\": null, \"source\": null, \"visibility\": \"PUBLIC\", \"path\": \"0000-0003-3541-1144\"}, \"other-names\": {\"last-modified-date\": null, \"other-name\": [], \"path\": \"/0000-0003-3541-1144/other-names\"}, \"biography\": null, \"researcher-urls\": {\"last-modified-date\": null, \"researcher-url\": [], \"path\": \"/0000-0003-3541-1144/researcher-urls\"}, \"emails\": {\"last-modified-date\": null, \"email\": [], \"path\": \"/0000-0003-3541-1144/email\"}, \"addresses\": {\"last-modified-date\": null, \"address\": [], \"path\": \"/0000-0003-3541-1144/address\"}, \"keywords\": {\"last-modified-date\": null, \"keyword\": [], \"path\": \"/0000-0003-3541-1144/keywords\"}, \"external-identifiers\": {\"last-modified-date\": null, \"external-identifier\": [], \"path\": \"/0000-0003-3541-1144/external-identifiers\"}, \"path\": \"/0000-0003-3541-1144/person\"}, \"activities-summary\": {\"last-modified-date\": null, \"educations\": {\"last-modified-date\": null, \"education-summary\": [], \"path\": \"/0000-0003-3541-1144/educations\"}, \"employments\": {\"last-modified-date\": null, \"employment-summary\": [], \"path\": \"/0000-0003-3541-1144/employments\"}, \"fundings\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0003-3541-1144/fundings\"}, \"peer-reviews\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0003-3541-1144/peer-reviews\"}, \"works\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0003-3541-1144/works\"}, \"path\": \"/0000-0003-3541-1144/activities\"}, \"path\": \"/0000-0003-3541-1144\"}', 7),
(13, 'orcid', '0000-0001-5683-9428', '2022-02-21 12:38:14.025564', '2022-02-21 12:37:21.139960', '{\"orcid-identifier\": {\"uri\": \"https://orcid.org/0000-0001-5683-9428\", \"path\": \"0000-0001-5683-9428\", \"host\": \"orcid.org\"}, \"preferences\": {\"locale\": \"EN\"}, \"history\": {\"creation-method\": \"MEMBER_REFERRED\", \"completion-date\": null, \"submission-date\": {\"value\": 1627025779173}, \"last-modified-date\": {\"value\": 1645447092965}, \"claimed\": true, \"source\": null, \"deactivation-date\": null, \"verified-email\": true, \"verified-primary-email\": true}, \"person\": {\"last-modified-date\": null, \"name\": {\"created-date\": {\"value\": 1627025779440}, \"last-modified-date\": {\"value\": 1627025779440}, \"given-names\": {\"value\": \"Jonne\"}, \"family-name\": {\"value\": \"Sotala\"}, \"credit-name\": null, \"source\": null, \"visibility\": \"PUBLIC\", \"path\": \"0000-0001-5683-9428\"}, \"other-names\": {\"last-modified-date\": null, \"other-name\": [], \"path\": \"/0000-0001-5683-9428/other-names\"}, \"biography\": null, \"researcher-urls\": {\"last-modified-date\": null, \"researcher-url\": [], \"path\": \"/0000-0001-5683-9428/researcher-urls\"}, \"emails\": {\"last-modified-date\": null, \"email\": [], \"path\": \"/0000-0001-5683-9428/email\"}, \"addresses\": {\"last-modified-date\": null, \"address\": [], \"path\": \"/0000-0001-5683-9428/address\"}, \"keywords\": {\"last-modified-date\": null, \"keyword\": [], \"path\": \"/0000-0001-5683-9428/keywords\"}, \"external-identifiers\": {\"last-modified-date\": null, \"external-identifier\": [], \"path\": \"/0000-0001-5683-9428/external-identifiers\"}, \"path\": \"/0000-0001-5683-9428/person\"}, \"activities-summary\": {\"last-modified-date\": null, \"educations\": {\"last-modified-date\": null, \"education-summary\": [], \"path\": \"/0000-0001-5683-9428/educations\"}, \"employments\": {\"last-modified-date\": null, \"employment-summary\": [], \"path\": \"/0000-0001-5683-9428/employments\"}, \"fundings\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0001-5683-9428/fundings\"}, \"peer-reviews\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0001-5683-9428/peer-reviews\"}, \"works\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0001-5683-9428/works\"}, \"path\": \"/0000-0001-5683-9428/activities\"}, \"path\": \"/0000-0001-5683-9428\"}', 13),
(18, 'orcid', '0000-0001-6032-2472', '2022-03-01 13:58:03.179411', '2022-03-01 13:00:21.734863', '{\"orcid-identifier\": {\"uri\": \"https://orcid.org/0000-0001-6032-2472\", \"path\": \"0000-0001-6032-2472\", \"host\": \"orcid.org\"}, \"preferences\": {\"locale\": \"EN\"}, \"history\": {\"creation-method\": \"DIRECT\", \"completion-date\": null, \"submission-date\": {\"value\": 1643886302720}, \"last-modified-date\": {\"value\": 1646143082553}, \"claimed\": true, \"source\": null, \"deactivation-date\": null, \"verified-email\": true, \"verified-primary-email\": true}, \"person\": {\"last-modified-date\": null, \"name\": {\"created-date\": {\"value\": 1643886303002}, \"last-modified-date\": {\"value\": 1643886303002}, \"given-names\": {\"value\": \"Tuomas\"}, \"family-name\": {\"value\": \"Testaaja\"}, \"credit-name\": null, \"source\": null, \"visibility\": \"PUBLIC\", \"path\": \"0000-0001-6032-2472\"}, \"other-names\": {\"last-modified-date\": null, \"other-name\": [], \"path\": \"/0000-0001-6032-2472/other-names\"}, \"biography\": null, \"researcher-urls\": {\"last-modified-date\": null, \"researcher-url\": [], \"path\": \"/0000-0001-6032-2472/researcher-urls\"}, \"emails\": {\"last-modified-date\": null, \"email\": [], \"path\": \"/0000-0001-6032-2472/email\"}, \"addresses\": {\"last-modified-date\": null, \"address\": [], \"path\": \"/0000-0001-6032-2472/address\"}, \"keywords\": {\"last-modified-date\": null, \"keyword\": [], \"path\": \"/0000-0001-6032-2472/keywords\"}, \"external-identifiers\": {\"last-modified-date\": null, \"external-identifier\": [], \"path\": \"/0000-0001-6032-2472/external-identifiers\"}, \"path\": \"/0000-0001-6032-2472/person\"}, \"activities-summary\": {\"last-modified-date\": null, \"educations\": {\"last-modified-date\": null, \"education-summary\": [], \"path\": \"/0000-0001-6032-2472/educations\"}, \"employments\": {\"last-modified-date\": null, \"employment-summary\": [], \"path\": \"/0000-0001-6032-2472/employments\"}, \"fundings\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0001-6032-2472/fundings\"}, \"peer-reviews\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0001-6032-2472/peer-reviews\"}, \"works\": {\"last-modified-date\": null, \"group\": [], \"path\": \"/0000-0001-6032-2472/works\"}, \"path\": \"/0000-0001-6032-2472/activities\"}, \"path\": \"/0000-0001-6032-2472\"}', 18);

-- --------------------------------------------------------

--
-- Rakenne taululle `socialaccount_socialapp`
--

CREATE TABLE `socialaccount_socialapp` (
  `id` int(11) NOT NULL,
  `provider` varchar(30) NOT NULL,
  `name` varchar(40) NOT NULL,
  `client_id` varchar(191) NOT NULL,
  `secret` varchar(191) NOT NULL,
  `key` varchar(191) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Rakenne taululle `socialaccount_socialapp_sites`
--

CREATE TABLE `socialaccount_socialapp_sites` (
  `id` bigint(20) NOT NULL,
  `socialapp_id` int(11) NOT NULL,
  `site_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Rakenne taululle `socialaccount_socialtoken`
--

CREATE TABLE `socialaccount_socialtoken` (
  `id` int(11) NOT NULL,
  `token` longtext NOT NULL,
  `token_secret` longtext NOT NULL,
  `expires_at` datetime(6) DEFAULT NULL,
  `account_id` int(11) NOT NULL,
  `app_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account_emailaddress`
--
ALTER TABLE `account_emailaddress`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `account_emailaddress_user_id_2c513194_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `account_emailconfirmation`
--
ALTER TABLE `account_emailconfirmation`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `key` (`key`),
  ADD KEY `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` (`email_address_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `django_site`
--
ALTER TABLE `django_site`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`);

--
-- Indexes for table `front_comment`
--
ALTER TABLE `front_comment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `front_expert`
--
ALTER TABLE `front_expert`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `front_expertsgeographicdiv`
--
ALTER TABLE `front_expertsgeographicdiv`
  ADD PRIMARY KEY (`id`),
  ADD KEY `front_expertsgeograp_geographic_tsn_id_9f249f3b_fk_front_geo` (`geographic_tsn_id`),
  ADD KEY `front_expertsgeograp_expert_id_id_e81903e2_fk_front_exp` (`expert_id_id`);

--
-- Indexes for table `front_geographicdiv`
--
ALTER TABLE `front_geographicdiv`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `tsn_id` (`tsn_id`),
  ADD UNIQUE KEY `front_geographicdiv_tsn_id_geographic_value_754bbf7a_uniq` (`tsn_id`,`geographic_value`);

--
-- Indexes for table `front_hierarchy`
--
ALTER TABLE `front_hierarchy`
  ADD PRIMARY KEY (`id`),
  ADD KEY `front_hierarchy_tsn_id_967745dd_fk_front_taxonomicunit_tsn` (`tsn_id`);

--
-- Indexes for table `front_historicalreference`
--
ALTER TABLE `front_historicalreference`
  ADD PRIMARY KEY (`history_id`),
  ADD KEY `front_historicalrefe_history_user_id_76133f5c_fk_auth_user` (`history_user_id`),
  ADD KEY `front_historicalreference_id_6b5d0926` (`id`);

--
-- Indexes for table `front_kingdom`
--
ALTER TABLE `front_kingdom`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `front_publication`
--
ALTER TABLE `front_publication`
  ADD PRIMARY KEY (`publication_id`),
  ADD UNIQUE KEY `pub_id_prefix` (`pub_id_prefix`),
  ADD UNIQUE KEY `front_publication_pub_id_prefix_publication_id_183f82e9_uniq` (`pub_id_prefix`,`publication_id`);

--
-- Indexes for table `front_reference`
--
ALTER TABLE `front_reference`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `front_referencelink`
--
ALTER TABLE `front_referencelink`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `front_referencelink_tsn_id_doc_id_prefix_doc_8c5226ec_uniq` (`tsn_id`,`doc_id_prefix`,`documentation_id_id`),
  ADD KEY `front_referencelink_documentation_id_id_4e4abd21_fk_front_pub` (`documentation_id_id`);

--
-- Indexes for table `front_synonymlink`
--
ALTER TABLE `front_synonymlink`
  ADD PRIMARY KEY (`id`),
  ADD KEY `front_synonymlink_tsn_accepted_id_d70def56_fk_front_tax` (`tsn_accepted_id`);

--
-- Indexes for table `front_taxonauthorlkp`
--
ALTER TABLE `front_taxonauthorlkp`
  ADD PRIMARY KEY (`taxon_author_id`),
  ADD UNIQUE KEY `front_taxonauthorlkp_taxon_author_id_kingdom_id_4c381ae5_uniq` (`taxon_author_id`,`kingdom_id`),
  ADD KEY `front_taxonauthorlkp_kingdom_id_0014563d_fk_front_kingdom_id` (`kingdom_id`);

--
-- Indexes for table `front_taxonomicunit`
--
ALTER TABLE `front_taxonomicunit`
  ADD PRIMARY KEY (`tsn`),
  ADD KEY `front_taxonomicunit_kingdom_id_b87f9a82_fk_front_kingdom_id` (`kingdom_id`),
  ADD KEY `front_taxonomicunit_taxon_author_id_id_e2ff7220_fk_front_tax` (`taxon_author_id_id`);

--
-- Indexes for table `front_taxonunittype`
--
ALTER TABLE `front_taxonunittype`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `front_taxonunittype_kingdom_id_rank_id_382d9759_uniq` (`kingdom_id`,`rank_id`);

--
-- Indexes for table `front_tucommentlink`
--
ALTER TABLE `front_tucommentlink`
  ADD PRIMARY KEY (`id`),
  ADD KEY `front_tucommentlink_comment_id_id_34cad991_fk_front_comment_id` (`comment_id_id`),
  ADD KEY `front_tucommentlink_tsn_id_918fe12c_fk_front_taxonomicunit_tsn` (`tsn_id`);

--
-- Indexes for table `refs_ref`
--
ALTER TABLE `refs_ref`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `socialaccount_socialaccount`
--
ALTER TABLE `socialaccount_socialaccount`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `socialaccount_socialaccount_provider_uid_fc810c6e_uniq` (`provider`,`uid`),
  ADD KEY `socialaccount_socialaccount_user_id_8146e70c_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `socialaccount_socialapp`
--
ALTER TABLE `socialaccount_socialapp`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `socialaccount_socialapp_sites`
--
ALTER TABLE `socialaccount_socialapp_sites`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `socialaccount_socialapp_sites_socialapp_id_site_id_71a9a768_uniq` (`socialapp_id`,`site_id`),
  ADD KEY `socialaccount_socialapp_sites_site_id_2579dee5_fk_django_site_id` (`site_id`);

--
-- Indexes for table `socialaccount_socialtoken`
--
ALTER TABLE `socialaccount_socialtoken`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq` (`app_id`,`account_id`),
  ADD KEY `socialaccount_social_account_id_951f210e_fk_socialacc` (`account_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account_emailaddress`
--
ALTER TABLE `account_emailaddress`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `account_emailconfirmation`
--
ALTER TABLE `account_emailconfirmation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=113;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=262;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `django_site`
--
ALTER TABLE `django_site`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `front_comment`
--
ALTER TABLE `front_comment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `front_expert`
--
ALTER TABLE `front_expert`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `front_expertsgeographicdiv`
--
ALTER TABLE `front_expertsgeographicdiv`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `front_geographicdiv`
--
ALTER TABLE `front_geographicdiv`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `front_hierarchy`
--
ALTER TABLE `front_hierarchy`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `front_historicalreference`
--
ALTER TABLE `front_historicalreference`
  MODIFY `history_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `front_kingdom`
--
ALTER TABLE `front_kingdom`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `front_reference`
--
ALTER TABLE `front_reference`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `front_referencelink`
--
ALTER TABLE `front_referencelink`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `front_synonymlink`
--
ALTER TABLE `front_synonymlink`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `front_taxonomicunit`
--
ALTER TABLE `front_taxonomicunit`
  MODIFY `tsn` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `front_taxonunittype`
--
ALTER TABLE `front_taxonunittype`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=181;

--
-- AUTO_INCREMENT for table `front_tucommentlink`
--
ALTER TABLE `front_tucommentlink`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `refs_ref`
--
ALTER TABLE `refs_ref`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `socialaccount_socialaccount`
--
ALTER TABLE `socialaccount_socialaccount`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `socialaccount_socialapp`
--
ALTER TABLE `socialaccount_socialapp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `socialaccount_socialapp_sites`
--
ALTER TABLE `socialaccount_socialapp_sites`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `socialaccount_socialtoken`
--
ALTER TABLE `socialaccount_socialtoken`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Rajoitteet vedostauluille
--

--
-- Rajoitteet taululle `account_emailaddress`
--
ALTER TABLE `account_emailaddress`
  ADD CONSTRAINT `account_emailaddress_user_id_2c513194_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Rajoitteet taululle `account_emailconfirmation`
--
ALTER TABLE `account_emailconfirmation`
  ADD CONSTRAINT `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` FOREIGN KEY (`email_address_id`) REFERENCES `account_emailaddress` (`id`);

--
-- Rajoitteet taululle `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Rajoitteet taululle `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Rajoitteet taululle `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Rajoitteet taululle `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Rajoitteet taululle `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Rajoitteet taululle `front_expertsgeographicdiv`
--
ALTER TABLE `front_expertsgeographicdiv`
  ADD CONSTRAINT `front_expertsgeograp_expert_id_id_e81903e2_fk_front_exp` FOREIGN KEY (`expert_id_id`) REFERENCES `front_expert` (`id`),
  ADD CONSTRAINT `front_expertsgeograp_geographic_tsn_id_9f249f3b_fk_front_geo` FOREIGN KEY (`geographic_tsn_id`) REFERENCES `front_geographicdiv` (`tsn_id`);

--
-- Rajoitteet taululle `front_geographicdiv`
--
ALTER TABLE `front_geographicdiv`
  ADD CONSTRAINT `front_geographicdiv_tsn_id_f41a8eef_fk_front_taxonomicunit_tsn` FOREIGN KEY (`tsn_id`) REFERENCES `front_taxonomicunit` (`tsn`);

--
-- Rajoitteet taululle `front_hierarchy`
--
ALTER TABLE `front_hierarchy`
  ADD CONSTRAINT `front_hierarchy_tsn_id_967745dd_fk_front_taxonomicunit_tsn` FOREIGN KEY (`tsn_id`) REFERENCES `front_taxonomicunit` (`tsn`);

--
-- Rajoitteet taululle `front_historicalreference`
--
ALTER TABLE `front_historicalreference`
  ADD CONSTRAINT `front_historicalrefe_history_user_id_76133f5c_fk_auth_user` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`);

--
-- Rajoitteet taululle `front_referencelink`
--
ALTER TABLE `front_referencelink`
  ADD CONSTRAINT `front_referencelink_documentation_id_id_4e4abd21_fk_front_pub` FOREIGN KEY (`documentation_id_id`) REFERENCES `front_publication` (`publication_id`),
  ADD CONSTRAINT `front_referencelink_tsn_id_e860f4df_fk_front_taxonomicunit_tsn` FOREIGN KEY (`tsn_id`) REFERENCES `front_taxonomicunit` (`tsn`);

--
-- Rajoitteet taululle `front_synonymlink`
--
ALTER TABLE `front_synonymlink`
  ADD CONSTRAINT `front_synonymlink_tsn_accepted_id_d70def56_fk_front_tax` FOREIGN KEY (`tsn_accepted_id`) REFERENCES `front_taxonomicunit` (`tsn`);

--
-- Rajoitteet taululle `front_taxonauthorlkp`
--
ALTER TABLE `front_taxonauthorlkp`
  ADD CONSTRAINT `front_taxonauthorlkp_kingdom_id_0014563d_fk_front_kingdom_id` FOREIGN KEY (`kingdom_id`) REFERENCES `front_kingdom` (`id`);

--
-- Rajoitteet taululle `front_taxonomicunit`
--
ALTER TABLE `front_taxonomicunit`
  ADD CONSTRAINT `front_taxonomicunit_kingdom_id_b87f9a82_fk_front_kingdom_id` FOREIGN KEY (`kingdom_id`) REFERENCES `front_kingdom` (`id`),
  ADD CONSTRAINT `front_taxonomicunit_taxon_author_id_id_e2ff7220_fk_front_tax` FOREIGN KEY (`taxon_author_id_id`) REFERENCES `front_taxonauthorlkp` (`taxon_author_id`);

--
-- Rajoitteet taululle `front_taxonunittype`
--
ALTER TABLE `front_taxonunittype`
  ADD CONSTRAINT `front_taxonunittype_kingdom_id_6c75ffcf_fk_front_kingdom_id` FOREIGN KEY (`kingdom_id`) REFERENCES `front_kingdom` (`id`);

--
-- Rajoitteet taululle `front_tucommentlink`
--
ALTER TABLE `front_tucommentlink`
  ADD CONSTRAINT `front_tucommentlink_comment_id_id_34cad991_fk_front_comment_id` FOREIGN KEY (`comment_id_id`) REFERENCES `front_comment` (`id`),
  ADD CONSTRAINT `front_tucommentlink_tsn_id_918fe12c_fk_front_taxonomicunit_tsn` FOREIGN KEY (`tsn_id`) REFERENCES `front_taxonomicunit` (`tsn`);

--
-- Rajoitteet taululle `socialaccount_socialaccount`
--
ALTER TABLE `socialaccount_socialaccount`
  ADD CONSTRAINT `socialaccount_socialaccount_user_id_8146e70c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Rajoitteet taululle `socialaccount_socialapp_sites`
--
ALTER TABLE `socialaccount_socialapp_sites`
  ADD CONSTRAINT `socialaccount_social_socialapp_id_97fb6e7d_fk_socialacc` FOREIGN KEY (`socialapp_id`) REFERENCES `socialaccount_socialapp` (`id`),
  ADD CONSTRAINT `socialaccount_socialapp_sites_site_id_2579dee5_fk_django_site_id` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`);

--
-- Rajoitteet taululle `socialaccount_socialtoken`
--
ALTER TABLE `socialaccount_socialtoken`
  ADD CONSTRAINT `socialaccount_social_account_id_951f210e_fk_socialacc` FOREIGN KEY (`account_id`) REFERENCES `socialaccount_socialaccount` (`id`),
  ADD CONSTRAINT `socialaccount_social_app_id_636a42d7_fk_socialacc` FOREIGN KEY (`app_id`) REFERENCES `socialaccount_socialapp` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
