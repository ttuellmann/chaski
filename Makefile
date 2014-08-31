.PHONY: all assets build clean

all: assets build

assets:
	cp -r assets/* deploy

build: 
	@echo not implemented

clean:
	rm -rf deploy/*
