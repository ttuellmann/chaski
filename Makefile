# Makefile for chaski

vpath %.yaml conf
vpath %.j2   src

all: prod

assets:
	cp -r assets/* deploy

%.html: %.yaml
	src/render.py -o deploy/$@ -i $< -t src/chaski.html.j2

prod: assets
	@:

test: assets example.html

clean:
	rm -rf deploy/*

.PHONY: all assets prod test clean
