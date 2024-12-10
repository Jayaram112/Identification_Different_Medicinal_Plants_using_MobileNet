from flask import Flask, request, render_template, send_from_directory,flash
import os
import numpy as np
import tensorflow as tf
from keras.preprocessing import image
from keras.models import load_model


app=Flask(__name__)
app.secret_key='random string'


pathlis=os.listdir(r'C:\Users\bjaya\Desktop\App\data')
classess=[]
for i in pathlis:
    classess.append(i)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory('images',filename)

@app.route("/upload", methods=["POST","GET"])
def upload():
    print('a')
    if request.method=='POST':
        myfile = request.files['file']
        print("sdgfsdgfdf")
        fn = myfile.filename
        mypath = os.path.join('images/', fn)
        myfile.save(mypath)

        print("{} is the file name", fn)
        print("Accept incoming file:", fn)
        print("Save it to:", mypath)
        
        new_model = load_model(r'C:\Users\bjaya\Desktop\App\Backend\Updated_MobileNet.keras')
        test_image = image.load_img(mypath, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = test_image / 255.0
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = new_model.predict(test_image)

        prediction = classess[np.argmax(result)]
        if prediction=='Arive-Dantu':
            msg=["Scientific Name: ","Sauropus androgynus", "Меdicinal Use:", "arive dantu possesses anti-inflammatory properties, making it potentially useful in managing inflammatory conditions. Additionally, its antioxidant activity may help protect cells from oxidative stress, reducing the risk of chronic diseases. Furthermore, this plant exhibits antimicrobial effects, which could aid in combating bacterial and fungal infections. Traditionally, it has been employed for wound healing due to its believed antimicrobial and anti-inflammatory properties, while also being utilized to promote digestive health, potentially due to its mild laxative properties.", "Simple Remedy: ", "Start by washing a handful of fresh arive dantu leaves thoroughly. Then, blend the leaves with a small amount of water until smooth. Strain the mixture to remove any solids, and if desired, add a touch of honey for sweetness.", "Availability:"," It is commonly found in states such as Rajasthan, Gujarat, Maharashtra, and Madhya Pradesh.", "For More Visit : ", "https://www.easyayurveda.com/2019/12/06/amaranth/"]
        elif prediction=='Basale':
            msg=["Scientific Name:","Basella alba","Medicinal Use:","Firstly, they aid in digestion, relieving constipation and improving bowel movements due to their mild laxative properties. Additionally, Basale leaves are packed with essential vitamins and minerals, supporting overall health and well-being. Their anti-inflammatory properties make them beneficial for managing conditions like arthritis, while their antioxidant content helps protect cells from damage, reducing the risk of chronic diseases. Moreover, Basale leaves can be used externally to soothe skin irritations or minor wounds, thanks to their anti-inflammatory and antimicrobial properties.", "Simple Remedy:","To create a soothing paste, start by gathering a handful of fresh Basale leaves and crushing them until you achieve a smooth consistency. Apply this paste directly onto the affected area of the skin, ensuring it covers the irritated area completely. Allow the paste to sit for approximately 15-20 minutes before rinsing it off with lukewarm water.","Availability:","Basale is widely available in India, commonly available include Karnataka, Kerala, Tamil Nadu, Andhra Pradesh, Maharashtra, and Goa.", "For More Visit : ", "https://www.easyayurveda.com/2019/12/05/malabar-spinach/"]           
        elif prediction=='Betel':
            msg=["Scientific Name:","Piper betle","Medicinal Use:","Betel leaves find applications in traditional medicine systems like Ayurveda and traditional Chinese medicine, where they are utilized to alleviate digestive issues, respiratory ailments, and skin conditions. Topically, betel leaves are employed for wound healing and to soothe insect bites. Culturally, betel is integral to religious and ceremonial practices, often symbolizing hospitality and goodwill, and featuring prominently in rituals and festivals. Beyond these uses, betel leaves lend their distinct peppery flavor to culinary creations in South Asian cuisines, while also being explored for potential aromatherapeutic benefits, thanks to their calming fragrance.","Simple Remedy:","Take a fresh betel leaf and wash it thoroughly. Then, chew the betel leaf for a few minutes, making sure to move it around your mouth. After chewing, you can either spit out the leaf or swallow it, depending on your preference.","Availability:"," Betel is commonly available in regions across India, especially in the states of West Bengal, Assam, and Tamil Nadu, where it is often used in religious and cultural practices.", "For More Visit:", "https://www.easyayurveda.com/2019/05/23/betel-benefits-uses-side-effects-dose-research/"]
        elif prediction=='Crape_Jasmine':
            msg=['Scientific Name:','Tabernaemontana divaricata',"Medicinal Use:","The plant's bark and leaves are commonly employed to reduce fever, with decoctions or infusions prepared from these parts of the plant believed to possess antipyretic effects. Additionally, crape jasmine is utilized as a natural remedy for pain relief, particularly for conditions like rheumatism and arthritis. Its bark, when used topically, may alleviate discomfort and inflammation associated with these ailments. Furthermore, crape jasmine is applied externally to the skin to soothe irritations, insect bites, and minor wounds, owing to its anti-inflammatory and antimicrobial properties.","Simple Remedy:","Crush a few fresh crape jasmine leaves to extract their juice. Apply this juice directly to the affected area of the skin, such as rashes, insect bites, or minor. Leave the juice on for about 15-20 minutes before rinsing it off with lukewarm water. Repeat as needed until the skin condition improves.","Availability:"," Crape Jasmine is commonly found in various regions of India, especially in states like Kerala, Tamil Nadu, and Karnataka, where it is grown for ornamental purposes and used in traditional medicine.","For More Visit:","https://www.easyayurveda.com/2016/11/30/jati-jasminum-grandiflorum-sambac-jasminum-officinale/"]
        elif prediction=='Curry':
            msg=['Scientific Name:',' Murraya koenigii',"Medicinal Use:","Rich in antioxidants, curry leaves are believed to aid in reducing oxidative stress and inflammation in the body, potentially lowering the risk of chronic diseases. Additionally, they are used in traditional herbal medicine to help manage various health conditions. For example, curry leaves are known for their potential to improve digestive health by promoting enzyme activity and reducing gastrointestinal discomfort. They are also believed to have anti-diabetic properties, helping to regulate blood sugar levels. Furthermore, curry leaves are used topically in some traditional practices to promote hair health and stimulate hair growth, thanks to their nutrient-rich composition.","Simple Remedy:","Take a handful of fresh curry leaves and wash them thoroughly. Next, chew the washed curry leaves directly. Chewing a few curry leaves daily, preferably in the morning on an empty stomach, may help alleviate digestive issues such as bloating, indigestion, and constipation.","Availability:","Curry leaves are widely available in India, particularly in regions with a tropical climate, such as Kerala, Karnataka, and Tamil Nadu, where they are used in cooking and traditional medicine.","For More Visit:","https://www.easyayurveda.com/2022/12/26/curry-leaves/"]
        elif prediction=='Drumstick':
            msg=['Scientific Name:','Moringa oleifera',"Medicinal Use:","Rich in antioxidants, vitamins, and minerals, drumstick is known to boost the immune system, enhance overall health, and prevent various diseases. Its anti-inflammatory properties make it effective in reducing inflammation and relieving pain associated with conditions like arthritis. Additionally, drumstick is valued for its ability to regulate blood sugar levels, making it beneficial for individuals with diabetes. Its high fiber content aids in digestion, alleviating digestive issues such as constipation and bloating. Moreover, drumstick leaves and pods are used to promote healthy skin and hair due to their abundance of nutrients.","Simple Remedy:","Take a handful of fresh drumstick leaves and wash them thoroughly. Next, boil the washed leaves in water for about 5-10 minutes to make a decoction. Strain the decoction and allow it to cool slightly. Drink this drumstick leaf decoction once daily, preferably in the morning on an empty stomach.","Availability:","Drumstick is widely available in India, especially in states like Tamil Nadu, Andhra Pradesh, and Karnataka, where it is grown for its culinary and medicinal uses.","For More Visit: ","https://www.easyayurveda.com/2012/12/06/moringa-benefits-medicinal-usage-complete-ayurveda-details/"]
        elif prediction=='Fenugreek':
            msg=['Scientific Name:','Trigonella foenum-graecum',"Medicinal Use:","Rich in antioxidants, fenugreek seeds are known to help reduce oxidative stress in the body, potentially lowering the risk of chronic diseases. Additionally, fenugreek is valued for its potential to regulate blood sugar levels, making it beneficial for individuals with diabetes. Its high fiber content aids in digestion, alleviating digestive issues such as constipation and indigestion. Fenugreek is also believed to have anti-inflammatory properties, which may help reduce inflammation and relieve pain associated with conditions like arthritis. Moreover, fenugreek seeds and leaves are used to support lactation in breastfeeding mothers, as they are believed to help increase milk production.","Simple Remedy:","Take a handful of fresh fenugreek leaves and wash them thoroughly. Next, chop the washed leaves finely. Then, heat a teaspoon of ghee (clarified butter) or oil in a pan and add the chopped fenugreek leaves to it. Sauté the leaves for a few minutes until they become tender. Season with a pinch of salt and a dash of turmeric powder for added flavor and digestive benefits","Availability:","Fenugreek is widely available in India, especially in states like Rajasthan, Gujarat, and Uttar Pradesh, where it is grown for culinary and medicinal purposes.","For More Vist:","https://www.easyayurveda.com/2015/12/14/fenugreek-methi-uses-research/"]
        elif prediction=='Guava':
            msg=['Scientific Name:','Psidium guajava',"Medicinal Use:","Rich in antioxidants, including flavonoids and polyphenols, guava leaves help combat oxidative stress and inflammation in the body, contributing to overall health and well-being. They are also known for their antimicrobial properties, making them effective in fighting off bacterial and fungal infections. Additionally, guava leaves are believed to aid in regulating blood sugar levels, making them beneficial for individuals with diabetes. Furthermore, guava leaf tea is often consumed to alleviate digestive issues such as diarrhea, constipation, and indigestion. Its high content of tannins and other bioactive compounds helps soothe the gastrointestinal tract and promote digestive health.","Simple Remedy:","Take a handful of fresh guava leaves and wash them thoroughly. Next, boil the washed leaves in water for about 10-15 minutes to make a decoction. Strain the decoction and allow it to cool slightly.","Availability:","Guava is widely available in India, particularly in states like Uttar Pradesh, Maharashtra, and Bihar, where it is grown for its leaves and medicinal uses.","For More Visit:","https://www.easyayurveda.com/2017/10/05/kumbhi-tree-careya-abrorea-ceylon-oak/"]
        elif prediction=='Hibiscus':
            msg=['Scientific Name:','Hibiscus sabdariffa',"Medicinal Use:","Rich in antioxidants such as flavonoids and anthocyanins, hibiscus helps combat oxidative stress and inflammation in the body, contributing to overall health and well-being. Its potential to lower blood pressure has garnered significant attention, with hibiscus tea often recommended as a natural remedy for hypertension. Additionally, hibiscus is believed to support cardiovascular health by reducing cholesterol levels and improving lipid profiles. Furthermore, hibiscus tea is known for its diuretic properties, aiding in detoxification and promoting kidney health. Its high vitamin C content makes it beneficial for boosting immunity and fighting off infections.","Simple Remedy:","Prepare hibiscus tea by steeping dried hibiscus flowers in hot water for 5-10 minutes. Strain the tea and allow it to cool slightly. Drink a cup of hibiscus tea daily, preferably in the morning or evening.","Availability:","Hibiscus is widely available in tropical and subtropical regions, including India, Africa, and Southeast Asia. It is commonly grown in home gardens.", "For More Visit:","https://www.easyayurveda.com/2018/01/12/hibiscus-flower-leaves-uses/"]
        elif prediction=='Indian_Beech':
            msg=['Scientific Name:','Pongamia pinnata',"Medicinal Use:","Rich in bioactive compounds such as flavonoids, alkaloids, and terpenoids, Indian beech exhibits diverse pharmacological activities. One of its primary uses is as a natural remedy for skin conditions, including eczema, psoriasis, and dermatitis. The oil extracted from Indian beech seeds is valued for its anti-inflammatory, antimicrobial, and wound-healing properties, making it an effective treatment for various skin ailments. Additionally, Indian beech oil is used topically to alleviate joint pain and inflammation associated with conditions like arthritis and rheumatism.","Simple Remedy:","Clean the affected area of the skin thoroughly. Take a few drops of Indian beech oil and apply it directly to the irritated or wounded skin. Gently massage the oil into the skin until it is absorbed.","Availability:","Indian Beech is commonly found in various regions of India, especially in states like Kerala, Karnataka, and Tamil Nadu.","For More Visit:","https://www.easyayurveda.com/2012/12/21/karanja-pongamia-pinnata-benefits-usage-ayurveda-details/"]
        elif prediction=='Indian_Mustard':
            msg=['Scientific Name:','Brassica juncea',"Medicinal Use:","Rich in bioactive compounds such as glucosinolates, phenolic compounds, and essential fatty acids, Indian mustard exhibits diverse pharmacological activities. One of its primary uses is as a natural remedy for respiratory conditions, including coughs, colds, and bronchitis. The seeds and leaves of Indian mustard are valued for their expectorant properties, which help loosen mucus and facilitate easier breathing. Additionally, Indian mustard is used topically as a poultice to alleviate joint pain and inflammation associated with conditions like arthritis and rheumatism. Its anti-inflammatory and analgesic properties offer relief from pain and improve joint mobility.","Simple Remedy:","Grind a tablespoon of Indian mustard seeds into a fine powder. Mix the powdered seeds with a teaspoon of honey to form a paste. Consume this paste once daily, preferably in the morning on an empty stomach.","Availability:","Indian Beech is commonly found in various regions of India, especially in states like Kerala, Karnataka, and Tamil Nadu.","For More Visit:","https://www.easyayurveda.com/2015/03/19/mustard-benefits-types-side-effects-research/"]
        elif prediction=='Jackfruit':
            msg=['Scientific Name:','Artocarpus heterophyllus',"Medicinal Use:","Rich in phytochemicals such as flavonoids, polyphenols, and saponins, jackfruit leaves exhibit diverse pharmacological activities. One of their primary uses is as a natural remedy for diabetes management. Extracts from jackfruit leaves have shown potential in lowering blood sugar levels, improving insulin sensitivity, and reducing the risk of diabetic complications. Additionally, jackfruit leaves are valued for their anti-inflammatory properties, making them effective in relieving pain and inflammation associated with conditions like arthritis and rheumatism. Moreover, the leaves possess antimicrobial and antifungal properties, which can help combat infections and promote wound healing.","Simple Remedy:","Take a handful of fresh jackfruit leaves and wash them thoroughly. Next, boil the washed leaves in water for about 10-15 minutes to make a decoction. Strain the decoction and allow it to cool slightly. Drink this jackfruit leaf decoction once daily, preferably after meals.","Availability:","Jackfruit is widely available in India, especially in states like Kerala, Karnataka, and Tamil Nadu.","For More Visit:","https://www.easyayurveda.com/2017/05/24/jackfruit-uses/"]
        elif prediction=='Jamaica_Cherry-Gasagase':
            msg=['Scientific Name:','Muntingia calabura',"Medicinal Use:","These leaves are commonly utilized in traditional herbal medicine for their potential digestive properties, aiding in digestion and relieving gastrointestinal discomfort such as bloating and indigestion. Additionally, gasagase leaves may possess anti-inflammatory effects, which could help reduce inflammation and alleviate pain associated with conditions like arthritis. Their antioxidant properties are also noteworthy, potentially contributing to overall health by neutralizing harmful free radicals in the body. Moreover, some traditional practices suggest the use of gasagase leaves externally for wound healing,","Simple Remedy:","Start by washing a handful of fresh gasagase leaves thoroughly. Next, boil these leaves in water for approximately 10-15 minutes to create a decoction. Once boiled, strain the liquid and allow it to cool slightly. Consume this gasagase leaf decoction once daily, ideally after meals.","Availability:","Kashmir Valley contributes to 95 per cent of the total cherry production in India. Eight cherry varieties grown in Kashmir include makhmali, siya, mishri, jaddi, Italy, dabal, vishkan and stela.","For More Visit:","https://www.flowersofindia.net/catalog/slides/Jamaica%20Cherry.html"]
        elif prediction=='Jamun':
            msg=['Scientific Name:','Syzygium cumini',"Medicinal Use:","One of the primary uses of jamun leaves is in managing diabetes. The leaves contain compounds like anthocyanins, ellagic acid, and corosolic acid, which are believed to help regulate blood sugar levels by increasing insulin sensitivity and stimulating insulin secretion. Jamun leaf extracts or decoctions are often consumed regularly by individuals with diabetes to help manage their condition effectively. Additionally, jamun leaves possess antioxidant properties, which help neutralize harmful free radicals in the body, reducing oxidative stress and lowering the risk of chronic diseases. They are also known for their antimicrobial and anti-inflammatory effects, making them beneficial for boosting immunity and fighting infections.","Simple Remedy:","Take a handful of fresh jamun leaves, wash them thoroughly, and crush them to extract their juice or grind them to make a paste. Consume 1-2 teaspoons of jamun leaf juice or paste on an empty stomach every morning. Repeat this remedy daily for effective diabetes management.","Availability:","Jamun trees are native to India and are commonly found throughout the country, especially in states like Maharashtra, Karnataka, and Tamil Nadu.","For More Visit:","https://www.easyayurveda.com/2013/01/29/jamun-benefits-usage-dose-side-effects-complete-ayurveda-details/"]
        elif prediction=='Jasmine':
            msg=['Scientific Name:','Jasminum',"Medicinal Use:","Jasmine, known for its calming and soothing properties, has been used in traditional medicine for various purposes. It is often used to relieve stress, anxiety, and improve sleep quality. Additionally, jasmine has been historically used for liver disease, such as hepatitis, as well as for pain associated with liver scarring (cirrhosis) and abdominal pain due to severe diarrhea (dysentery).","Simple Remedy:","One simple remedy is jasmine tea, which can help relieve stress, anxiety, and improve sleep quality. To make jasmine tea, boil water and pour it over a few fresh jasmine flowers or a jasmine tea bag in a cup. Let it steep for 3-5 minutes, then remove the flowers or tea bag.","Availability:","Jasmine is widely available in India, especially in states like Tamil Nadu, Karnataka, and Kerala.","For More Visit:","https://www.webmd.com/vitamins/ai/ingredientmono-617/jasmine"]
        elif prediction=='Karanda':
            msg=['Scientific Name:','Carissa carandas',"Medicinal Use:","Rich in bioactive compounds such as alkaloids, flavonoids, and tannins, karanda leaves offer several medicinal properties. One of their primary uses is their potential to alleviate digestive issues. Karanda leaf extracts or decoctions are often consumed to relieve symptoms of indigestion, bloating, and gastrointestinal discomfort. Additionally, karanda leaves are believed to possess antimicrobial properties, which may help combat infections and promote wound healing when applied topically. Furthermore, the leaves are used in some traditional practices to support respiratory health, offering relief from coughs, colds, and respiratory congestion.","Simple Remedy:","Take a handful of fresh karanda leaves, wash them thoroughly, and boil them in water for 10-15 minutes to make a decoction. Strain the decoction and allow it to cool slightly. Drink this karanda leaf decoction once daily, preferably after meals.","Availability:","Karanda is commonly found in regions across India, especially in states like Maharashtra, Gujarat, and Rajasthan.","For More Visit:","https://www.easyayurveda.com/2016/12/13/karonda-carissa-carandas-karamarda/"]
        elif prediction=='Lemon':
            msg=['Scientific Name:','Citrus limon',"Medicinal Use:","Rich in bioactive compounds like citronellol, limonene, and flavonoids, lemon leaves are renowned for their diverse therapeutic benefits. One of their primary uses is their potential to promote digestive health. Lemon leaf tea or decoctions are commonly consumed to alleviate symptoms of indigestion, bloating, and gastrointestinal discomfort. Additionally, lemon leaves are believed to possess antimicrobial and anti-inflammatory properties, which may help combat infections and reduce inflammation when applied topically.","Simple Remedy:","Take a handful of fresh lemon leaves, wash them thoroughly, and boil them in water for 10-15 minutes to make a decoction. Strain the decoction and allow it to cool slightly before drinking. Consuming this lemon leaf decoction once daily, preferably after meals.", "Availability:","Lemon leaves are widely available in India, especially in regions where lemon trees are grown, such as Maharashtra, Andhra Pradesh, and Tamil Nadu.","For More Visit:","https://www.easyayurveda.com/2012/11/14/health-benefits-of-lemon-ayurveda-details/"]
        elif prediction=='Mango':
            msg=['Scientific Name:','Mangifera indica',"Medicinal Use:","Rich in bioactive compounds such as flavonoids, phenols, and triterpenoids, mango leaves exhibit diverse pharmacological activities. One of their primary uses is their potential to regulate blood sugar levels. Mango leaf extracts or decoctions are often consumed to help manage diabetes by improving insulin sensitivity and reducing blood glucose levels. Additionally, mango leaves possess antioxidant properties, which help neutralize free radicals and reduce oxidative stress in the body, contributing to overall health and well-being.","Simple Remedy:","Take a handful of fresh mango leaves and wash them thoroughly. Then, boil the washed leaves in water for about 10-15 minutes to make a decoction. Once boiled, strain the decoction and allow it to cool slightly. Consume this mango leaf decoction once daily, preferably in the morning on an empty stomach.", "Availability:","The major mango-growing states are Andhra Pradesh, Uttar Pradesh, Karnataka, Bihar, Gujarat and Telangana.","For More Visit:","https://www.easyayurveda.com/2015/08/20/mango-uses/"]  
        elif prediction=='Mexican_Mint':
            msg=['Scientific Name:','Tagetes lucida',"Medicinal Use:","Rich in essential oils, flavonoids, and phenolic compounds, Mexican mint leaves exhibit several pharmacological activities. One of their primary uses is for respiratory health. Mexican mint leaves are believed to have expectorant properties, helping to alleviate coughs, colds, and respiratory congestion. Additionally, they possess antimicrobial and anti-inflammatory properties, making them effective in combating infections and reducing inflammation in the body. Moreover, Mexican mint leaves are used to relieve gastrointestinal issues such as indigestion, bloating, and stomachaches.","Simple Remedy:","Take a handful of fresh Mexican mint leaves and wash them thoroughly. Boil the washed leaves in water for about 10-15 minutes to make a decoction. Strain the decoction and allow it to cool slightly. Drink this Mexican mint leaf decoction once daily, preferably after meals.", "Availability:","Major producing States are Andhra Pradesh, Bihar, Gujarat, Karnataka, Maharashtra, Orissa, Tamil Nadu, Uttar Pradesh and West Bengal.", "For More Visit: ","https://www.easyayurveda.com/2017/03/27/country-borage-parnayavani/"]
        elif prediction=='Mint':
            msg=['Scientific Name:','Mentha',"Medicinal Use:","Rich in essential oils, flavonoids, and phenolic compounds mint leaves exhibit several pharmacological activities. One of their primary uses is for respiratory health. mint leaves are believed to have expectorant properties, helping to alleviate coughs, colds, and respiratory congestion. Additionally, they possess antimicrobial and anti-inflammatory properties, making them effective in combating infections and reducing inflammation in the body. Moreover mint leaves are used to relieve gastrointestinal issues such as indigestion, bloating, and stomachaches.","Simple Remedy:","Take a handful of fresh  mint leaves and wash them thoroughly. Boil the washed leaves in water for about 10-15 minutes to make a decoction. Strain the decoction and allow it to cool slightly. Drink this mint leaf decoction once daily, preferably after meals.","Availability:","Mint are widely available in India, particularly in regions with a temperate climate, such as Himachal Pradesh, Jammu and Kashmir, and parts of Uttarakhand.","For More Visit:","https://www.easyayurveda.com/2017/09/03/indian-mint-plectranthus-amboinicus-remedies/"]
        elif prediction=='Neem':
            msg=['Scientific Name:','Azadirachta indica',"Medicinal Use:","Rich in bioactive compounds such as azadirachtin, nimbin, and quercetin, neem leaves exhibit potent antimicrobial, anti-inflammatory, and antioxidant effects. One of their primary uses is for skin health. Neem leaves are widely used to treat various skin conditions, including acne, eczema, and psoriasis, due to their antibacterial and antifungal properties. Additionally, neem leaves are believed to promote wound healing and alleviate skin irritation when applied topically. Moreover, neem leaves are used to support oral health, as they possess antibacterial properties that can help prevent dental cavities and gum disease.","Simple Remedy:","Take a handful of fresh neem leaves and wash them thoroughly. Boil the washed leaves in water for about 10-15 minutes to make a decoction. Strain the decoction and allow it to cool slightly. Apply the neem leaf decoction topically to the affected area of the skin using a clean cotton ball or pad. Leave it on for about 15-20 minutes, then rinse it off with lukewarm water.", "Availability:","Neem is widely available in India, especially in regions with a tropical climate, such as Kerala, Tamil Nadu, and Karnataka.","For More Visit:","https://www.easyayurveda.com/2012/11/28/neem-in-ayurveda-benefits-usage-side-effects-full-reference/"]    
        elif prediction=='Oleander':
            msg=['Scientific Name:','Nerium oleander',"Medicinal Use:","In Ayurveda, it's mentioned in various ancient texts as a remedy for skin ailments. According to Ayurvedic principles, Karvira is considered poisonous but is used externally to treat chronic skin conditions like leprosy. It's also recommended for infected wounds, skin diseases, itching, and microbial infections. Overall, Karvira is valued for its potential to alleviate serious skin issues, as described in ancient Ayurvedic texts.","Simple Remedy:","One simple remedy is to use lavender essential oil for relaxation and stress relief. You can add a few drops of lavender oil to a diffuser or dilute it with a carrier oil and apply it to your skin for a calming effect.", "Availability:","Oleander is native to a wide range of regions, including parts of Asia, Africa, and the Mediterranean. It is cultivated as an ornamental plant in many areas in india.","For More visit:","https://www.easyayurveda.com/2017/05/01/yellow-oleander-remedies/#:~:text=According%20to%20Ayurvedic%20literature%2C%20it,drug%20useful%20in%20vatic%20disorders."]     
        elif prediction=='Parijata':
            msg=['Scientific Name:','Nyctanthes arbor-tristis',"Medicinal Use:","Parijatha leaves are commonly used to alleviate digestive issues such as indigestion, bloating, and stomachaches. They are also valued for their potential to relieve respiratory ailments, including coughs and colds. Additionally, Parijatha leaves are believed to possess anti-inflammatory properties, making them beneficial for reducing inflammation in the body. Some traditional practices also use Parijatha leaves for their analgesic properties to alleviate pain.","Simple Remedy:","start by gathering a handful of fresh Parijatha leaves and washing them thoroughly. Next, boil the cleaned leaves in water for approximately 10-15 minutes until a decoction is formed. Afterward, strain the decoction and allow it to cool slightly before consumption.", "Availability:","Parijata leaves are commonly found in regions across India, especially in states like West Bengal, Assam, and Tamil Nadu.","For More Visit:","https://www.easyayurveda.com/2016/11/30/parijatha-nyctanthes-arbor-tristis-night-jasmine-coral-jasmine/"]  
        elif prediction=='Peepal':
            msg=['Scientific Name:','Ficus religiosa',"Medicinal Use:","Peepal leaves are esteemed for their anti-inflammatory properties, which make them beneficial in managing inflammatory conditions like arthritis and joint pain. They are also revered for their anti-diabetic potential, as they may help regulate blood sugar levels and improve insulin sensitivity. Additionally, peepal leaves are believed to possess antimicrobial properties, aiding in the treatment of various infections. Moreover, they are used in traditional practices to promote digestive health, relieve constipation, and alleviate gastrointestinal discomfort.","Simple Remedy:","Start by taking a handful of fresh peepal leaves and washing them thoroughly. Then, boil the cleaned leaves in water for about 10-15 minutes until the water reduces to half its original quantity. Afterward, strain the decoction and allow it to cool slightly before consumption.", "Availability:","Peepal trees are found throughout India, especially in regions with a tropical climate. They are often found near temples.","For More Visit:","https://pharmeasy.in/blog/ayurveda-uses-benefits-side-effects-of-peepal-tree/"]
        elif prediction=='Pomegranate':
            msg=['Scientific Name:','Punica granatum',"Medicinal Use:","Rich in bioactive compounds such as tannins, flavonoids, and alkaloids, pomegranate leaves are known for their antioxidant, anti-inflammatory, and antimicrobial effects. One of their primary uses is in promoting cardiovascular health. Pomegranate leaf extracts have been shown to help lower blood pressure, reduce cholesterol levels, and improve overall heart function. Additionally, pomegranate leaves are believed to have anti-diabetic properties, as they may help regulate blood sugar levels and improve insulin sensitivity.","Simple Remedy:","Start by taking a handful of fresh pomegranate leaves and washing them thoroughly. Then, place the washed leaves in a pot with water and bring it to a boil. Let the leaves simmer in the water for about 10-15 minutes until the water turns slightly brown. Strain the decoction and allow it to cool down to a comfortable temperature. Finally, drink this pomegranate leaf decoction once daily, preferably after meals.","Availability:","Pomegranate trees are native to regions with a Mediterranean climate, including parts of India such as Maharashtra, Karnataka, and Andhra Pradesh.","For More Visit:","https://www.easyayurveda.com/2011/11/04/pomegranate-fruit-benefits-anti-oxidants-plus-tridosha-balancing-ayurveda-details/"]         
        elif prediction=='Rasna':
            msg=['Scientific Name:','Pluchea lanceolata',"Medicinal Use:","Rasna leaves contain bioactive compounds such as flavonoids, alkaloids, and terpenoids, which exhibit anti-inflammatory and analgesic effects. They are often prepared as decoctions or poultices and applied topically to affected areas to reduce pain and swelling. Additionally, Rasna leaves are believed to possess diuretic properties, promoting urine flow and aiding in the elimination of toxins from the body.","Simple Remedy:","Begin by taking a handful of fresh Rasna leaves and washing them thoroughly. Boil the washed leaves in water for about 10-15 minutes until the water reduces to half its original quantity. Afterward, strain the decoction and allow it to cool slightly.","Availability:","Rasna is found in various regions across India, especially in the Himalayan foothills and in states like Uttarakhand, Himachal Pradesh, and Jammu and Kashmir.","For More Visit:","https://www.netmeds.com/health-library/post/rasna-health-benefits-ayurvedic-uses-formulations-dosage-and-side-effects#:~:text=Rasna%20can%20help%20to%20ease,owing%20to%20its%20Ushna%20trait."]
        elif prediction=='Rose_apple':
            msg=['Scientific Name:','Syzygium jambos',"Medicinal Use:","These leaves contain bioactive compounds such as flavonoids, tannins, and phenolic acids, which contribute to their therapeutic effects. Rose apple leaves are commonly used to treat gastrointestinal issues such as diarrhea and dysentery due to their astringent properties, which help to reduce intestinal inflammation and promote bowel regularity. Additionally, the leaves are believed to have antimicrobial properties, making them useful in combating infections caused by bacteria and fungi.","Simple Remedy:","Start by taking a handful of fresh rose apple leaves and washing them thoroughly. Then, boil the washed leaves in water for about 10-15 minutes until the water reduces to half its original quantity. Afterward, strain the decoction and allow it to cool slightly. It's recommended to drink this rose apple leaf decoction once daily, preferably after meals.", "Availability:","Rose Apple leaves are commonly available in tropical regions, including parts of India, Southeast Asia, and the Caribbean.","For More Visit:","https://www.netmeds.com/health-library/post/water-apple-nutrition-health-benefits-uses-for-skin-and-applications-in-ayurveda"]
        elif prediction=='Roxburgh_fig':
            msg=['Scientific Name:','Ficus auriculata',"Medicinal Use:","These leaves contain bioactive compounds such as alkaloids, flavonoids, and phenolic acids, which contribute to their medicinal effects. Roxburgh leaves are commonly used in traditional herbal remedies to alleviate pain and inflammation, particularly in conditions like arthritis and rheumatism. The leaves are believed to possess analgesic and anti-inflammatory properties, which can help reduce pain and swelling in affected joints. ","Simple Remedy:","Start by taking a handful of fresh Roxburgh leaves and washing them thoroughly. Then, boil the washed leaves in water for about 10-15 minutes until the water reduces to half its original quantity. Afterward, strain the decoction and allow it to cool slightly.", "Availability:","It is mostly confined to Western Parts of Maharashtra, Gujarat, Uttar Pradesh (Lucknow & Saharanpur) Karnataka (Bellary, Chitradurga & Srirangapatna) and Tamilnadu (Coimbatore).","For More Visit:","https://www.easyayurveda.com/2017/04/20/putrajivaka-putranjiva-roxburghii/"]
        elif prediction=='Sandalwood':
            msg=['Scientific Name:','Santalum',"Medicinal Use:","Sandalwood leaves are used in Ayurvedic medicine for their anti-inflammatory properties, soothing skin irritations and aiding wound healing. They also have antimicrobial effects, beneficial for treating infections.Sandalwood leaves, known for their aromatic and medicinal properties, are commonly used in Ayurvedic medicine. They contain compounds that exhibit anti-inflammatory effects, making them beneficial for reducing skin inflammation and soothing irritations such as acne, eczema, and rashes.","Simple Remedy:","Simple Remedy: Start by collecting a handful of fresh sandalwood leaves and washing them thoroughly. Then, grind the washed leaves into a fine paste using a mortar and pestle or a food processor. Once you have a smooth paste, apply it directly to the affected area of the skin. Leave the paste on for about 20-30 minutes, allowing it to dry before rinsing it off with lukewarm water.","Availability:","Sandalwood trees, including their leaves, are primarily found in regions known for sandalwood cultivation, such as parts of India (Karnataka, Tamil Nadu).","For More Visit:","https://www.drugs.com/npc/sandalwood.html#:~:text=The%20leaves%20and%20bark%20were,two%2Dspotted%20spider%20mite"]
        elif prediction=='Tulsi':
            msg=['Scientific Name:','Ocimum tenuiflorum And also known as Ocimum sanctum',"Medicinal Use:","Tulasi leaves are commonly used to boost the immune system and promote overall health and well-being. They are believed to possess antimicrobial properties, making them effective in fighting off infections and reducing the severity of colds, coughs, and other respiratory ailments. Additionally, Tulasi leaves are known for their anti-inflammatory effects, which can help alleviate symptoms of arthritis and other inflammatory conditions. Furthermore, Tulasi leaves are used to support digestive health, relieve indigestion, and reduce bloating.","Simple Remedy:","To make this tea, start by collecting a handful of fresh Tulasi leaves and washing them thoroughly. Then, boil a cup of water and add the washed Tulasi leaves to it. Let the leaves steep in the hot water for about 5-10 minutes, allowing their beneficial compounds to infuse into the water. Afterward, strain the tea and add a teaspoon of honey for taste, if desired.", "Availability:","It is commonly grown in home gardens, temples, and farms, and is used extensively in Ayurvedic medicine in India.","For More Visit:","https://www.easyayurveda.com/2014/11/13/tulsi-ocimum-sanctum-benefits-research-side-effects/"]
        for message_index, message in enumerate(msg):
            flash((message_index, message)) 
            
        return render_template("template.html", image_name=fn, text=prediction)
    return render_template("index.html")



if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0")