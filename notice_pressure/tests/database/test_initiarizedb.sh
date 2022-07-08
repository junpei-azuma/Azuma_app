#!/bin/bash
###
# 開発用のデータベースとテーブルを作成します
###
service mysql start

# データベース作成
mysql --defaults-extra-file=/etc/mysql/my.cnf -u root  < /usr/local/my_app/tests/database/test_create_dev_db.sql

# テーブル作成
mysql --defaults-extra-file=/etc/mysql/my.cnf -u root  test_myapp < /usr/local/my_app/tests/database/test_create_tables.sql