import spacy
import numpy as np
import json
from sentence_transformers import SentenceTransformer

def get_dependencies():
    #using spacy for tokenization
    nlp = spacy.load("en_core_web_md")
    #using this for embeddings
    model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
    #english
    with open("product_tree.json", 'r', errors="ignore") as file:
        product_tree = json.load(file)
    #hinglish
    with open("hi_en_product_tree.json", 'r', errors="ignore") as hi_en_file:
        hi_en_product_tree = json.load(hi_en_file)
    #english labels
    all_labels = ["Smart Neckband,Device,Health,GPS,Sensors","Pharma,Medicine,Dawai","Vaccine,Injection,Immunity","Fodder,Bhusa,Nutrition,Hay,Straw","Feed,Nutrition,Food","Accessories,Collar,Harness,Tools,comfort","Valuation,Worth,Price,Buy,Sell","Apparels,clothing,fashion,warm,protection,traditional,dresses","Vet,care,checkup,treatment,emergency,health","Livestock,farm,productivity","Grooming,bath,haircut,nails","Tele Assistance,guide,support","Finance,payment,loan","Insurance,coverage,medical,expense","Government,Schemes,Initiative,welfare","E-guide,Digital,resource","Introduction,myanimal","Account,Create,Sign Up,Register,Verify","Password,Reset","Update,Profile,Edit","Delete,Account,Remove,Management","Adoption","Shopping,Delivery,Shipping","Refund,Return,Cod,Cash On Delively,Payment","Selling,Listing,Sellers,Vendor"]
    #hinglish labels
    hi_en_all_labels = ["smart neckband,device,health,gps,sensors,machine","pharma,medicine,dawai","vaccine,injection,immunity,tika,teeka,teekakaran,tikakaran,sui","fodder,bhusa,nutrition,hay,straw,chara,chaara,bhoosa","feed,nutrition,food,khaana,poshan","accessories,collar,harness,tools,comfort","valuation,worth,price,buy,sell,mooly,keemat,khareeden,bechen","apparels,clothing,fashion,warm,protection,traditional,dresses,vastr,kapde","vet,care,checkup,treatment,emergency,health,jaanch,upachaar,dekhabhaal","livestock,farm,productivity,khet","grooming,bath,haircut,nails,nahana,nakhun","tele assistance,guide,support,sahaayata","finance,payment,loan,bhugataan,vitt","insurance,coverage,medical,expense,beema,kavarej,chikitsa,vyay","government,schemes,initiative,welfare,sarakaar,yojana,kalyaan","e-guide,digital,resource","introduction,myanimal","account,create,sign up,register,verify","password,reset","update,profile,edit","delete,account,remove,management","adoption","shopping,delivery,shipping,kharidari,kharid","refund,return,cod,cash on delively,payment,vapasi,vapas","selling,listing,sellers,vendor,vikray,vikreta","order,place,track"]

    hi_en_label_embeddings = model.encode(hi_en_all_labels)
    label_embeddings = model.encode(all_labels)

    return {
        "nlp":nlp,
        "label_embeddings":label_embeddings,
        "all_labels":all_labels, 
        "product_tree":product_tree,
        "model":model,
        "hi_en_product_tree":hi_en_product_tree,
        "hi_en_all_labels":hi_en_all_labels,
        "hi_en_label_embeddings":hi_en_label_embeddings
        }

def other():
    return