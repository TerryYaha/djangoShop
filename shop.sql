create database hf200915 character set utf8 collate utf8_general_ci;
-- 使用数据库文件
use hf200915;

-- 后台管理人员信息表（1条）
create table admin_info (
	admin_id int primary key auto_increment, 
	admin_name varchar(200),
	admin_pwd varchar(200)
);
insert into admin_info(admin_id,admin_name,admin_pwd) values (null,'admin','123');

-- 用户信息表（1条）
create table user_info (
	user_id int primary key auto_increment,
	user_name varchar(200),
	user_pwd varchar(200),
	user_email varchar(200),
	user_tel varchar(200),
	user_addr varchar(200),
	user_money int,
    u_name varchar(200)
);
insert into user_info(user_id,user_name,user_pwd,user_email,user_tel,user_addr,user_money,u_name) values(null,'tyl','12345','788532@163.com','177324356752','江苏省无锡市',50,'陶云亮');

-- 商品信息表(goods_type:商品类型，goods_price：价格， goods_num：数量)（20条）
create table goods_info (
	goods_id int primary key auto_increment,
	goods_name varchar(200),
	goods_img varchar(200),
	type_id int, 
	type_name varchar(200),
	goods_price int,
	goods_num int,
    goods_salenum int
);
insert into goods_info(goods_id,goods_name,goods_img,type_id,type_name,goods_price,goods_num,goods_salenum) values(null,'联想(lenovo)小新Air15','leneovo1.jpg',1,'电脑',4799,200,212);
insert into goods_info(goods_id,goods_name,goods_img,type_id,type_name,goods_price,goods_num,goods_salenum) values(null,'Apple MacBook Air 13.3 新款八核M1芯片','macbook1.jpg',1,'电脑',7999,10,2222);
insert into goods_info(goods_id,goods_name,goods_img,type_id,type_name,goods_price,goods_num,goods_salenum) values(null,'Apple MacBook Pro 13.3','macbookpro.jpg',1,'电脑',11490,20,1890);
insert into goods_info(goods_id,goods_name,goods_img,type_id,type_name,goods_price,goods_num,goods_salenum) values(null,'惠普（HP）战66 四代 14英寸轻薄笔记本','hp.jpg',1,'电脑',6599,5,2322);
insert into goods_info(goods_id,goods_name,goods_img,type_id,type_name,goods_price,goods_num,goods_salenum) values(null,'戴尔DELL灵越5000 14英寸酷睿i5网课学','dell1.jpg',1,'电脑',3880,100,3000);
insert into goods_info(goods_id,goods_name,goods_img,type_id,type_name,goods_price,goods_num,goods_salenum) values(null,'悦宝莱（YUEBAOLAI）','yuebaolai.jpg',2,'护肤品',320,100,3121);
insert into goods_info(goods_id,goods_name,goods_img,type_id,type_name,goods_price,goods_num,goods_salenum) values(null,'完美日记 PERFECT DIARY','mianmo1.jpg',2,'护肤品',59,20,9999);
insert into goods_info(goods_id,goods_name,goods_img,type_id,type_name,goods_price,goods_num,goods_salenum) values(null,'凡士林(Vaseline)润唇膏','fsl.jpg',2,'护肤品',27.4,123,1000);
insert into goods_info(goods_id,goods_name,goods_img,type_id,type_name,goods_price,goods_num,goods_salenum) values(null,'LAN兰天然水感植物卸妆油','product1.png',2,'护肤品',99,30,24);
insert into goods_info(goods_id,goods_name,goods_img,type_id,type_name,goods_price,goods_num,goods_salenum) values(null,'得力(deli) 家用多功能五金工具箱手动工具套装','product2.jpg',3,'五金',116,80,666);
insert into goods_info(goods_id,goods_name,goods_img,type_id,type_name,goods_price,goods_num,goods_salenum) values(null,'鑫瑞SRUNV卫浴扳手','product3.jpg',3,'五金',27,80,4322);
insert into goods_info(goods_id,goods_name,goods_img,type_id,type_name,goods_price,goods_num,goods_salenum) values(null,'威克（vico）WK33519 5米精品钢卷尺','product4.jpg',3,'五金',9.9,100,213);
insert into goods_info(goods_id,goods_name,goods_img,type_id,type_name,goods_price,goods_num,goods_salenum) values(null,'沪豪万能断丝取出器4分6分水龙头','product5.jpg',3,'五金',9.9,100,1000);
insert into goods_info(goods_id,goods_name,goods_img,type_id,type_name,goods_price,goods_num,goods_salenum) values(null,'标康 BK-0744加厚不锈钢角码固定件支架','product6.jpg',3,'五金',25,12,2000);
insert into goods_info(goods_id,goods_name,goods_img,type_id,type_name,goods_price,goods_num,goods_salenum) values(null,'安诺威 修枝剪剪枝剪整枝剪','product7.jpg',3,'五金',30,40,9128);
insert into goods_info(goods_id,goods_name,goods_img,type_id,type_name,goods_price,goods_num,goods_salenum) values(null,'机械革命（MECHREVO）蛟龙P AMD 17.3','pro8.jpg',1,'电脑',6999,1000,1000);
insert into goods_info(goods_id,goods_name,goods_img,type_id,type_name,goods_price,goods_num,goods_salenum) values(null,'联想（Lenovo）拯救者R7000 2020款','pro9.jpg',1,'电脑',5678,100,2000);
insert into goods_info(goods_id,goods_name,goods_img,type_id,type_name,goods_price,goods_num,goods_salenum) values(null,'Apple Pencil (第二代)','pro10.jpg',1,'电脑',889,2000,1231);
insert into goods_info(goods_id,goods_name,goods_img,type_id,type_name,goods_price,goods_num,goods_salenum) values(null,'联想( Lenovo )M10 PLUS平板电脑','pro11.jpg',1,'电脑',2220,470,2201);
insert into goods_info(goods_id,goods_name,goods_img,type_id,type_name,goods_price,goods_num,goods_salenum) values(null,'小米笔记本电脑红米RedmiBook','pro10.jpg',1,'电脑',3200,40,3330);
insert into goods_info(goods_id,goods_name,goods_img,type_id,type_name,goods_price,goods_num,goods_salenum) values(null,'鑫瑞SRUNV卫浴扳手','product3.jpg',3,'五金',27,80,6004);
insert into goods_info(goods_id,goods_name,goods_img,type_id,type_name,goods_price,goods_num,goods_salenum) values(null,'威克（vico）WK33519 5米精品钢卷尺','product4.jpg',3,'五金',9.9,100,12);
insert into goods_info(goods_id,goods_name,goods_img,type_id,type_name,goods_price,goods_num,goods_salenum) values(null,'沪豪万能断丝取出器4分6分水龙头','product5.jpg',3,'五金',9.9,100,20);
insert into goods_info(goods_id,goods_name,goods_img,type_id,type_name,goods_price,goods_num,goods_salenum) values(null,'标康 BK-0744加厚不锈钢角码固定件支架','product6.jpg',3,'五金',25,12,100);


-- 商品类型表（？条）
create table type_info (
	type_id int primary key auto_increment, 
	type_name varchar(200)
);
insert into type_info(type_id,type_name) values(null,'电脑');
insert into type_info(type_id,type_name) values(null,'护肤品');
insert into type_info(type_id,type_name) values(null,'五金');

-- 购物车信息表
create table buy_car (
	buy_id int primary key auto_increment,
	user_id int,
	goods_id int,
	goods_name varchar(200),
	goods_img varchar(200),
	goods_price int,
	buy_ctime datetime,
	goods_num int
);

-- 订单信息表(order_state:订单状态：已取消，已支付，未支付)
create table order_info(
	order_id int primary key auto_increment,
	order_num varchar(200),
	order_ctime datetime,
	order_state varchar(200),
	user_id int,
	order_price int
);

-- 订单商品信息表
create table order_goods(
	order_goods_id int primary key auto_increment,
	order_num varchar(200),
	goods_id int,
	goods_name varchar(200),
	goods_price int,	
	goods_img varchar(200),
	goods_num int
);

