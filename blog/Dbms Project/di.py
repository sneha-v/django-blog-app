import mysql.connector as con

db = con.connect(
    host = "localhost",
    user = "root",
    password = "snehasindhu@3",
    database = "pro"
)
cur = db.cursor()
# name='MACHINELEARNING'
# name=(name,)
# cur.execute("CALL call_cid11(%s,@a)",name)
# # q=cur.fetchall()
# cur.execute("SELECT @a")
# a= cur.fetchall()
# print(a[0])
# cname = "PYTHON"
# sql1 = "select cid from course where cname = %s"
# val1 =(cname,)
# cur.execute(sql1,val1)
# cid = cur.fetchone()
# sql2 = "select quest,answer,options from test1 where cid=%s"
# val2 = (cid[0],)
# cur.execute(sql2,val2)
# qao = cur.fetchall()
# print(qao)
# DELIMITER $$
#
# CREATE PROCEDURE call_cid1(IN cnamee VARCHAR(100))
#     BEGIN
#  SELECT cid FROM course
#  WHERE cname = cnamee;
#     END$$
#
# DELIMITER ;
# CREATE PROCEDURE cid_call @cname varchar(100)
# AS
# # SELECT cid FROM course WHERE cname = @cname
# # GO;
# cur.callproc('cid_call',['MACHINELEARNING',])
# # CALL call_cid('MACHINELEARNING',@cid)
# # result = cur.stored_results()
# # print(result)
# for result in cur.stored_results():
#     print(result.fetchall())
# # print(re)
# # SELECT @cid;
# DELIMITER //
# CREATE PROCEDURE cid_call
# (
#    cname varchar(100)
# )
# BEGIN
#    SELECT cid FROM course WHERE cname = @cname
# END //
# DELIMITER;

# DELIMITER $$
# CREATE TRIGGER before_enroll_delete
#     after insert ON profile1
#     FOR EACH ROW
# BEGIN
#     delete from enroll where cid=new.cid and uid=new.uid;
# END;$$
# DELIMITER ;
cur.execute("select count(cid) from course")
q=cur.fetchall()
print(q)
