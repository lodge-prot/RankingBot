---- drop ----
DROP TABLE IF EXISTS `qiita`;

---- create ----
create table IF not exists `qiita`
(
 `id`               INT(20) AUTO_INCREMENT,
 `title`            VARCHAR(64) NOT NULL,
 `url`              VARCHAR(255) NOT NULL,
 `fav`              INT(15) NOT NULL,
 `created_at`       Datetime DEFAULT NULL,
 `updated_at`       Datetime DEFAULT NULL,
    PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

---- drop ----
DROP TABLE IF EXISTS `test_tqable`;

---- create ----
create table IF not exists `test_table`
(
 `id`               INT(20) AUTO_INCREMENT,
 `name`             VARCHAR(20) NOT NULL,
 `created_at`       Datetime DEFAULT NULL,
 `updated_at`       Datetime DEFAULT NULL,
    PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
