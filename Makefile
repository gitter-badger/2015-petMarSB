CPUS=4

environment:
	conda env export --file environment.conda

list-tasks:
	./pipeline list --resources-metadata resources.json --config-metadata config.json

clean:
	./pipeline clean --resources-metadata resources.json --config-metadata config.json
