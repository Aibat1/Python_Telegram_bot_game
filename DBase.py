import sqlite3

db = sqlite3.connect('DBases.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users(
	user_id INT PRIMARY KEY,
	nick INT,
	players INT
)""")

sql.execute("""CREATE TABLE IF NOT EXISTS person(
	user_id INT PRIMARY KEY,
	level INT,
	hp INT,
	max_hp INT,
	money INT,
	attack INT,
	magic_attack INT,
	xp INT,
	max_xp INT,
	armor INT,
	magic_armor INT,
	location_id INT
)""")

sql.execute("""CREATE TABLE IF NOT EXISTS mob(
	user_id INT PRIMARY KEY,
	mob_id INT,
	mob TEXT,
	hp_mob INT,
	max_hpMob INT,
	reg_level INT,
	phisik_attackMob INT,
	magic_attackMob INT,
	armor_mob INT,
	magic_armorMob INT
)""")

sql.execute("""CREATE TABLE IF NOT EXISTS location(
	user_id INT PRIMARY KEY,
	lock_x INT,
	lock_y INT,
	location_name TEXT
)""")

sql.execute("""CREATE TABLE IF NOT EXISTS items(
	user_id INT PRIMARY KEY,
	item_id INT,
	cost INT,
	cost_sale INT,
	item_type TEXT,
	item_hp INT,
	item_mana INT,
	item_attack INT,
	item_MagickAttack INT,
	item_armor INT,
	item_MagickArmor INT,
	reg_level INT
)""")

sql.execute("""CREATE TABLE IF NOT EXISTS developer_mod(
	user_id INT PRIMARY KEY,
	shop INT DEFAULT (0)
)""")