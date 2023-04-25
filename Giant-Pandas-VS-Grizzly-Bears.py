import streamlit as st
import pandas as pd
from PIL import Image as img

st.set_page_config(page_title="Giant Pandas VS Grizzly Bears: What's The Difference?", page_icon="🐼", layout='centered', initial_sidebar_state='auto')

sects = [
	"Home",
	"How to Tell if a Bear is a Bear",
	"Diet and Habitat: Giant Pandas",
	"Diet and Habitat: Grizzly Bears",
	"Sources"
]
sect = st.sidebar.radio("Section:", sects)

if sect == "Home":

	st.title("Giant Pandas VS Grizzly Bears")
	st.write("Most of us know that giant pandas are bears, so they're just like grizzly and polar bears, right? Well, you're not wrong, but you're not right either. While giant pandas are bears, they're not *really* the same kind of bears as the big brown cuddly beasts you might find in a forest. Both bears have large bodies, stubby legs and short tails. However, the giant pandas - even though they were built to eat meat - need to eat bamboo to survive. Giant pandas also are a weak and soft type of bear, so they can't fight with other animals for food. Of course, no animal wants to die, so they started eating lots of **bamboo**. The bamboo only gives them a little bit of energy, which is why they need to eat a lot to survive. However, this has kept a decent few alive (around *2000*), and - thanks to ***nature reserves*** - they continue to live peacefully in a habitat with lots of bamboo for them to eat.")
	st.image("https://whc.unesco.org/uploads/thumbs/site_1213_0001-1200-630-20090928160826.jpg", caption="https://whc.unesco.org/en/list/1213/")


if sect == "How to Tell if a Bear is a Bear":

	st.title(sect)
	st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Carl_von_Linn%C3%A9%2C_1707-1778%2C_botanist%2C_professor_%28Alexander_Roslin%29_-_Nationalmuseum_-_15723.tif/lossy-page1-1200px-Carl_von_Linn%C3%A9%2C_1707-1778%2C_botanist%2C_professor_%28Alexander_Roslin%29_-_Nationalmuseum_-_15723.tif.jpg", width=300, caption="https://en.wikipedia.org/wiki/Carl_Linnaeus")
	st.write("This guy named ***Carolus Linnaeus*** (we'll call him Carl) was super famous for the way he named living things (which often involved Latin words). Carl created a way to show the difference between different types of animals. His system (called the ***Linnaean Classification System***) used **7** main levels:")

	desc = [
		["Kingdom", "What type of living thing it is (like an animal or fungus)"],
		["Phylum", "The way the living thing became what it is (like an animal with a spinal cord)"],
		["Class", "The way the living thing survives (a mammal lives on land and uses lungs to breathe)"],
		["Order", "How the living thing eats things (like carnivores (meat-eaters) or insectivores (insect-eaters))"],
		["Family", "What general type of living thing it is (like a bear (Ursidae) or cat (Felidae))"],
		["Genus", "The group of living things that share features (like Ursus - Grizzly, Black or Polar Bears)"],
		["Species", "The specific type of living thing that it is (like Arctos - Grizzly (part of the Ursus genus))"]
	]
	
	lcddf = pd.DataFrame(desc, columns=["Class Level", "What it Means"])

	st.dataframe(lcddf)
	st.write("He also came up with something called ***binomial nomenclature*** - it's just a way of naming things that has a living thing's species after the *genus* that it's in.")

	lcdf = pd.DataFrame([["Kingdom", "Animalia (Animal)", "Animalia (Animal)"], ["Phylum", "Chordata (Has a Spine)", "Chordata (Has a Spine)"], ["Class", "Mammalia (Mammal)", "Mammalia (Mammal)"], ["Order", "Carnivora (Carnivore - Meat Eater)", "Carnivora (Carnivore - Meat Eater)"], ["Family", "Ursidae (Bear)", "Ursidae (Bear)"], ["Genus", "Ursus (Group of Bears (Grizzly, Polar and Black))", "Ailuropoda (Pandas)"], ["Species", "Arctos (Grizzly Bear)", "Melanoleuca (Giant Panda)"], ["Latin Name", "Ursus Arctos", "Ailuropoda Melanoleuca"]], columns=["Class Level", "Grizzly Bear", "Giant Panda"])
	lcin = st.expander("Linnaean Classification Table (For Giant Pandas and Grizzly Bears)").dataframe(lcdf)
	

if sect == "Diet and Habitat: Giant Pandas":

	st.title(sect)
	st.write("Giant pandas are *really* picky with what they eat and where they live.")
	st.write("They're not actually picky, but they only eat bamboo, since anything else means fighting with other animals (they're not very good at that). ")
	
	st.image("data:image/jpeg;base64,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", caption="https://www.expatolife.com/bamboo-forest-kyoto-japan/")

	st.write("Since they only eat bamboo, it means that they are a ***herbivore specialist*** species, which just means that they only eat plants, and will only eat a specific type or group of plants at that (in this case, bamboo). The first giant pandas, were ***carnivores*** (which means that they ate meat), but because of the fact that they couldn't fight other ***predators***, they had to find something that they wouldn't have to fight for in the first place - **bamboo**. They can only get bamboo in certain places, but it's really easy to get in China, since there are huge ***bamboo forests*** there that have lots and lots of bamboo for the pandas to eat. Bamboo has lots of fibre, but it doesn't have very much energy or protein, and it's not very easy to digest. This means that the giant pandas have to eat 9-14kg a day just to keep themselves fed! That's why they spend most of their time outside eating - to make sure they keep themselves well-fed. Eating bamboo does mean that the pandas will live a safer life though, since they're the only animals that eat it.")

	st.image("https://24.media.tumblr.com/a004f04e310d1ea5a1494e5dd11ddc98/tumblr_mfp2pl3qbB1raju2zo1_1280.jpg", caption="https://www.pandasinternational.org/bamboo-the-giant-diet-of-the-giant-panda/")

	st.write("Giant pandas live high up in mountain ranges in China's Central Provinces of Sichuan, Shaanxi and Gansu - in ***montane forests*** (rainforests) and ***mixed forests** (with lots of different types of plants) - where they can find lots of different types of bamboo to eat. They also use evergreen trees to hide from predators like jackals, snow leopards and yellow-throated martens, who try to eat panda cubs.")

	c1, c2 = st.columns(2)

	with c1:
		st.expander("Zhangjajie National Montane Forest Park").image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/1_tianzishan_wulingyuan_zhangjiajie_2012.jpg/1200px-1_tianzishan_wulingyuan_zhangjiajie_2012.jpg", caption="https://en.wikipedia.org/wiki/Zhangjiajie_National_Forest_Park", width=350)
	with c2:
		st.expander("Changbai Mountains Mixed Forest").image("https://upload.wikimedia.org/wikipedia/commons/b/b2/Forests_in_Changbai_Mountain.jpg", caption="https://en.wikipedia.org/wiki/Changbai_Mountains_mixed_forests", width=350)


if sect == "Diet and Habitat: Grizzly Bears":

	st.title(sect)

	st.write("Grizzly bears eat *a lot* of different things.")
	st.write("They're ***omnivore generalist*** species, which means that they eat lots of different types of meat and plants. Grizzly bears eat deer elk, berriess, thistle, cow parsnip, grasses, roots, fungi, plant bulbs, roots, spawning fish, insects... basically, *a lot* of stuff. This gives them lots of options year-round, but this does also mean that they'll have to fight more against other animals for food, and some food sources might not be *as* filling as others, so they'll need more to keep their strength up,")

	st.image("https://i.cbc.ca/1.5741941.1628294335!/fileImage/httpImage/image.jpg_gen/derivatives/16x9_780/black-bear-jasper.jpg", caption="https://www.cbc.ca/news/canada/edmonton/berry-picking-alberta-bears-can-t-compete-with-the-salmon-slammin-big-boys-in-alaska-1.5741848")

	st.write("Grizzly bears are strong bears that live in high-up slopes, avalanche chutes and low wetlands, using the food they get from plants, and giving back the seeds in their ***manure***, which acts as ***fertilizer*** for the seeds and nearby plants.")

	st.image("https://www.animalsaroundtheglobe.com/wp-content/uploads/2023/03/pete-nuij-lWHvAw1Inbs-unsplash-1200x800.jpg.webp", caption="https://www.animalsaroundtheglobe.com/bear-poop/")

	st.write("Adult grizzly bears are strong, but what about the cubs? Grizzly bear cubs are hunted by mountain lions, wolves and other bears, putting them at a pretty big risk. That means that it's up to the parents to defend their cubs against other powerful beasts.")

	st.image("https://cdn.roaring.earth/wp-content/uploads/2015/11/87820435_626779078153564_1101763526373933056_n.jpg", caption="https://roaring.earth/cougar-vs-bear/", width=500)

if sect == "Sources":
	
	src = {
		"Giant Panda (Ailuropoda Melanoleuca) Fact Sheet: Taxonomy & History": "https://ielc.libguides.com/sdzg/factsheets/giantpanda/taxonomy",
		"Giant Panda - Facts, Diet, Habitat & Pictures on Animalia.bio": "https://animalia.bio/giant-panda",
		"Panda's natural enemies and defences | WWF": "https://wwf.panda.org/discover/knowledge_hub/endangered_species/giant_panda/panda/kung_fu_panda_enemies_defences/",
		"Giant Pandas 101 | Nat Geo Wild": "https://youtu.be/dqT-UlYlg1s",
		"ITIS - Report: Ursus Arctos": "https://www.itis.gov/servlet/SingleRpt/SingleRpt?search_topic=TSN&search_value=180543#null",
		"Grizzly Bear Biology & Behavior| Western Wildlife": "https://westernwildlife.org/grizzly-bear-ursus-arctos-horribilis/biology-behavior/",
		"Ursus Arctos - Interactions with Other Species": "http://bioweb.uwlax.edu/bio203/f2013/hackfort_dawn/interactions.htm"
	}

	st.title(sect)

	for x, y in zip(src.keys(), src.values()):
		st.write(f" - [{x}]({y})")
