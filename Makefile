all: clean pack

clean:
	rm -f xfindr01.zip

pack:
	zip -r xfindr01.zip report.pdf requirements.txt environment.py features/