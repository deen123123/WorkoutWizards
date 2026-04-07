from fastapi import APIRouter

router = APIRouter (perfix="/api/meals", tags=["meals"])

meals = [
 #BREAKFAST 
{
    "id": 1,
    "type": "breakfast",
    "name": "Protein Pancakes",
    "image": "https://images.unsplash.com/photo-1587731556938-38755b4803a6",
    "ingredients": [
        "1 scoop whey protein",
        "1/2 cup oats",
        "1 banana",
        "2 egg whites",
        "Greek yogurt",
        "cinnamon"
    ],
    "instructions": "Blend all ingredients, cook on pan like pancakes, top with berries.",
    "prep_time": "10 mins",
    "protein": 40, "carbs": 55, "fat": 12, "calories": 450
},
{
    "id": 2,
    "type": "breakfast",
    "name": "Egg & Avocado Toast",
    "image": "https://images.unsplash.com/photo-1603048297172-c92544798d5a",
    "ingredients": ["eggs", "avocado", "toast"],
    "instructions": "Toast bread, fry eggs, add avocado on top.",
    "prep_time": "10 mins",
    "protein": 25, "carbs": 30, "fat": 20, "calories": 400
},
{
    "id": 3,
    "type": "breakfast",
    "name": "Oatmeal Power Bowl",
    "image": "https://images.unsplash.com/photo-1517673400267-0251440c45dc",
    "ingredients": ["oats", "milk", "banana", "peanut butter"],
    "instructions": "Cook oats, mix toppings.",
    "prep_time": "5 mins",
    "protein": 20, "carbs": 60, "fat": 10, "calories": 420
},
{
    "id": 4,
    "type": "breakfast",
    "name": "Greek Yogurt Parfait",
    "image": "https://images.unsplash.com/photo-1488477181946-6428a0291777",
    "ingredients": ["yogurt", "granola", "berries"],
    "instructions": "Layer all ingredients.",
    "prep_time": "3 mins",
    "protein": 30, "carbs": 40, "fat": 8, "calories": 350
},
{
    "id": 5,
    "type": "breakfast",
    "name": "Protein Smoothie",
    "image": "https://images.unsplash.com/photo-1553530666-ba11a7da3888",
    "ingredients": ["protein powder", "milk", "banana"],
    "instructions": "Blend everything.",
    "prep_time": "2 mins",
    "protein": 35, "carbs": 45, "fat": 10, "calories": 400
},
{
    "id": 6,
    "type": "breakfast",
    "name": "Scrambled Eggs & Toast",
    "image": "https://images.unsplash.com/photo-1551782450-17144efb9c50",
    "ingredients": ["eggs", "toast", "butter"],
    "instructions": "Scramble eggs and toast bread.",
    "prep_time": "7 mins",
    "protein": 20, "carbs": 25, "fat": 15, "calories": 350
},
{
    "id": 7,
    "type": "breakfast",
    "name": "Peanut Butter Banana Toast",
    "image": "https://images.unsplash.com/photo-1603048297172-c92544798d5a",
    "ingredients": ["toast", "peanut butter", "banana"],
    "instructions": "Spread PB and add banana slices.",
    "prep_time": "5 mins",
    "protein": 15, "carbs": 40, "fat": 12, "calories": 350
},
{
    "id": 8,
    "type": "breakfast",
    "name": "Breakfast Burrito",
    "image": "https://images.unsplash.com/photo-1552332386-f8dd00dc2f85",
    "ingredients": ["tortilla", "eggs", "chicken", "cheese"],
    "instructions": "Cook filling and wrap in tortilla.",
    "prep_time": "15 mins",
    "protein": 35, "carbs": 50, "fat": 18, "calories": 550
},

 # LUNCH 
{
    "id": 9,
    "type": "lunch",
    "name": "Chicken Rice Bowl",
    "image": "https://images.unsplash.com/photo-1604908176997-431dfecf3c3c",
    "ingredients": ["chicken", "rice", "broccoli"],
    "instructions": "Grill chicken, cook rice, steam broccoli.",
    "prep_time": "20 mins",
    "protein": 50, "carbs": 60, "fat": 15, "calories": 600
},
{
    "id": 10,
    "type": "lunch",
    "name": "Turkey Wrap",
    "image": "https://images.unsplash.com/photo-1552332386-f8dd00dc2f85",
    "ingredients": ["wrap", "turkey", "veggies"],
    "instructions": "Assemble wrap.",
    "prep_time": "5 mins",
    "protein": 40, "carbs": 50, "fat": 12, "calories": 520
},
{
    "id": 11,
    "type": "lunch",
    "name": "Salmon Quinoa Bowl",
    "image": "https://images.unsplash.com/photo-1546069901-eacef0df6022",
    "ingredients": ["salmon", "quinoa", "greens"],
    "instructions": "Cook salmon and quinoa, combine.",
    "prep_time": "25 mins",
    "protein": 45, "carbs": 55, "fat": 18, "calories": 650
},
{
    "id": 12,
    "type": "lunch",
    "name": "Beef Burrito Bowl",
    "image": "https://images.unsplash.com/photo-1550547660-d9450f859349",
    "ingredients": ["beef", "rice", "beans"],
    "instructions": "Cook beef, assemble bowl.",
    "prep_time": "20 mins",
    "protein": 50, "carbs": 65, "fat": 20, "calories": 700
},
{
    "id": 13,
    "type": "lunch",
    "name": "Grilled Chicken Salad",
    "image": "https://images.unsplash.com/photo-1568605114967-8130f3a36994",
    "ingredients": ["chicken", "lettuce", "tomato"],
    "instructions": "Grill chicken and mix salad.",
    "prep_time": "15 mins",
    "protein": 35, "carbs": 20, "fat": 12, "calories": 400
},
{
    "id": 14,
    "type": "lunch",
    "name": "Pasta Chicken Alfredo",
    "image": "https://images.unsplash.com/photo-1604908177522-040d7c6f7d6b",
    "ingredients": ["pasta", "chicken", "cream"],
    "instructions": "Cook pasta, add sauce and chicken.",
    "prep_time": "20 mins",
    "protein": 45, "carbs": 70, "fat": 22, "calories": 750
},
{
    "id": 15,
    "type": "lunch",
    "name": "Tuna Sandwich",
    "image": "https://images.unsplash.com/photo-1553621042-f6e147245754",
    "ingredients": ["tuna", "bread", "mayo"],
    "instructions": "Mix tuna and assemble sandwich.",
    "prep_time": "5 mins",
    "protein": 35, "carbs": 40, "fat": 10, "calories": 450
},
{
    "id": 16,
    "type": "lunch",
    "name": "Chicken Stir Fry",
    "image": "https://images.unsplash.com/photo-1604909052749-df0c6b4b5483",
    "ingredients": ["chicken", "veggies", "soy sauce"],
    "instructions": "Stir fry all ingredients.",
    "prep_time": "15 mins",
    "protein": 40, "carbs": 45, "fat": 12, "calories": 500
},


 # DINNER 
{
    "id": 17,
    "type": "dinner",
    "name": "Steak & Sweet Potato",
    "image": "https://images.unsplash.com/photo-1551183053-bf91a1d81141",
    "ingredients": ["steak", "sweet potato"],
    "instructions": "Grill steak, bake potato.",
    "prep_time": "40 mins",
    "protein": 55, "carbs": 70, "fat": 20, "calories": 700
},
{
    "id": 18,
    "type": "dinner",
    "name": "Grilled Salmon Plate",
    "image": "https://images.unsplash.com/photo-1467003909585-2f8a72700288",
    "ingredients": ["salmon", "vegetables"],
    "instructions": "Grill salmon and serve.",
    "prep_time": "20 mins",
    "protein": 50, "carbs": 40, "fat": 18, "calories": 600
},
{
    "id": 19,
    "type": "dinner",
    "name": "Shrimp Stir Fry",
    "image": "https://images.unsplash.com/photo-1604909052749-df0c6b4b5483",
    "ingredients": ["shrimp", "veggies"],
    "instructions": "Cook shrimp and veggies.",
    "prep_time": "15 mins",
    "protein": 40, "carbs": 50, "fat": 12, "calories": 500
},
{
    "id": 20,
    "type": "dinner",
    "name": "Beef & Veggies",
    "image": "https://images.unsplash.com/photo-1604908812255-9b9cbb18ce19",
    "ingredients": ["beef", "vegetables"],
    "instructions": "Cook beef with veggies.",
    "prep_time": "20 mins",
    "protein": 50, "carbs": 30, "fat": 18, "calories": 550
},

#  SNACKS 
{
    "id": 21,
    "type": "snack",
    "name": "Greek Yogurt Bowl",
    "image": "https://images.unsplash.com/photo-1488477181946-6428a0291777",
    "ingredients": ["yogurt", "nuts"],
    "instructions": "Mix together.",
    "prep_time": "2 mins",
    "protein": 30, "carbs": 20, "fat": 10, "calories": 350
},
{
    "id": 22,
    "type": "snack",
    "name": "Protein Shake",
    "image": "https://images.unsplash.com/photo-1572449043416-55f4685c9bb7",
    "ingredients": ["protein powder", "milk"],
    "instructions": "Blend.",
    "prep_time": "1 min",
    "protein": 35, "carbs": 25, "fat": 12, "calories": 400
},
{
    "id": 23,
    "type": "snack",
    "name": "Tuna Salad",
    "image": "https://images.unsplash.com/photo-1553621042-f6e147245754",
    "ingredients": ["tuna", "veggies"],
    "instructions": "Mix ingredients.",
    "prep_time": "5 mins",
    "protein": 40, "carbs": 10, "fat": 8, "calories": 300
},
{
    "id": 24,
    "type": "snack",
    "name": "Cottage Cheese & Fruit",
    "image": "https://images.unsplash.com/photo-1560807707-8cc77767d783",
    "ingredients": ["cottage cheese", "apple"],
    "instructions": "Serve together.",
    "prep_time": "2 mins",
    "protein": 28, "carbs": 30, "fat": 5, "calories": 280
},
{
    "id": 25,
    "type": "snack",
    "name": "Peanut Butter Apple",
    "image": "https://images.unsplash.com/photo-1574226516831-e1dff420e43e",
    "ingredients": ["apple", "peanut butter"],
    "instructions": "Slice apple and dip.",
    "prep_time": "3 mins",
    "protein": 15, "carbs": 35, "fat": 12, "calories": 300
},
{
    "id": 26,
    "type": "snack",
    "name": "Boiled Eggs",
    "image": "https://images.unsplash.com/photo-1604908176997-egg",
    "ingredients": ["eggs"],
    "instructions": "Boil eggs.",
    "prep_time": "10 mins",
    "protein": 12, "carbs": 1, "fat": 10, "calories": 150
}
]

@router.get("/")
def get_all_meals():
 return meals

@router.get("/{meal_type}")
def get_by_type(meal_type: str):
 return [m for m in meals if m["type"] == meal_type]
