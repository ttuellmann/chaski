# Makefile for chaski

PROD_FILES := $(filter-out conf/example.yaml, $(wildcard conf/*.yaml))
PROD_FILES := $(notdir $(PROD_FILES:.yaml=.html))

prod: assets $(PROD_FILES)

assets:
	cp -r assets/* deploy

%.html: conf/%.yaml
	src/render.py -o deploy/$@ -i $< -t src/chaski.html.j2

test: assets example.html

clean:
	rm -rf deploy/*

.PHONY: prod assets test clean
