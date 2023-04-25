import streamlit as st
import pandas as pd
from PIL import Image as img

st.set_page_config(page_title="Giant Pandas VS Grizzly Bears: What's The Difference?", page_icon="🐼", layout='centered', initial_sidebar_state='auto')

sects = [
	"Giant Pandas VS Grizzly Bears",
	"How to Tell if A Bear is a Bear",
	"Diet and Habitat: Giant Pandas",
	"Diet and Habitat: Grizzly Bears",
	"Sources"
]
sect = st.sidebar.radio("Section:", sects)

if sect == "Giant Pandas VS Grizzly Bears":

	st.title(sect)
	st.write("Most of us know that giant pandas are bears, so they're just like grizzly and polar bears, right? Well, you're not wrong, but you're not right either. While giant pandas are bears, they're not *really* the same kind of bears as the big brown cuddly beasts you might find in a forest. Both bears have large bodies, stubby legs and short tails. However, the giant pandas - even though they were built to eat meat - need to eat bamboo to survive. Giant pandas also are a weak and soft type of bear, so they can't fight with other animals for food. Of course, no animal wants to die, so they started eating lots of **bamboo**. The bamboo only gives them a little bit of energy, which is why they need to eat a lot to survive. However, this has kept a decent few alive (around *2000*), and - thanks to ***nature reserves*** - they continue to live peacefully in a habitat with lots of bamboo for them to eat.")
	st.image("https://whc.unesco.org/uploads/thumbs/site_1213_0001-1200-630-20090928160826.jpg", caption="https://whc.unesco.org/en/list/1213/")

if sect == "How to Tell if A Bear is a Bear":

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
	st.write("Giant Pandas are really picky with what they eat and where they live.")
	st.write("They're not really picky, but they only eat bamboo, since anything else means fighting with other animals, which they are not good at.")

if sect == "Diet and Habitat: Grizzly Bears":
	st.title(sect)

if sect == "Sources":
	
	src = [
		"https://ielc.libguides.com/sdzg/factsheets/giantpanda/taxonomy",
		"https://www.itis.gov/servlet/SingleRpt/SingleRpt?search_topic=TSN&search_value=180543#null",
		"https://a-z-animals.com/blog/how-many-pandas-are-left-in-the-world/#",
		"http://bioweb.uwlax.edu/bio203/f2013/hackfort_dawn/classification.htm#"
	]

	st.title(sect)
	for i in src:
		st.write(f" - {i}")
