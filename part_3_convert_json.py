import cc_dat_utils
import cc_classes
import json

#Part 3

#Load your custom JSON file
json_data = json.load(open('data/cc_level_pack.json'))
print(json_data)

#Convert JSON data to CCLevelPack
level_pack = cc_classes.CCLevelPack()
level1 = cc_classes.CCLevel()
level1.num_chips = 1
level1.level_number = 1
level1.time = 100
level1.title = "test level"
level_pack.add_level(level1)
#Save converted data to DAT file
cc_dat_utils.write_cc_level_pack_to_dat(level_pack,'data/jia_level_pack.dat')