# Card generation makefile
# Attributes definition file
ATT=img_attributes.json
# Model file
MODEL=img_model.json
# Images directory
IMGS_DIR=./img
# Output directory
OUT=./out
# RNG seed
ifndef SEED
	SEED=$$RANDOM
endif


all:
	@echo seed : $(SEED)
	@echo Use \"make SEED=seed\" to regenerate this card game
	exec python ./src/edgen.py -a $(ATT) -d $(IMGS_DIR) -m $(MODEL) -o $(OUT) -s $(SEED)

clean:
	rm -rf $(OUT)
