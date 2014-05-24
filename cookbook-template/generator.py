#!/usr/bin/env python
from __future__ import print_function
import os
import glob
import sys

#print glob.glob("/home/adam/*.txt")

# file = open('newfile.txt', 'r')
# file.readline():

catego

class Recipe:
	def set_recipe_name(self, recipe_name):
		self.recipe_name = recipe_name

	def set_category(self, category):
		self.category = category

	def set_tags(self, tags):
		self.tags = tags

	def foo(self, file_name):
		file = open(file_name, 'r')
		self.file_name = file_name
		self.recipe_name = file.readline()[2:]
		self.category = file.readline()[2:]
		self.tags = file.readline()[2:].split()
		file.close()
#if(glob.glob("cookbook.tex"))

def main():
	this_dir = os.path.dirname(os.path.realpath(__file__))
	recipes_dir = this_dir + "recipes/"
	recipes = []
	for file_name in glob.glob(recipes_dir):
		recipe = Recipe()
		recipe.foo(file_name)
		recipes.append(recipe)
	bookfile = open(this_dir + cookbook.tex, 'w')
	bookfile.write("\\documentclass{mycookbook}\n\\begin{document}")
	for item in recipes:
		bookfile.write("\include{" + item.file_name +"}\n")
	bookfile.write("\\end{document}")
	

#ABLAUF

# delete (if it exists) cookbook.tex, tags.tex, ingredients.tex
# create new (blank) cookbook.tex
# if(template.tex) -> copy to cookbook.tex
# 	else -> copy template string to cookbook.tex

# get names of all .tex-files in recipes/
# for each tex-file
#	get name/ \label from first line
# 	get category from second line
#		add name to category.recipeList
# 	get tags from third line
#		if(tag is known) -> add name to tag.recipeList
# 	get main ingredients from forth line
#		if(ingredient is known) -> add name to ingredient.recipeList

# for each category
# 	\chapter{category} to cookbook.tex
#	sort recipes by title alphabetically
#	\include .tex-files in order of recipes to cookbook.tex

# sort tags alphabetically
# for each tag
#	for each recipe in tag.recipeList
#		print recipe \nameref, page of recipe (\pageref or something)

# sort ingredients alphabetically
# for each ingredient
#	for each recipe in ingredient.recipeList
#		print recipe \nameref, page of recipe (\pageref or something)

# build latex pdf
