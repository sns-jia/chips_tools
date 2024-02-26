import cc_dat_utils
import cc_classes
import json

#Part 3

#Load your custom JSON file
def load_json_data(json_file):
    with open(json_file,'r') as file:
        json_data = json.load(file)
    return json_data

#Create the monster movement field
def create_monster_movement_field(monsters_data):
    monsters = [cc_classes.CCCoordinate(monster['x'],monster['y']) for monster in monsters_data]
    monster_movement_field = cc_classes.CCMonsterMovementField(monsters)
    return monster_movement_field

#Convert JSON data to CCLevelPack
def json_to_cc_level_pack(json_data):
    level_pack = cc_classes.CCLevelPack()
    #loop to add json information into level_data
    for level_data in json_data["levels"]:
        level = cc_classes.CCLevel()
        level.level_number = level_data["level_number"]
        level.time = level_data["time"]
        level.num_chips = level_data["num_chips"]
        level.upper_layer = level_data["upper_layer"]
        level.lower_layer = level_data["lower_layer"]
        level.add_field(cc_classes.CCEncodedPasswordField(level_data["password"]))
        level.add_field(cc_classes.CCMapTitleField(level_data["title"]))
        level.add_field(cc_classes.CCMapHintField(level_data["hint"]))

        '''
        for field_data in level_data["optional_fields"]:
            if field_data["field_type"] == "field1":
                field = cc_classes.CCMapTitleField(field_data["level One"])
            elif field_data["field_type"] == "field2":
                field = cc_classes.CCMapTitleField(field_data["level Two"])
            elif field_data["field_type"] == "field3":
                field = cc_classes.CCMapTitleField(field_data["level Three"])
            elif field_data["field_type"] == "monsters":
                field = cc_classes.CCMapTitleField(field_data["monsters"])
            level.add_field(field)
        '''
        level_pack.add_level(level)
    return level_pack

parsed_json = load_json_data("data/cc_level_pack.json")
my_pack = json_to_cc_level_pack(parsed_json)

#Save converted data to DAT file
cc_dat_utils.write_cc_level_pack_to_dat(my_pack,'D:/TWorld/sets/jia_level_pack.dat')