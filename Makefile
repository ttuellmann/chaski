# Makefile for chaski

all: assets build

assets:
	cp -r assets/* deploy

build: 
	@echo build not implemented

clean:
	rm -rf deploy/*

.PHONY: all assets build clean
