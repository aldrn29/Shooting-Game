from settings import *
import random, sys

###
# Class
###

class ObjectController:
    __player_id = set()
    __player_object = dict()
    __player_missile_ids = set()
    __player_missile_objects = dict()

    __enemy_ids = set()
    __enemy_objects = dict()
    __enemy_missile_ids = set()
    __enemy_missile_objects = dict()

    __effect_ids = set()
    __effect_objects = dict()

    @classmethod
    def reset(cls):
        __player_id = set()
        __player_object = dict()
        __player_missile_ids = set()
        __player_missile_objects = dict()

        __enemy_ids = set()
        __enemy_objects = dict()
        __enemy_missile_ids = set()
        __enemy_missile_objects = dict()

        __effect_ids = set()
        __effect_objects = dict()        

    @classmethod
    def getPlayerObjects(cls):
        return cls.__player_object, cls.__player_missile_objects

    @classmethod
    def getEnemyObjects(cls):
        return cls.__enemy_objects, cls.__enemy_missile_objects

    @classmethod
    def getEffectObjects(cls):
        return cls.__effect_objects

    @classmethod
    def __init_effect_objects(cls):
        cls.__effect_ids = set()
        cls.__effect_objects = dict()

    ###
    # when an object is created, the object must be enrolled.
    ###
    @classmethod
    def enroll(cls, my_object):
        if my_object.team == 'enemy':
            if my_object.role == 'missile':
                object_id = cls.__issueID(cls.__enemy_missile_ids)
                cls.__enemy_missile_objects[object_id] = my_object
            elif my_object.role == 'fighter-plane' :
                object_id = cls.__issueID(cls.__enemy_ids)
                cls.__enemy_objects[object_id] = my_object

        elif my_object.team == 'player':
            if my_object.role == 'missile':
                object_id = cls.__issueID(cls.__player_missile_ids)
                cls.__player_missile_objects[object_id] = my_object
            elif my_object.role == 'fighter-plane' :
                object_id = cls.__issueID(cls.__player_id)
                cls.__player_object[object_id] = my_object

        elif my_object.team == 'none' :
            if my_object.role == 'effect':
                object_id = cls.__issueID(cls.__effect_ids)
                cls.__effect_objects[object_id] = my_object

        return object_id


    @classmethod
    def __issueID(cls, id_set):
        while True :
            new_id = random.randrange(sys.maxsize)
            if new_id in id_set: continue
            else :
                id_set.add(new_id)
                return new_id																						


    @classmethod
    def __remove_objects(cls, object1_ids, objects1, object2_ids=None, objects2=None, criterion='screen-out'):
        if criterion == 'screen-out' :
            while True : 
                flag = True
                for object1_id in object1_ids:
                    object1 = objects1[object1_id]

                    x, y = object1.obj_coord
                    if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT :
                        flag = False
                        break
                if flag == False :
                    object1_ids.remove(object1_id)
                    del objects1[object1_id]
                else : break

        elif criterion == 'iou' :
            while True :
                flag = True
                for object1_id in object1_ids :
                    object1 = objects1[object1_id]
                    object1_coord = object1.image_coord
                    for object2_id in object2_ids:
                        object2 = objects2[object2_id]
                        object2_coord = object2.image_coord
                        iou = max(0, min(object1_coord[2], object2_coord[2])- max(object1_coord[0], object2_coord[0]))*max(0, min(object1_coord[3], object2_coord[3])-max(object1_coord[1], object2_coord[1]))

                        if iou > 0 : 
                            flag = False
                            break
                    if flag == False :
                        if object1.role == 'fighter-plane' and object2.role == 'missile' :
                            object1._be_attacked(object2)
                            if object1.hp <= 0 : 
                                object1_ids.remove(object1_id)
                                del objects1[object1_id]
                                if object1.team == 'enemy' and object2.team == 'player':
                                    player_id = list(cls.__player_id)[0]
                                    cls.__player_object[player_id]._add_kill_point()

                            object2_ids.remove(object2_id)
                            del objects2[object2_id]
                        elif object1.role == 'missile' and object2.role == 'missile' :
                            object1_ids.remove(object1_id)
                            object2_ids.remove(object2_id)
                            del objects1[object1_id]
                            del objects2[object2_id]
                        break
                if flag : break

    ###
    # when objects moved, the objects must be renewed.
    ###
    @classmethod
    def renew(cls):
        cls.__init_effect_objects()

        ###
        # Enemy shoots
        ###
        for enemy_id in cls.__enemy_ids:
            enemy_object = cls.__enemy_objects[enemy_id]
            enemy_object.shoot()

        ###
        # All objects move
        ###
        for player_missile_id in cls.__player_missile_ids:
            player_missile_object = cls.__player_missile_objects[player_missile_id]
            player_missile_object.move()

        for enemy_id in cls.__enemy_ids:
            enemy_object = cls.__enemy_objects[enemy_id]
            enemy_object.move()

        for enemy_missile_id in cls.__enemy_missile_ids:
            enemy_missile_object = cls.__enemy_missile_objects[enemy_missile_id]
            enemy_missile_object.move()        

        cls.__remove_objects(cls.__player_missile_ids, cls.__player_missile_objects)
        cls.__remove_objects(cls.__enemy_ids, cls.__enemy_objects)
        cls.__remove_objects(cls.__enemy_missile_ids, cls.__enemy_missile_objects)

        ###
        # Renew code
        # 1. When the player's airplane is attacked by enemy's missiles
        # 2. When player's missiles crashed by enemy's missiles
        # 3. When enemies are attacked by player's missile
        ###
        cls.__remove_objects(cls.__player_id, cls.__player_object, cls.__enemy_missile_ids, cls.__enemy_missile_objects, 'iou')                       
        cls.__remove_objects(cls.__player_missile_ids, cls.__player_missile_objects, cls.__enemy_missile_ids, cls.__enemy_missile_objects, 'iou')
        cls.__remove_objects(cls.__enemy_ids, cls.__enemy_objects, cls.__player_missile_ids, cls.__player_missile_objects, 'iou')

