import os

def generate():
    
    os.mkdir(name) # Creates Main Folder
    
    data = os.path.join(name, "data")
    
    os.mkdir(data) # Creates Data folder
    
    os.mkdir(data + f"\\{namespace}") # Creates Namespace
    
    os.mkdir(data + "\\minecraft") # Creates Minecraft namespace
    
    with open(f'{name}\pack.mcmeta', 'w') as pack:
        pack.write('{\n    "pack": {\n        "pack_format": 15,\n        "description": "Generated by Python"\n    }\n}\n')
    
    mynamespace = data + f"\\{namespace}"
      
    os.mkdir(mynamespace + "\\functions")
    os.mkdir(mynamespace + "\\loot_tables")
    os.mkdir(mynamespace + "\\structures")
    os.mkdir(mynamespace + "\\worldgen")
    os.mkdir(mynamespace + "\\advancements")
    os.mkdir(mynamespace + "\\recipes")
    os.mkdir(mynamespace + "\\tags")
    os.mkdir(mynamespace + "\\predicates")
    os.mkdir(mynamespace + "\\dimension")
    os.mkdir(mynamespace + "\\dimension_type")
    
    os.mkdir(mynamespace + "\\worldgen\\noise_settings") # Startig Generation Of All Worldgen Sub-Folders
    os.mkdir(mynamespace + "\\worldgen\\biome")
    os.mkdir(mynamespace + "\\worldgen\\configured_carver")
    os.mkdir(mynamespace + "\\worldgen\\template_pool")
    os.mkdir(mynamespace + "\\worldgen\\structure")
    os.mkdir(mynamespace + "\\worldgen\\structure_set")
    os.mkdir(mynamespace + "\\worldgen\\processor_list")
    
    os.mkdir(mynamespace + "\\tags\\blocks") # Starting Generation Of All Tags Sub-Folders
    os.mkdir(mynamespace + "\\tags\\fluids")
    os.mkdir(mynamespace + "\\tags\\items")
    os.mkdir(mynamespace + "\\tags\\entity_types")
    os.mkdir(mynamespace + "\\tags\\game_events")
    os.mkdir(mynamespace + "\\tags\\worldgen")
    os.mkdir(mynamespace + "\\tags\\functions")
    os.mkdir(mynamespace + "\\tags\\loot_tables")
    os.mkdir(mynamespace + "\\tags\\structures")
    os.mkdir(mynamespace + "\\tags\\advancements")
    os.mkdir(mynamespace + "\\tags\\recipes")
    os.mkdir(mynamespace + "\\tags\\tags")
    os.mkdir(mynamespace + "\\tags\\predicates")
    os.mkdir(mynamespace + "\\tags\\dimension")
    
    os.mkdir(mynamespace + "\\tags\\worldgen\\noise_settings") # Starting Generation Of All Worldgen Sub-Folders In Tags
    os.mkdir(mynamespace + "\\tags\\worldgen\\biome")
    os.mkdir(mynamespace + "\\tags\\worldgen\\configured_carver")
    os.mkdir(mynamespace + "\\tags\\worldgen\\template_pool")
    os.mkdir(mynamespace + "\\tags\\worldgen\\structure")
    os.mkdir(mynamespace + "\\tags\\worldgen\\structure_set")
    os.mkdir(mynamespace + "\\tags\\worldgen\\processor_list")



name = input("Whats your datapack called? \n")
namespace = input("What is your namespace called? \n").lower()
go = input("Generate? Y/N \n")


if go == "y" or "Y":
    generate()
else:
    print("Generation Canceled.")
    