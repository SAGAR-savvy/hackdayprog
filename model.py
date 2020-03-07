from peewee import *

db=SqliteDatabase("Aptitude.db")


class User(Model):
    username=CharField()
    password=CharField()
    compcomplete=BooleanField(default=False)

    class Meta:
        database=db

class Marks(Model):
    user=ForeignKeyField(User,backref="Marks")
    l1mark=IntegerField()
    l2mark=IntegerField()
    l3mark=IntegerField()
    total=IntegerField()
    

    class Meta:
        database=db

class Level1(Model):
    l1que=TextField()
    l1ans=CharField()
    l1a=CharField()
    l1b=CharField()
    l1c=CharField()
    l1d=CharField()
    class Meta:
        databse=db

class Level2(Model):
    l2que=TextField()
    l2ans=CharField()
    l2a=CharField()
    l2b=CharField()
    l2c=CharField()
    l2d=CharField()
    class Meta:
        databse=db

class Level3(Model):
    l3que=TextField()
    l3ans=CharField()
    l3a=CharField()
    l3b=CharField()
    l3c=CharField()
    l3d=CharField()
    class Meta:
        databse=db

if __name__=="__main__":
    db.connect()
    db.create_tables([User,Marks,Questions])