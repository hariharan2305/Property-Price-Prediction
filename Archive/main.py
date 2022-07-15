from fastapi import FastAPI

app = FastAPI()


@app.get("/item/{item_id}")
def read_item(item_id: int):
    return {"item": item_id, "value": "Hello World!"}

##-------------------------------------------------------------------------------------
## Order is important if a route has same name
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}

# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}

##------------------------------------------------------------------------------------


# from enum import Enum

# from fastapi import FastAPI


# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"


# app = FastAPI()


# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name == ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}

##-----------------------------------------------------------------------------------------


# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
#     return {"file_path": file_path}

##-----------------------------------------------------------------------------------------



    [[PropertyType,
    ClubHouse,
    School_University_in_Township,
    Hospital_in_TownShip,
    Mall_in_TownShip,
    Park_Jogging_track,
    Swimming_Pool,
    Gym,
    Property_Area_in_Sq_Ft,
    Price_in_lakhs,
    Price_by_sub_area,
    Amenities_score,
    Price_by_Amenities_score,
    Noun_Counts,
    Verb_Counts,
    Adjective_Counts,
    boasts_elegant,
    elegant_towers,
    every_day,
    great_community,
    mantra_gold,
    offering_bedroom,
    quality_specification,
    stories_offering,
    towers_stories,
    world_class]]