# 04/20 15 min.

import streamlit as st
import pandas as pd
from PIL import Image as img

st.set_page_config(page_title="Giant Pandas VS Grizzly Bears: What's The Difference?", page_icon="🐼", layout='centered', initial_sidebar_state='auto')

sects = [
	"Giant Pandas VS Grizzly Bears",
	"How to Tell if A Bear is a Bear",
	"Sources"
]
sect = st.sidebar.radio("Section:", sects)

if sect == "Giant Pandas VS Grizzly Bears":

	st.title(sect)
	st.write("Most of us know that giant pandas are bears, so they're just like grizzly and polar bears, right? Well, you're not wrong, but you're not right either. While giant pandas are bears, they're not really the same kind of bears as the big brown cuddly beasts you might find in a forest. Both bears have large bodies, stubby legs and short tails. However, the giant pandas - even though they were built to eat meat - need to eat bamboo to survive. Giant pandas also are a weak and soft type of bear, so they can't fight with other animals for food. Of course, no animal wants to die, so they started eating lots of bamboo. The bamboo only gives them a little bit of energy, which is why they need to eat a lot to survive. However, this has kept a decent few alive (around 2000), and - thanks to nature reserves - they continue to live peacefully in a habitat with lots of bamboo for them to eat.")
	st.image(img.open("Reserve.png"), caption="Woolong National Nature Reserve: https://peapix.com/bing/1732")

if sect == "How to Tell if A Bear is a Bear":

	st.title(sect)
	st.write("This guy named Carolus Linnaeus (we'll call him Carl) was super famous for the way he named living things. Carl created a way to show the difference between different types of animals. His system used 7 main levels:")

	desc = [
		["Kingdom", "What type of living thing it is (like an animal or fungus)"],
		["Phylum", "The way the living thing became what it is (like an animal with a spinal cord)"],
		["Class", "The way the animal lives (a mammal lives on land and uses lungs to breathe)"],
		["Order", "How the living thing eats things (like carnivores (meat-eaters) or insectivores (insect-eaters))"],
		["Family", "What general type of animal it is (like a bear (Ursus) or cat (Felis))"],
		["Genus", "The group of living things that share features (eg. Panthera (cats that roar), like lions or tigers)"],
		["Species", "The specific type of living thing that it is (like a house cat - in scientific terms, Felis Catus)"]
	]
	
	lcddf = pd.DataFrame(desc, columns=["Class Level", "What it Means"])

	st.dataframe(lcddf)
	st.write("He also came up with something called $binomial$ $nomenclature$ - it's just a way of naming things that has the scientific name for a type of animal after the scientific name for the group that it's in.")

	lcdf = pd.DataFrame([["Kingdom", "Animalia", "Animalia"], ["Phylum", "Chordata", "Chordata"], ["Class", "Mammalia", "Mammalia"], ["Order", "Carnivora", "Carnivora"], ["Family", "Ursidae", "Ursidae"], ["Genus", "Ursus", "Ailurupoda"], ["Species", "Arctos", "Melanoleuca"]], columns=["Class Level", "Grizzly Bear", "Giant Panda"])
	c1, c2 = st.columns(2)

	with c1:
		lcin = st.expander("Linnaean Classification Table").dataframe(lcdf)
	
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