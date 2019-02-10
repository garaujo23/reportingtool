CREATE view view1 as SELECT title, name from articles, authors WHERE articles.author = authors.id;
CREATE view view2 as SELECT count(path) as num, articles.title from log JOIN articles on CONCAT('/article/',articles.slug)=log.path GROUP by articles.title;
CREATE view view3 as SELECT TO_CHAR(time :: DATE, 'Mon dd, yyyy') as day, count(status) as total_log FROM log group by day;
CREATE view view4 as SELECT TO_CHAR(time :: DATE, 'Mon dd, yyyy') as day, count(status) as error_log FROM log WHERE status not like '200%' GROUP by day ORDER by day;
CREATE view view5 as SELECT view3.day, ROUND(error_log*1.0/total_log*100.0, 2) as error_percent from view3, view4 WHERE view3.day = view4.day;