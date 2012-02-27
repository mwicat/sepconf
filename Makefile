DIST=`pwd`/dist
PICKLE=$(DIST)/users.pickle

GENERATE_CMD=python sepgen.py generate
FILL_CMD=cheetah fill --pickle $(PICKLE) --odir dist --oext out templates/*

ASTERISK_PHONES=/etc/asterisk/sccp_phones.conf
FREESWITCH_PHONES=/usr/local/freeswitch/conf/directory/default/sccp_phones.xml

all: init generate fill install

init:
	-mkdir dist

generate:
	$(GENERATE_CMD) 10 > $(PICKLE)

fill:
	$(FILL_CMD)

install:
	cp dist/sccp_phones_asterisk.out $(ASTERISK_PHONES)
	cp dist/sccp_phones_freeswitch.out $(FREESWITCH_PHONES)
